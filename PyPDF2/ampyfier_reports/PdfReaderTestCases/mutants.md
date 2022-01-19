



# /home/ubuntu/projects/PyPDF2/PyPDF2/generic.py

## Newly Killed Mutants

## Alive Mutants
  
Lines 62:68

```diff
	        # hexadecimal string OR dictionary
	        peek = stream.read(2)
	        stream.seek(-2, 1) # reset to start
-	        if peek == b_('<<'):
+	        if (peek >= b_('<<')):
	            return DictionaryObject.readFromStream(stream, pdf)
	        else:
	            return readHexStringFromStream(stream)

```  
Lines 66:72

```diff
	            return DictionaryObject.readFromStream(stream, pdf)
	        else:
	            return readHexStringFromStream(stream)
-	    elif idx == 2:
+	    elif (idx >= 2):
	        # array object
	        return ArrayObject.readFromStream(stream, pdf)
	    elif idx == 3 or idx == 4:

```  
Lines 69:75

```diff
	    elif idx == 2:
	        # array object
	        return ArrayObject.readFromStream(stream, pdf)
-	    elif idx == 3 or idx == 4:
+	    elif (idx == 3 and idx == 4):
	        # boolean object
	        return BooleanObject.readFromStream(stream)
	    elif idx == 5:

```  
Lines 69:75

```diff
	    elif idx == 2:
	        # array object
	        return ArrayObject.readFromStream(stream, pdf)
-	    elif idx == 3 or idx == 4:
+	    elif False:
	        # boolean object
	        return BooleanObject.readFromStream(stream)
	    elif idx == 5:

```  
Lines 69:75

```diff
	    elif idx == 2:
	        # array object
	        return ArrayObject.readFromStream(stream, pdf)
-	    elif idx == 3 or idx == 4:
+	    elif (idx >= 3) or idx == 4:
	        # boolean object
	        return BooleanObject.readFromStream(stream)
	    elif idx == 5:

```  
Lines 69:75

```diff
	    elif idx == 2:
	        # array object
	        return ArrayObject.readFromStream(stream, pdf)
-	    elif idx == 3 or idx == 4:
+	    elif (idx > 3) or idx == 4:
	        # boolean object
	        return BooleanObject.readFromStream(stream)
	    elif idx == 5:

```  
Lines 69:75

```diff
	    elif idx == 2:
	        # array object
	        return ArrayObject.readFromStream(stream, pdf)
-	    elif idx == 3 or idx == 4:
+	    elif idx == 3 or (idx >= 4):
	        # boolean object
	        return BooleanObject.readFromStream(stream)
	    elif idx == 5:

```  
Lines 69:75

```diff
	    elif idx == 2:
	        # array object
	        return ArrayObject.readFromStream(stream, pdf)
-	    elif idx == 3 or idx == 4:
+	    elif idx == 3 or (idx > 4):
	        # boolean object
	        return BooleanObject.readFromStream(stream)
	    elif idx == 5:

```  
Lines 72:78

```diff
	    elif idx == 3 or idx == 4:
	        # boolean object
	        return BooleanObject.readFromStream(stream)
-	    elif idx == 5:
+	    elif False:
	        # string object
	        return readStringFromStream(stream)
	    elif idx == 6:

```  
Lines 72:78

```diff
	    elif idx == 3 or idx == 4:
	        # boolean object
	        return BooleanObject.readFromStream(stream)
-	    elif idx == 5:
+	    elif (idx >= 5):
	        # string object
	        return readStringFromStream(stream)
	    elif idx == 6:

```  
Lines 72:78

```diff
	    elif idx == 3 or idx == 4:
	        # boolean object
	        return BooleanObject.readFromStream(stream)
-	    elif idx == 5:
+	    elif (idx > 5):
	        # string object
	        return readStringFromStream(stream)
	    elif idx == 6:

```  
Lines 75:81

```diff
	    elif idx == 5:
	        # string object
	        return readStringFromStream(stream)
-	    elif idx == 6:
+	    elif False:
	        # null object
	        return NullObject.readFromStream(stream)
	    elif idx == 7:

```  
Lines 75:81

```diff
	    elif idx == 5:
	        # string object
	        return readStringFromStream(stream)
-	    elif idx == 6:
+	    elif (idx >= 6):
	        # null object
	        return NullObject.readFromStream(stream)
	    elif idx == 7:

```  
Lines 75:81

```diff
	    elif idx == 5:
	        # string object
	        return readStringFromStream(stream)
-	    elif idx == 6:
+	    elif (idx > 6):
	        # null object
	        return NullObject.readFromStream(stream)
	    elif idx == 7:

```  
Lines 78:84

```diff
	    elif idx == 6:
	        # null object
	        return NullObject.readFromStream(stream)
-	    elif idx == 7:
+	    elif False:
	        # comment
	        while tok not in (b_('\r'), b_('\n')):
	            tok = stream.read(1)

```  
Lines 78:84

```diff
	    elif idx == 6:
	        # null object
	        return NullObject.readFromStream(stream)
-	    elif idx == 7:
+	    elif (idx >= 7):
	        # comment
	        while tok not in (b_('\r'), b_('\n')):
	            tok = stream.read(1)

```  
Lines 78:84

```diff
	    elif idx == 6:
	        # null object
	        return NullObject.readFromStream(stream)
-	    elif idx == 7:
+	    elif (idx > 7):
	        # comment
	        while tok not in (b_('\r'), b_('\n')):
	            tok = stream.read(1)

```  
Lines 150:156

```diff
	    def readFromStream(stream, pdf):
	        arr = ArrayObject()
	        tmp = stream.read(1)
-	        if tmp != b_("["):
+	        if (tmp < b_('[')):
	            raise utils.PdfReadError("Could not read array")
	        while True:
	            # skip leading whitespace

```  
Lines 150:156

```diff
	    def readFromStream(stream, pdf):
	        arr = ArrayObject()
	        tmp = stream.read(1)
-	        if tmp != b_("["):
+	        if (tmp > b_('[')):
	            raise utils.PdfReadError("Could not read array")
	        while True:
	            # skip leading whitespace

```  
Lines 150:156

```diff
	    def readFromStream(stream, pdf):
	        arr = ArrayObject()
	        tmp = stream.read(1)
-	        if tmp != b_("["):
+	        if False:
	            raise utils.PdfReadError("Could not read array")
	        while True:
	            # skip leading whitespace

```  
Lines 160:166

```diff
	            stream.seek(-1, 1)
	            # check for array ending
	            peekahead = stream.read(1)
-	            if peekahead == b_("]"):
+	            if (peekahead >= b_(']')):
	                break
	            stream.seek(-1, 1)
	            # read and append obj

```  
Lines 179:185

```diff
	        return self.pdf.getObject(self).getObject()
	
	    def __repr__(self):
-	        return "IndirectObject(%r, %r)" % (self.idnum, self.generation)
+	        return ('IndirectObject(%r, %r)' // (self.idnum, self.generation))
	
	    def __eq__(self, other):
	        return (

```  
Lines 179:185

```diff
	        return self.pdf.getObject(self).getObject()
	
	    def __repr__(self):
-	        return "IndirectObject(%r, %r)" % (self.idnum, self.generation)
+	        return ('IndirectObject(%r, %r)' * (self.idnum, self.generation))
	
	    def __eq__(self, other):
	        return (

```  
Lines 179:185

```diff
	        return self.pdf.getObject(self).getObject()
	
	    def __repr__(self):
-	        return "IndirectObject(%r, %r)" % (self.idnum, self.generation)
+	        return ('IndirectObject(%r, %r)' - (self.idnum, self.generation))
	
	    def __eq__(self, other):
	        return (

```  
Lines 179:185

```diff
	        return self.pdf.getObject(self).getObject()
	
	    def __repr__(self):
-	        return "IndirectObject(%r, %r)" % (self.idnum, self.generation)
+	        return ('IndirectObject(%r, %r)' / (self.idnum, self.generation))
	
	    def __eq__(self, other):
	        return (

```  
Lines 179:185

```diff
	        return self.pdf.getObject(self).getObject()
	
	    def __repr__(self):
-	        return "IndirectObject(%r, %r)" % (self.idnum, self.generation)
+	        return ('IndirectObject(%r, %r)' + (self.idnum, self.generation))
	
	    def __eq__(self, other):
	        return (

```  
Lines 179:185

```diff
	        return self.pdf.getObject(self).getObject()
	
	    def __repr__(self):
-	        return "IndirectObject(%r, %r)" % (self.idnum, self.generation)
+	        return ('IndirectObject(%r, %r)' ** (self.idnum, self.generation))
	
	    def __eq__(self, other):
	        return (

```  
Lines 200:206

```diff
	        idnum = b_("")
	        while True:
	            tok = stream.read(1)
-	            if not tok:
+	            if False:
	                # stream has truncated prematurely
	                raise PdfStreamError("Stream has ended unexpectedly")
	            if tok.isspace():

```  
Lines 209:215

```diff
	        generation = b_("")
	        while True:
	            tok = stream.read(1)
-	            if not tok:
+	            if False:
	                # stream has truncated prematurely
	                raise PdfStreamError("Stream has ended unexpectedly")
	            if tok.isspace():

```  
Lines 213:219

```diff
	                # stream has truncated prematurely
	                raise PdfStreamError("Stream has ended unexpectedly")
	            if tok.isspace():
-	                if not generation:
+	                if False:
	                    continue
	                break
	            generation += tok

```  
Lines 218:224

```diff
	                break
	            generation += tok
	        r = readNonWhitespace(stream)
-	        if r != b_("R"):
+	        if (r < b_('R')):
	            raise utils.PdfReadError("Error reading indirect object reference at byte %s" % utils.hexStr(stream.tell()))
	        return IndirectObject(int(idnum), int(generation), pdf)
	    readFromStream = staticmethod(readFromStream)

```  
Lines 218:224

```diff
	                break
	            generation += tok
	        r = readNonWhitespace(stream)
-	        if r != b_("R"):
+	        if (r > b_('R')):
	            raise utils.PdfReadError("Error reading indirect object reference at byte %s" % utils.hexStr(stream.tell()))
	        return IndirectObject(int(idnum), int(generation), pdf)
	    readFromStream = staticmethod(readFromStream)

```  
Lines 218:224

```diff
	                break
	            generation += tok
	        r = readNonWhitespace(stream)
-	        if r != b_("R"):
+	        if False:
	            raise utils.PdfReadError("Error reading indirect object reference at byte %s" % utils.hexStr(stream.tell()))
	        return IndirectObject(int(idnum), int(generation), pdf)
	    readFromStream = staticmethod(readFromStream)

```  
Lines 225:231

```diff
	
	
	class FloatObject(decimal.Decimal, PdfObject):
-	    def __new__(cls, value="0", context=None):
+	    def __new__(cls, value="0", context=(False)):
	        try:
	            return decimal.Decimal.__new__(cls, utils.str_(value), context)
	        except:

```  
Lines 225:231

```diff
	
	
	class FloatObject(decimal.Decimal, PdfObject):
-	    def __new__(cls, value="0", context=None):
+	    def __new__(cls, value="0", context=(True)):
	        try:
	            return decimal.Decimal.__new__(cls, utils.str_(value), context)
	        except:

```  
Lines 268:274

```diff
	
	    def readFromStream(stream):
	        num = utils.readUntilRegex(stream, NumberObject.NumberPattern)
-	        if num.find(NumberObject.ByteDot) != -1:
+	        if False:
	            return FloatObject(num)
	        else:
	            return NumberObject(num)

```  
Lines 268:274

```diff
	
	    def readFromStream(stream):
	        num = utils.readUntilRegex(stream, NumberObject.NumberPattern)
-	        if num.find(NumberObject.ByteDot) != -1:
+	        if (num.find(NumberObject.ByteDot) < -1):
	            return FloatObject(num)
	        else:
	            return NumberObject(num)

```  
Lines 268:274

```diff
	
	    def readFromStream(stream):
	        num = utils.readUntilRegex(stream, NumberObject.NumberPattern)
-	        if num.find(NumberObject.ByteDot) != -1:
+	        if (num.find(NumberObject.ByteDot) > -1):
	            return FloatObject(num)
	        else:
	            return NumberObject(num)

```  
Lines 279:285

```diff
	# Given a string (either a "str" or "unicode"), create a ByteStringObject or a
	# TextStringObject to represent the string.
	def createStringObject(string):
-	    if isinstance(string, utils.string_type):
+	    if True:
	        return TextStringObject(string)
	    elif isinstance(string, utils.bytes_type):
	        try:

```  
Lines 281:287

```diff
	def createStringObject(string):
	    if isinstance(string, utils.string_type):
	        return TextStringObject(string)
-	    elif isinstance(string, utils.bytes_type):
+	    elif True:
	        try:
	            if string.startswith(codecs.BOM_UTF16_BE):
	                retval = TextStringObject(string.decode("utf-16"))

```  
Lines 283:289

```diff
	        return TextStringObject(string)
	    elif isinstance(string, utils.bytes_type):
	        try:
-	            if string.startswith(codecs.BOM_UTF16_BE):
+	            if True:
	                retval = TextStringObject(string.decode("utf-16"))
	                retval.autodetect_utf16 = True
	                return retval

```  
Lines 283:289

```diff
	        return TextStringObject(string)
	    elif isinstance(string, utils.bytes_type):
	        try:
-	            if string.startswith(codecs.BOM_UTF16_BE):
+	            if False:
	                retval = TextStringObject(string.decode("utf-16"))
	                retval.autodetect_utf16 = True
	                return retval

```  
Lines 285:291

```diff
	        try:
	            if string.startswith(codecs.BOM_UTF16_BE):
	                retval = TextStringObject(string.decode("utf-16"))
-	                retval.autodetect_utf16 = True
+	                retval.autodetect_utf16 = (False)
	                return retval
	            else:
	                # This is probably a big performance hit here, but we need to

```  
Lines 285:291

```diff
	        try:
	            if string.startswith(codecs.BOM_UTF16_BE):
	                retval = TextStringObject(string.decode("utf-16"))
-	                retval.autodetect_utf16 = True
+	                retval.autodetect_utf16 = None
	                return retval
	            else:
	                # This is probably a big performance hit here, but we need to

```  
Lines 307:313

```diff
	    x = b_("")
	    while True:
	        tok = readNonWhitespace(stream)
-	        if not tok:
+	        if False:
	            # stream has truncated prematurely
	            raise PdfStreamError("Stream has ended unexpectedly")
	        if tok == b_(">"):

```  
Lines 313:319

```diff
	        if tok == b_(">"):
	            break
	        x += tok
-	        if len(x) == 2:
+	        if (len(x) < 2):
	            txt += chr(int(x, base=16))
	            x = b_("")
	    if len(x) == 1:

```  
Lines 313:319

```diff
	        if tok == b_(">"):
	            break
	        x += tok
-	        if len(x) == 2:
+	        if (len(x) >= 2):
	            txt += chr(int(x, base=16))
	            x = b_("")
	    if len(x) == 1:

```  
Lines 313:319

```diff
	        if tok == b_(">"):
	            break
	        x += tok
-	        if len(x) == 2:
+	        if (len(x) != 2):
	            txt += chr(int(x, base=16))
	            x = b_("")
	    if len(x) == 1:

```  
Lines 313:319

```diff
	        if tok == b_(">"):
	            break
	        x += tok
-	        if len(x) == 2:
+	        if (len(x) <= 2):
	            txt += chr(int(x, base=16))
	            x = b_("")
	    if len(x) == 1:

```  
Lines 313:319

```diff
	        if tok == b_(">"):
	            break
	        x += tok
-	        if len(x) == 2:
+	        if True:
	            txt += chr(int(x, base=16))
	            x = b_("")
	    if len(x) == 1:

```  
Lines 313:319

```diff
	        if tok == b_(">"):
	            break
	        x += tok
-	        if len(x) == 2:
+	        if False:
	            txt += chr(int(x, base=16))
	            x = b_("")
	    if len(x) == 1:

```  
Lines 316:322

```diff
	        if len(x) == 2:
	            txt += chr(int(x, base=16))
	            x = b_("")
-	    if len(x) == 1:
+	    if (len(x) < 1):
	        x += b_("0")
	    if len(x) == 2:
	        txt += chr(int(x, base=16))

```  
Lines 316:322

```diff
	        if len(x) == 2:
	            txt += chr(int(x, base=16))
	            x = b_("")
-	    if len(x) == 1:
+	    if (len(x) >= 1):
	        x += b_("0")
	    if len(x) == 2:
	        txt += chr(int(x, base=16))

```  
Lines 316:322

```diff
	        if len(x) == 2:
	            txt += chr(int(x, base=16))
	            x = b_("")
-	    if len(x) == 1:
+	    if (len(x) != 1):
	        x += b_("0")
	    if len(x) == 2:
	        txt += chr(int(x, base=16))

```  
Lines 316:322

```diff
	        if len(x) == 2:
	            txt += chr(int(x, base=16))
	            x = b_("")
-	    if len(x) == 1:
+	    if (len(x) > 1):
	        x += b_("0")
	    if len(x) == 2:
	        txt += chr(int(x, base=16))

```  
Lines 316:322

```diff
	        if len(x) == 2:
	            txt += chr(int(x, base=16))
	            x = b_("")
-	    if len(x) == 1:
+	    if (len(x) <= 1):
	        x += b_("0")
	    if len(x) == 2:
	        txt += chr(int(x, base=16))

```  
Lines 316:322

```diff
	        if len(x) == 2:
	            txt += chr(int(x, base=16))
	            x = b_("")
-	    if len(x) == 1:
+	    if True:
	        x += b_("0")
	    if len(x) == 2:
	        txt += chr(int(x, base=16))

```  
Lines 316:322

```diff
	        if len(x) == 2:
	            txt += chr(int(x, base=16))
	            x = b_("")
-	    if len(x) == 1:
+	    if False:
	        x += b_("0")
	    if len(x) == 2:
	        txt += chr(int(x, base=16))

```  
Lines 318:324

```diff
	            x = b_("")
	    if len(x) == 1:
	        x += b_("0")
-	    if len(x) == 2:
+	    if False:
	        txt += chr(int(x, base=16))
	    return createStringObject(b_(txt))
	

```  
Lines 318:324

```diff
	            x = b_("")
	    if len(x) == 1:
	        x += b_("0")
-	    if len(x) == 2:
+	    if (len(x) >= 2):
	        txt += chr(int(x, base=16))
	    return createStringObject(b_(txt))
	

```  
Lines 318:324

```diff
	            x = b_("")
	    if len(x) == 1:
	        x += b_("0")
-	    if len(x) == 2:
+	    if (len(x) > 2):
	        txt += chr(int(x, base=16))
	    return createStringObject(b_(txt))
	

```  
Lines 421:427

```diff
	# PDFDocEncoding, or contained a UTF-16BE BOM mark to cause UTF-16 decoding to
	# occur.
	class TextStringObject(utils.string_type, PdfObject):
-	    autodetect_pdfdocencoding = False
+	    autodetect_pdfdocencoding = (True)
	    autodetect_utf16 = False
	
	    ##

```  
Lines 421:427

```diff
	# PDFDocEncoding, or contained a UTF-16BE BOM mark to cause UTF-16 decoding to
	# occur.
	class TextStringObject(utils.string_type, PdfObject):
-	    autodetect_pdfdocencoding = False
+	    autodetect_pdfdocencoding = None
	    autodetect_utf16 = False
	
	    ##

```  
Lines 422:428

```diff
	# occur.
	class TextStringObject(utils.string_type, PdfObject):
	    autodetect_pdfdocencoding = False
-	    autodetect_utf16 = False
+	    autodetect_utf16 = (True)
	
	    ##
	    # It is occasionally possible that a text string object gets created where

```  
Lines 422:428

```diff
	# occur.
	class TextStringObject(utils.string_type, PdfObject):
	    autodetect_pdfdocencoding = False
-	    autodetect_utf16 = False
+	    autodetect_utf16 = None
	
	    ##
	    # It is occasionally possible that a text string object gets created where

```  
Lines 474:480

```diff
	        stream.write(b_(self))
	
	    def readFromStream(stream, pdf):
-	        debug = False
+	        debug = (True)
	        if debug: print((stream.tell()))
	        name = stream.read(1)
	        if name != NameObject.surfix:

```  
Lines 474:480

```diff
	        stream.write(b_(self))
	
	    def readFromStream(stream, pdf):
-	        debug = False
+	        debug = None
	        if debug: print((stream.tell()))
	        name = stream.read(1)
	        if name != NameObject.surfix:

```  
Lines 475:481

```diff
	
	    def readFromStream(stream, pdf):
	        debug = False
-	        if debug: print((stream.tell()))
+	        if True: print((stream.tell()))
	        name = stream.read(1)
	        if name != NameObject.surfix:
	            raise utils.PdfReadError("name read error")

```  
Lines 475:481

```diff
	
	    def readFromStream(stream, pdf):
	        debug = False
-	        if debug: print((stream.tell()))
+	        if False: print((stream.tell()))
	        name = stream.read(1)
	        if name != NameObject.surfix:
	            raise utils.PdfReadError("name read error")

```  
Lines 477:483

```diff
	        debug = False
	        if debug: print((stream.tell()))
	        name = stream.read(1)
-	        if name != NameObject.surfix:
+	        if (name < NameObject.surfix):
	            raise utils.PdfReadError("name read error")
	        name += utils.readUntilRegex(stream, NameObject.delimiterPattern, 
	            ignore_eof=True)

```  
Lines 477:483

```diff
	        debug = False
	        if debug: print((stream.tell()))
	        name = stream.read(1)
-	        if name != NameObject.surfix:
+	        if (name > NameObject.surfix):
	            raise utils.PdfReadError("name read error")
	        name += utils.readUntilRegex(stream, NameObject.delimiterPattern, 
	            ignore_eof=True)

```  
Lines 477:483

```diff
	        debug = False
	        if debug: print((stream.tell()))
	        name = stream.read(1)
-	        if name != NameObject.surfix:
+	        if False:
	            raise utils.PdfReadError("name read error")
	        name += utils.readUntilRegex(stream, NameObject.delimiterPattern, 
	            ignore_eof=True)

```  
Lines 480:486

```diff
	        if name != NameObject.surfix:
	            raise utils.PdfReadError("name read error")
	        name += utils.readUntilRegex(stream, NameObject.delimiterPattern, 
-	            ignore_eof=True)
+	            ignore_eof=(False))
	        if debug: print(name)
	        try:
	            return NameObject(name.decode('utf-8'))

```  
Lines 480:486

```diff
	        if name != NameObject.surfix:
	            raise utils.PdfReadError("name read error")
	        name += utils.readUntilRegex(stream, NameObject.delimiterPattern, 
-	            ignore_eof=True)
+	            ignore_eof=None)
	        if debug: print(name)
	        try:
	            return NameObject(name.decode('utf-8'))

```  
Lines 481:487

```diff
	            raise utils.PdfReadError("name read error")
	        name += utils.readUntilRegex(stream, NameObject.delimiterPattern, 
	            ignore_eof=True)
-	        if debug: print(name)
+	        if True: print(name)
	        try:
	            return NameObject(name.decode('utf-8'))
	        except (UnicodeEncodeError, UnicodeDecodeError) as e:

```  
Lines 481:487

```diff
	            raise utils.PdfReadError("name read error")
	        name += utils.readUntilRegex(stream, NameObject.delimiterPattern, 
	            ignore_eof=True)
-	        if debug: print(name)
+	        if False: print(name)
	        try:
	            return NameObject(name.decode('utf-8'))
	        except (UnicodeEncodeError, UnicodeDecodeError) as e:

```  
Lines 501:507

```diff
	        return dict.__getitem__(self, key)
	
	    def __setitem__(self, key, value):
-	        if not isinstance(key, PdfObject):
+	        if False:
	            raise ValueError("key must be PdfObject")
	        if not isinstance(value, PdfObject):
	            raise ValueError("value must be PdfObject")

```  
Lines 503:509

```diff
	    def __setitem__(self, key, value):
	        if not isinstance(key, PdfObject):
	            raise ValueError("key must be PdfObject")
-	        if not isinstance(value, PdfObject):
+	        if False:
	            raise ValueError("value must be PdfObject")
	        return dict.__setitem__(self, key, value)
	

```  
Lines 507:513

```diff
	            raise ValueError("value must be PdfObject")
	        return dict.__setitem__(self, key, value)
	
-	    def setdefault(self, key, value=None):
+	    def setdefault(self, key, value=(False)):
	        if not isinstance(key, PdfObject):
	            raise ValueError("key must be PdfObject")
	        if not isinstance(value, PdfObject):

```  
Lines 507:513

```diff
	            raise ValueError("value must be PdfObject")
	        return dict.__setitem__(self, key, value)
	
-	    def setdefault(self, key, value=None):
+	    def setdefault(self, key, value=(True)):
	        if not isinstance(key, PdfObject):
	            raise ValueError("key must be PdfObject")
	        if not isinstance(value, PdfObject):

```  
Lines 541:547

```diff
	    # #DictionaryObject.getXmpData getXmpData} function.
	    # <p>
	    # Stability: Added in v1.12, will exist for all future v1.x releases.
-	    xmpMetadata = property(lambda self: self.getXmpMetadata(), None, None)
+	    xmpMetadata = property(lambda self: self.getXmpMetadata(), None, (False))
	
	    def writeToStream(self, stream, encryption_key):
	        stream.write(b_("<<\n"))

```  
Lines 541:547

```diff
	    # #DictionaryObject.getXmpData getXmpData} function.
	    # <p>
	    # Stability: Added in v1.12, will exist for all future v1.x releases.
-	    xmpMetadata = property(lambda self: self.getXmpMetadata(), None, None)
+	    xmpMetadata = property(lambda self: self.getXmpMetadata(), None, (True))
	
	    def writeToStream(self, stream, encryption_key):
	        stream.write(b_("<<\n"))

```  
Lines 541:547

```diff
	    # #DictionaryObject.getXmpData getXmpData} function.
	    # <p>
	    # Stability: Added in v1.12, will exist for all future v1.x releases.
-	    xmpMetadata = property(lambda self: self.getXmpMetadata(), None, None)
+	    xmpMetadata = property(lambda self: self.getXmpMetadata(), (False), None)
	
	    def writeToStream(self, stream, encryption_key):
	        stream.write(b_("<<\n"))

```  
Lines 541:547

```diff
	    # #DictionaryObject.getXmpData getXmpData} function.
	    # <p>
	    # Stability: Added in v1.12, will exist for all future v1.x releases.
-	    xmpMetadata = property(lambda self: self.getXmpMetadata(), None, None)
+	    xmpMetadata = property(lambda self: self.getXmpMetadata(), (True), None)
	
	    def writeToStream(self, stream, encryption_key):
	        stream.write(b_("<<\n"))

```  
Lines 553:559

```diff
	        stream.write(b_(">>"))
	
	    def readFromStream(stream, pdf):
-	        debug = False
+	        debug = (True)
	        tmp = stream.read(2)
	        if tmp != b_("<<"):
	            raise utils.PdfReadError("Dictionary read error at byte %s: stream must begin with '<<'" % utils.hexStr(stream.tell()))

```  
Lines 553:559

```diff
	        stream.write(b_(">>"))
	
	    def readFromStream(stream, pdf):
-	        debug = False
+	        debug = None
	        tmp = stream.read(2)
	        if tmp != b_("<<"):
	            raise utils.PdfReadError("Dictionary read error at byte %s: stream must begin with '<<'" % utils.hexStr(stream.tell()))

```  
Lines 555:561

```diff
	    def readFromStream(stream, pdf):
	        debug = False
	        tmp = stream.read(2)
-	        if tmp != b_("<<"):
+	        if False:
	            raise utils.PdfReadError("Dictionary read error at byte %s: stream must begin with '<<'" % utils.hexStr(stream.tell()))
	        data = {}
	        while True:

```  
Lines 555:561

```diff
	    def readFromStream(stream, pdf):
	        debug = False
	        tmp = stream.read(2)
-	        if tmp != b_("<<"):
+	        if (tmp < b_('<<')):
	            raise utils.PdfReadError("Dictionary read error at byte %s: stream must begin with '<<'" % utils.hexStr(stream.tell()))
	        data = {}
	        while True:

```  
Lines 555:561

```diff
	    def readFromStream(stream, pdf):
	        debug = False
	        tmp = stream.read(2)
-	        if tmp != b_("<<"):
+	        if (tmp > b_('<<')):
	            raise utils.PdfReadError("Dictionary read error at byte %s: stream must begin with '<<'" % utils.hexStr(stream.tell()))
	        data = {}
	        while True:

```  
Lines 560:566

```diff
	        data = {}
	        while True:
	            tok = readNonWhitespace(stream)
-	            if tok == b_('\x00'):
+	            if False:
	                continue
	            elif tok == b_('%'):
	                stream.seek(-1, 1)

```  
Lines 560:566

```diff
	        data = {}
	        while True:
	            tok = readNonWhitespace(stream)
-	            if tok == b_('\x00'):
+	            if (tok < b_('\x00')):
	                continue
	            elif tok == b_('%'):
	                stream.seek(-1, 1)

```  
Lines 560:566

```diff
	        data = {}
	        while True:
	            tok = readNonWhitespace(stream)
-	            if tok == b_('\x00'):
+	            if (tok <= b_('\x00')):
	                continue
	            elif tok == b_('%'):
	                stream.seek(-1, 1)

```  
Lines 562:568

```diff
	            tok = readNonWhitespace(stream)
	            if tok == b_('\x00'):
	                continue
-	            elif tok == b_('%'):
+	            elif (tok < b_('%')):
	                stream.seek(-1, 1)
	                skipOverComment(stream)
	                continue

```  
Lines 562:568

```diff
	            tok = readNonWhitespace(stream)
	            if tok == b_('\x00'):
	                continue
-	            elif tok == b_('%'):
+	            elif (tok <= b_('%')):
	                stream.seek(-1, 1)
	                skipOverComment(stream)
	                continue

```  
Lines 562:568

```diff
	            tok = readNonWhitespace(stream)
	            if tok == b_('\x00'):
	                continue
-	            elif tok == b_('%'):
+	            elif False:
	                stream.seek(-1, 1)
	                skipOverComment(stream)
	                continue

```  
Lines 566:572

```diff
	                stream.seek(-1, 1)
	                skipOverComment(stream)
	                continue
-	            if not tok:
+	            if False:
	                # stream has truncated prematurely
	                raise PdfStreamError("Stream has ended unexpectedly")
	

```  
Lines 570:576

```diff
	                # stream has truncated prematurely
	                raise PdfStreamError("Stream has ended unexpectedly")
	
-	            if debug: print(("Tok:", tok))
+	            if True:", tok))
	            if tok == b_(">"):
	                stream.read(1)
	                break

```  
Lines 570:576

```diff
	                # stream has truncated prematurely
	                raise PdfStreamError("Stream has ended unexpectedly")
	
-	            if debug: print(("Tok:", tok))
+	            if False:", tok))
	            if tok == b_(">"):
	                stream.read(1)
	                break

```  
Lines 571:577

```diff
	                raise PdfStreamError("Stream has ended unexpectedly")
	
	            if debug: print(("Tok:", tok))
-	            if tok == b_(">"):
+	            if (tok >= b_('>')):
	                stream.read(1)
	                break
	            stream.seek(-1, 1)

```  
Lines 579:585

```diff
	            tok = readNonWhitespace(stream)
	            stream.seek(-1, 1)
	            value = readObject(stream, pdf)
-	            if not data.get(key):
+	            if True:
	                data[key] = value
	            elif pdf.strict:
	                # multiple definitions of key not permitted

```  
Lines 591:597

```diff
	
	        pos = stream.tell()
	        s = readNonWhitespace(stream)
-	        if s == b_('s') and stream.read(5) == b_('tream'):
+	        if (s >= b_('s')) and stream.read(5) == b_('tream'):
	            eol = stream.read(1)
	            # odd PDF file output has spaces after 'stream' keyword but before EOL.
	            # patch provided by Danial Sandler

```  
Lines 591:597

```diff
	
	        pos = stream.tell()
	        s = readNonWhitespace(stream)
-	        if s == b_('s') and stream.read(5) == b_('tream'):
+	        if (s <= b_('s')) and stream.read(5) == b_('tream'):
	            eol = stream.read(1)
	            # odd PDF file output has spaces after 'stream' keyword but before EOL.
	            # patch provided by Danial Sandler

```  
Lines 591:597

```diff
	
	        pos = stream.tell()
	        s = readNonWhitespace(stream)
-	        if s == b_('s') and stream.read(5) == b_('tream'):
+	        if s == b_('s') and (stream.read(5) >= b_('tream')):
	            eol = stream.read(1)
	            # odd PDF file output has spaces after 'stream' keyword but before EOL.
	            # patch provided by Danial Sandler

```  
Lines 591:597

```diff
	
	        pos = stream.tell()
	        s = readNonWhitespace(stream)
-	        if s == b_('s') and stream.read(5) == b_('tream'):
+	        if s == b_('s') and (stream.read(5) <= b_('tream')):
	            eol = stream.read(1)
	            # odd PDF file output has spaces after 'stream' keyword but before EOL.
	            # patch provided by Danial Sandler

```  
Lines 595:601

```diff
	            eol = stream.read(1)
	            # odd PDF file output has spaces after 'stream' keyword but before EOL.
	            # patch provided by Danial Sandler
-	            while eol == b_(' '):
+	            while (eol >= b_(' ')):
	                eol = stream.read(1)
	            assert eol in (b_("\n"), b_("\r"))
	            if eol == b_("\r"):

```  
Lines 595:601

```diff
	            eol = stream.read(1)
	            # odd PDF file output has spaces after 'stream' keyword but before EOL.
	            # patch provided by Danial Sandler
-	            while eol == b_(' '):
+	            while (eol > b_(' ')):
	                eol = stream.read(1)
	            assert eol in (b_("\n"), b_("\r"))
	            if eol == b_("\r"):

```  
Lines 598:604

```diff
	            while eol == b_(' '):
	                eol = stream.read(1)
	            assert eol in (b_("\n"), b_("\r"))
-	            if eol == b_("\r"):
+	            if True:
	                # read \n after
	                if stream.read(1)  != b_('\n'):
	                    stream.seek(-1, 1)

```  
Lines 598:604

```diff
	            while eol == b_(' '):
	                eol = stream.read(1)
	            assert eol in (b_("\n"), b_("\r"))
-	            if eol == b_("\r"):
+	            if False:
	                # read \n after
	                if stream.read(1)  != b_('\n'):
	                    stream.seek(-1, 1)

```  
Lines 598:604

```diff
	            while eol == b_(' '):
	                eol = stream.read(1)
	            assert eol in (b_("\n"), b_("\r"))
-	            if eol == b_("\r"):
+	            if (eol < b_('\r')):
	                # read \n after
	                if stream.read(1)  != b_('\n'):
	                    stream.seek(-1, 1)

```  
Lines 598:604

```diff
	            while eol == b_(' '):
	                eol = stream.read(1)
	            assert eol in (b_("\n"), b_("\r"))
-	            if eol == b_("\r"):
+	            if (eol >= b_('\r')):
	                # read \n after
	                if stream.read(1)  != b_('\n'):
	                    stream.seek(-1, 1)

```  
Lines 598:604

```diff
	            while eol == b_(' '):
	                eol = stream.read(1)
	            assert eol in (b_("\n"), b_("\r"))
-	            if eol == b_("\r"):
+	            if (eol != b_('\r')):
	                # read \n after
	                if stream.read(1)  != b_('\n'):
	                    stream.seek(-1, 1)

```  
Lines 598:604

```diff
	            while eol == b_(' '):
	                eol = stream.read(1)
	            assert eol in (b_("\n"), b_("\r"))
-	            if eol == b_("\r"):
+	            if (eol > b_('\r')):
	                # read \n after
	                if stream.read(1)  != b_('\n'):
	                    stream.seek(-1, 1)

```  
Lines 598:604

```diff
	            while eol == b_(' '):
	                eol = stream.read(1)
	            assert eol in (b_("\n"), b_("\r"))
-	            if eol == b_("\r"):
+	            if (eol <= b_('\r')):
	                # read \n after
	                if stream.read(1)  != b_('\n'):
	                    stream.seek(-1, 1)

```  
Lines 605:611

```diff
	            # this is a stream object, not a dictionary
	            assert "/Length" in data
	            length = data["/Length"]
-	            if debug: print(data)
+	            if True: print(data)
	            if isinstance(length, IndirectObject):
	                t = stream.tell()
	                length = pdf.getObject(length)

```  
Lines 605:611

```diff
	            # this is a stream object, not a dictionary
	            assert "/Length" in data
	            length = data["/Length"]
-	            if debug: print(data)
+	            if False: print(data)
	            if isinstance(length, IndirectObject):
	                t = stream.tell()
	                length = pdf.getObject(length)

```  
Lines 606:612

```diff
	            assert "/Length" in data
	            length = data["/Length"]
	            if debug: print(data)
-	            if isinstance(length, IndirectObject):
+	            if False:
	                t = stream.tell()
	                length = pdf.getObject(length)
	                stream.seek(t, 0)

```  
Lines 611:617

```diff
	                length = pdf.getObject(length)
	                stream.seek(t, 0)
	            data["__streamdata__"] = stream.read(length)
-	            if debug: print("here")
+	            if True: print("here")
	            #if debug: print(binascii.hexlify(data["__streamdata__"]))
	            e = readNonWhitespace(stream)
	            ndstream = stream.read(8)

```  
Lines 611:617

```diff
	                length = pdf.getObject(length)
	                stream.seek(t, 0)
	            data["__streamdata__"] = stream.read(length)
-	            if debug: print("here")
+	            if False: print("here")
	            #if debug: print(binascii.hexlify(data["__streamdata__"]))
	            e = readNonWhitespace(stream)
	            ndstream = stream.read(8)

```  
Lines 615:621

```diff
	            #if debug: print(binascii.hexlify(data["__streamdata__"]))
	            e = readNonWhitespace(stream)
	            ndstream = stream.read(8)
-	            if (e + ndstream) != b_("endstream"):
+	            if (e + ndstream < b_('endstream')):
	                # (sigh) - the odd PDF file has a length that is too long, so
	                # we need to read backwards to find the "endstream" ending.
	                # ReportLab (unknown version) generates files with this bug,

```  
Lines 615:621

```diff
	            #if debug: print(binascii.hexlify(data["__streamdata__"]))
	            e = readNonWhitespace(stream)
	            ndstream = stream.read(8)
-	            if (e + ndstream) != b_("endstream"):
+	            if (e + ndstream > b_('endstream')):
	                # (sigh) - the odd PDF file has a length that is too long, so
	                # we need to read backwards to find the "endstream" ending.
	                # ReportLab (unknown version) generates files with this bug,

```  
Lines 615:621

```diff
	            #if debug: print(binascii.hexlify(data["__streamdata__"]))
	            e = readNonWhitespace(stream)
	            ndstream = stream.read(8)
-	            if (e + ndstream) != b_("endstream"):
+	            if False:
	                # (sigh) - the odd PDF file has a length that is too long, so
	                # we need to read backwards to find the "endstream" ending.
	                # ReportLab (unknown version) generates files with this bug,

```  
Lines 776:782

```diff
	
	class StreamObject(DictionaryObject):
	    def __init__(self):
-	        self._data = None
+	        self._data = (False)
	        self.decodedSelf = None
	
	    def writeToStream(self, stream, encryption_key):

```  
Lines 776:782

```diff
	
	class StreamObject(DictionaryObject):
	    def __init__(self):
-	        self._data = None
+	        self._data = (True)
	        self.decodedSelf = None
	
	    def writeToStream(self, stream, encryption_key):

```  
Lines 777:783

```diff
	class StreamObject(DictionaryObject):
	    def __init__(self):
	        self._data = None
-	        self.decodedSelf = None
+	        self.decodedSelf = (False)
	
	    def writeToStream(self, stream, encryption_key):
	        self[NameObject("/Length")] = NumberObject(len(self._data))

```  
Lines 777:783

```diff
	class StreamObject(DictionaryObject):
	    def __init__(self):
	        self._data = None
-	        self.decodedSelf = None
+	        self.decodedSelf = (True)
	
	    def writeToStream(self, stream, encryption_key):
	        self[NameObject("/Length")] = NumberObject(len(self._data))

```  
Lines 791:797

```diff
	        stream.write(b_("\nendstream"))
	
	    def initializeFromDictionary(data):
-	        if "/Filter" in data:
+	        if True:
	            retval = EncodedStreamObject()
	        else:
	            retval = DecodedStreamObject()

```  
Lines 830:836

```diff
	
	class EncodedStreamObject(StreamObject):
	    def __init__(self):
-	        self.decodedSelf = None
+	        self.decodedSelf = (False)
	
	    def getData(self):
	        if self.decodedSelf:

```  
Lines 833:839

```diff
	        self.decodedSelf = None
	
	    def getData(self):
-	        if self.decodedSelf:
+	        if False:
	            # cached version of decoded object
	            return self.decodedSelf.getData()
	        else:

```  
Lines 842:848

```diff
	
	            decoded._data = filters.decodeStreamData(self)
	            for key, value in list(self.items()):
-	                if not key in ("/Length", "/Filter", "/DecodeParms"):
+	                if not (key not in ('/Length', '/Filter', '/DecodeParms')):
	                    decoded[key] = value
	            self.decodedSelf = decoded
	            return decoded._data

```  
Lines 842:848

```diff
	
	            decoded._data = filters.decodeStreamData(self)
	            for key, value in list(self.items()):
-	                if not key in ("/Length", "/Filter", "/DecodeParms"):
+	                if True:
	                    decoded[key] = value
	            self.decodedSelf = decoded
	            return decoded._data

```  
Lines 842:848

```diff
	
	            decoded._data = filters.decodeStreamData(self)
	            for key, value in list(self.items()):
-	                if not key in ("/Length", "/Filter", "/DecodeParms"):
+	                if False:
	                    decoded[key] = value
	            self.decodedSelf = decoded
	            return decoded._data

```  
Lines 929:935

```diff
	    def getHeight(self):
	        return self.getUpperRight_y() - self.getLowerLeft_y()
	
-	    lowerLeft = property(getLowerLeft, setLowerLeft, None, None)
+	    lowerLeft = property(getLowerLeft, setLowerLeft, None, (False))
	    """
	    Property to read and modify the lower left coordinate of this box
	    in (x,y) form.

```  
Lines 929:935

```diff
	    def getHeight(self):
	        return self.getUpperRight_y() - self.getLowerLeft_y()
	
-	    lowerLeft = property(getLowerLeft, setLowerLeft, None, None)
+	    lowerLeft = property(getLowerLeft, setLowerLeft, None, (True))
	    """
	    Property to read and modify the lower left coordinate of this box
	    in (x,y) form.

```  
Lines 929:935

```diff
	    def getHeight(self):
	        return self.getUpperRight_y() - self.getLowerLeft_y()
	
-	    lowerLeft = property(getLowerLeft, setLowerLeft, None, None)
+	    lowerLeft = property(getLowerLeft, setLowerLeft, (False), None)
	    """
	    Property to read and modify the lower left coordinate of this box
	    in (x,y) form.

```  
Lines 929:935

```diff
	    def getHeight(self):
	        return self.getUpperRight_y() - self.getLowerLeft_y()
	
-	    lowerLeft = property(getLowerLeft, setLowerLeft, None, None)
+	    lowerLeft = property(getLowerLeft, setLowerLeft, (True), None)
	    """
	    Property to read and modify the lower left coordinate of this box
	    in (x,y) form.

```  
Lines 934:940

```diff
	    Property to read and modify the lower left coordinate of this box
	    in (x,y) form.
	    """
-	    lowerRight = property(getLowerRight, setLowerRight, None, None)
+	    lowerRight = property(getLowerRight, setLowerRight, None, (False))
	    """
	    Property to read and modify the lower right coordinate of this box
	    in (x,y) form.

```  
Lines 934:940

```diff
	    Property to read and modify the lower left coordinate of this box
	    in (x,y) form.
	    """
-	    lowerRight = property(getLowerRight, setLowerRight, None, None)
+	    lowerRight = property(getLowerRight, setLowerRight, None, (True))
	    """
	    Property to read and modify the lower right coordinate of this box
	    in (x,y) form.

```  
Lines 934:940

```diff
	    Property to read and modify the lower left coordinate of this box
	    in (x,y) form.
	    """
-	    lowerRight = property(getLowerRight, setLowerRight, None, None)
+	    lowerRight = property(getLowerRight, setLowerRight, (False), None)
	    """
	    Property to read and modify the lower right coordinate of this box
	    in (x,y) form.

```  
Lines 934:940

```diff
	    Property to read and modify the lower left coordinate of this box
	    in (x,y) form.
	    """
-	    lowerRight = property(getLowerRight, setLowerRight, None, None)
+	    lowerRight = property(getLowerRight, setLowerRight, (True), None)
	    """
	    Property to read and modify the lower right coordinate of this box
	    in (x,y) form.

```  
Lines 939:945

```diff
	    Property to read and modify the lower right coordinate of this box
	    in (x,y) form.
	    """
-	    upperLeft = property(getUpperLeft, setUpperLeft, None, None)
+	    upperLeft = property(getUpperLeft, setUpperLeft, None, (False))
	    """
	    Property to read and modify the upper left coordinate of this box
	    in (x,y) form.

```  
Lines 939:945

```diff
	    Property to read and modify the lower right coordinate of this box
	    in (x,y) form.
	    """
-	    upperLeft = property(getUpperLeft, setUpperLeft, None, None)
+	    upperLeft = property(getUpperLeft, setUpperLeft, None, (True))
	    """
	    Property to read and modify the upper left coordinate of this box
	    in (x,y) form.

```  
Lines 939:945

```diff
	    Property to read and modify the lower right coordinate of this box
	    in (x,y) form.
	    """
-	    upperLeft = property(getUpperLeft, setUpperLeft, None, None)
+	    upperLeft = property(getUpperLeft, setUpperLeft, (False), None)
	    """
	    Property to read and modify the upper left coordinate of this box
	    in (x,y) form.

```  
Lines 939:945

```diff
	    Property to read and modify the lower right coordinate of this box
	    in (x,y) form.
	    """
-	    upperLeft = property(getUpperLeft, setUpperLeft, None, None)
+	    upperLeft = property(getUpperLeft, setUpperLeft, (True), None)
	    """
	    Property to read and modify the upper left coordinate of this box
	    in (x,y) form.

```  
Lines 944:950

```diff
	    Property to read and modify the upper left coordinate of this box
	    in (x,y) form.
	    """
-	    upperRight = property(getUpperRight, setUpperRight, None, None)
+	    upperRight = property(getUpperRight, setUpperRight, (False), None)
	    """
	    Property to read and modify the upper right coordinate of this box
	    in (x,y) form.

```  
Lines 944:950

```diff
	    Property to read and modify the upper left coordinate of this box
	    in (x,y) form.
	    """
-	    upperRight = property(getUpperRight, setUpperRight, None, None)
+	    upperRight = property(getUpperRight, setUpperRight, (True), None)
	    """
	    Property to read and modify the upper right coordinate of this box
	    in (x,y) form.

```  
Lines 944:950

```diff
	    Property to read and modify the upper left coordinate of this box
	    in (x,y) form.
	    """
-	    upperRight = property(getUpperRight, setUpperRight, None, None)
+	    upperRight = property(getUpperRight, setUpperRight, None, (False))
	    """
	    Property to read and modify the upper right coordinate of this box
	    in (x,y) form.

```  
Lines 944:950

```diff
	    Property to read and modify the upper left coordinate of this box
	    in (x,y) form.
	    """
-	    upperRight = property(getUpperRight, setUpperRight, None, None)
+	    upperRight = property(getUpperRight, setUpperRight, None, (True))
	    """
	    Property to read and modify the upper right coordinate of this box
	    in (x,y) form.

```  
Lines 1107:1113

```diff
	    :rtype: str
	    """
	
-	    zoom = property(lambda self: self.get("/Zoom", None))
+	    zoom = property(lambda self: self.get("/Zoom", (False)))
	    """
	    Read-only property accessing the zoom factor.
	

```  
Lines 1107:1113

```diff
	    :rtype: str
	    """
	
-	    zoom = property(lambda self: self.get("/Zoom", None))
+	    zoom = property(lambda self: self.get("/Zoom", (True)))
	    """
	    Read-only property accessing the zoom factor.
	

```  
Lines 1114:1120

```diff
	    :rtype: int, or ``None`` if not available.
	    """
	
-	    left = property(lambda self: self.get("/Left", None))
+	    left = property(lambda self: self.get("/Left", (False)))
	    """
	    Read-only property accessing the left horizontal coordinate.
	

```  
Lines 1114:1120

```diff
	    :rtype: int, or ``None`` if not available.
	    """
	
-	    left = property(lambda self: self.get("/Left", None))
+	    left = property(lambda self: self.get("/Left", (True)))
	    """
	    Read-only property accessing the left horizontal coordinate.
	

```  
Lines 1121:1127

```diff
	    :rtype: int, or ``None`` if not available.
	    """
	
-	    right = property(lambda self: self.get("/Right", None))
+	    right = property(lambda self: self.get("/Right", (False)))
	    """
	    Read-only property accessing the right horizontal coordinate.
	

```  
Lines 1121:1127

```diff
	    :rtype: int, or ``None`` if not available.
	    """
	
-	    right = property(lambda self: self.get("/Right", None))
+	    right = property(lambda self: self.get("/Right", (True)))
	    """
	    Read-only property accessing the right horizontal coordinate.
	

```  
Lines 1128:1134

```diff
	    :rtype: int, or ``None`` if not available.
	    """
	
-	    top = property(lambda self: self.get("/Top", None))
+	    top = property(lambda self: self.get("/Top", (False)))
	    """
	    Read-only property accessing the top vertical coordinate.
	

```  
Lines 1128:1134

```diff
	    :rtype: int, or ``None`` if not available.
	    """
	
-	    top = property(lambda self: self.get("/Top", None))
+	    top = property(lambda self: self.get("/Top", (True)))
	    """
	    Read-only property accessing the top vertical coordinate.
	

```  
Lines 1135:1141

```diff
	    :rtype: int, or ``None`` if not available.
	    """
	
-	    bottom = property(lambda self: self.get("/Bottom", None))
+	    bottom = property(lambda self: self.get("/Bottom", (False)))
	    """
	    Read-only property accessing the bottom vertical coordinate.
	

```  
Lines 1135:1141

```diff
	    :rtype: int, or ``None`` if not available.
	    """
	
-	    bottom = property(lambda self: self.get("/Bottom", None))
+	    bottom = property(lambda self: self.get("/Bottom", (True)))
	    """
	    Read-only property accessing the bottom vertical coordinate.
	

```  
Lines 1176:1182

```diff
	    retval = u_('')
	    for b in byte_array:
	        c = _pdfDocEncoding[ord_(b)]
-	        if c == u_('\u0000'):
+	        if (c < u_('\x00')):
	            raise UnicodeDecodeError("pdfdocencoding", utils.barray(b), -1, -1,
	                    "does not exist in translation table")
	        retval += c

```  
Lines 1176:1182

```diff
	    retval = u_('')
	    for b in byte_array:
	        c = _pdfDocEncoding[ord_(b)]
-	        if c == u_('\u0000'):
+	        if (c >= u_('\x00')):
	            raise UnicodeDecodeError("pdfdocencoding", utils.barray(b), -1, -1,
	                    "does not exist in translation table")
	        retval += c

```  
Lines 1176:1182

```diff
	    retval = u_('')
	    for b in byte_array:
	        c = _pdfDocEncoding[ord_(b)]
-	        if c == u_('\u0000'):
+	        if (c != u_('\x00')):
	            raise UnicodeDecodeError("pdfdocencoding", utils.barray(b), -1, -1,
	                    "does not exist in translation table")
	        retval += c

```  
Lines 1176:1182

```diff
	    retval = u_('')
	    for b in byte_array:
	        c = _pdfDocEncoding[ord_(b)]
-	        if c == u_('\u0000'):
+	        if (c > u_('\x00')):
	            raise UnicodeDecodeError("pdfdocencoding", utils.barray(b), -1, -1,
	                    "does not exist in translation table")
	        retval += c

```  
Lines 1176:1182

```diff
	    retval = u_('')
	    for b in byte_array:
	        c = _pdfDocEncoding[ord_(b)]
-	        if c == u_('\u0000'):
+	        if (c <= u_('\x00')):
	            raise UnicodeDecodeError("pdfdocencoding", utils.barray(b), -1, -1,
	                    "does not exist in translation table")
	        retval += c

```  
Lines 1176:1182

```diff
	    retval = u_('')
	    for b in byte_array:
	        c = _pdfDocEncoding[ord_(b)]
-	        if c == u_('\u0000'):
+	        if True:
	            raise UnicodeDecodeError("pdfdocencoding", utils.barray(b), -1, -1,
	                    "does not exist in translation table")
	        retval += c

```  
Lines 1176:1182

```diff
	    retval = u_('')
	    for b in byte_array:
	        c = _pdfDocEncoding[ord_(b)]
-	        if c == u_('\u0000'):
+	        if False:
	            raise UnicodeDecodeError("pdfdocencoding", utils.barray(b), -1, -1,
	                    "does not exist in translation table")
	        retval += c

```  
Lines 1217:1223

```diff
	  u_('\u00f8'), u_('\u00f9'), u_('\u00fa'), u_('\u00fb'), u_('\u00fc'), u_('\u00fd'), u_('\u00fe'), u_('\u00ff')
	)
	
-	assert len(_pdfDocEncoding) == 256
+	assert (len(_pdfDocEncoding) >= 256)
	
	_pdfDocEncoding_rev = {}
	for i in range(256):

```  
Lines 1217:1223

```diff
	  u_('\u00f8'), u_('\u00f9'), u_('\u00fa'), u_('\u00fb'), u_('\u00fc'), u_('\u00fd'), u_('\u00fe'), u_('\u00ff')
	)
	
-	assert len(_pdfDocEncoding) == 256
+	assert (len(_pdfDocEncoding) <= 256)
	
	_pdfDocEncoding_rev = {}
	for i in range(256):

```  
Lines 1222:1228

```diff
	_pdfDocEncoding_rev = {}
	for i in range(256):
	    char = _pdfDocEncoding[i]
-	    if char == u_("\u0000"):
+	    if (char >= u_('\x00')):
	        continue
	    assert char not in _pdfDocEncoding_rev
	    _pdfDocEncoding_rev[char] = i

```  
Lines 1222:1228

```diff
	_pdfDocEncoding_rev = {}
	for i in range(256):
	    char = _pdfDocEncoding[i]
-	    if char == u_("\u0000"):
+	    if (char <= u_('\x00')):
	        continue
	    assert char not in _pdfDocEncoding_rev
	    _pdfDocEncoding_rev[char] = i

```  
Lines 1222:1228

```diff
	_pdfDocEncoding_rev = {}
	for i in range(256):
	    char = _pdfDocEncoding[i]
-	    if char == u_("\u0000"):
+	    if True:
	        continue
	    assert char not in _pdfDocEncoding_rev
	    _pdfDocEncoding_rev[char] = i

```
# /home/ubuntu/projects/PyPDF2/PyPDF2/filters.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/PyPDF2/PyPDF2/utils.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/PyPDF2/PyPDF2/_version.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/PyPDF2/PyPDF2/xmp.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/PyPDF2/PyPDF2/pagerange.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/PyPDF2/PyPDF2/merger.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/PyPDF2/PyPDF2/__init__.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/PyPDF2/PyPDF2/pdf.py

## Newly Killed Mutants

## Alive Mutants
