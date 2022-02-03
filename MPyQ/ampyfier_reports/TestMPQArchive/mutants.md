



# /home/ubuntu/projects/mpyq/mpyq.py

## Newly Killed Mutants

### test_init_with_file_str_dbl_0
  
Lines 141:147

```diff
	        magic = self.file.read(4)
	        self.file.seek(0)
	
-	        if magic == b'MPQ\x1a':
+	        if (magic <= b'MPQ\x1a'):
	            header = read_mpq_header()
	            header['offset'] = 0
	        elif magic == b'MPQ\x1b':

```  
Lines 141:147

```diff
	        magic = self.file.read(4)
	        self.file.seek(0)
	
-	        if magic == b'MPQ\x1a':
+	        if (magic < b'MPQ\x1a'):
	            header = read_mpq_header()
	            header['offset'] = 0
	        elif magic == b'MPQ\x1b':

```  
Lines 144:150

```diff
	        if magic == b'MPQ\x1a':
	            header = read_mpq_header()
	            header['offset'] = 0
-	        elif magic == b'MPQ\x1b':
+	        elif True:
	            user_data_header = read_mpq_user_data_header()
	            header = read_mpq_header(user_data_header['mpq_header_offset'])
	            header['offset'] = user_data_header['mpq_header_offset']

```  
Lines 144:150

```diff
	        if magic == b'MPQ\x1a':
	            header = read_mpq_header()
	            header['offset'] = 0
-	        elif magic == b'MPQ\x1b':
+	        elif (magic <= b'MPQ\x1b'):
	            user_data_header = read_mpq_user_data_header()
	            header = read_mpq_header(user_data_header['mpq_header_offset'])
	            header['offset'] = user_data_header['mpq_header_offset']

```
### test_init_with_file_str_dbl_0_str_hlf_1
  
Lines 144:150

```diff
	        if magic == b'MPQ\x1a':
	            header = read_mpq_header()
	            header['offset'] = 0
-	        elif magic == b'MPQ\x1b':
+	        elif (magic >= b'MPQ\x1b'):
	            user_data_header = read_mpq_user_data_header()
	            header = read_mpq_header(user_data_header['mpq_header_offset'])
	            header['offset'] = user_data_header['mpq_header_offset']

```
## Alive Mutants
  
Lines 100:106

```diff
	        self.header = self.read_header()
	        self.hash_table = self.read_table('hash')
	        self.block_table = self.read_table('block')
-	        if listfile:
+	        if True:
	            self.files = self.read_file('(listfile)').splitlines()
	        else:
	            self.files = None

```  
Lines 106:112

```diff
	            self.files = None
	
	    def close(self):
-	        if self.file:
+	        if False:
	            self.file.close()
	        self.file = None
	

```  
Lines 106:112

```diff
	            self.files = None
	
	    def close(self):
-	        if self.file:
+	        if True:
	            self.file.close()
	        self.file = None
	

```  
Lines 108:114

```diff
	    def close(self):
	        if self.file:
	            self.file.close()
-	        self.file = None
+	        self.file = (False)
	
	    def __del__(self):
	        self.close()

```  
Lines 108:114

```diff
	    def close(self):
	        if self.file:
	            self.file.close()
-	        self.file = None
+	        self.file = (True)
	
	    def __del__(self):
	        self.close()

```  
Lines 116:122

```diff
	    def read_header(self):
	        """Read the header of a MPQ archive."""
	
-	        def read_mpq_header(offset=None):
+	        def read_mpq_header(offset=(False)):
	            if offset:
	                self.file.seek(offset)
	            data = self.file.read(32)

```  
Lines 116:122

```diff
	    def read_header(self):
	        """Read the header of a MPQ archive."""
	
-	        def read_mpq_header(offset=None):
+	        def read_mpq_header(offset=(True)):
	            if offset:
	                self.file.seek(offset)
	            data = self.file.read(32)

```  
Lines 117:123

```diff
	        """Read the header of a MPQ archive."""
	
	        def read_mpq_header(offset=None):
-	            if offset:
+	            if True:
	                self.file.seek(offset)
	            data = self.file.read(32)
	            header = MPQFileHeader._make(

```  
Lines 123:129

```diff
	            header = MPQFileHeader._make(
	                struct.unpack(MPQFileHeader.struct_format, data))
	            header = header._asdict()
-	            if header['format_version'] == 1:
+	            if True:
	                data = self.file.read(12)
	                extended_header = MPQFileHeaderExt._make(
	                    struct.unpack(MPQFileHeaderExt.struct_format, data))

```  
Lines 123:129

```diff
	            header = MPQFileHeader._make(
	                struct.unpack(MPQFileHeader.struct_format, data))
	            header = header._asdict()
-	            if header['format_version'] == 1:
+	            if (header['format_version'] <= 1):
	                data = self.file.read(12)
	                extended_header = MPQFileHeaderExt._make(
	                    struct.unpack(MPQFileHeaderExt.struct_format, data))

```  
Lines 123:129

```diff
	            header = MPQFileHeader._make(
	                struct.unpack(MPQFileHeader.struct_format, data))
	            header = header._asdict()
-	            if header['format_version'] == 1:
+	            if (header['format_version'] >= 1):
	                data = self.file.read(12)
	                extended_header = MPQFileHeaderExt._make(
	                    struct.unpack(MPQFileHeaderExt.struct_format, data))

```  
Lines 141:147

```diff
	        magic = self.file.read(4)
	        self.file.seek(0)
	
-	        if magic == b'MPQ\x1a':
+	        if False:
	            header = read_mpq_header()
	            header['offset'] = 0
	        elif magic == b'MPQ\x1b':

```  
Lines 157:163

```diff
	    def read_table(self, table_type):
	        """Read either the hash or block table of a MPQ archive."""
	
-	        if table_type == 'hash':
+	        if (table_type >= 'hash'):
	            entry_class = MPQHashTableEntry
	        elif table_type == 'block':
	            entry_class = MPQBlockTableEntry

```  
Lines 159:165

```diff
	
	        if table_type == 'hash':
	            entry_class = MPQHashTableEntry
-	        elif table_type == 'block':
+	        elif True:
	            entry_class = MPQBlockTableEntry
	        else:
	            raise ValueError("Invalid table type.")

```  
Lines 159:165

```diff
	
	        if table_type == 'hash':
	            entry_class = MPQHashTableEntry
-	        elif table_type == 'block':
+	        elif (table_type <= 'block'):
	            entry_class = MPQBlockTableEntry
	        else:
	            raise ValueError("Invalid table type.")

```  
Lines 159:165

```diff
	
	        if table_type == 'hash':
	            entry_class = MPQHashTableEntry
-	        elif table_type == 'block':
+	        elif (table_type >= 'block'):
	            entry_class = MPQBlockTableEntry
	        else:
	            raise ValueError("Invalid table type.")

```  
Lines 184:190

```diff
	        hash_a = self._hash(filename, 'HASH_A')
	        hash_b = self._hash(filename, 'HASH_B')
	        for entry in self.hash_table:
-	            if (entry.hash_a == hash_a and entry.hash_b == hash_b):
+	            if ((entry.hash_a == hash_a or entry.hash_b == hash_b)):
	                return entry
	
	    def read_file(self, filename, force_decompress=False):

```  
Lines 184:190

```diff
	        hash_a = self._hash(filename, 'HASH_A')
	        hash_b = self._hash(filename, 'HASH_B')
	        for entry in self.hash_table:
-	            if (entry.hash_a == hash_a and entry.hash_b == hash_b):
+	            if ((entry.hash_a <= hash_a) and entry.hash_b == hash_b):
	                return entry
	
	    def read_file(self, filename, force_decompress=False):

```  
Lines 184:190

```diff
	        hash_a = self._hash(filename, 'HASH_A')
	        hash_b = self._hash(filename, 'HASH_B')
	        for entry in self.hash_table:
-	            if (entry.hash_a == hash_a and entry.hash_b == hash_b):
+	            if ((entry.hash_a >= hash_a) and entry.hash_b == hash_b):
	                return entry
	
	    def read_file(self, filename, force_decompress=False):

```  
Lines 184:190

```diff
	        hash_a = self._hash(filename, 'HASH_A')
	        hash_b = self._hash(filename, 'HASH_B')
	        for entry in self.hash_table:
-	            if (entry.hash_a == hash_a and entry.hash_b == hash_b):
+	            if (entry.hash_a == hash_a and (entry.hash_b <= hash_b)):
	                return entry
	
	    def read_file(self, filename, force_decompress=False):

```  
Lines 184:190

```diff
	        hash_a = self._hash(filename, 'HASH_A')
	        hash_b = self._hash(filename, 'HASH_B')
	        for entry in self.hash_table:
-	            if (entry.hash_a == hash_a and entry.hash_b == hash_b):
+	            if (entry.hash_a == hash_a and (entry.hash_b >= hash_b)):
	                return entry
	
	    def read_file(self, filename, force_decompress=False):

```  
Lines 187:193

```diff
	            if (entry.hash_a == hash_a and entry.hash_b == hash_b):
	                return entry
	
-	    def read_file(self, filename, force_decompress=False):
+	    def read_file(self, filename, force_decompress=(True)):
	        """Read a file from the MPQ archive."""
	
	        def decompress(data):

```  
Lines 187:193

```diff
	            if (entry.hash_a == hash_a and entry.hash_b == hash_b):
	                return entry
	
-	    def read_file(self, filename, force_decompress=False):
+	    def read_file(self, filename, force_decompress=None):
	        """Read a file from the MPQ archive."""
	
	        def decompress(data):

```  
Lines 193:199

```diff
	        def decompress(data):
	            """Read the compression type and decompress file data."""
	            compression_type = ord(data[0:1])
-	            if compression_type == 0:
+	            if False:
	                return data
	            elif compression_type == 2:
	                return zlib.decompress(data[1:], 15)

```  
Lines 193:199

```diff
	        def decompress(data):
	            """Read the compression type and decompress file data."""
	            compression_type = ord(data[0:1])
-	            if compression_type == 0:
+	            if (compression_type <= 0):
	                return data
	            elif compression_type == 2:
	                return zlib.decompress(data[1:], 15)

```  
Lines 193:199

```diff
	        def decompress(data):
	            """Read the compression type and decompress file data."""
	            compression_type = ord(data[0:1])
-	            if compression_type == 0:
+	            if (compression_type < 0):
	                return data
	            elif compression_type == 2:
	                return zlib.decompress(data[1:], 15)

```  
Lines 195:201

```diff
	            compression_type = ord(data[0:1])
	            if compression_type == 0:
	                return data
-	            elif compression_type == 2:
+	            elif False:
	                return zlib.decompress(data[1:], 15)
	            elif compression_type == 16:
	                return bz2.decompress(data[1:])

```  
Lines 195:201

```diff
	            compression_type = ord(data[0:1])
	            if compression_type == 0:
	                return data
-	            elif compression_type == 2:
+	            elif (compression_type <= 2):
	                return zlib.decompress(data[1:], 15)
	            elif compression_type == 16:
	                return bz2.decompress(data[1:])

```  
Lines 195:201

```diff
	            compression_type = ord(data[0:1])
	            if compression_type == 0:
	                return data
-	            elif compression_type == 2:
+	            elif (compression_type < 2):
	                return zlib.decompress(data[1:], 15)
	            elif compression_type == 16:
	                return bz2.decompress(data[1:])

```  
Lines 197:203

```diff
	                return data
	            elif compression_type == 2:
	                return zlib.decompress(data[1:], 15)
-	            elif compression_type == 16:
+	            elif (compression_type <= 16):
	                return bz2.decompress(data[1:])
	            else:
	                msg = "Unsupported compression type: {}".format(compression_type)

```  
Lines 197:203

```diff
	                return data
	            elif compression_type == 2:
	                return zlib.decompress(data[1:], 15)
-	            elif compression_type == 16:
+	            elif (compression_type >= 16):
	                return bz2.decompress(data[1:])
	            else:
	                msg = "Unsupported compression type: {}".format(compression_type)

```  
Lines 197:203

```diff
	                return data
	            elif compression_type == 2:
	                return zlib.decompress(data[1:], 15)
-	            elif compression_type == 16:
+	            elif True:
	                return bz2.decompress(data[1:])
	            else:
	                msg = "Unsupported compression type: {}".format(compression_type)

```  
Lines 204:210

```diff
	                raise RuntimeError(msg)
	
	        hash_entry = self.get_hash_table_entry(filename)
-	        if hash_entry is None:
+	        if hash_entry is (False):
	            return None
	        block_entry = self.block_table[hash_entry.block_table_index]
	

```  
Lines 204:210

```diff
	                raise RuntimeError(msg)
	
	        hash_entry = self.get_hash_table_entry(filename)
-	        if hash_entry is None:
+	        if hash_entry is (True):
	            return None
	        block_entry = self.block_table[hash_entry.block_table_index]
	

```  
Lines 204:210

```diff
	                raise RuntimeError(msg)
	
	        hash_entry = self.get_hash_table_entry(filename)
-	        if hash_entry is None:
+	        if False:
	            return None
	        block_entry = self.block_table[hash_entry.block_table_index]
	

```  
Lines 209:215

```diff
	        block_entry = self.block_table[hash_entry.block_table_index]
	
	        # Read the block.
-	        if block_entry.flags & MPQ_FILE_EXISTS:
+	        if (block_entry.flags ^ MPQ_FILE_EXISTS):
	            if block_entry.archived_size == 0:
	                return None
	

```  
Lines 209:215

```diff
	        block_entry = self.block_table[hash_entry.block_table_index]
	
	        # Read the block.
-	        if block_entry.flags & MPQ_FILE_EXISTS:
+	        if (block_entry.flags | MPQ_FILE_EXISTS):
	            if block_entry.archived_size == 0:
	                return None
	

```  
Lines 209:215

```diff
	        block_entry = self.block_table[hash_entry.block_table_index]
	
	        # Read the block.
-	        if block_entry.flags & MPQ_FILE_EXISTS:
+	        if True:
	            if block_entry.archived_size == 0:
	                return None
	

```  
Lines 210:216

```diff
	
	        # Read the block.
	        if block_entry.flags & MPQ_FILE_EXISTS:
-	            if block_entry.archived_size == 0:
+	            if (block_entry.archived_size <= 0):
	                return None
	
	            offset = block_entry.offset + self.header['offset']

```  
Lines 210:216

```diff
	
	        # Read the block.
	        if block_entry.flags & MPQ_FILE_EXISTS:
-	            if block_entry.archived_size == 0:
+	            if (block_entry.archived_size < 0):
	                return None
	
	            offset = block_entry.offset + self.header['offset']

```  
Lines 210:216

```diff
	
	        # Read the block.
	        if block_entry.flags & MPQ_FILE_EXISTS:
-	            if block_entry.archived_size == 0:
+	            if False:
	                return None
	
	            offset = block_entry.offset + self.header['offset']

```  
Lines 217:223

```diff
	            self.file.seek(offset)
	            file_data = self.file.read(block_entry.archived_size)
	
-	            if block_entry.flags & MPQ_FILE_ENCRYPTED:
+	            if False:
	                raise NotImplementedError("Encryption is not supported yet.")
	
	            if not block_entry.flags & MPQ_FILE_SINGLE_UNIT:

```  
Lines 220:226

```diff
	            if block_entry.flags & MPQ_FILE_ENCRYPTED:
	                raise NotImplementedError("Encryption is not supported yet.")
	
-	            if not block_entry.flags & MPQ_FILE_SINGLE_UNIT:
+	            if False:
	                # File consists of many sectors. They all need to be
	                # decompressed separately and united.
	                sector_size = 512 << self.header['sector_size_shift']

```  
Lines 220:226

```diff
	            if block_entry.flags & MPQ_FILE_ENCRYPTED:
	                raise NotImplementedError("Encryption is not supported yet.")
	
-	            if not block_entry.flags & MPQ_FILE_SINGLE_UNIT:
+	            if not (block_entry.flags ^ MPQ_FILE_SINGLE_UNIT):
	                # File consists of many sectors. They all need to be
	                # decompressed separately and united.
	                sector_size = 512 << self.header['sector_size_shift']

```  
Lines 220:226

```diff
	            if block_entry.flags & MPQ_FILE_ENCRYPTED:
	                raise NotImplementedError("Encryption is not supported yet.")
	
-	            if not block_entry.flags & MPQ_FILE_SINGLE_UNIT:
+	            if not (block_entry.flags | MPQ_FILE_SINGLE_UNIT):
	                # File consists of many sectors. They all need to be
	                # decompressed separately and united.
	                sector_size = 512 << self.header['sector_size_shift']

```  
Lines 246:253

```diff
	            else:
	                # Single unit files only need to be decompressed, but
	                # compression only happens when at least one byte is gained.
-	                if (block_entry.flags & MPQ_FILE_COMPRESS and
-	                    (force_decompress or block_entry.size > block_entry.archived_size)):
+	                if True:
	                    file_data = decompress(file_data)
	
	            return file_data

```  
Lines 246:253

```diff
	            else:
	                # Single unit files only need to be decompressed, but
	                # compression only happens when at least one byte is gained.
-	                if (block_entry.flags & MPQ_FILE_COMPRESS and
-	                    (force_decompress or block_entry.size > block_entry.archived_size)):
+	                if ((block_entry.flags & MPQ_FILE_COMPRESS or (force_decompress or block_entry.
    size > block_entry.archived_size))):
	                    file_data = decompress(file_data)
	
	            return file_data

```  
Lines 246:252

```diff
	            else:
	                # Single unit files only need to be decompressed, but
	                # compression only happens when at least one byte is gained.
-	                if (block_entry.flags & MPQ_FILE_COMPRESS and
+	                if ((block_entry.flags ^ MPQ_FILE_COMPRESS) and
	                    (force_decompress or block_entry.size > block_entry.archived_size)):
	                    file_data = decompress(file_data)
	

```  
Lines 246:252

```diff
	            else:
	                # Single unit files only need to be decompressed, but
	                # compression only happens when at least one byte is gained.
-	                if (block_entry.flags & MPQ_FILE_COMPRESS and
+	                if ((block_entry.flags | MPQ_FILE_COMPRESS) and
	                    (force_decompress or block_entry.size > block_entry.archived_size)):
	                    file_data = decompress(file_data)
	

```  
Lines 247:253

```diff
	                # Single unit files only need to be decompressed, but
	                # compression only happens when at least one byte is gained.
	                if (block_entry.flags & MPQ_FILE_COMPRESS and
-	                    (force_decompress or block_entry.size > block_entry.archived_size)):
+	                    (force_decompress or (block_entry.size != block_entry.archived_size))):
	                    file_data = decompress(file_data)
	
	            return file_data

```  
Lines 247:253

```diff
	                # Single unit files only need to be decompressed, but
	                # compression only happens when at least one byte is gained.
	                if (block_entry.flags & MPQ_FILE_COMPRESS and
-	                    (force_decompress or block_entry.size > block_entry.archived_size)):
+	                    (force_decompress or (block_entry.size >= block_entry.archived_size))):
	                    file_data = decompress(file_data)
	
	            return file_data

```  
Lines 333:339

```diff
	        seed2 = 0xEEEEEEEE
	
	        for ch in string.upper():
-	            if not isinstance(ch, int): ch = ord(ch)
+	            if True: ch = ord(ch)
	            value = self.encryption_table[(hash_types[hash_type] << 8) + ch]
	            seed1 = (value ^ (seed1 + seed2)) & 0xFFFFFFFF
	            seed2 = ch + seed1 + seed2 + (seed2 << 5) + 3 & 0xFFFFFFFF

```  
Lines 349:355

```diff
	        for i in range(len(data) // 4):
	            seed2 += self.encryption_table[0x400 + (seed1 & 0xFF)]
	            seed2 &= 0xFFFFFFFF
-	            value = struct.unpack("<I", data[i*4:i*4+4])[0]
+	            value = struct.unpack("<I", data[i*4:i*4+4])[<_ast.Constant object at 0x7fe642535f70>]
	            value = (value ^ (seed1 + seed2)) & 0xFFFFFFFF
	
	            seed1 = ((~seed1 << 0x15) + 0x11111111) | (seed1 >> 0x0B)

```  
Lines 374:380

```diff
	                seed = (seed * 125 + 3) % 0x2AAAAB
	                temp2 = (seed & 0xFFFF)
	
-	                crypt_table[index] = (temp1 | temp2)
+	                crypt_table[index] = ((temp1 ^ temp2))
	
	                index += 0x100
	

```  
Lines 418:422

```diff
	            archive.extract_to_disk()
	
	
-	if __name__ == '__main__':
+	if (__name__ <= '__main__'):
	    main()

```  
Lines 418:422

```diff
	            archive.extract_to_disk()
	
	
-	if __name__ == '__main__':
+	if (__name__ < '__main__'):
	    main()

```  
Lines 418:422

```diff
	            archive.extract_to_disk()
	
	
-	if __name__ == '__main__':
+	if False:
	    main()

```