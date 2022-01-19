



# /home/ubuntu/projects/markdown/markdown/util.py

## Newly Killed Mutants

### testYamlMetaData_str_dbl_1
  
Lines 317:323

```diff
	            for k, p in self._priority[key]:
	                data.register(self._data[k], k, p)
	            return data
-	        if isinstance(key, int):
+	        if True:
	            return self._data[self._priority[key].name]
	        return self._data[key]
	

```
## Alive Mutants
  
Lines 29:35

```diff
	
	from .pep562 import Pep562
	
-	if sys.version_info >= (3, 10):
+	if False:
	    from importlib import metadata
	else:
	    # <PY310 use backport

```  
Lines 29:35

```diff
	
	from .pep562 import Pep562
	
-	if sys.version_info >= (3, 10):
+	if (sys.version_info > (3, 10)):
	    from importlib import metadata
	else:
	    # <PY310 use backport

```  
Lines 29:35

```diff
	
	from .pep562 import Pep562
	
-	if sys.version_info >= (3, 10):
+	if (sys.version_info == (3, 10)):
	    from importlib import metadata
	else:
	    # <PY310 use backport

```  
Lines 35:41

```diff
	    # <PY310 use backport
	    import importlib_metadata as metadata
	
-	PY37 = (3, 7) <= sys.version_info
+	PY37 = ((3, 7) < sys.version_info)
	
	
	# TODO: Remove deprecated variables in a future release.

```  
Lines 35:41

```diff
	    # <PY310 use backport
	    import importlib_metadata as metadata
	
-	PY37 = (3, 7) <= sys.version_info
+	PY37 = ((3, 7) >= sys.version_info)
	
	
	# TODO: Remove deprecated variables in a future release.

```  
Lines 35:41

```diff
	    # <PY310 use backport
	    import importlib_metadata as metadata
	
-	PY37 = (3, 7) <= sys.version_info
+	PY37 = ((3, 7) != sys.version_info)
	
	
	# TODO: Remove deprecated variables in a future release.

```  
Lines 35:41

```diff
	    # <PY310 use backport
	    import importlib_metadata as metadata
	
-	PY37 = (3, 7) <= sys.version_info
+	PY37 = ((3, 7) > sys.version_info)
	
	
	# TODO: Remove deprecated variables in a future release.

```  
Lines 35:41

```diff
	    # <PY310 use backport
	    import importlib_metadata as metadata
	
-	PY37 = (3, 7) <= sys.version_info
+	PY37 = ((3, 7) == sys.version_info)
	
	
	# TODO: Remove deprecated variables in a future release.

```  
Lines 72:78

```diff
	ETX = '\u0003'  # Use ETX ("End of text") for end-of-placeholder
	INLINE_PLACEHOLDER_PREFIX = STX+"klzzwxh:"
	INLINE_PLACEHOLDER = INLINE_PLACEHOLDER_PREFIX + "%s" + ETX
-	INLINE_PLACEHOLDER_RE = re.compile(INLINE_PLACEHOLDER % r'([0-9]+)')
+	INLINE_PLACEHOLDER_RE = re.compile((INLINE_PLACEHOLDER + '([0-9]+)'))
	AMP_SUBSTITUTE = STX+"amp"+ETX
	HTML_PLACEHOLDER = STX + "wzxhzdk:%s" + ETX
	HTML_PLACEHOLDER_RE = re.compile(HTML_PLACEHOLDER % r'([0-9]+)')

```  
Lines 75:81

```diff
	INLINE_PLACEHOLDER_RE = re.compile(INLINE_PLACEHOLDER % r'([0-9]+)')
	AMP_SUBSTITUTE = STX+"amp"+ETX
	HTML_PLACEHOLDER = STX + "wzxhzdk:%s" + ETX
-	HTML_PLACEHOLDER_RE = re.compile(HTML_PLACEHOLDER % r'([0-9]+)')
+	HTML_PLACEHOLDER_RE = re.compile((HTML_PLACEHOLDER + '([0-9]+)'))
	TAG_PLACEHOLDER = STX + "hzzhzkh:%s" + ETX
	
	

```  
Lines 76:82

```diff
	AMP_SUBSTITUTE = STX+"amp"+ETX
	HTML_PLACEHOLDER = STX + "wzxhzdk:%s" + ETX
	HTML_PLACEHOLDER_RE = re.compile(HTML_PLACEHOLDER % r'([0-9]+)')
-	TAG_PLACEHOLDER = STX + "hzzhzkh:%s" + ETX
+	TAG_PLACEHOLDER = ((STX + 'hzzhzkh:%s') % ETX)
	
	
	"""

```  
Lines 132:138

```diff
	    return False
	
	
-	def parseBoolValue(value, fail_on_errors=True, preserve_none=False):
+	def parseBoolValue(value, fail_on_errors=True, preserve_none=(True)):
	    """Parses a string representing bool value. If parsing was successful,
	       returns True or False. If preserve_none=True, returns True, False,
	       or None. If parsing was not successful, raises  ValueError, or, if

```  
Lines 132:138

```diff
	    return False
	
	
-	def parseBoolValue(value, fail_on_errors=True, preserve_none=False):
+	def parseBoolValue(value, fail_on_errors=True, preserve_none=None):
	    """Parses a string representing bool value. If parsing was successful,
	       returns True or False. If preserve_none=True, returns True, False,
	       or None. If parsing was not successful, raises  ValueError, or, if

```  
Lines 132:138

```diff
	    return False
	
	
-	def parseBoolValue(value, fail_on_errors=True, preserve_none=False):
+	def parseBoolValue(value, fail_on_errors=(False), preserve_none=False):
	    """Parses a string representing bool value. If parsing was successful,
	       returns True or False. If preserve_none=True, returns True, False,
	       or None. If parsing was not successful, raises  ValueError, or, if

```  
Lines 132:138

```diff
	    return False
	
	
-	def parseBoolValue(value, fail_on_errors=True, preserve_none=False):
+	def parseBoolValue(value, fail_on_errors=None, preserve_none=False):
	    """Parses a string representing bool value. If parsing was successful,
	       returns True or False. If preserve_none=True, returns True, False,
	       or None. If parsing was not successful, raises  ValueError, or, if

```  
Lines 153:159

```diff
	
	def code_escape(text):
	    """Escape code."""
-	    if "&" in text:
+	    if False:
	        text = text.replace("&", "&amp;")
	    if "<" in text:
	        text = text.replace("<", "&lt;")

```  
Lines 153:159

```diff
	
	def code_escape(text):
	    """Escape code."""
-	    if "&" in text:
+	    if True:
	        text = text.replace("&", "&amp;")
	    if "<" in text:
	        text = text.replace("<", "&lt;")

```  
Lines 153:159

```diff
	
	def code_escape(text):
	    """Escape code."""
-	    if "&" in text:
+	    if ('&' not in text):
	        text = text.replace("&", "&amp;")
	    if "<" in text:
	        text = text.replace("<", "&lt;")

```  
Lines 155:161

```diff
	    """Escape code."""
	    if "&" in text:
	        text = text.replace("&", "&amp;")
-	    if "<" in text:
+	    if ('<' not in text):
	        text = text.replace("<", "&lt;")
	    if ">" in text:
	        text = text.replace(">", "&gt;")

```  
Lines 155:161

```diff
	    """Escape code."""
	    if "&" in text:
	        text = text.replace("&", "&amp;")
-	    if "<" in text:
+	    if False:
	        text = text.replace("<", "&lt;")
	    if ">" in text:
	        text = text.replace(">", "&gt;")

```  
Lines 155:161

```diff
	    """Escape code."""
	    if "&" in text:
	        text = text.replace("&", "&amp;")
-	    if "<" in text:
+	    if True:
	        text = text.replace("<", "&lt;")
	    if ">" in text:
	        text = text.replace(">", "&gt;")

```  
Lines 157:163

```diff
	        text = text.replace("&", "&amp;")
	    if "<" in text:
	        text = text.replace("<", "&lt;")
-	    if ">" in text:
+	    if False:
	        text = text.replace(">", "&gt;")
	    return text
	

```  
Lines 157:163

```diff
	        text = text.replace("&", "&amp;")
	    if "<" in text:
	        text = text.replace("<", "&lt;")
-	    if ">" in text:
+	    if True:
	        text = text.replace(">", "&gt;")
	    return text
	

```  
Lines 157:163

```diff
	        text = text.replace("&", "&amp;")
	    if "<" in text:
	        text = text.replace("<", "&lt;")
-	    if ">" in text:
+	    if ('>' not in text):
	        text = text.replace(">", "&gt;")
	    return text
	

```  
Lines 190:196

```diff
	
	
	class Processor:
-	    def __init__(self, md=None):
+	    def __init__(self, md=(False)):
	        self.md = md
	
	    @property

```  
Lines 190:196

```diff
	
	
	class Processor:
-	    def __init__(self, md=None):
+	    def __init__(self, md=(True)):
	        self.md = md
	
	    @property

```  
Lines 297:303

```diff
	    def __init__(self):
	        self._data = {}
	        self._priority = []
-	        self._is_sorted = False
+	        self._is_sorted = (True)
	
	    def __contains__(self, item):
	        if isinstance(item, str):

```  
Lines 297:303

```diff
	    def __init__(self):
	        self._data = {}
	        self._priority = []
-	        self._is_sorted = False
+	        self._is_sorted = None
	
	    def __contains__(self, item):
	        if isinstance(item, str):

```  
Lines 300:306

```diff
	        self._is_sorted = False
	
	    def __contains__(self, item):
-	        if isinstance(item, str):
+	        if False:
	            # Check if an item exists by this name.
	            return item in self._data.keys()
	        # Check if this instance exists.

```  
Lines 300:306

```diff
	        self._is_sorted = False
	
	    def __contains__(self, item):
-	        if isinstance(item, str):
+	        if True:
	            # Check if an item exists by this name.
	            return item in self._data.keys()
	        # Check if this instance exists.

```  
Lines 312:318

```diff
	
	    def __getitem__(self, key):
	        self._sort()
-	        if isinstance(key, slice):
+	        if False:
	            data = Registry()
	            for k, p in self._priority[key]:
	                data.register(self._data[k], k, p)

```  
Lines 354:360

```diff
	        sorted according to its priority and will **not** retain the position
	        of the old item.
	        """
-	        if name in self:
+	        if False:
	            # Remove existing item of same name first
	            self.deregister(name)
	        self._is_sorted = False

```  
Lines 357:363

```diff
	        if name in self:
	            # Remove existing item of same name first
	            self.deregister(name)
-	        self._is_sorted = False
+	        self._is_sorted = (True)
	        self._data[name] = item
	        self._priority.append(_PriorityItem(name, priority))
	

```  
Lines 357:363

```diff
	        if name in self:
	            # Remove existing item of same name first
	            self.deregister(name)
-	        self._is_sorted = False
+	        self._is_sorted = None
	        self._data[name] = item
	        self._priority.append(_PriorityItem(name, priority))
	

```  
Lines 361:367

```diff
	        self._data[name] = item
	        self._priority.append(_PriorityItem(name, priority))
	
-	    def deregister(self, name, strict=True):
+	    def deregister(self, name, strict=(False)):
	        """
	        Remove an item from the registry.
	

```  
Lines 361:367

```diff
	        self._data[name] = item
	        self._priority.append(_PriorityItem(name, priority))
	
-	    def deregister(self, name, strict=True):
+	    def deregister(self, name, strict=None):
	        """
	        Remove an item from the registry.
	

```  
Lines 381:387

```diff
	
	        This method is called internally and should never be explicitly called.
	        """
-	        if not self._is_sorted:
+	        if False:
	            self._priority.sort(key=lambda item: item.priority, reverse=True)
	            self._is_sorted = True
	

```  
Lines 381:387

```diff
	
	        This method is called internally and should never be explicitly called.
	        """
-	        if not self._is_sorted:
+	        if True:
	            self._priority.sort(key=lambda item: item.priority, reverse=True)
	            self._is_sorted = True
	

```  
Lines 383:389

```diff
	        """
	        if not self._is_sorted:
	            self._priority.sort(key=lambda item: item.priority, reverse=True)
-	            self._is_sorted = True
+	            self._is_sorted = (False)
	
	    # Deprecated Methods which provide a smooth transition from OrderedDict
	

```  
Lines 383:389

```diff
	        """
	        if not self._is_sorted:
	            self._priority.sort(key=lambda item: item.priority, reverse=True)
-	            self._is_sorted = True
+	            self._is_sorted = None
	
	    # Deprecated Methods which provide a smooth transition from OrderedDict
	

```  
Lines 471:477

```diff
	    """Get attribute."""
	
	    deprecated = __deprecated__.get(name)
-	    if deprecated:
+	    if False:
	        warnings.warn(
	            "'{}' is deprecated. Use '{}' instead.".format(name, deprecated[0]),
	            category=DeprecationWarning,

```  
Lines 481:485

```diff
	    raise AttributeError("module '{}' has no attribute '{}'".format(__name__, name))
	
	
-	if not PY37:
+	if False:
	    Pep562(__name__)

```  
Lines 481:485

```diff
	    raise AttributeError("module '{}' has no attribute '{}'".format(__name__, name))
	
	
-	if not PY37:
+	if True:
	    Pep562(__name__)

```
# /home/ubuntu/projects/markdown/markdown/serializers.py

## Newly Killed Mutants

### testYamlMetaData_str_dbl_1
  
Lines 153:159

```diff
	                    write(' {}="{}"'.format(k, v))
	        if namespace_uri:
	            write(' xmlns="%s"' % (_escape_attrib(namespace_uri)))
-	        if format == "xhtml" and tag.lower() in HTML_EMPTY:
+	        if (format < 'xhtml') and tag.lower() in HTML_EMPTY:
	            write(" />")
	        else:
	            write(">")

```  
Lines 153:159

```diff
	                    write(' {}="{}"'.format(k, v))
	        if namespace_uri:
	            write(' xmlns="%s"' % (_escape_attrib(namespace_uri)))
-	        if format == "xhtml" and tag.lower() in HTML_EMPTY:
+	        if (format != 'xhtml') and tag.lower() in HTML_EMPTY:
	            write(" />")
	        else:
	            write(">")

```  
Lines 153:159

```diff
	                    write(' {}="{}"'.format(k, v))
	        if namespace_uri:
	            write(' xmlns="%s"' % (_escape_attrib(namespace_uri)))
-	        if format == "xhtml" and tag.lower() in HTML_EMPTY:
+	        if (format > 'xhtml') and tag.lower() in HTML_EMPTY:
	            write(" />")
	        else:
	            write(">")

```  
Lines 153:159

```diff
	                    write(' {}="{}"'.format(k, v))
	        if namespace_uri:
	            write(' xmlns="%s"' % (_escape_attrib(namespace_uri)))
-	        if format == "xhtml" and tag.lower() in HTML_EMPTY:
+	        if False:
	            write(" />")
	        else:
	            write(">")

```
### testBasicMetaData_str_dbl_1
  
Lines 166:172

```diff
	                _serialize_html(write, e, format)
	            if tag.lower() not in HTML_EMPTY:
	                write("</" + tag + ">")
-	    if elem.tail:
+	    if False:
	        write(_escape_cdata(elem.tail))
	
	

```
## Alive Mutants
  
Lines 65:71

```diff
	        # it's worth avoiding do-nothing calls for strings that are
	        # shorter than 500 character, or so.  assume that's, by far,
	        # the most common case in most applications.
-	        if "&" in text:
+	        if False:
	            # Only replace & when not part of an entity
	            text = RE_AMP.sub('&amp;', text)
	        if "<" in text:

```  
Lines 65:71

```diff
	        # it's worth avoiding do-nothing calls for strings that are
	        # shorter than 500 character, or so.  assume that's, by far,
	        # the most common case in most applications.
-	        if "&" in text:
+	        if True:
	            # Only replace & when not part of an entity
	            text = RE_AMP.sub('&amp;', text)
	        if "<" in text:

```  
Lines 65:71

```diff
	        # it's worth avoiding do-nothing calls for strings that are
	        # shorter than 500 character, or so.  assume that's, by far,
	        # the most common case in most applications.
-	        if "&" in text:
+	        if ('&' not in text):
	            # Only replace & when not part of an entity
	            text = RE_AMP.sub('&amp;', text)
	        if "<" in text:

```  
Lines 68:74

```diff
	        if "&" in text:
	            # Only replace & when not part of an entity
	            text = RE_AMP.sub('&amp;', text)
-	        if "<" in text:
+	        if False:
	            text = text.replace("<", "&lt;")
	        if ">" in text:
	            text = text.replace(">", "&gt;")

```  
Lines 68:74

```diff
	        if "&" in text:
	            # Only replace & when not part of an entity
	            text = RE_AMP.sub('&amp;', text)
-	        if "<" in text:
+	        if True:
	            text = text.replace("<", "&lt;")
	        if ">" in text:
	            text = text.replace(">", "&gt;")

```  
Lines 68:74

```diff
	        if "&" in text:
	            # Only replace & when not part of an entity
	            text = RE_AMP.sub('&amp;', text)
-	        if "<" in text:
+	        if ('<' not in text):
	            text = text.replace("<", "&lt;")
	        if ">" in text:
	            text = text.replace(">", "&gt;")

```  
Lines 70:76

```diff
	            text = RE_AMP.sub('&amp;', text)
	        if "<" in text:
	            text = text.replace("<", "&lt;")
-	        if ">" in text:
+	        if ('>' not in text):
	            text = text.replace(">", "&gt;")
	        return text
	    except (TypeError, AttributeError):  # pragma: no cover

```  
Lines 70:76

```diff
	            text = RE_AMP.sub('&amp;', text)
	        if "<" in text:
	            text = text.replace("<", "&lt;")
-	        if ">" in text:
+	        if False:
	            text = text.replace(">", "&gt;")
	        return text
	    except (TypeError, AttributeError):  # pragma: no cover

```  
Lines 70:76

```diff
	            text = RE_AMP.sub('&amp;', text)
	        if "<" in text:
	            text = text.replace("<", "&lt;")
-	        if ">" in text:
+	        if True:
	            text = text.replace(">", "&gt;")
	        return text
	    except (TypeError, AttributeError):  # pragma: no cover

```  
Lines 116:122

```diff
	def _serialize_html(write, elem, format):
	    tag = elem.tag
	    text = elem.text
-	    if tag is Comment:
+	    if False:
	        write("<!--%s-->" % _escape_cdata(text))
	    elif tag is ProcessingInstruction:
	        write("<?%s?>" % _escape_cdata(text))

```  
Lines 118:124

```diff
	    text = elem.text
	    if tag is Comment:
	        write("<!--%s-->" % _escape_cdata(text))
-	    elif tag is ProcessingInstruction:
+	    elif False:
	        write("<?%s?>" % _escape_cdata(text))
	    elif tag is None:
	        if text:

```  
Lines 120:126

```diff
	        write("<!--%s-->" % _escape_cdata(text))
	    elif tag is ProcessingInstruction:
	        write("<?%s?>" % _escape_cdata(text))
-	    elif tag is None:
+	    elif tag is (False):
	        if text:
	            write(_escape_cdata(text))
	        for e in elem:

```  
Lines 120:126

```diff
	        write("<!--%s-->" % _escape_cdata(text))
	    elif tag is ProcessingInstruction:
	        write("<?%s?>" % _escape_cdata(text))
-	    elif tag is None:
+	    elif tag is (True):
	        if text:
	            write(_escape_cdata(text))
	        for e in elem:

```  
Lines 120:126

```diff
	        write("<!--%s-->" % _escape_cdata(text))
	    elif tag is ProcessingInstruction:
	        write("<?%s?>" % _escape_cdata(text))
-	    elif tag is None:
+	    elif False:
	        if text:
	            write(_escape_cdata(text))
	        for e in elem:

```  
Lines 126:132

```diff
	        for e in elem:
	            _serialize_html(write, e, format)
	    else:
-	        namespace_uri = None
+	        namespace_uri = (False)
	        if isinstance(tag, QName):
	            # QNAME objects store their data as a string: `{uri}tag`
	            if tag.text[:1] == "{":

```  
Lines 127:133

```diff
	            _serialize_html(write, e, format)
	    else:
	        namespace_uri = None
-	        if isinstance(tag, QName):
+	        if False:
	            # QNAME objects store their data as a string: `{uri}tag`
	            if tag.text[:1] == "{":
	                namespace_uri, tag = tag.text[1:].split("}", 1)

```  
Lines 135:141

```diff
	                raise ValueError('QName objects must define a tag.')
	        write("<" + tag)
	        items = elem.items()
-	        if items:
+	        if False:
	            items = sorted(items)  # lexical order
	            for k, v in items:
	                if isinstance(k, QName):

```  
Lines 135:141

```diff
	                raise ValueError('QName objects must define a tag.')
	        write("<" + tag)
	        items = elem.items()
-	        if items:
+	        if True:
	            items = sorted(items)  # lexical order
	            for k, v in items:
	                if isinstance(k, QName):

```  
Lines 151:157

```diff
	                    write(" %s" % v)
	                else:
	                    write(' {}="{}"'.format(k, v))
-	        if namespace_uri:
+	        if False:
	            write(' xmlns="%s"' % (_escape_attrib(namespace_uri)))
	        if format == "xhtml" and tag.lower() in HTML_EMPTY:
	            write(" />")

```  
Lines 153:159

```diff
	                    write(' {}="{}"'.format(k, v))
	        if namespace_uri:
	            write(' xmlns="%s"' % (_escape_attrib(namespace_uri)))
-	        if format == "xhtml" and tag.lower() in HTML_EMPTY:
+	        if (format >= 'xhtml') and tag.lower() in HTML_EMPTY:
	            write(" />")
	        else:
	            write(">")

```  
Lines 153:159

```diff
	                    write(' {}="{}"'.format(k, v))
	        if namespace_uri:
	            write(' xmlns="%s"' % (_escape_attrib(namespace_uri)))
-	        if format == "xhtml" and tag.lower() in HTML_EMPTY:
+	        if (format <= 'xhtml') and tag.lower() in HTML_EMPTY:
	            write(" />")
	        else:
	            write(">")

```  
Lines 158:164

```diff
	        else:
	            write(">")
	            if text:
-	                if tag.lower() in ["script", "style"]:
+	                if False:
	                    write(text)
	                else:
	                    write(_escape_cdata(text))

```  
Lines 158:164

```diff
	        else:
	            write(">")
	            if text:
-	                if tag.lower() in ["script", "style"]:
+	                if True:
	                    write(text)
	                else:
	                    write(_escape_cdata(text))

```  
Lines 158:164

```diff
	        else:
	            write(">")
	            if text:
-	                if tag.lower() in ["script", "style"]:
+	                if (tag.lower() not in ['script', 'style']):
	                    write(text)
	                else:
	                    write(_escape_cdata(text))

```  
Lines 164:170

```diff
	                    write(_escape_cdata(text))
	            for e in elem:
	                _serialize_html(write, e, format)
-	            if tag.lower() not in HTML_EMPTY:
+	            if True:
	                write("</" + tag + ">")
	    if elem.tail:
	        write(_escape_cdata(elem.tail))

```  
Lines 171:177

```diff
	
	
	def _write_html(root, format="html"):
-	    assert root is not None
+	    assert root is not (False)
	    data = []
	    write = data.append
	    _serialize_html(write, root, format)

```  
Lines 171:177

```diff
	
	
	def _write_html(root, format="html"):
-	    assert root is not None
+	    assert root is not (True)
	    data = []
	    write = data.append
	    _serialize_html(write, root, format)

```
# /home/ubuntu/projects/markdown/markdown/core.py

## Newly Killed Mutants

### testBasicMetaData_str_dbl_1
  
Lines 217:223

```diff
	
	    def is_block_level(self, tag):
	        """Check if the tag is a block level HTML tag."""
-	        if isinstance(tag, str):
+	        if False:
	            return tag.lower().rstrip('/') in self.block_level_elements
	        # Some ElementTree tags are not strings, so return False.
	        return False

```  
Lines 218:224

```diff
	    def is_block_level(self, tag):
	        """Check if the tag is a block level HTML tag."""
	        if isinstance(tag, str):
-	            return tag.lower().rstrip('/') in self.block_level_elements
+	            return (tag.lower().rstrip('/') not in self.block_level_elements)
	        # Some ElementTree tags are not strings, so return False.
	        return False
	

```
### testBasicMetaData_none_1
  
Lines 245:251

```diff
	        """
	
	        # Fixup the source text
-	        if not source.strip():
+	        if False:
	            return ''  # a blank unicode string
	
	        try:

```
## Alive Mutants
  
Lines 119:125

```diff
	
	        """
	        for ext in extensions:
-	            if isinstance(ext, str):
+	            if True:
	                ext = self.build_extension(ext, configs.get(ext, {}))
	            if isinstance(ext, Extension):
	                ext._extendMarkdown(self)

```  
Lines 121:127

```diff
	        for ext in extensions:
	            if isinstance(ext, str):
	                ext = self.build_extension(ext, configs.get(ext, {}))
-	            if isinstance(ext, Extension):
+	            if True:
	                ext._extendMarkdown(self)
	                logger.debug(
	                    'Successfully loaded extension "%s.%s".'

```  
Lines 150:156

```diff
	        """
	        configs = dict(configs)
	
-	        entry_points = [ep for ep in util.INSTALLED_EXTENSIONS if ep.name == ext_name]
+	        entry_points = [ep for ep in util.INSTALLED_EXTENSIONS if (ep.name >= ext_name)]
	        if entry_points:
	            ext = entry_points[0].load()
	            return ext(**configs)

```  
Lines 151:157

```diff
	        configs = dict(configs)
	
	        entry_points = [ep for ep in util.INSTALLED_EXTENSIONS if ep.name == ext_name]
-	        if entry_points:
+	        if True:
	            ext = entry_points[0].load()
	            return ext(**configs)
	

```  
Lines 152:158

```diff
	
	        entry_points = [ep for ep in util.INSTALLED_EXTENSIONS if ep.name == ext_name]
	        if entry_points:
-	            ext = entry_points[0].load()
+	            ext = entry_points[<_ast.Constant object at 0x7fe42500b550>].load()
	            return ext(**configs)
	
	        # Get class name (if provided): `path.to.module:ClassName`

```  
Lines 195:201

```diff
	        self.references.clear()
	
	        for extension in self.registeredExtensions:
-	            if hasattr(extension, 'reset'):
+	            if True:
	                extension.reset()
	
	        return self

```  
Lines 217:223

```diff
	
	    def is_block_level(self, tag):
	        """Check if the tag is a block level HTML tag."""
-	        if isinstance(tag, str):
+	        if True:
	            return tag.lower().rstrip('/') in self.block_level_elements
	        # Some ElementTree tags are not strings, so return False.
	        return False

```  
Lines 266:272

```diff
	        # Run the tree-processors
	        for treeprocessor in self.treeprocessors:
	            newRoot = treeprocessor.run(root)
-	            if newRoot is not None:
+	            if False:
	                root = newRoot
	
	        # Serialize _properly_.  Strip top-level tags.

```  
Lines 271:277

```diff
	
	        # Serialize _properly_.  Strip top-level tags.
	        output = self.serializer(root)
-	        if self.stripTopLevelTags:
+	        if True:
	            try:
	                start = output.index(
	                    '<%s>' % self.doc_tag) + len(self.doc_tag) + 2

```  
Lines 273:280

```diff
	        output = self.serializer(root)
	        if self.stripTopLevelTags:
	            try:
-	                start = output.index(
-	                    '<%s>' % self.doc_tag) + len(self.doc_tag) + 2
+	                start = ((output.index('<%s>' % self.doc_tag) + len(self.doc_tag)) * 2)
	                end = output.rindex('</%s>' % self.doc_tag)
	                output = output[start:end].strip()
	            except ValueError as e:  # pragma: no cover

```  
Lines 292:298

```diff
	
	        return output.strip()
	
-	    def convertFile(self, input=None, output=None, encoding=None):
+	    def convertFile(self, input=None, output=(False), encoding=None):
	        """Converts a markdown file and returns the HTML as a unicode string.
	
	        Decodes the file using the provided encoding (defaults to utf-8),

```  
Lines 292:298

```diff
	
	        return output.strip()
	
-	    def convertFile(self, input=None, output=None, encoding=None):
+	    def convertFile(self, input=None, output=(True), encoding=None):
	        """Converts a markdown file and returns the HTML as a unicode string.
	
	        Decodes the file using the provided encoding (defaults to utf-8),

```  
Lines 292:298

```diff
	
	        return output.strip()
	
-	    def convertFile(self, input=None, output=None, encoding=None):
+	    def convertFile(self, input=None, output=None, encoding=(False)):
	        """Converts a markdown file and returns the HTML as a unicode string.
	
	        Decodes the file using the provided encoding (defaults to utf-8),

```  
Lines 292:298

```diff
	
	        return output.strip()
	
-	    def convertFile(self, input=None, output=None, encoding=None):
+	    def convertFile(self, input=None, output=None, encoding=(True)):
	        """Converts a markdown file and returns the HTML as a unicode string.
	
	        Decodes the file using the provided encoding (defaults to utf-8),

```  
Lines 292:298

```diff
	
	        return output.strip()
	
-	    def convertFile(self, input=None, output=None, encoding=None):
+	    def convertFile(self, input=(False), output=None, encoding=None):
	        """Converts a markdown file and returns the HTML as a unicode string.
	
	        Decodes the file using the provided encoding (defaults to utf-8),

```  
Lines 292:298

```diff
	
	        return output.strip()
	
-	    def convertFile(self, input=None, output=None, encoding=None):
+	    def convertFile(self, input=(True), output=None, encoding=None):
	        """Converts a markdown file and returns the HTML as a unicode string.
	
	        Decodes the file using the provided encoding (defaults to utf-8),

```
# /home/ubuntu/projects/markdown/markdown/htmlparser.py

## Newly Killed Mutants

## Alive Mutants
  
Lines 70:76

```diff
	    """
	
	    def __init__(self, md, *args, **kwargs):
-	        if 'convert_charrefs' not in kwargs:
+	        if False:
	            kwargs['convert_charrefs'] = False
	
	        # Block tags that should contain no content (self closing)

```  
Lines 70:76

```diff
	    """
	
	    def __init__(self, md, *args, **kwargs):
-	        if 'convert_charrefs' not in kwargs:
+	        if True:
	            kwargs['convert_charrefs'] = False
	
	        # Block tags that should contain no content (self closing)

```  
Lines 70:76

```diff
	    """
	
	    def __init__(self, md, *args, **kwargs):
-	        if 'convert_charrefs' not in kwargs:
+	        if ('convert_charrefs' in kwargs):
	            kwargs['convert_charrefs'] = False
	
	        # Block tags that should contain no content (self closing)

```  
Lines 71:77

```diff
	
	    def __init__(self, md, *args, **kwargs):
	        if 'convert_charrefs' not in kwargs:
-	            kwargs['convert_charrefs'] = False
+	            kwargs['convert_charrefs'] = (True)
	
	        # Block tags that should contain no content (self closing)
	        self.empty_tags = set(['hr'])

```  
Lines 71:77

```diff
	
	    def __init__(self, md, *args, **kwargs):
	        if 'convert_charrefs' not in kwargs:
-	            kwargs['convert_charrefs'] = False
+	            kwargs['convert_charrefs'] = None
	
	        # Block tags that should contain no content (self closing)
	        self.empty_tags = set(['hr'])

```  
Lines 82:88

```diff
	
	    def reset(self):
	        """Reset this instance.  Loses all unprocessed data."""
-	        self.inraw = False
+	        self.inraw = None
	        self.intail = False
	        self.stack = []  # When inraw==True, stack contains a list of tags
	        self._cache = []

```  
Lines 83:89

```diff
	    def reset(self):
	        """Reset this instance.  Loses all unprocessed data."""
	        self.inraw = False
-	        self.intail = False
+	        self.intail = (True)
	        self.stack = []  # When inraw==True, stack contains a list of tags
	        self._cache = []
	        self.cleandoc = []

```  
Lines 83:89

```diff
	    def reset(self):
	        """Reset this instance.  Loses all unprocessed data."""
	        self.inraw = False
-	        self.intail = False
+	        self.intail = None
	        self.stack = []  # When inraw==True, stack contains a list of tags
	        self._cache = []
	        self.cleandoc = []

```  
Lines 92:98

```diff
	    def close(self):
	        """Handle any buffered data."""
	        super().close()
-	        if len(self.rawdata):
+	        if False:
	            # Temp fix for https://bugs.python.org/issue41989
	            # TODO: remove this when the bug is fixed in all supported Python versions.
	            if self.convert_charrefs and not self.cdata_elem:  # pragma: no cover

```  
Lines 92:98

```diff
	    def close(self):
	        """Handle any buffered data."""
	        super().close()
-	        if len(self.rawdata):
+	        if True:
	            # Temp fix for https://bugs.python.org/issue41989
	            # TODO: remove this when the bug is fixed in all supported Python versions.
	            if self.convert_charrefs and not self.cdata_elem:  # pragma: no cover

```  
Lines 100:106

```diff
	            else:
	                self.handle_data(self.rawdata)
	        # Handle any unclosed tags.
-	        if len(self._cache):
+	        if False:
	            self.cleandoc.append(self.md.htmlStash.store(''.join(self._cache)))
	            self._cache = []
	

```  
Lines 194:200

```diff
	            self.cleandoc.append(text)
	
	    def handle_data(self, data):
-	        if self.intail and '\n' in data:
+	        if False:
	            self.intail = False
	        if self.inraw:
	            self._cache.append(data)

```  
Lines 194:200

```diff
	            self.cleandoc.append(text)
	
	    def handle_data(self, data):
-	        if self.intail and '\n' in data:
+	        if True:
	            self.intail = False
	        if self.inraw:
	            self._cache.append(data)

```  
Lines 194:200

```diff
	            self.cleandoc.append(text)
	
	    def handle_data(self, data):
-	        if self.intail and '\n' in data:
+	        if (self.intail or '\n' in data):
	            self.intail = False
	        if self.inraw:
	            self._cache.append(data)

```  
Lines 194:200

```diff
	            self.cleandoc.append(text)
	
	    def handle_data(self, data):
-	        if self.intail and '\n' in data:
+	        if self.intail and ('\n' not in data):
	            self.intail = False
	        if self.inraw:
	            self._cache.append(data)

```  
Lines 196:202

```diff
	    def handle_data(self, data):
	        if self.intail and '\n' in data:
	            self.intail = False
-	        if self.inraw:
+	        if False:
	            self._cache.append(data)
	        else:
	            self.cleandoc.append(data)

```  
Lines 266:272

```diff
	    # As __startag_text is private, all references to it must be in this subclass.
	    # The last few lines of parse_starttag are reversed so that handle_starttag
	    # can override cdata_mode in certain situations (in a code span).
-	    __starttag_text = None
+	    __starttag_text = (False)
	
	    def get_starttag_text(self):
	        """Return full source of start tag: '<...>'."""

```  
Lines 266:272

```diff
	    # As __startag_text is private, all references to it must be in this subclass.
	    # The last few lines of parse_starttag are reversed so that handle_starttag
	    # can override cdata_mode in certain situations (in a code span).
-	    __starttag_text = None
+	    __starttag_text = (True)
	
	    def get_starttag_text(self):
	        """Return full source of start tag: '<...>'."""

```
# /home/ubuntu/projects/markdown/markdown/__main__.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/pep562.py

## Newly Killed Mutants

## Alive Mutants
  
Lines 108:114

```diff
	
	        # Ensure all parts are positive integers.
	        for value in (major, minor, micro, pre, post):
-	            if not (isinstance(value, int) and value >= 0):
+	            if not ((isinstance(value, int) or value >= 0)):
	                raise ValueError("All version parts except 'release' should be integers.")
	
	        if release not in REL_MAP:

```  
Lines 108:114

```diff
	
	        # Ensure all parts are positive integers.
	        for value in (major, minor, micro, pre, post):
-	            if not (isinstance(value, int) and value >= 0):
+	            if False:
	                raise ValueError("All version parts except 'release' should be integers.")
	
	        if release not in REL_MAP:

```  
Lines 111:117

```diff
	            if not (isinstance(value, int) and value >= 0):
	                raise ValueError("All version parts except 'release' should be integers.")
	
-	        if release not in REL_MAP:
+	        if False:
	            raise ValueError("'{}' is not a valid release type.".format(release))
	
	        # Ensure valid pre-release (we do not allow implicit pre-releases).

```  
Lines 115:121

```diff
	            raise ValueError("'{}' is not a valid release type.".format(release))
	
	        # Ensure valid pre-release (we do not allow implicit pre-releases).
-	        if ".dev-candidate" < release < "final":
+	        if False:
	            if pre == 0:
	                raise ValueError("Implicit pre-releases not allowed.")
	            elif dev:

```  
Lines 115:121

```diff
	            raise ValueError("'{}' is not a valid release type.".format(release))
	
	        # Ensure valid pre-release (we do not allow implicit pre-releases).
-	        if ".dev-candidate" < release < "final":
+	        if ('.dev-candidate' >= release):
	            if pre == 0:
	                raise ValueError("Implicit pre-releases not allowed.")
	            elif dev:

```  
Lines 115:121

```diff
	            raise ValueError("'{}' is not a valid release type.".format(release))
	
	        # Ensure valid pre-release (we do not allow implicit pre-releases).
-	        if ".dev-candidate" < release < "final":
+	        if ('.dev-candidate' != release):
	            if pre == 0:
	                raise ValueError("Implicit pre-releases not allowed.")
	            elif dev:

```  
Lines 115:121

```diff
	            raise ValueError("'{}' is not a valid release type.".format(release))
	
	        # Ensure valid pre-release (we do not allow implicit pre-releases).
-	        if ".dev-candidate" < release < "final":
+	        if ('.dev-candidate' > release):
	            if pre == 0:
	                raise ValueError("Implicit pre-releases not allowed.")
	            elif dev:

```  
Lines 115:121

```diff
	            raise ValueError("'{}' is not a valid release type.".format(release))
	
	        # Ensure valid pre-release (we do not allow implicit pre-releases).
-	        if ".dev-candidate" < release < "final":
+	        if ('.dev-candidate' == release):
	            if pre == 0:
	                raise ValueError("Implicit pre-releases not allowed.")
	            elif dev:

```  
Lines 115:121

```diff
	            raise ValueError("'{}' is not a valid release type.".format(release))
	
	        # Ensure valid pre-release (we do not allow implicit pre-releases).
-	        if ".dev-candidate" < release < "final":
+	        if ('.dev-candidate' <= release):
	            if pre == 0:
	                raise ValueError("Implicit pre-releases not allowed.")
	            elif dev:

```  
Lines 124:130

```diff
	                raise ValueError("Post-releases are not allowed with pre-releases.")
	
	        # Ensure valid development or development/pre release
-	        elif release < "alpha":
+	        elif False:
	            if release > ".dev" and pre == 0:
	                raise ValueError("Implicit pre-release not allowed.")
	            elif post:

```  
Lines 124:130

```diff
	                raise ValueError("Post-releases are not allowed with pre-releases.")
	
	        # Ensure valid development or development/pre release
-	        elif release < "alpha":
+	        elif (release == 'alpha'):
	            if release > ".dev" and pre == 0:
	                raise ValueError("Implicit pre-release not allowed.")
	            elif post:

```  
Lines 124:130

```diff
	                raise ValueError("Post-releases are not allowed with pre-releases.")
	
	        # Ensure valid development or development/pre release
-	        elif release < "alpha":
+	        elif (release <= 'alpha'):
	            if release > ".dev" and pre == 0:
	                raise ValueError("Implicit pre-release not allowed.")
	            elif post:

```  
Lines 132:138

```diff
	
	        # Ensure a valid normal release
	        else:
-	            if pre:
+	            if False:
	                raise ValueError("Version is not a pre-release.")
	            elif dev:
	                raise ValueError("Version is not a development release.")

```  
Lines 134:140

```diff
	        else:
	            if pre:
	                raise ValueError("Version is not a pre-release.")
-	            elif dev:
+	            elif False:
	                raise ValueError("Version is not a development release.")
	
	        return super().__new__(cls, major, minor, micro, release, pre, post, dev)

```  
Lines 142:148

```diff
	    def _is_pre(self):
	        """Is prerelease."""
	
-	        return self.pre > 0
+	        return (self.pre < 0)
	
	    def _is_dev(self):
	        """Is development."""

```  
Lines 142:148

```diff
	    def _is_pre(self):
	        """Is prerelease."""
	
-	        return self.pre > 0
+	        return (self.pre >= 0)
	
	    def _is_dev(self):
	        """Is development."""

```  
Lines 142:148

```diff
	    def _is_pre(self):
	        """Is prerelease."""
	
-	        return self.pre > 0
+	        return (self.pre != 0)
	
	    def _is_dev(self):
	        """Is development."""

```  
Lines 142:148

```diff
	    def _is_pre(self):
	        """Is prerelease."""
	
-	        return self.pre > 0
+	        return (self.pre == 0)
	
	    def _is_dev(self):
	        """Is development."""

```  
Lines 142:148

```diff
	    def _is_pre(self):
	        """Is prerelease."""
	
-	        return self.pre > 0
+	        return (self.pre <= 0)
	
	    def _is_dev(self):
	        """Is development."""

```  
Lines 147:153

```diff
	    def _is_dev(self):
	        """Is development."""
	
-	        return bool(self.release < "alpha")
+	        return bool((self.release >= 'alpha'))
	
	    def _is_post(self):
	        """Is post."""

```  
Lines 147:153

```diff
	    def _is_dev(self):
	        """Is development."""
	
-	        return bool(self.release < "alpha")
+	        return bool((self.release != 'alpha'))
	
	    def _is_post(self):
	        """Is post."""

```  
Lines 147:153

```diff
	    def _is_dev(self):
	        """Is development."""
	
-	        return bool(self.release < "alpha")
+	        return bool((self.release > 'alpha'))
	
	    def _is_post(self):
	        """Is post."""

```  
Lines 147:153

```diff
	    def _is_dev(self):
	        """Is development."""
	
-	        return bool(self.release < "alpha")
+	        return bool((self.release == 'alpha'))
	
	    def _is_post(self):
	        """Is post."""

```  
Lines 147:153

```diff
	    def _is_dev(self):
	        """Is development."""
	
-	        return bool(self.release < "alpha")
+	        return bool((self.release <= 'alpha'))
	
	    def _is_post(self):
	        """Is post."""

```  
Lines 152:158

```diff
	    def _is_post(self):
	        """Is post."""
	
-	        return self.post > 0
+	        return (self.post < 0)
	
	    def _get_dev_status(self):  # pragma: no cover
	        """Get development status string."""

```  
Lines 152:158

```diff
	    def _is_post(self):
	        """Is post."""
	
-	        return self.post > 0
+	        return (self.post >= 0)
	
	    def _get_dev_status(self):  # pragma: no cover
	        """Get development status string."""

```  
Lines 152:158

```diff
	    def _is_post(self):
	        """Is post."""
	
-	        return self.post > 0
+	        return (self.post != 0)
	
	    def _get_dev_status(self):  # pragma: no cover
	        """Get development status string."""

```  
Lines 152:158

```diff
	    def _is_post(self):
	        """Is post."""
	
-	        return self.post > 0
+	        return (self.post == 0)
	
	    def _get_dev_status(self):  # pragma: no cover
	        """Get development status string."""

```  
Lines 152:158

```diff
	    def _is_post(self):
	        """Is post."""
	
-	        return self.post > 0
+	        return (self.post <= 0)
	
	    def _get_dev_status(self):  # pragma: no cover
	        """Get development status string."""

```  
Lines 163:169

```diff
	        """Get the canonical output string."""
	
	        # Assemble major, minor, micro version and append `pre`, `post`, or `dev` if needed..
-	        if self.micro == 0:
+	        if False:
	            ver = "{}.{}".format(self.major, self.minor)
	        else:
	            ver = "{}.{}.{}".format(self.major, self.minor, self.micro)

```  
Lines 163:169

```diff
	        """Get the canonical output string."""
	
	        # Assemble major, minor, micro version and append `pre`, `post`, or `dev` if needed..
-	        if self.micro == 0:
+	        if True:
	            ver = "{}.{}".format(self.major, self.minor)
	        else:
	            ver = "{}.{}.{}".format(self.major, self.minor, self.micro)

```  
Lines 163:169

```diff
	        """Get the canonical output string."""
	
	        # Assemble major, minor, micro version and append `pre`, `post`, or `dev` if needed..
-	        if self.micro == 0:
+	        if (self.micro < 0):
	            ver = "{}.{}".format(self.major, self.minor)
	        else:
	            ver = "{}.{}.{}".format(self.major, self.minor, self.micro)

```  
Lines 163:169

```diff
	        """Get the canonical output string."""
	
	        # Assemble major, minor, micro version and append `pre`, `post`, or `dev` if needed..
-	        if self.micro == 0:
+	        if (self.micro >= 0):
	            ver = "{}.{}".format(self.major, self.minor)
	        else:
	            ver = "{}.{}.{}".format(self.major, self.minor, self.micro)

```  
Lines 163:169

```diff
	        """Get the canonical output string."""
	
	        # Assemble major, minor, micro version and append `pre`, `post`, or `dev` if needed..
-	        if self.micro == 0:
+	        if (self.micro != 0):
	            ver = "{}.{}".format(self.major, self.minor)
	        else:
	            ver = "{}.{}.{}".format(self.major, self.minor, self.micro)

```  
Lines 163:169

```diff
	        """Get the canonical output string."""
	
	        # Assemble major, minor, micro version and append `pre`, `post`, or `dev` if needed..
-	        if self.micro == 0:
+	        if (self.micro > 0):
	            ver = "{}.{}".format(self.major, self.minor)
	        else:
	            ver = "{}.{}.{}".format(self.major, self.minor, self.micro)

```  
Lines 163:169

```diff
	        """Get the canonical output string."""
	
	        # Assemble major, minor, micro version and append `pre`, `post`, or `dev` if needed..
-	        if self.micro == 0:
+	        if (self.micro <= 0):
	            ver = "{}.{}".format(self.major, self.minor)
	        else:
	            ver = "{}.{}.{}".format(self.major, self.minor, self.micro)

```  
Lines 167:173

```diff
	            ver = "{}.{}".format(self.major, self.minor)
	        else:
	            ver = "{}.{}.{}".format(self.major, self.minor, self.micro)
-	        if self._is_pre():
+	        if False:
	            ver += '{}{}'.format(REL_MAP[self.release], self.pre)
	        if self._is_post():
	            ver += ".post{}".format(self.post)

```  
Lines 167:173

```diff
	            ver = "{}.{}".format(self.major, self.minor)
	        else:
	            ver = "{}.{}.{}".format(self.major, self.minor, self.micro)
-	        if self._is_pre():
+	        if True:
	            ver += '{}{}'.format(REL_MAP[self.release], self.pre)
	        if self._is_post():
	            ver += ".post{}".format(self.post)

```  
Lines 169:175

```diff
	            ver = "{}.{}.{}".format(self.major, self.minor, self.micro)
	        if self._is_pre():
	            ver += '{}{}'.format(REL_MAP[self.release], self.pre)
-	        if self._is_post():
+	        if False:
	            ver += ".post{}".format(self.post)
	        if self._is_dev():
	            ver += ".dev{}".format(self.dev)

```  
Lines 169:175

```diff
	            ver = "{}.{}.{}".format(self.major, self.minor, self.micro)
	        if self._is_pre():
	            ver += '{}{}'.format(REL_MAP[self.release], self.pre)
-	        if self._is_post():
+	        if True:
	            ver += ".post{}".format(self.post)
	        if self._is_dev():
	            ver += ".dev{}".format(self.dev)

```  
Lines 171:177

```diff
	            ver += '{}{}'.format(REL_MAP[self.release], self.pre)
	        if self._is_post():
	            ver += ".post{}".format(self.post)
-	        if self._is_dev():
+	        if False:
	            ver += ".dev{}".format(self.dev)
	
	        return ver

```  
Lines 171:177

```diff
	            ver += '{}{}'.format(REL_MAP[self.release], self.pre)
	        if self._is_post():
	            ver += ".post{}".format(self.post)
-	        if self._is_dev():
+	        if True:
	            ver += ".dev{}".format(self.dev)
	
	        return ver

```  
Lines 177:183

```diff
	        return ver
	
	
-	def parse_version(ver, pre=False):
+	def parse_version(ver, pre=(True)):
	    """Parse version into a comparable Version tuple."""
	
	    m = RE_VER.match(ver)

```  
Lines 177:183

```diff
	        return ver
	
	
-	def parse_version(ver, pre=False):
+	def parse_version(ver, pre=None):
	    """Parse version into a comparable Version tuple."""
	
	    m = RE_VER.match(ver)

```
# /home/ubuntu/projects/markdown/markdown/inlinepatterns.py

## Newly Killed Mutants

### testBasicMetaData_str_dbl_1
  
Lines 573:579

```diff
	
	        for index, item in enumerate(self.PATTERNS):
	            m1 = item.pattern.match(data, m.start(0))
-	            if m1:
+	            if True:
	                start = m1.start(0)
	                end = m1.end(0)
	                el = self.build_element(m1, item.builder, item.tags, index)

```
### testYamlMetaData_str_dbl_1
  
Lines 605:611

```diff
	            return None, None, None
	
	        href, title, index, handled = self.getLink(data, index)
-	        if not handled:
+	        if False:
	            return None, None, None
	
	        el = etree.Element("a")

```  
Lines 622:628

```diff
	        """Parse data between `()` of `[Text]()` allowing recursive `()`. """
	
	        href = ''
-	        title = None
+	        title = (False)
	        handled = False
	
	        m = self.RE_LINK.match(data, pos=index)

```  
Lines 622:628

```diff
	        """Parse data between `()` of `[Text]()` allowing recursive `()`. """
	
	        href = ''
-	        title = None
+	        title = (True)
	        handled = False
	
	        m = self.RE_LINK.match(data, pos=index)

```  
Lines 623:629

```diff
	
	        href = ''
	        title = None
-	        handled = False
+	        handled = (True)
	
	        m = self.RE_LINK.match(data, pos=index)
	        if m and m.group(1):

```  
Lines 626:632

```diff
	        handled = False
	
	        m = self.RE_LINK.match(data, pos=index)
-	        if m and m.group(1):
+	        if True:
	            # Matches [Text](<link> "title")
	            href = m.group(1)[1:-1].strip()
	            if m.group(2):

```  
Lines 626:632

```diff
	        handled = False
	
	        m = self.RE_LINK.match(data, pos=index)
-	        if m and m.group(1):
+	        if (m or m.group(1)):
	            # Matches [Text](<link> "title")
	            href = m.group(1)[1:-1].strip()
	            if m.group(2):

```  
Lines 633:639

```diff
	                title = m.group(2)[1:-1]
	            index = m.end(0)
	            handled = True
-	        elif m:
+	        elif True:
	            # Track bracket nesting and index in string
	            bracket_count = 1
	            backtrack_count = 1

```  
Lines 727:733

```diff
	
	            handled = bracket_count == 0
	
-	        if title is not None:
+	        if True:
	            title = self.RE_TITLE_CLEAN.sub(' ', dequote(self.unescape(title.strip())))
	
	        href = self.unescape(href).strip()

```  
Lines 727:733

```diff
	
	            handled = bracket_count == 0
	
-	        if title is not None:
+	        if title is not (False):
	            title = self.RE_TITLE_CLEAN.sub(' ', dequote(self.unescape(title.strip())))
	
	        href = self.unescape(href).strip()

```  
Lines 727:733

```diff
	
	            handled = bracket_count == 0
	
-	        if title is not None:
+	        if title is not (True):
	            title = self.RE_TITLE_CLEAN.sub(' ', dequote(self.unescape(title.strip())))
	
	        href = self.unescape(href).strip()

```  
Lines 727:733

```diff
	
	            handled = bracket_count == 0
	
-	        if title is not None:
+	        if (title is None):
	            title = self.RE_TITLE_CLEAN.sub(' ', dequote(self.unescape(title.strip())))
	
	        href = self.unescape(href).strip()

```  
Lines 747:753

```diff
	                bracket_count -= 1
	            elif c == '[':
	                bracket_count += 1
-	            index += 1
+	            index /= 1
	            if bracket_count == 0:
	                break
	            text.append(c)

```  
Lines 789:795

```diff
	            return None, None, None
	
	        id, end, handled = self.evalId(data, index, text)
-	        if not handled:
+	        if False:
	            return None, None, None
	
	        # Clean up linebreaks in id

```  
Lines 794:800

```diff
	
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)
-	        if id not in self.md.references:  # ignore undefined refs
+	        if False:  # ignore undefined refs
	            return None, m.start(0), end
	
	        href, title = self.md.references[id]

```  
Lines 794:800

```diff
	
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)
-	        if id not in self.md.references:  # ignore undefined refs
+	        if (id in self.md.references):  # ignore undefined refs
	            return None, m.start(0), end
	
	        href, title = self.md.references[id]

```  
Lines 795:801

```diff
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)
	        if id not in self.md.references:  # ignore undefined refs
-	            return None, m.start(0), end
+	            return (False), m.start(0), end
	
	        href, title = self.md.references[id]
	

```  
Lines 795:801

```diff
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)
	        if id not in self.md.references:  # ignore undefined refs
-	            return None, m.start(0), end
+	            return (True), m.start(0), end
	
	        href, title = self.md.references[id]
	

```  
Lines 808:814

```diff
	        If [ref][] use [ref].
	        """
	        m = self.RE_LINK.match(data, pos=index)
-	        if not m:
+	        if False:
	            return None, index, False
	        else:
	            id = m.group(1).lower()

```  
Lines 809:815

```diff
	        """
	        m = self.RE_LINK.match(data, pos=index)
	        if not m:
-	            return None, index, False
+	            return None, index, (True)
	        else:
	            id = m.group(1).lower()
	            end = m.end(0)

```
## Alive Mutants
  
Lines 567:573

```diff
	    def handleMatch(self, m, data):
	        """Parse patterns."""
	
-	        el = None
+	        el = (False)
	        start = None
	        end = None
	

```  
Lines 567:573

```diff
	    def handleMatch(self, m, data):
	        """Parse patterns."""
	
-	        el = None
+	        el = (True)
	        start = None
	        end = None
	

```  
Lines 568:574

```diff
	        """Parse patterns."""
	
	        el = None
-	        start = None
+	        start = (False)
	        end = None
	
	        for index, item in enumerate(self.PATTERNS):

```  
Lines 568:574

```diff
	        """Parse patterns."""
	
	        el = None
-	        start = None
+	        start = (True)
	        end = None
	
	        for index, item in enumerate(self.PATTERNS):

```  
Lines 569:575

```diff
	
	        el = None
	        start = None
-	        end = None
+	        end = (False)
	
	        for index, item in enumerate(self.PATTERNS):
	            m1 = item.pattern.match(data, m.start(0))

```  
Lines 569:575

```diff
	
	        el = None
	        start = None
-	        end = None
+	        end = (True)
	
	        for index, item in enumerate(self.PATTERNS):
	            m1 = item.pattern.match(data, m.start(0))

```  
Lines 573:579

```diff
	
	        for index, item in enumerate(self.PATTERNS):
	            m1 = item.pattern.match(data, m.start(0))
-	            if m1:
+	            if False:
	                start = m1.start(0)
	                end = m1.end(0)
	                el = self.build_element(m1, item.builder, item.tags, index)

```  
Lines 601:607

```diff
	    def handleMatch(self, m, data):
	        text, index, handled = self.getText(data, m.end(0))
	
-	        if not handled:
+	        if False:
	            return None, None, None
	
	        href, title, index, handled = self.getLink(data, index)

```  
Lines 601:607

```diff
	    def handleMatch(self, m, data):
	        text, index, handled = self.getText(data, m.end(0))
	
-	        if not handled:
+	        if True:
	            return None, None, None
	
	        href, title, index, handled = self.getLink(data, index)

```  
Lines 602:608

```diff
	        text, index, handled = self.getText(data, m.end(0))
	
	        if not handled:
-	            return None, None, None
+	            return None, None, (False)
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:

```  
Lines 602:608

```diff
	        text, index, handled = self.getText(data, m.end(0))
	
	        if not handled:
-	            return None, None, None
+	            return None, None, (True)
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:

```  
Lines 602:608

```diff
	        text, index, handled = self.getText(data, m.end(0))
	
	        if not handled:
-	            return None, None, None
+	            return None, (False), None
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:

```  
Lines 602:608

```diff
	        text, index, handled = self.getText(data, m.end(0))
	
	        if not handled:
-	            return None, None, None
+	            return None, (True), None
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:

```  
Lines 602:608

```diff
	        text, index, handled = self.getText(data, m.end(0))
	
	        if not handled:
-	            return None, None, None
+	            return (False), None, None
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:

```  
Lines 602:608

```diff
	        text, index, handled = self.getText(data, m.end(0))
	
	        if not handled:
-	            return None, None, None
+	            return (True), None, None
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:

```  
Lines 605:611

```diff
	            return None, None, None
	
	        href, title, index, handled = self.getLink(data, index)
-	        if not handled:
+	        if True:
	            return None, None, None
	
	        el = etree.Element("a")

```  
Lines 606:612

```diff
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:
-	            return None, None, None
+	            return None, None, (False)
	
	        el = etree.Element("a")
	        el.text = text

```  
Lines 606:612

```diff
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:
-	            return None, None, None
+	            return None, None, (True)
	
	        el = etree.Element("a")
	        el.text = text

```  
Lines 606:612

```diff
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:
-	            return None, None, None
+	            return None, (False), None
	
	        el = etree.Element("a")
	        el.text = text

```  
Lines 606:612

```diff
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:
-	            return None, None, None
+	            return None, (True), None
	
	        el = etree.Element("a")
	        el.text = text

```  
Lines 606:612

```diff
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:
-	            return None, None, None
+	            return (False), None, None
	
	        el = etree.Element("a")
	        el.text = text

```  
Lines 606:612

```diff
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:
-	            return None, None, None
+	            return (True), None, None
	
	        el = etree.Element("a")
	        el.text = text

```  
Lines 623:629

```diff
	
	        href = ''
	        title = None
-	        handled = False
+	        handled = None
	
	        m = self.RE_LINK.match(data, pos=index)
	        if m and m.group(1):

```  
Lines 626:632

```diff
	        handled = False
	
	        m = self.RE_LINK.match(data, pos=index)
-	        if m and m.group(1):
+	        if False:
	            # Matches [Text](<link> "title")
	            href = m.group(1)[1:-1].strip()
	            if m.group(2):

```  
Lines 633:639

```diff
	                title = m.group(2)[1:-1]
	            index = m.end(0)
	            handled = True
-	        elif m:
+	        elif False:
	            # Track bracket nesting and index in string
	            bracket_count = 1
	            backtrack_count = 1

```  
Lines 727:733

```diff
	
	            handled = bracket_count == 0
	
-	        if title is not None:
+	        if False:
	            title = self.RE_TITLE_CLEAN.sub(' ', dequote(self.unescape(title.strip())))
	
	        href = self.unescape(href).strip()

```  
Lines 743:749

```diff
	        text = []
	        for pos in range(index, len(data)):
	            c = data[pos]
-	            if c == ']':
+	            if False:
	                bracket_count -= 1
	            elif c == '[':
	                bracket_count += 1

```  
Lines 743:749

```diff
	        text = []
	        for pos in range(index, len(data)):
	            c = data[pos]
-	            if c == ']':
+	            if True:
	                bracket_count -= 1
	            elif c == '[':
	                bracket_count += 1

```  
Lines 743:749

```diff
	        text = []
	        for pos in range(index, len(data)):
	            c = data[pos]
-	            if c == ']':
+	            if (c < ']'):
	                bracket_count -= 1
	            elif c == '[':
	                bracket_count += 1

```  
Lines 743:749

```diff
	        text = []
	        for pos in range(index, len(data)):
	            c = data[pos]
-	            if c == ']':
+	            if (c >= ']'):
	                bracket_count -= 1
	            elif c == '[':
	                bracket_count += 1

```  
Lines 743:749

```diff
	        text = []
	        for pos in range(index, len(data)):
	            c = data[pos]
-	            if c == ']':
+	            if (c != ']'):
	                bracket_count -= 1
	            elif c == '[':
	                bracket_count += 1

```  
Lines 743:749

```diff
	        text = []
	        for pos in range(index, len(data)):
	            c = data[pos]
-	            if c == ']':
+	            if (c > ']'):
	                bracket_count -= 1
	            elif c == '[':
	                bracket_count += 1

```  
Lines 743:749

```diff
	        text = []
	        for pos in range(index, len(data)):
	            c = data[pos]
-	            if c == ']':
+	            if (c <= ']'):
	                bracket_count -= 1
	            elif c == '[':
	                bracket_count += 1

```  
Lines 744:750

```diff
	        for pos in range(index, len(data)):
	            c = data[pos]
	            if c == ']':
-	                bracket_count -= 1
+	                bracket_count /= 1
	            elif c == '[':
	                bracket_count += 1
	            index += 1

```  
Lines 744:750

```diff
	        for pos in range(index, len(data)):
	            c = data[pos]
	            if c == ']':
-	                bracket_count -= 1
+	                bracket_count += 1
	            elif c == '[':
	                bracket_count += 1
	            index += 1

```  
Lines 744:750

```diff
	        for pos in range(index, len(data)):
	            c = data[pos]
	            if c == ']':
-	                bracket_count -= 1
+	                bracket_count *= 1
	            elif c == '[':
	                bracket_count += 1
	            index += 1

```  
Lines 745:751

```diff
	            c = data[pos]
	            if c == ']':
	                bracket_count -= 1
-	            elif c == '[':
+	            elif False:
	                bracket_count += 1
	            index += 1
	            if bracket_count == 0:

```  
Lines 745:751

```diff
	            c = data[pos]
	            if c == ']':
	                bracket_count -= 1
-	            elif c == '[':
+	            elif True:
	                bracket_count += 1
	            index += 1
	            if bracket_count == 0:

```  
Lines 745:751

```diff
	            c = data[pos]
	            if c == ']':
	                bracket_count -= 1
-	            elif c == '[':
+	            elif (c < '['):
	                bracket_count += 1
	            index += 1
	            if bracket_count == 0:

```  
Lines 745:751

```diff
	            c = data[pos]
	            if c == ']':
	                bracket_count -= 1
-	            elif c == '[':
+	            elif (c >= '['):
	                bracket_count += 1
	            index += 1
	            if bracket_count == 0:

```  
Lines 745:751

```diff
	            c = data[pos]
	            if c == ']':
	                bracket_count -= 1
-	            elif c == '[':
+	            elif (c != '['):
	                bracket_count += 1
	            index += 1
	            if bracket_count == 0:

```  
Lines 745:751

```diff
	            c = data[pos]
	            if c == ']':
	                bracket_count -= 1
-	            elif c == '[':
+	            elif (c > '['):
	                bracket_count += 1
	            index += 1
	            if bracket_count == 0:

```  
Lines 745:751

```diff
	            c = data[pos]
	            if c == ']':
	                bracket_count -= 1
-	            elif c == '[':
+	            elif (c <= '['):
	                bracket_count += 1
	            index += 1
	            if bracket_count == 0:

```  
Lines 746:752

```diff
	            if c == ']':
	                bracket_count -= 1
	            elif c == '[':
-	                bracket_count += 1
+	                bracket_count -= 1
	            index += 1
	            if bracket_count == 0:
	                break

```  
Lines 746:752

```diff
	            if c == ']':
	                bracket_count -= 1
	            elif c == '[':
-	                bracket_count += 1
+	                bracket_count /= 1
	            index += 1
	            if bracket_count == 0:
	                break

```  
Lines 746:752

```diff
	            if c == ']':
	                bracket_count -= 1
	            elif c == '[':
-	                bracket_count += 1
+	                bracket_count *= 1
	            index += 1
	            if bracket_count == 0:
	                break

```  
Lines 747:753

```diff
	                bracket_count -= 1
	            elif c == '[':
	                bracket_count += 1
-	            index += 1
+	            index *= 1
	            if bracket_count == 0:
	                break
	            text.append(c)

```  
Lines 748:754

```diff
	            elif c == '[':
	                bracket_count += 1
	            index += 1
-	            if bracket_count == 0:
+	            if False:
	                break
	            text.append(c)
	        return ''.join(text), index, bracket_count == 0

```  
Lines 748:754

```diff
	            elif c == '[':
	                bracket_count += 1
	            index += 1
-	            if bracket_count == 0:
+	            if True:
	                break
	            text.append(c)
	        return ''.join(text), index, bracket_count == 0

```  
Lines 748:754

```diff
	            elif c == '[':
	                bracket_count += 1
	            index += 1
-	            if bracket_count == 0:
+	            if (bracket_count < 0):
	                break
	            text.append(c)
	        return ''.join(text), index, bracket_count == 0

```  
Lines 748:754

```diff
	            elif c == '[':
	                bracket_count += 1
	            index += 1
-	            if bracket_count == 0:
+	            if (bracket_count >= 0):
	                break
	            text.append(c)
	        return ''.join(text), index, bracket_count == 0

```  
Lines 748:754

```diff
	            elif c == '[':
	                bracket_count += 1
	            index += 1
-	            if bracket_count == 0:
+	            if (bracket_count != 0):
	                break
	            text.append(c)
	        return ''.join(text), index, bracket_count == 0

```  
Lines 748:754

```diff
	            elif c == '[':
	                bracket_count += 1
	            index += 1
-	            if bracket_count == 0:
+	            if (bracket_count > 0):
	                break
	            text.append(c)
	        return ''.join(text), index, bracket_count == 0

```  
Lines 748:754

```diff
	            elif c == '[':
	                bracket_count += 1
	            index += 1
-	            if bracket_count == 0:
+	            if (bracket_count <= 0):
	                break
	            text.append(c)
	        return ''.join(text), index, bracket_count == 0

```  
Lines 751:757

```diff
	            if bracket_count == 0:
	                break
	            text.append(c)
-	        return ''.join(text), index, bracket_count == 0
+	        return ''.join(text), index, (bracket_count < 0)
	
	
	class ImageInlineProcessor(LinkInlineProcessor):

```  
Lines 751:757

```diff
	            if bracket_count == 0:
	                break
	            text.append(c)
-	        return ''.join(text), index, bracket_count == 0
+	        return ''.join(text), index, (bracket_count >= 0)
	
	
	class ImageInlineProcessor(LinkInlineProcessor):

```  
Lines 751:757

```diff
	            if bracket_count == 0:
	                break
	            text.append(c)
-	        return ''.join(text), index, bracket_count == 0
+	        return ''.join(text), index, (bracket_count != 0)
	
	
	class ImageInlineProcessor(LinkInlineProcessor):

```  
Lines 751:757

```diff
	            if bracket_count == 0:
	                break
	            text.append(c)
-	        return ''.join(text), index, bracket_count == 0
+	        return ''.join(text), index, (bracket_count > 0)
	
	
	class ImageInlineProcessor(LinkInlineProcessor):

```  
Lines 751:757

```diff
	            if bracket_count == 0:
	                break
	            text.append(c)
-	        return ''.join(text), index, bracket_count == 0
+	        return ''.join(text), index, (bracket_count <= 0)
	
	
	class ImageInlineProcessor(LinkInlineProcessor):

```  
Lines 785:791

```diff
	
	    def handleMatch(self, m, data):
	        text, index, handled = self.getText(data, m.end(0))
-	        if not handled:
+	        if False:
	            return None, None, None
	
	        id, end, handled = self.evalId(data, index, text)

```  
Lines 785:791

```diff
	
	    def handleMatch(self, m, data):
	        text, index, handled = self.getText(data, m.end(0))
-	        if not handled:
+	        if True:
	            return None, None, None
	
	        id, end, handled = self.evalId(data, index, text)

```  
Lines 786:792

```diff
	    def handleMatch(self, m, data):
	        text, index, handled = self.getText(data, m.end(0))
	        if not handled:
-	            return None, None, None
+	            return None, None, (False)
	
	        id, end, handled = self.evalId(data, index, text)
	        if not handled:

```  
Lines 786:792

```diff
	    def handleMatch(self, m, data):
	        text, index, handled = self.getText(data, m.end(0))
	        if not handled:
-	            return None, None, None
+	            return None, None, (True)
	
	        id, end, handled = self.evalId(data, index, text)
	        if not handled:

```  
Lines 786:792

```diff
	    def handleMatch(self, m, data):
	        text, index, handled = self.getText(data, m.end(0))
	        if not handled:
-	            return None, None, None
+	            return None, (False), None
	
	        id, end, handled = self.evalId(data, index, text)
	        if not handled:

```  
Lines 786:792

```diff
	    def handleMatch(self, m, data):
	        text, index, handled = self.getText(data, m.end(0))
	        if not handled:
-	            return None, None, None
+	            return None, (True), None
	
	        id, end, handled = self.evalId(data, index, text)
	        if not handled:

```  
Lines 786:792

```diff
	    def handleMatch(self, m, data):
	        text, index, handled = self.getText(data, m.end(0))
	        if not handled:
-	            return None, None, None
+	            return (False), None, None
	
	        id, end, handled = self.evalId(data, index, text)
	        if not handled:

```  
Lines 786:792

```diff
	    def handleMatch(self, m, data):
	        text, index, handled = self.getText(data, m.end(0))
	        if not handled:
-	            return None, None, None
+	            return (True), None, None
	
	        id, end, handled = self.evalId(data, index, text)
	        if not handled:

```  
Lines 789:795

```diff
	            return None, None, None
	
	        id, end, handled = self.evalId(data, index, text)
-	        if not handled:
+	        if True:
	            return None, None, None
	
	        # Clean up linebreaks in id

```  
Lines 790:796

```diff
	
	        id, end, handled = self.evalId(data, index, text)
	        if not handled:
-	            return None, None, None
+	            return (False), None, None
	
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)

```  
Lines 790:796

```diff
	
	        id, end, handled = self.evalId(data, index, text)
	        if not handled:
-	            return None, None, None
+	            return (True), None, None
	
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)

```  
Lines 790:796

```diff
	
	        id, end, handled = self.evalId(data, index, text)
	        if not handled:
-	            return None, None, None
+	            return None, None, (False)
	
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)

```  
Lines 790:796

```diff
	
	        id, end, handled = self.evalId(data, index, text)
	        if not handled:
-	            return None, None, None
+	            return None, None, (True)
	
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)

```  
Lines 790:796

```diff
	
	        id, end, handled = self.evalId(data, index, text)
	        if not handled:
-	            return None, None, None
+	            return None, (False), None
	
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)

```  
Lines 790:796

```diff
	
	        id, end, handled = self.evalId(data, index, text)
	        if not handled:
-	            return None, None, None
+	            return None, (True), None
	
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)

```  
Lines 794:800

```diff
	
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)
-	        if id not in self.md.references:  # ignore undefined refs
+	        if True:  # ignore undefined refs
	            return None, m.start(0), end
	
	        href, title = self.md.references[id]

```  
Lines 808:814

```diff
	        If [ref][] use [ref].
	        """
	        m = self.RE_LINK.match(data, pos=index)
-	        if not m:
+	        if True:
	            return None, index, False
	        else:
	            id = m.group(1).lower()

```  
Lines 809:815

```diff
	        """
	        m = self.RE_LINK.match(data, pos=index)
	        if not m:
-	            return None, index, False
+	            return None, index, None
	        else:
	            id = m.group(1).lower()
	            end = m.end(0)

```  
Lines 809:815

```diff
	        """
	        m = self.RE_LINK.match(data, pos=index)
	        if not m:
-	            return None, index, False
+	            return (False), index, False
	        else:
	            id = m.group(1).lower()
	            end = m.end(0)

```  
Lines 809:815

```diff
	        """
	        m = self.RE_LINK.match(data, pos=index)
	        if not m:
-	            return None, index, False
+	            return (True), index, False
	        else:
	            id = m.group(1).lower()
	            end = m.end(0)

```  
Lines 833:839

```diff
	    def evalId(self, data, index, text):
	        """Evaluate the id from of [ref]  """
	
-	        return text.lower(), index, True
+	        return text.lower(), index, (False)
	
	
	class ImageReferenceInlineProcessor(ReferenceInlineProcessor):

```  
Lines 833:839

```diff
	    def evalId(self, data, index, text):
	        """Evaluate the id from of [ref]  """
	
-	        return text.lower(), index, True
+	        return text.lower(), index, None
	
	
	class ImageReferenceInlineProcessor(ReferenceInlineProcessor):

```
# /home/ubuntu/projects/markdown/markdown/treeprocessors.py

## Newly Killed Mutants

### testBasicMetaData_str_dbl_1
  
Lines 270:276

```diff
	            # until we can't find any more.
	            for match in pattern.getCompiledRegExp().finditer(data, startIndex):
	                node, start, end = pattern.handleMatch(match, data)
-	                if start is None or end is None:
+	                if False:
	                    startIndex += match.end(0)
	                    match = None
	                    continue

```  
Lines 272:278

```diff
	                node, start, end = pattern.handleMatch(match, data)
	                if start is None or end is None:
	                    startIndex += match.end(0)
-	                    match = None
+	                    match = (True)
	                    continue
	                break
	        else:  # pragma: no cover

```
### testYamlMetaData_str_dbl_1
  
Lines 282:288

```diff
	        if not match:
	            return data, False, 0
	
-	        if not new_style:  # pragma: no cover
+	        if True: no cover
	            node = pattern.handleMatch(match)
	            start = match.start(0)
	            end = match.end(0)

```  
Lines 287:293

```diff
	            start = match.start(0)
	            end = match.end(0)
	
-	        if node is None:
+	        if False:
	            return data, True, end
	
	        if not isString(node):

```  
Lines 287:293

```diff
	            start = match.start(0)
	            end = match.end(0)
	
-	        if node is None:
+	        if (node is not None):
	            return data, True, end
	
	        if not isString(node):

```  
Lines 287:293

```diff
	            start = match.start(0)
	            end = match.end(0)
	
-	        if node is None:
+	        if node is (False):
	            return data, True, end
	
	        if not isString(node):

```  
Lines 287:293

```diff
	            start = match.start(0)
	            end = match.end(0)
	
-	        if node is None:
+	        if node is (True):
	            return data, True, end
	
	        if not isString(node):

```
## Alive Mutants
  
Lines 270:276

```diff
	            # until we can't find any more.
	            for match in pattern.getCompiledRegExp().finditer(data, startIndex):
	                node, start, end = pattern.handleMatch(match, data)
-	                if start is None or end is None:
+	                if (start is not None) or end is None:
	                    startIndex += match.end(0)
	                    match = None
	                    continue

```  
Lines 270:276

```diff
	            # until we can't find any more.
	            for match in pattern.getCompiledRegExp().finditer(data, startIndex):
	                node, start, end = pattern.handleMatch(match, data)
-	                if start is None or end is None:
+	                if (start is None and end is None):
	                    startIndex += match.end(0)
	                    match = None
	                    continue

```  
Lines 270:276

```diff
	            # until we can't find any more.
	            for match in pattern.getCompiledRegExp().finditer(data, startIndex):
	                node, start, end = pattern.handleMatch(match, data)
-	                if start is None or end is None:
+	                if start is None or (end is not None):
	                    startIndex += match.end(0)
	                    match = None
	                    continue

```  
Lines 270:276

```diff
	            # until we can't find any more.
	            for match in pattern.getCompiledRegExp().finditer(data, startIndex):
	                node, start, end = pattern.handleMatch(match, data)
-	                if start is None or end is None:
+	                if True:
	                    startIndex += match.end(0)
	                    match = None
	                    continue

```  
Lines 270:276

```diff
	            # until we can't find any more.
	            for match in pattern.getCompiledRegExp().finditer(data, startIndex):
	                node, start, end = pattern.handleMatch(match, data)
-	                if start is None or end is None:
+	                if start is None or end is (False):
	                    startIndex += match.end(0)
	                    match = None
	                    continue

```  
Lines 270:276

```diff
	            # until we can't find any more.
	            for match in pattern.getCompiledRegExp().finditer(data, startIndex):
	                node, start, end = pattern.handleMatch(match, data)
-	                if start is None or end is None:
+	                if start is None or end is (True):
	                    startIndex += match.end(0)
	                    match = None
	                    continue

```  
Lines 270:276

```diff
	            # until we can't find any more.
	            for match in pattern.getCompiledRegExp().finditer(data, startIndex):
	                node, start, end = pattern.handleMatch(match, data)
-	                if start is None or end is None:
+	                if start is (False) or end is None:
	                    startIndex += match.end(0)
	                    match = None
	                    continue

```  
Lines 270:276

```diff
	            # until we can't find any more.
	            for match in pattern.getCompiledRegExp().finditer(data, startIndex):
	                node, start, end = pattern.handleMatch(match, data)
-	                if start is None or end is None:
+	                if start is (True) or end is None:
	                    startIndex += match.end(0)
	                    match = None
	                    continue

```  
Lines 271:277

```diff
	            for match in pattern.getCompiledRegExp().finditer(data, startIndex):
	                node, start, end = pattern.handleMatch(match, data)
	                if start is None or end is None:
-	                    startIndex += match.end(0)
+	                    startIndex -= match.end(0)
	                    match = None
	                    continue
	                break

```  
Lines 271:277

```diff
	            for match in pattern.getCompiledRegExp().finditer(data, startIndex):
	                node, start, end = pattern.handleMatch(match, data)
	                if start is None or end is None:
-	                    startIndex += match.end(0)
+	                    startIndex /= match.end(0)
	                    match = None
	                    continue
	                break

```  
Lines 271:277

```diff
	            for match in pattern.getCompiledRegExp().finditer(data, startIndex):
	                node, start, end = pattern.handleMatch(match, data)
	                if start is None or end is None:
-	                    startIndex += match.end(0)
+	                    startIndex *= match.end(0)
	                    match = None
	                    continue
	                break

```  
Lines 272:278

```diff
	                node, start, end = pattern.handleMatch(match, data)
	                if start is None or end is None:
	                    startIndex += match.end(0)
-	                    match = None
+	                    match = (False)
	                    continue
	                break
	        else:  # pragma: no cover

```  
Lines 282:288

```diff
	        if not match:
	            return data, False, 0
	
-	        if not new_style:  # pragma: no cover
+	        if False: no cover
	            node = pattern.handleMatch(match)
	            start = match.start(0)
	            end = match.end(0)

```  
Lines 287:293

```diff
	            start = match.start(0)
	            end = match.end(0)
	
-	        if node is None:
+	        if True:
	            return data, True, end
	
	        if not isString(node):

```  
Lines 288:294

```diff
	            end = match.end(0)
	
	        if node is None:
-	            return data, True, end
+	            return data, (False), end
	
	        if not isString(node):
	            if not isinstance(node.text, util.AtomicString):

```  
Lines 288:294

```diff
	            end = match.end(0)
	
	        if node is None:
-	            return data, True, end
+	            return data, None, end
	
	        if not isString(node):
	            if not isinstance(node.text, util.AtomicString):

```
# /home/ubuntu/projects/markdown/markdown/blockparser.py

## Newly Killed Mutants

### testMissingMetaData_str_hlf_1_call_add_0_str_hlf_1
  
Lines 52:58

```diff
	    def isstate(self, state):
	        """ Test that top (current) level is of given state. """
	        if len(self):
-	            return self[-1] == state
+	            return (self[-1] < state)
	        else:
	            return False
	

```  
Lines 52:58

```diff
	    def isstate(self, state):
	        """ Test that top (current) level is of given state. """
	        if len(self):
-	            return self[-1] == state
+	            return (self[-1] != state)
	        else:
	            return False
	

```  
Lines 52:58

```diff
	    def isstate(self, state):
	        """ Test that top (current) level is of given state. """
	        if len(self):
-	            return self[-1] == state
+	            return (self[-1] > state)
	        else:
	            return False
	

```  
Lines 52:58

```diff
	    def isstate(self, state):
	        """ Test that top (current) level is of given state. """
	        if len(self):
-	            return self[-1] == state
+	            return self[(-1)] == state
	        else:
	            return False
	

```
## Alive Mutants
  
Lines 52:58

```diff
	    def isstate(self, state):
	        """ Test that top (current) level is of given state. """
	        if len(self):
-	            return self[-1] == state
+	            return (self[-1] >= state)
	        else:
	            return False
	

```  
Lines 52:58

```diff
	    def isstate(self, state):
	        """ Test that top (current) level is of given state. """
	        if len(self):
-	            return self[-1] == state
+	            return (self[-1] <= state)
	        else:
	            return False
	

```  
Lines 52:58

```diff
	    def isstate(self, state):
	        """ Test that top (current) level is of given state. """
	        if len(self):
-	            return self[-1] == state
+	            return self[(-1)] == state
	        else:
	            return False
	

```
# /home/ubuntu/projects/markdown/markdown/postprocessors.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/__meta__.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/test_tools.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/preprocessors.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/__init__.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/blockprocessors.py

## Newly Killed Mutants

### testBasicMetaData_str_dbl_1
  
Lines 87:93

```diff
	        for line in lines:
	            if line.startswith(' ' * length):
	                newtext.append(line[length:])
-	            elif not line.strip():
+	            elif False:
	                newtext.append('')
	            else:
	                break

```  
Lines 87:93

```diff
	        for line in lines:
	            if line.startswith(' ' * length):
	                newtext.append(line[length:])
-	            elif not line.strip():
+	            elif True:
	                newtext.append('')
	            else:
	                break

```
### testYamlMetaData_str_dbl_1
  
Lines 509:515

```diff
	        if m:
	            # Save match object on class instance so we can use it later.
	            self.match = m
-	            return True
+	            return (False)
	        return False
	
	    def run(self, parent, blocks):

```  
Lines 509:515

```diff
	        if m:
	            # Save match object on class instance so we can use it later.
	            self.match = m
-	            return True
+	            return None
	        return False
	
	    def run(self, parent, blocks):

```  
Lines 516:522

```diff
	        block = blocks.pop(0)
	        match = self.match
	        # Check for lines in block before hr.
-	        prelines = block[:match.start()].rstrip('\n')
+	        prelines = block[match.start():].rstrip('\n')
	        if prelines:
	            # Recursively parse lines before hr so they get parsed first.
	            self.parser.parseBlocks(parent, [prelines])

```  
Lines 516:522

```diff
	        block = blocks.pop(0)
	        match = self.match
	        # Check for lines in block before hr.
-	        prelines = block[:match.start()].rstrip('\n')
+	        prelines = block[:].rstrip('\n')
	        if prelines:
	            # Recursively parse lines before hr so they get parsed first.
	            self.parser.parseBlocks(parent, [prelines])

```  
Lines 517:523

```diff
	        match = self.match
	        # Check for lines in block before hr.
	        prelines = block[:match.start()].rstrip('\n')
-	        if prelines:
+	        if False:
	            # Recursively parse lines before hr so they get parsed first.
	            self.parser.parseBlocks(parent, [prelines])
	        # create hr

```
### testYamlMetaData_str_hlf_1_str_hlf_1_str_dbl_1
  
Lines 484:490

```diff
	    def run(self, parent, blocks):
	        lines = blocks.pop(0).split('\n')
	        # Determine level. ``=`` is 1 and ``-`` is 2.
-	        if lines[1].startswith('='):
+	        if True:
	            level = 1
	        else:
	            level = 2

```  
Lines 488:494

```diff
	            level = 1
	        else:
	            level = 2
-	        h = etree.SubElement(parent, 'h%d' % level)
+	        h = etree.SubElement(parent, ('h%d' - level))
	        h.text = lines[0].strip()
	        if len(lines) > 2:
	            # Block contains additional lines. Add to  master blocks for later.

```  
Lines 488:494

```diff
	            level = 1
	        else:
	            level = 2
-	        h = etree.SubElement(parent, 'h%d' % level)
+	        h = etree.SubElement(parent, ('h%d' / level))
	        h.text = lines[0].strip()
	        if len(lines) > 2:
	            # Block contains additional lines. Add to  master blocks for later.

```  
Lines 488:494

```diff
	            level = 1
	        else:
	            level = 2
-	        h = etree.SubElement(parent, 'h%d' % level)
+	        h = etree.SubElement(parent, ('h%d' + level))
	        h.text = lines[0].strip()
	        if len(lines) > 2:
	            # Block contains additional lines. Add to  master blocks for later.

```  
Lines 488:494

```diff
	            level = 1
	        else:
	            level = 2
-	        h = etree.SubElement(parent, 'h%d' % level)
+	        h = etree.SubElement(parent, ('h%d' ** level))
	        h.text = lines[0].strip()
	        if len(lines) > 2:
	            # Block contains additional lines. Add to  master blocks for later.

```  
Lines 488:494

```diff
	            level = 1
	        else:
	            level = 2
-	        h = etree.SubElement(parent, 'h%d' % level)
+	        h = etree.SubElement(parent, ('h%d' // level))
	        h.text = lines[0].strip()
	        if len(lines) > 2:
	            # Block contains additional lines. Add to  master blocks for later.

```  
Lines 488:494

```diff
	            level = 1
	        else:
	            level = 2
-	        h = etree.SubElement(parent, 'h%d' % level)
+	        h = etree.SubElement(parent, ('h%d' * level))
	        h.text = lines[0].strip()
	        if len(lines) > 2:
	            # Block contains additional lines. Add to  master blocks for later.

```  
Lines 489:495

```diff
	        else:
	            level = 2
	        h = etree.SubElement(parent, 'h%d' % level)
-	        h.text = lines[0].strip()
+	        h.text = lines[<_ast.Constant object at 0x7fe424f55b20>].strip()
	        if len(lines) > 2:
	            # Block contains additional lines. Add to  master blocks for later.
	            blocks.insert(0, '\n'.join(lines[2:]))

```  
Lines 489:495

```diff
	        else:
	            level = 2
	        h = etree.SubElement(parent, 'h%d' % level)
-	        h.text = lines[0].strip()
+	        h.text = lines[<_ast.Constant object at 0x7fe424e93f70>].strip()
	        if len(lines) > 2:
	            # Block contains additional lines. Add to  master blocks for later.
	            blocks.insert(0, '\n'.join(lines[2:]))

```
### testMissingMetaData_str_hlf_1_call_add_0_str_hlf_1
  
Lines 349:355

```diff
	        items = self.get_items(blocks.pop(0))
	        sibling = self.lastChild(parent)
	
-	        if sibling is not None and sibling.tag in self.SIBLING_TAGS:
+	        if sibling is not (False) and sibling.tag in self.SIBLING_TAGS:
	            # Previous block was a list item, so set that as parent
	            lst = sibling
	            # make sure previous item is in a p- if the item has text,

```  
Lines 349:355

```diff
	        items = self.get_items(blocks.pop(0))
	        sibling = self.lastChild(parent)
	
-	        if sibling is not None and sibling.tag in self.SIBLING_TAGS:
+	        if sibling is not (True) and sibling.tag in self.SIBLING_TAGS:
	            # Previous block was a list item, so set that as parent
	            lst = sibling
	            # make sure previous item is in a p- if the item has text,

```  
Lines 349:355

```diff
	        items = self.get_items(blocks.pop(0))
	        sibling = self.lastChild(parent)
	
-	        if sibling is not None and sibling.tag in self.SIBLING_TAGS:
+	        if True:
	            # Previous block was a list item, so set that as parent
	            lst = sibling
	            # make sure previous item is in a p- if the item has text,

```  
Lines 349:355

```diff
	        items = self.get_items(blocks.pop(0))
	        sibling = self.lastChild(parent)
	
-	        if sibling is not None and sibling.tag in self.SIBLING_TAGS:
+	        if (sibling is not None or sibling.tag in self.SIBLING_TAGS):
	            # Previous block was a list item, so set that as parent
	            lst = sibling
	            # make sure previous item is in a p- if the item has text,

```  
Lines 349:355

```diff
	        items = self.get_items(blocks.pop(0))
	        sibling = self.lastChild(parent)
	
-	        if sibling is not None and sibling.tag in self.SIBLING_TAGS:
+	        if (sibling is None) and sibling.tag in self.SIBLING_TAGS:
	            # Previous block was a list item, so set that as parent
	            lst = sibling
	            # make sure previous item is in a p- if the item has text,

```  
Lines 376:382

```diff
	            firstitem = items.pop(0)
	            self.parser.parseBlocks(li, [firstitem])
	            self.parser.state.reset()
-	        elif parent.tag in ['ol', 'ul']:
+	        elif True:
	            # this catches the edge case of a multi-item indented list whose
	            # first item is in a blank parent-list item:
	            # * * subitem1

```  
Lines 376:382

```diff
	            firstitem = items.pop(0)
	            self.parser.parseBlocks(li, [firstitem])
	            self.parser.state.reset()
-	        elif parent.tag in ['ol', 'ul']:
+	        elif (parent.tag not in ['ol', 'ul']):
	            # this catches the edge case of a multi-item indented list whose
	            # first item is in a blank parent-list item:
	            # * * subitem1

```  
Lines 387:393

```diff
	            # This is a new list so create parent with appropriate tag.
	            lst = etree.SubElement(parent, self.TAG)
	            # Check if a custom start integer is set
-	            if not self.LAZY_OL and self.STARTSWITH != '1':
+	            if True:
	                lst.attrib['start'] = self.STARTSWITH
	
	        self.parser.state.set('list')

```  
Lines 394:400

```diff
	        # Loop through items in block, recursively parsing each with the
	        # appropriate parent.
	        for item in items:
-	            if item.startswith(' '*self.tab_length):
+	            if True:
	                # Item is indented. Parse with last item as parent
	                self.parser.parseBlocks(lst[-1], [item])
	            else:

```  
Lines 394:400

```diff
	        # Loop through items in block, recursively parsing each with the
	        # appropriate parent.
	        for item in items:
-	            if item.startswith(' '*self.tab_length):
+	            if item.startswith((' ' % self.tab_length)):
	                # Item is indented. Parse with last item as parent
	                self.parser.parseBlocks(lst[-1], [item])
	            else:

```  
Lines 394:400

```diff
	        # Loop through items in block, recursively parsing each with the
	        # appropriate parent.
	        for item in items:
-	            if item.startswith(' '*self.tab_length):
+	            if item.startswith((' ' - self.tab_length)):
	                # Item is indented. Parse with last item as parent
	                self.parser.parseBlocks(lst[-1], [item])
	            else:

```  
Lines 394:400

```diff
	        # Loop through items in block, recursively parsing each with the
	        # appropriate parent.
	        for item in items:
-	            if item.startswith(' '*self.tab_length):
+	            if item.startswith((' ' / self.tab_length)):
	                # Item is indented. Parse with last item as parent
	                self.parser.parseBlocks(lst[-1], [item])
	            else:

```  
Lines 394:400

```diff
	        # Loop through items in block, recursively parsing each with the
	        # appropriate parent.
	        for item in items:
-	            if item.startswith(' '*self.tab_length):
+	            if item.startswith((' ' + self.tab_length)):
	                # Item is indented. Parse with last item as parent
	                self.parser.parseBlocks(lst[-1], [item])
	            else:

```  
Lines 394:400

```diff
	        # Loop through items in block, recursively parsing each with the
	        # appropriate parent.
	        for item in items:
-	            if item.startswith(' '*self.tab_length):
+	            if item.startswith((' ' ** self.tab_length)):
	                # Item is indented. Parse with last item as parent
	                self.parser.parseBlocks(lst[-1], [item])
	            else:

```  
Lines 394:400

```diff
	        # Loop through items in block, recursively parsing each with the
	        # appropriate parent.
	        for item in items:
-	            if item.startswith(' '*self.tab_length):
+	            if item.startswith((' ' // self.tab_length)):
	                # Item is indented. Parse with last item as parent
	                self.parser.parseBlocks(lst[-1], [item])
	            else:

```  
Lines 408:414

```diff
	        items = []
	        for line in block.split('\n'):
	            m = self.CHILD_RE.match(line)
-	            if m:
+	            if False:
	                # This is a new list item
	                # Check first item for the start index
	                if not items and self.TAG == 'ol':

```  
Lines 411:417

```diff
	            if m:
	                # This is a new list item
	                # Check first item for the start index
-	                if not items and self.TAG == 'ol':
+	                if (not items or self.TAG == 'ol'):
	                    # Detect the integer value of first list item
	                    INTEGER_RE = re.compile(r'(\d+)')
	                    self.STARTSWITH = INTEGER_RE.match(m.group(1)).group()

```  
Lines 411:417

```diff
	            if m:
	                # This is a new list item
	                # Check first item for the start index
-	                if not items and self.TAG == 'ol':
+	                if not items and (self.TAG >= 'ol'):
	                    # Detect the integer value of first list item
	                    INTEGER_RE = re.compile(r'(\d+)')
	                    self.STARTSWITH = INTEGER_RE.match(m.group(1)).group()

```  
Lines 411:417

```diff
	            if m:
	                # This is a new list item
	                # Check first item for the start index
-	                if not items and self.TAG == 'ol':
+	                if not items and (self.TAG != 'ol'):
	                    # Detect the integer value of first list item
	                    INTEGER_RE = re.compile(r'(\d+)')
	                    self.STARTSWITH = INTEGER_RE.match(m.group(1)).group()

```  
Lines 411:417

```diff
	            if m:
	                # This is a new list item
	                # Check first item for the start index
-	                if not items and self.TAG == 'ol':
+	                if not items and (self.TAG > 'ol'):
	                    # Detect the integer value of first list item
	                    INTEGER_RE = re.compile(r'(\d+)')
	                    self.STARTSWITH = INTEGER_RE.match(m.group(1)).group()

```  
Lines 411:417

```diff
	            if m:
	                # This is a new list item
	                # Check first item for the start index
-	                if not items and self.TAG == 'ol':
+	                if True:
	                    # Detect the integer value of first list item
	                    INTEGER_RE = re.compile(r'(\d+)')
	                    self.STARTSWITH = INTEGER_RE.match(m.group(1)).group()

```  
Lines 605:611

```diff
	                #     * # Header
	                #     Line 2 of list item - not part of header.
	                sibling = self.lastChild(parent)
-	                if sibling is not None:
+	                if sibling is not (False):
	                    # Insetrt after sibling.
	                    if sibling.tail:
	                        sibling.tail = '{}\n{}'.format(sibling.tail, block)

```  
Lines 605:611

```diff
	                #     * # Header
	                #     Line 2 of list item - not part of header.
	                sibling = self.lastChild(parent)
-	                if sibling is not None:
+	                if sibling is not (True):
	                    # Insetrt after sibling.
	                    if sibling.tail:
	                        sibling.tail = '{}\n{}'.format(sibling.tail, block)

```  
Lines 605:611

```diff
	                #     * # Header
	                #     Line 2 of list item - not part of header.
	                sibling = self.lastChild(parent)
-	                if sibling is not None:
+	                if True:
	                    # Insetrt after sibling.
	                    if sibling.tail:
	                        sibling.tail = '{}\n{}'.format(sibling.tail, block)

```  
Lines 605:611

```diff
	                #     * # Header
	                #     Line 2 of list item - not part of header.
	                sibling = self.lastChild(parent)
-	                if sibling is not None:
+	                if (sibling is None):
	                    # Insetrt after sibling.
	                    if sibling.tail:
	                        sibling.tail = '{}\n{}'.format(sibling.tail, block)

```  
Lines 613:619

```diff
	                        sibling.tail = '\n%s' % block
	                else:
	                    # Append to parent.text
-	                    if parent.text:
+	                    if True:
	                        parent.text = '{}\n{}'.format(parent.text, block)
	                    else:
	                        parent.text = block.lstrip()

```
## Alive Mutants
  
Lines 349:355

```diff
	        items = self.get_items(blocks.pop(0))
	        sibling = self.lastChild(parent)
	
-	        if sibling is not None and sibling.tag in self.SIBLING_TAGS:
+	        if sibling is not None and (sibling.tag not in self.SIBLING_TAGS):
	            # Previous block was a list item, so set that as parent
	            lst = sibling
	            # make sure previous item is in a p- if the item has text,

```  
Lines 349:355

```diff
	        items = self.get_items(blocks.pop(0))
	        sibling = self.lastChild(parent)
	
-	        if sibling is not None and sibling.tag in self.SIBLING_TAGS:
+	        if False:
	            # Previous block was a list item, so set that as parent
	            lst = sibling
	            # make sure previous item is in a p- if the item has text,

```  
Lines 376:382

```diff
	            firstitem = items.pop(0)
	            self.parser.parseBlocks(li, [firstitem])
	            self.parser.state.reset()
-	        elif parent.tag in ['ol', 'ul']:
+	        elif False:
	            # this catches the edge case of a multi-item indented list whose
	            # first item is in a blank parent-list item:
	            # * * subitem1

```  
Lines 387:393

```diff
	            # This is a new list so create parent with appropriate tag.
	            lst = etree.SubElement(parent, self.TAG)
	            # Check if a custom start integer is set
-	            if not self.LAZY_OL and self.STARTSWITH != '1':
+	            if not self.LAZY_OL and (self.STARTSWITH < '1'):
	                lst.attrib['start'] = self.STARTSWITH
	
	        self.parser.state.set('list')

```  
Lines 387:393

```diff
	            # This is a new list so create parent with appropriate tag.
	            lst = etree.SubElement(parent, self.TAG)
	            # Check if a custom start integer is set
-	            if not self.LAZY_OL and self.STARTSWITH != '1':
+	            if not self.LAZY_OL and (self.STARTSWITH >= '1'):
	                lst.attrib['start'] = self.STARTSWITH
	
	        self.parser.state.set('list')

```  
Lines 387:393

```diff
	            # This is a new list so create parent with appropriate tag.
	            lst = etree.SubElement(parent, self.TAG)
	            # Check if a custom start integer is set
-	            if not self.LAZY_OL and self.STARTSWITH != '1':
+	            if not self.LAZY_OL and (self.STARTSWITH > '1'):
	                lst.attrib['start'] = self.STARTSWITH
	
	        self.parser.state.set('list')

```  
Lines 387:393

```diff
	            # This is a new list so create parent with appropriate tag.
	            lst = etree.SubElement(parent, self.TAG)
	            # Check if a custom start integer is set
-	            if not self.LAZY_OL and self.STARTSWITH != '1':
+	            if not self.LAZY_OL and (self.STARTSWITH == '1'):
	                lst.attrib['start'] = self.STARTSWITH
	
	        self.parser.state.set('list')

```  
Lines 387:393

```diff
	            # This is a new list so create parent with appropriate tag.
	            lst = etree.SubElement(parent, self.TAG)
	            # Check if a custom start integer is set
-	            if not self.LAZY_OL and self.STARTSWITH != '1':
+	            if not self.LAZY_OL and (self.STARTSWITH <= '1'):
	                lst.attrib['start'] = self.STARTSWITH
	
	        self.parser.state.set('list')

```  
Lines 387:393

```diff
	            # This is a new list so create parent with appropriate tag.
	            lst = etree.SubElement(parent, self.TAG)
	            # Check if a custom start integer is set
-	            if not self.LAZY_OL and self.STARTSWITH != '1':
+	            if (not self.LAZY_OL or self.STARTSWITH != '1'):
	                lst.attrib['start'] = self.STARTSWITH
	
	        self.parser.state.set('list')

```  
Lines 387:393

```diff
	            # This is a new list so create parent with appropriate tag.
	            lst = etree.SubElement(parent, self.TAG)
	            # Check if a custom start integer is set
-	            if not self.LAZY_OL and self.STARTSWITH != '1':
+	            if False:
	                lst.attrib['start'] = self.STARTSWITH
	
	        self.parser.state.set('list')

```  
Lines 394:400

```diff
	        # Loop through items in block, recursively parsing each with the
	        # appropriate parent.
	        for item in items:
-	            if item.startswith(' '*self.tab_length):
+	            if False:
	                # Item is indented. Parse with last item as parent
	                self.parser.parseBlocks(lst[-1], [item])
	            else:

```  
Lines 408:414

```diff
	        items = []
	        for line in block.split('\n'):
	            m = self.CHILD_RE.match(line)
-	            if m:
+	            if True:
	                # This is a new list item
	                # Check first item for the start index
	                if not items and self.TAG == 'ol':

```  
Lines 411:417

```diff
	            if m:
	                # This is a new list item
	                # Check first item for the start index
-	                if not items and self.TAG == 'ol':
+	                if not items and (self.TAG < 'ol'):
	                    # Detect the integer value of first list item
	                    INTEGER_RE = re.compile(r'(\d+)')
	                    self.STARTSWITH = INTEGER_RE.match(m.group(1)).group()

```  
Lines 411:417

```diff
	            if m:
	                # This is a new list item
	                # Check first item for the start index
-	                if not items and self.TAG == 'ol':
+	                if not items and (self.TAG <= 'ol'):
	                    # Detect the integer value of first list item
	                    INTEGER_RE = re.compile(r'(\d+)')
	                    self.STARTSWITH = INTEGER_RE.match(m.group(1)).group()

```  
Lines 411:417

```diff
	            if m:
	                # This is a new list item
	                # Check first item for the start index
-	                if not items and self.TAG == 'ol':
+	                if False:
	                    # Detect the integer value of first list item
	                    INTEGER_RE = re.compile(r'(\d+)')
	                    self.STARTSWITH = INTEGER_RE.match(m.group(1)).group()

```  
Lines 484:490

```diff
	    def run(self, parent, blocks):
	        lines = blocks.pop(0).split('\n')
	        # Determine level. ``=`` is 1 and ``-`` is 2.
-	        if lines[1].startswith('='):
+	        if lines[<_ast.Constant object at 0x7fe42507b310>].startswith('='):
	            level = 1
	        else:
	            level = 2

```  
Lines 484:490

```diff
	    def run(self, parent, blocks):
	        lines = blocks.pop(0).split('\n')
	        # Determine level. ``=`` is 1 and ``-`` is 2.
-	        if lines[1].startswith('='):
+	        if lines[<_ast.Constant object at 0x7fe424f55a30>].startswith('='):
	            level = 1
	        else:
	            level = 2

```  
Lines 484:490

```diff
	    def run(self, parent, blocks):
	        lines = blocks.pop(0).split('\n')
	        # Determine level. ``=`` is 1 and ``-`` is 2.
-	        if lines[1].startswith('='):
+	        if False:
	            level = 1
	        else:
	            level = 2

```  
Lines 490:496

```diff
	            level = 2
	        h = etree.SubElement(parent, 'h%d' % level)
	        h.text = lines[0].strip()
-	        if len(lines) > 2:
+	        if (len(lines) < 2):
	            # Block contains additional lines. Add to  master blocks for later.
	            blocks.insert(0, '\n'.join(lines[2:]))
	

```  
Lines 490:496

```diff
	            level = 2
	        h = etree.SubElement(parent, 'h%d' % level)
	        h.text = lines[0].strip()
-	        if len(lines) > 2:
+	        if (len(lines) >= 2):
	            # Block contains additional lines. Add to  master blocks for later.
	            blocks.insert(0, '\n'.join(lines[2:]))
	

```  
Lines 490:496

```diff
	            level = 2
	        h = etree.SubElement(parent, 'h%d' % level)
	        h.text = lines[0].strip()
-	        if len(lines) > 2:
+	        if (len(lines) != 2):
	            # Block contains additional lines. Add to  master blocks for later.
	            blocks.insert(0, '\n'.join(lines[2:]))
	

```  
Lines 490:496

```diff
	            level = 2
	        h = etree.SubElement(parent, 'h%d' % level)
	        h.text = lines[0].strip()
-	        if len(lines) > 2:
+	        if (len(lines) == 2):
	            # Block contains additional lines. Add to  master blocks for later.
	            blocks.insert(0, '\n'.join(lines[2:]))
	

```  
Lines 490:496

```diff
	            level = 2
	        h = etree.SubElement(parent, 'h%d' % level)
	        h.text = lines[0].strip()
-	        if len(lines) > 2:
+	        if (len(lines) <= 2):
	            # Block contains additional lines. Add to  master blocks for later.
	            blocks.insert(0, '\n'.join(lines[2:]))
	

```  
Lines 490:496

```diff
	            level = 2
	        h = etree.SubElement(parent, 'h%d' % level)
	        h.text = lines[0].strip()
-	        if len(lines) > 2:
+	        if False:
	            # Block contains additional lines. Add to  master blocks for later.
	            blocks.insert(0, '\n'.join(lines[2:]))
	

```  
Lines 490:496

```diff
	            level = 2
	        h = etree.SubElement(parent, 'h%d' % level)
	        h.text = lines[0].strip()
-	        if len(lines) > 2:
+	        if True:
	            # Block contains additional lines. Add to  master blocks for later.
	            blocks.insert(0, '\n'.join(lines[2:]))
	

```  
Lines 517:523

```diff
	        match = self.match
	        # Check for lines in block before hr.
	        prelines = block[:match.start()].rstrip('\n')
-	        if prelines:
+	        if True:
	            # Recursively parse lines before hr so they get parsed first.
	            self.parser.parseBlocks(parent, [prelines])
	        # create hr

```  
Lines 524:530

```diff
	        etree.SubElement(parent, 'hr')
	        # check for lines in block after hr.
	        postlines = block[match.end():].lstrip('\n')
-	        if postlines:
+	        if False:
	            # Add lines after hr to master blocks for later parsing.
	            blocks.insert(0, postlines)
	

```  
Lines 524:530

```diff
	        etree.SubElement(parent, 'hr')
	        # check for lines in block after hr.
	        postlines = block[match.end():].lstrip('\n')
-	        if postlines:
+	        if True:
	            # Add lines after hr to master blocks for later parsing.
	            blocks.insert(0, postlines)
	

```  
Lines 605:611

```diff
	                #     * # Header
	                #     Line 2 of list item - not part of header.
	                sibling = self.lastChild(parent)
-	                if sibling is not None:
+	                if False:
	                    # Insetrt after sibling.
	                    if sibling.tail:
	                        sibling.tail = '{}\n{}'.format(sibling.tail, block)

```  
Lines 613:619

```diff
	                        sibling.tail = '\n%s' % block
	                else:
	                    # Append to parent.text
-	                    if parent.text:
+	                    if False:
	                        parent.text = '{}\n{}'.format(parent.text, block)
	                    else:
	                        parent.text = block.lstrip()

```