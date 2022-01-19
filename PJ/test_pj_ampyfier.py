import unittest
import pj


class TestStringMethods(unittest.TestCase):

    def test_empty_object(self):
        self.assertEqual(pj.from_string('{}'), {})

    def test_basic_object(self):
        self.assertEqual(pj.from_string('{"foo":"bar"}'), {'foo': 'bar'})

    def test_basic_number(self):
        self.assertEqual(pj.from_string('{"foo":1}'), {'foo': 1})

    def test_empty_array(self):
        self.assertEqual(pj.from_string('{"foo":[]}'), {'foo': []})

    def test_basic_array(self):
        self.assertEqual(pj.from_string('{"foo":[1,2,"three"]}'), {'foo': [
            1, 2, 'three']})

    def test_nested_object(self):
        self.assertEqual(pj.from_string('{"foo":{"bar":2}}'), {'foo': {
            'bar': 2}})

    def test_true(self):
        self.assertEqual(pj.from_string('{"foo":true}'), {'foo': True})

    def test_false(self):
        self.assertEqual(pj.from_string('{"foo":false}'), {'foo': False})

    def test_null(self):
        self.assertEqual(pj.from_string('{"foo":null}'), {'foo': None})

    def test_basic_whitespace(self):
        self.assertEqual(pj.from_string('{ "foo" : [1, 2, "three"] }'), {
            'foo': [1, 2, 'three']})

    def test_empty_object_str_emp_0_str_chr_0(self):
        with self.assertRaises(Exception):
            pj.from_string('n')

    def test_empty_object_str_hlf_0(self):
        with self.assertRaises(Exception):
            pj.from_string('}')

    def test_basic_object_str_hlf_0_str_hlf_0(self):
        with self.assertRaises(Exception):
            pj.from_string(':"b')

    def test_basic_object_call_add_0_call_add_1_str_hlf_0(self):
        with self.assertRaises(Exception):
            pj.from_string('"foo":')

    def test_nested_object_call_add_0_str_hlf_0_str_dbl_0(self):
        with self.assertRaises(Exception):
            pj.from_string('{"bar":2{"bar":2')

    def test_false_call_dup_0_str_hlf_1_str_dbl_0(self):
        self.assertEqual(pj.from_string('{"foo":false}'), {'foo': False})
        with self.assertRaises(Exception):
            pj.from_string('{"foo"{"foo"')


if __name__ == '__main__':
    unittest.main()
