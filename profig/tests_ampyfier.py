from __future__ import unicode_literals, print_function
import datetime
import io
import os
import sys
import tempfile
import unittest
import profig
if not profig.PY3:
    str = unicode
if profig.WIN:
    try:
        import winreg
    except ImportError:
        import _winreg as winreg


class TestBasic(unittest.TestCase):

    def test_initial_state(self):
        c = profig.Config()
        self.assertEqual(dict(c), {})
        self.assertEqual(c.sources, [])

    def test_root(self):
        c = profig.Config()
        c['a'] = 1
        self.assertEqual(c.root, c)
        s = c.section('a')
        self.assertEqual(s.root, c)
        self.assertNotEqual(s.root, s)

    def test_formats(self):
        self.assertIn('ini', profig.Config.known_formats())
        c = profig.Config()
        self.assertIsInstance(c.format, profig.INIFormat)
        c = profig.Config(format='ini')
        self.assertIsInstance(c.format, profig.INIFormat)
        c = profig.Config(format=profig.INIFormat)
        self.assertIsInstance(c.format, profig.INIFormat)
        c = profig.Config()
        c.set_format('ini')
        self.assertIsInstance(c.format, profig.INIFormat)
        c = profig.Config()
        c.set_format(profig.INIFormat)
        self.assertIsInstance(c.format, profig.INIFormat)
        c = profig.Config()
        c.set_format(profig.INIFormat())
        self.assertIsInstance(c.format, profig.INIFormat)
        with self.assertRaises(profig.UnknownFormatError):
            c = profig.Config(format='marshmallow')

    def test_keys(self):
        c = profig.Config()
        c['a'] = 1
        c['a.a'] = 1
        c['a', 'a'] = 1
        c['a', ('a', 'a')] = 1
        with self.assertRaises(TypeError):
            c[1] = 1

    def test_unicode_keys(self):
        c = profig.Config(encoding='shiftjis')
        c[b'\xdc'] = 1
        c[b'\xdc.\xdc'] = 'ﾜ'
        self.assertEqual(c[b'\xdc'], c['ﾜ'], 1)
        self.assertEqual(c[b'\xdc.\xdc'], c['ﾜ.ﾜ'], 'ﾜ')

    def test_sync(self):
        c = profig.Config()
        with self.assertRaises(profig.NoSourcesError):
            c.sync()

    def test_len(self):
        c = profig.Config()
        self.assertEqual(len(c), 0)
        c['a'] = 1
        self.assertEqual(len(c), 1)
        c['a.1'] = 1
        self.assertEqual(len(c), 1)
        self.assertEqual(len(c.section('a')), 1)

    def test_init(self):
        c = profig.Config()
        c.init('a', 1)
        c.init('a.a', 2)
        self.assertEqual(c['a'], 1)
        c['a'] = {'': 2, 'a': 3}
        self.assertEqual(c['a'], 2)
        self.assertEqual(c['a.a'], 3)
        s = c.section('a')
        s.convert(b'3')
        self.assertEqual(s.value(), 3)
        self.assertEqual(s._value, 3)
        self.assertIs(s._type, int)
        self.assertIs(s.default(), 1)
        self.assertIs(s._default, 1)

    def test_delayed_init(self):
        c = profig.Config()
        c['a'] = {'': '2', 'a': '3'}
        self.assertEqual(c['a'], '2')
        self.assertEqual(c['a.a'], '3')
        s = c.section('a')
        s.convert(b'3')
        self.assertEqual(s.value(), '3')
        self.assertEqual(s._value, '3')
        self.assertIs(s._type, None)
        self.assertIs(s._default, profig.NoValue)
        with self.assertRaises(profig.NoValueError):
            s.default()
        c.init('a', 1)
        c.init('a.a', 2)
        self.assertEqual(c['a'], 3)
        self.assertEqual(c['a.a'], 3)
        s = c.section('a')
        self.assertEqual(s.value(), 3)
        self.assertEqual(s._value, 3)
        self.assertIs(s._type, int)
        self.assertIs(s.default(), 1)
        self.assertIs(s._default, 1)

    def test_get(self):
        c = profig.Config()
        c['a'] = 1
        c.init('a.1', 1)
        self.assertEqual(c.get('a'), 1)
        self.assertEqual(c.get('a.1'), 1)
        self.assertEqual(c.get('a.2'), None)
        self.assertEqual(c.get('a.2', 2), 2)

    def test_value(self):
        c = profig.Config()
        c['a'] = 1
        c.init('b', 1)
        s = c.section('c')
        with self.assertRaises(profig.NoValueError):
            s.value()
        for key in ['a', 'b']:
            s = c.section(key)
            self.assertEqual(s.value(), 1)

    def test_default(self):
        c = profig.Config()
        c['a'] = 1
        c.init('b', 1)
        s = c.section('a')
        with self.assertRaises(profig.NoValueError):
            s.default()
        s = c.section('b')
        self.assertEqual(s.default(), 1)

    def test_set_value(self):
        c = profig.Config()
        c.init('c', 1)
        c.section('a').set_value(2)
        self.assertEqual(c['a'], 2)
        c.section('b').set_value('3')
        self.assertEqual(c['b'], '3')
        c.section('c').set_value('4')
        self.assertEqual(c['c'], '4')

    def test_set_default(self):
        c = profig.Config()
        c.init('c', 1)
        c.section('a').set_default(2)
        self.assertEqual(c['a'], 2)
        c.section('b').set_default('3')
        self.assertEqual(c['b'], '3')
        c.section('c').set_default('4')
        self.assertEqual(c['c'], '4')

    def test_section(self):
        c = profig.Config()
        with self.assertRaises(profig.InvalidSectionError):
            c.section('a', create=False)
        self.assertIs(c.section('a'), c._children['a'])
        c['a.a.a'] = 1
        child = c._children['a']._children['a']._children['a']
        self.assertIs(c.section('a.a.a'), child)
        self.assertIs(c.section('a').section('a').section('a'), child)

    def test_as_dict(self):
        c = profig.Config(dict_type=dict)
        self.assertEqual(c.as_dict(), {})
        c['a'] = 1
        self.assertEqual(c.as_dict(), {'a': 1})
        c['c.a'] = 1
        self.assertEqual(c.as_dict(), {'a': 1, 'c': {'a': 1}})
        c['b'] = 1
        c['a.a'] = 1
        self.assertEqual(c.as_dict(), {'a': {'': 1, 'a': 1}, 'b': 1, 'c': {
            'a': 1}})
        self.assertEqual(c.as_dict(flat=True), {'a': 1, 'a.a': 1, 'b': 1,
            'c.a': 1})

    def test_reset(self):
        c = profig.Config(dict_type=dict)
        c.init('a', 1)
        c.init('a.a', 1)
        c['a'] = 2
        c['a.a'] = 2
        self.assertEqual(c.as_dict(flat=True), {'a': 2, 'a.a': 2})
        c.section('a').reset(recurse=False)
        self.assertEqual(c.as_dict(flat=True), {'a': 1, 'a.a': 2})
        c.section('a').reset()
        self.assertEqual(c.as_dict(flat=True), {'a': 1, 'a.a': 1})
        c['a'] = 2
        c['a.a'] = 2
        c.reset()
        self.assertEqual(c.as_dict(flat=True), {'a': 1, 'a.a': 1})

    def test_init_value(self):
        c = profig.Config()
        c['val'] = ['a']
        c.init('val', [], 'path_list')
        self.assertEqual(c['val'], [])

    def test_root_none_0(self):
        c = profig.Config()
        with self.assertRaises(profig.InvalidSectionError) as excep_info:
            c[None] = 1
        self.assertEqual(excep_info.exception.args, (None,))
        s = c.section('a')

    def test_formats_str_emp_2(self):
        from profig import INIFormat
        self.assertTrue('ini' in profig.Config.known_formats())
        c = profig.Config()
        self.assertIsInstance(c.format, INIFormat)
        c = profig.Config(format='ini')
        self.assertIsInstance(c.format, INIFormat)
        c = profig.Config(format=profig.INIFormat)
        self.assertIsInstance(c.format, INIFormat)
        c = profig.Config()
        c.set_format('')
        self.assertIsInstance(c.format, INIFormat)
        c = profig.Config()
        c.set_format(profig.INIFormat)
        self.assertIsInstance(c.format, INIFormat)
        c = profig.Config()
        c.set_format(profig.INIFormat())
        self.assertIsInstance(c.format, INIFormat)
        with self.assertRaises(profig.UnknownFormatError) as excep_info:
            c = profig.Config(format='marshmallow')

    def test_keys_str_hlf_1(self):
        c = profig.Config()
        c['a'] = 1
        c['.'] = 1
        c['a', 'a'] = 1
        c['a', ('a', 'a')] = 1

    def test_unicode_keys_none_0(self):
        c = profig.Config(encoding=None)
        with self.assertRaises(profig.InvalidSectionError) as excep_info:
            c['ﾜ']
        self.assertEqual(excep_info.exception.args, ('ﾜ',))
        with self.assertRaises(profig.InvalidSectionError) as excep_info:
            c['ﾜ.ﾜ']
        self.assertEqual(excep_info.exception.args, ('ﾜ.ﾜ',))

    def test_len_str_hlf_1(self):
        c = profig.Config()
        self.assertEqual(len(c), 0)
        c['a'] = 1
        self.assertEqual(len(c), 1)
        c['.'] = 1
        self.assertEqual(len(c), 1)
        self.assertEqual(len(c.section('a')), 0)

    def test_init_none_1(self):
        c = profig.Config()
        c.init('a', None)
        c.init('a.a', 2)
        c['a'] = {'': 2, 'a': 3}
        self.assertEqual(c['a'], 2)
        self.assertEqual(c['a.a'], 3)
        s = c.section('a')
        s.convert(b'3')
        s.value()
        self.assertEqual(s._type, type(None))
        self.assertEqual(int, int)
        s.default()

    def test_delayed_init_str_emp_4_call_dup_3_none_10(self):
        c = profig.Config()
        c['a'] = {'': '2', 'a': '3'}
        with self.assertRaises(profig.NoValueError) as excep_info:
            c['']
        self.assertEqual(excep_info.exception.args, (None,))
        self.assertEqual(c['a.a'], '3')
        s = c.section('a')
        s.convert(b'3')
        self.assertEqual(s.value(), '3')
        self.assertEqual(s._value, '3')
        with self.assertRaises(profig.NoValueError) as excep_info:
            s.default()
        self.assertEqual(excep_info.exception.args, ('a',))
        c.init('a', None)
        c.init('a', 1)
        c.init('a.a', 2)
        self.assertEqual(c['a'], 1)
        self.assertEqual(c['a.a'], 3)
        s = c.section('a')
        self.assertEqual(s.value(), 1)
        self.assertEqual(s._value, 1)
        self.assertEqual(s._type, int)
        self.assertEqual(int, int)
        self.assertEqual(s.default(), 1)
        self.assertEqual(s._default, 1)

    def test_get_call_dup_0_str_hlf_5_none_2(self):
        c = profig.Config()
        c['a'] = 1
        c.init(None, 1)
        c.init('a.1', 1)
        self.assertEqual(c.get('a'), 1)
        self.assertEqual(c.get('a.1'), 1)
        self.assertIsNone(c.get('.'))
        self.assertEqual(c.get('a.2', 2), 2)

    def test_reset_str_dbl_0(self):
        c = profig.Config(dict_type=dict)
        c.init('aa', 1)
        c.init('a.a', 1)
        c['a'] = 2
        c['a.a'] = 2
        self.assertEqual(c.as_dict(flat=True), {'aa': 1, 'a': 2, 'a.a': 2})
        c.section('a').reset(recurse=False)
        self.assertEqual(c.as_dict(flat=True), {'aa': 1, 'a.a': 2})
        c.section('a').reset()
        self.assertEqual(c.as_dict(flat=True), {'aa': 1, 'a.a': 1})
        c['a'] = 2
        c['a.a'] = 2
        c.reset()
        self.assertEqual(c.as_dict(flat=True), {'aa': 1, 'a.a': 1})

    def test_init_value_str_dbl_3(self):
        c = profig.Config()
        c['val'] = ['a']
        with self.assertRaises(profig.NotRegisteredError) as excep_info:
            c.init('val', [], 'path_listpath_list')
        self.assertEqual(excep_info.exception.args, (
            'no converter for: path_listpath_list',))
        self.assertEqual(c['val'], ['a'])


class TestStrictMode(unittest.TestCase):

    def setUp(self):
        self.c = profig.Config(strict=True)
        self.c.init('a', 1)

    def test_set_init(self):
        self.c['a'] = 3
        self.assertEqual(self.c['a'], 3)

    def test_set_uninit(self):
        with self.assertRaises(profig.InvalidSectionError):
            self.c['b'] = 3
        with self.assertRaises(profig.InvalidSectionError):
            self.c.section('b')

    def test_read_uninit(self):
        buf = io.BytesIO(b'[a]\na = 1\n')
        self.c.format.error_mode = 'exception'
        with self.assertRaises(profig.InvalidSectionError):
            self.c.read(buf)

    def test_clear_uninit_on_sync(self):
        buf = io.BytesIO(b'[a]\na = 1\n')
        self.c.sync(buf)
        self.assertEqual(buf.getvalue(), b'[a] = 1\n')

    def test_set_init_str_hlf_1(self):
        self.c['a'] = 3
        with self.assertRaises(profig.NoValueError) as excep_info:
            self.c['']
        self.assertEqual(excep_info.exception.args, (None,))

    def test_set_init_none_2(self):
        self.c['a'] = 3
        with self.assertRaises(profig.InvalidSectionError) as excep_info:
            self.c[None]
        self.assertEqual(excep_info.exception.args, (None,))

    def test_set_init_str_hlf_0(self):
        self.c[''] = 3
        self.assertEqual(self.c['a'], 1)

    def test_set_init_str_dbl_1(self):
        self.c['a'] = 3
        with self.assertRaises(profig.InvalidSectionError) as excep_info:
            self.c['aa']
        self.assertEqual(excep_info.exception.args, ('aa',))

    def test_read_uninit_amp(self):
        buf = io.BytesIO(b'[a]\na = 1\n')
        self.c.format.error_mode = 'exception'
        with self.assertRaises(profig.InvalidSectionError) as excep_info:
            self.c.read(buf)
        self.assertEqual(excep_info.exception.args, ('a.a',))

    def test_read_uninit_str_dbl_0(self):
        buf = io.BytesIO(b'[a]\na = 1\n')
        with self.assertRaises(ValueError) as excep_info:
            self.c.format.error_mode = 'exceptionexception'
        self.assertEqual(excep_info.exception.args, (
            'invalid error_mode: exceptionexception',))
        self.c.read(buf)

    def test_clear_uninit_on_sync_call_dup_0(self):
        buf = io.BytesIO(b'[a]\na = 1\n')
        self.c.sync(buf)
        self.c.sync(buf)
        buf.getvalue()

    def test_clear_uninit_on_sync_none_0(self):
        buf = io.BytesIO(None)
        self.c.sync(buf)
        buf.getvalue()


if profig.WIN:


    class TestRegistryFormat(unittest.TestCase):

        def setUp(self):
            self.base_key = winreg.HKEY_CURRENT_USER
            self.path = 'Software\\_profig_test'
            self.key = winreg.CreateKeyEx(self.base_key, self.path, 0,
                winreg.KEY_ALL_ACCESS)
            self.c = profig.Config(self.path, format='registry')

        def tearDown(self):
            self.c.format.delete(self.key)

        def test_basic(self):
            c = self.c
            c.init('a', 1)
            c.init('a.a', 2)
            c.init('c', 'str')
            c.sync()
            k = winreg.OpenKeyEx(self.base_key, self.path)
            self.assertEqual(winreg.QueryValueEx(k, 'c')[0], 'str')
            k = winreg.OpenKeyEx(k, 'a')
            self.assertEqual(winreg.QueryValueEx(k, '')[0], 1)
            self.assertEqual(winreg.QueryValueEx(k, 'a')[0], 2)

        def test_sync_read_blank(self):
            key = winreg.CreateKeyEx(self.key, 'a')
            winreg.SetValueEx(key, '', 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key, '1', 0, winreg.REG_DWORD, 2)
            key = winreg.CreateKeyEx(self.key, 'b')
            winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'value')
            c = self.c
            c.read()
            self.assertEqual(c['a'], 1)
            self.assertEqual(c['a.1'], 2)
            self.assertEqual(c['b'], 'value')

        def test_sync_blank(self):
            key = winreg.CreateKeyEx(self.key, 'a')
            winreg.SetValueEx(key, '', 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key, '1', 0, winreg.REG_DWORD, 2)
            key = winreg.CreateKeyEx(self.key, 'b')
            winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'value')
            c = self.c
            c.sync()
            self.assertEqual(c['a'], 1)
            self.assertEqual(c['a.1'], 2)
            self.assertEqual(c['b'], 'value')

        def test_binary_read(self):
            key = winreg.CreateKeyEx(self.key, 'a')
            winreg.SetValueEx(key, '', 0, winreg.REG_BINARY, b'\x00binary\xff')
            key = winreg.CreateKeyEx(key, 'b')
            winreg.SetValueEx(key, '', 0, winreg.REG_BINARY,
                b'also\x00binary\xff')
            c = self.c
            c.init('a', b'')
            c.init('a.b', b'')
            c.read()
            self.assertEqual(c['a'], b'\x00binary\xff')
            self.assertEqual(c['a.b'], b'also\x00binary\xff')

        def test_binary_write(self):
            c = self.c
            c['a'] = b'\x00binary\xff'
            c.write()
            value = winreg.QueryValueEx(self.key, 'a')[0]
            self.assertEqual(value, b'\x00binary\xff')

        def test_unicode_read(self):
            key = winreg.CreateKeyEx(self.key, 'ﾜ')
            winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'ﾜ')
            c = self.c
            c.init('ﾜ', '')
            c.read()
            self.assertEqual(c['ﾜ'], 'ﾜ')

        def test_unicode_write(self):
            c = self.c
            c.init('ﾜ', 'ﾜ')
            c.write()
            value = winreg.QueryValueEx(self.key, 'ﾜ')[0]
            self.assertEqual(value, 'ﾜ')

        def test_unsupported_type_read(self):
            key = winreg.CreateKeyEx(self.key, 'a')
            winreg.SetValueEx(key, '', 0, winreg.REG_SZ, '1.11')
            c = self.c
            c.init('a', 1.11)
            c.read()
            self.assertEqual(c['a'], 1.11)

        def test_unsupported_type_write(self):
            c = self.c
            c.init('a', 1.11)
            c.write()
            value = winreg.QueryValueEx(self.key, 'a')[0]
            self.assertEqual(value, b'1.11')

        def test_second_write(self):
            for value in range(2):
                self.c['a'] = str(value)
                self.c.sync()
                self.c.reset()
            self.c.sync()
            self.assertEqual(self.c['a'], '1')
if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.CRITICAL)
    unittest.main()
