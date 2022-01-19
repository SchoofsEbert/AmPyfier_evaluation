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

    def test_encrypt_decrypt_amp(self):
        """Test encryption and decryption"""
        some_string = 'Some Random String to Encrypt'
        encrypted = self.crypt1.encrypt(some_string)
        self.assertEqual(self.crypt1.BS, 16)
        self.assertEqual(self.crypt1.key,
            b'\x89\xe0\x156\xac ry@\x9dM\xe1\xe5%>\x01\xf4\xa1v\x9eim\xb0\xd6\x06,\xa9\xb8\xf5gg\xc8'
            )
        self.assertEqual(self.crypt1.salt, '61606982')
        self.assertEqual(some_string, 'Some Random String to Encrypt')
        self.assertEqual(self.crypt1.decrypt(encrypted),
            'Some Random String to Encrypt')
        self.assertEqual(self.crypt1.BS, 16)
        self.assertEqual(self.crypt1.key,
            b'\x89\xe0\x156\xac ry@\x9dM\xe1\xe5%>\x01\xf4\xa1v\x9eim\xb0\xd6\x06,\xa9\xb8\xf5gg\xc8'
            )
        self.assertEqual(self.crypt1.salt, '61606982')
        self.assertEqual(some_string, 'Some Random String to Encrypt')
        with self.assertRaises(DecryptionError):
            self.crypt2.decrypt(encrypted)

    def test_encrypt_decrypt_str_emp_1_call_rem_1(self):
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

    def test_encrypt_decrypt_str_dbl_0_call_rem_0(self):
        """Test encryption and decryptionTest encryption and decryption"""
        some_string = 'Some Random String to Encrypt'
        encrypted = self.crypt1.encrypt(some_string)
        self.assertEqual(self.crypt1.BS, 16)
        self.assertEqual(self.crypt1.key,
            b'\x89\xe0\x156\xac ry@\x9dM\xe1\xe5%>\x01\xf4\xa1v\x9eim\xb0\xd6\x06,\xa9\xb8\xf5gg\xc8'
            )
        self.assertEqual(self.crypt1.salt, '61606982')
        self.assertEqual(some_string, 'Some Random String to Encrypt')
        self.assertEqual(some_string, 'Some Random String to Encrypt')
        with self.assertRaises(DecryptionError):
            self.crypt2.decrypt(encrypted)

    def test_encrypt_decrypt_call_rem_0(self):
        """Test encryption and decryption"""
        some_string = 'Some Random String to Encrypt'
        encrypted = self.crypt1.encrypt(some_string)
        self.assertEqual(self.crypt1.BS, 16)
        self.assertEqual(self.crypt1.key,
            b'\x89\xe0\x156\xac ry@\x9dM\xe1\xe5%>\x01\xf4\xa1v\x9eim\xb0\xd6\x06,\xa9\xb8\xf5gg\xc8'
            )
        self.assertEqual(self.crypt1.salt, '61606982')
        self.assertEqual(some_string, 'Some Random String to Encrypt')
        self.assertEqual(some_string, 'Some Random String to Encrypt')
        with self.assertRaises(DecryptionError):
            self.crypt2.decrypt(encrypted)
