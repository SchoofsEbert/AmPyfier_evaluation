



# /home/ubuntu/projects/pippin_nano_wallet/pippin/util/crypt.py

## Newly Killed Mutants

### test_encrypt_decrypt_str_dbl_0_call_rem_0
  
Lines 29:35

```diff
	        # Test if decrypt was successful
	        if len(decrypted) < len(self.salt):
	            raise DecryptionError()
-	        elif decrypted[:len(self.salt)] != self.salt:
+	        elif False:
	            raise DecryptionError()
	        return decrypted[len(self.salt):]
	

```
### test_encrypt_decrypt_call_rem_0
  
Lines 29:35

```diff
	        # Test if decrypt was successful
	        if len(decrypted) < len(self.salt):
	            raise DecryptionError()
-	        elif decrypted[:len(self.salt)] != self.salt:
+	        elif (decrypted[:len(self.salt)] > self.salt):
	            raise DecryptionError()
	        return decrypted[len(self.salt):]
	

```
### test_encrypt_decrypt_str_emp_1_call_rem_1
  
Lines 27:33

```diff
	        cipher = AES.new(self.key, AES.MODE_CBC, iv)
	        decrypted = self.unpad(cipher.decrypt(encrypted[16:])).decode('latin-1')
	        # Test if decrypt was successful
-	        if len(decrypted) < len(self.salt):
+	        if (len(decrypted) == len(self.salt)):
	            raise DecryptionError()
	        elif decrypted[:len(self.salt)] != self.salt:
	            raise DecryptionError()

```  
Lines 27:33

```diff
	        cipher = AES.new(self.key, AES.MODE_CBC, iv)
	        decrypted = self.unpad(cipher.decrypt(encrypted[16:])).decode('latin-1')
	        # Test if decrypt was successful
-	        if len(decrypted) < len(self.salt):
+	        if (len(decrypted) <= len(self.salt)):
	            raise DecryptionError()
	        elif decrypted[:len(self.salt)] != self.salt:
	            raise DecryptionError()

```
## Alive Mutants
  
Lines 27:33

```diff
	        cipher = AES.new(self.key, AES.MODE_CBC, iv)
	        decrypted = self.unpad(cipher.decrypt(encrypted[16:])).decode('latin-1')
	        # Test if decrypt was successful
-	        if len(decrypted) < len(self.salt):
+	        if False:
	            raise DecryptionError()
	        elif decrypted[:len(self.salt)] != self.salt:
	            raise DecryptionError()

```