from pippin.util.crypt import AESCrypt, DecryptionError
import unittest


class TestAESCrypt(unittest.TestCase):
    def setUp(self):
        self.crypt1 = AESCrypt('mypassword')
        self.crypt2 = AESCrypt('someotherpassword')

    def test_encrypt_decrypt(self):
        """Test encryption and decryption"""
        some_string = 'Some Random String to Encrypt'
        encrypted = self.crypt1.encrypt(some_string)
        self.assertNotEqual(encrypted, some_string)
        self.assertEqual(self.crypt1.decrypt(encrypted), some_string)
        with self.assertRaises(DecryptionError) as exc:
            self.crypt2.decrypt(encrypted)

    def test_encrypt_decrypt_amp_str_hlf_0_call_rem_0_call_rem_0(self):
        """n and decryptio"""
        some_string = 'Some Random String to Encrypt'
        encrypted = self.crypt1.encrypt(some_string)
        self.assertEqual(self.crypt1.BS, 16)
        self.assertEqual(self.crypt1.key,
            b'\x89\xe0\x156\xac ry@\x9dM\xe1\xe5%>\x01\xf4\xa1v\x9eim\xb0\xd6\x06,\xa9\xb8\xf5gg\xc8'
            )
        self.assertEqual(self.crypt1.salt, '61606982')
        self.assertEqual(some_string, 'Some Random String to Encrypt')
        self.assertEqual(some_string, 'Some Random String to Encrypt')

    def test_encrypt_decrypt_amp_call_rem_0_str_hlf_0_str_hlf_1(self):
        """Test encryption"""
        some_string = 'tring to Encry'
        encrypted = self.crypt1.encrypt(some_string)
        self.assertEqual(self.crypt1.BS, 16)
        self.assertEqual(self.crypt1.key,
            b'\x89\xe0\x156\xac ry@\x9dM\xe1\xe5%>\x01\xf4\xa1v\x9eim\xb0\xd6\x06,\xa9\xb8\xf5gg\xc8'
            )
        self.assertEqual(self.crypt1.salt, '61606982')
        self.assertEqual(some_string, 'tring to Encry')
        self.assertEqual(some_string, 'tring to Encry')
        with self.assertRaises(DecryptionError):
            self.crypt2.decrypt(encrypted)

    def test_encrypt_decrypt_amp_str_dbl_1_call_rem_0_call_rem_0(self):
        """Test encryption and decryption"""
        some_string = (
            'Some Random String to EncryptSome Random String to Encrypt')
        encrypted = self.crypt1.encrypt(some_string)
        self.assertEqual(self.crypt1.BS, 16)
        self.assertEqual(self.crypt1.key,
            b'\x89\xe0\x156\xac ry@\x9dM\xe1\xe5%>\x01\xf4\xa1v\x9eim\xb0\xd6\x06,\xa9\xb8\xf5gg\xc8'
            )
        self.assertEqual(self.crypt1.salt, '61606982')
        self.assertEqual(some_string,
            'Some Random String to EncryptSome Random String to Encrypt')
        self.assertEqual(some_string,
            'Some Random String to EncryptSome Random String to Encrypt')

    def test_encrypt_decrypt_amp_str_emp_1_call_rem_0(self):
        """Test encryption and decryption"""
        some_string = ''
        encrypted = self.crypt1.encrypt(some_string)
        self.assertEqual(self.crypt1.BS, 16)
        self.assertEqual(self.crypt1.key,
            b'\x89\xe0\x156\xac ry@\x9dM\xe1\xe5%>\x01\xf4\xa1v\x9eim\xb0\xd6\x06,\xa9\xb8\xf5gg\xc8'
            )
        self.assertEqual(self.crypt1.salt, '61606982')
        self.assertEqual(some_string, '')
        self.assertEqual(self.crypt1.decrypt(encrypted), '')
        self.assertEqual(self.crypt1.BS, 16)
        self.assertEqual(self.crypt1.key,
            b'\x89\xe0\x156\xac ry@\x9dM\xe1\xe5%>\x01\xf4\xa1v\x9eim\xb0\xd6\x06,\xa9\xb8\xf5gg\xc8'
            )
        self.assertEqual(self.crypt1.salt, '61606982')
        self.assertEqual(some_string, '')
