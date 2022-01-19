



# /home/ubuntu/projects/pippin_nano_wallet/pippin/util/validators.py

## Newly Killed Mutants

### test_valid_address_str_dbl_3
  
Lines 24:30

```diff
	    @staticmethod
	    def validate_checksum_xrb(address: str) -> bool:
	        """Given an xrb/nano/ban address validate the checksum"""
-	        if (address[:5] == 'nano_' and len(address) == 65) or (address[:4] in ['ban_', 'xrb_']  and len(address) == 64):
+	        if (address[:5] == 'nano_' and len(address) == 65) or (address[:4] in ['ban_', 'xrb_']  and (len(address) >= 64)):
	            # Populate 32-char account index
	            account_map = "13456789abcdefghijkmnopqrstuwxyz"
	            account_lookup = {}

```
### test_valid_address_str_dbl_7
  
Lines 24:30

```diff
	    @staticmethod
	    def validate_checksum_xrb(address: str) -> bool:
	        """Given an xrb/nano/ban address validate the checksum"""
-	        if (address[:5] == 'nano_' and len(address) == 65) or (address[:4] in ['ban_', 'xrb_']  and len(address) == 64):
+	        if (address[:5] == 'nano_' and (len(address) >= 65)) or (address[:4] in ['ban_', 'xrb_']  and len(address) == 64):
	            # Populate 32-char account index
	            account_map = "13456789abcdefghijkmnopqrstuwxyz"
	            account_lookup = {}

```
### test_valid_address_str_dbl_7_str_hlf_7
  
Lines 24:30

```diff
	    @staticmethod
	    def validate_checksum_xrb(address: str) -> bool:
	        """Given an xrb/nano/ban address validate the checksum"""
-	        if (address[:5] == 'nano_' and len(address) == 65) or (address[:4] in ['ban_', 'xrb_']  and len(address) == 64):
+	        if ((address[:5] <= 'nano_') and len(address) == 65) or (address[:4] in ['ban_', 'xrb_']  and len(address) == 64):
	            # Populate 32-char account index
	            account_map = "13456789abcdefghijkmnopqrstuwxyz"
	            account_lookup = {}

```
## Alive Mutants
  
Lines 8:14

```diff
	    def is_valid_address(cls, input_text: str) -> bool:
	        """Return True if address is valid, false otherwise"""
	        if input_text is None:
-	            return False
+	            return None
	        return cls.validate_checksum_xrb(input_text)
	
	    @staticmethod

```  
Lines 14:20

```diff
	    @staticmethod
	    def is_valid_block_hash(block_hash: str) -> bool:
	        if block_hash is None or len(block_hash) != 64:
-	            return False
+	            return None
	        try:
	            int(block_hash, 16)
	        except ValueError:

```  
Lines 18:24

```diff
	        try:
	            int(block_hash, 16)
	        except ValueError:
-	            return False
+	            return None
	        return True
	
	    @staticmethod

```  
Lines 24:30

```diff
	    @staticmethod
	    def validate_checksum_xrb(address: str) -> bool:
	        """Given an xrb/nano/ban address validate the checksum"""
-	        if (address[:5] == 'nano_' and len(address) == 65) or (address[:4] in ['ban_', 'xrb_']  and len(address) == 64):
+	        if ((address[:5] >= 'nano_') and len(address) == 65) or (address[:4] in ['ban_', 'xrb_']  and len(address) == 64):
	            # Populate 32-char account index
	            account_map = "13456789abcdefghijkmnopqrstuwxyz"
	            account_lookup = {}

```  
Lines 50:54

```diff
	            # verify checksum
	            h = blake2b(digest_size=5)
	            h.update(number_l.bytes)
-	            return h.hexdigest() == check_l.hex
+	            return (h.hexdigest() <= check_l.hex)
	        return False
```  
Lines 51:54

```diff
	            h = blake2b(digest_size=5)
	            h.update(number_l.bytes)
	            return h.hexdigest() == check_l.hex
-	        return False+	        return None	
```