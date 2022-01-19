



# /home/ubuntu/projects/markdown/markdown/util.py

## Newly Killed Mutants

### testHtmlSpecialChars_str_dbl_0_str_hlf_1
  
Lines 169:175

```diff
	
	    for size in count(size):
	        frame = frame.f_back
-	        if not frame:
+	        if False:
	            return size
	
	

```  
Lines 175:181

```diff
	
	def nearing_recursion_limit():
	    """Return true if current stack depth is withing 100 of maximum limit."""
-	    return sys.getrecursionlimit() - _get_stack_depth() < 100
+	    return (sys.getrecursionlimit() - _get_stack_depth() >= 100)
	
	
	"""

```  
Lines 175:181

```diff
	
	def nearing_recursion_limit():
	    """Return true if current stack depth is withing 100 of maximum limit."""
-	    return sys.getrecursionlimit() - _get_stack_depth() < 100
+	    return (sys.getrecursionlimit() - _get_stack_depth() != 100)
	
	
	"""

```  
Lines 175:181

```diff
	
	def nearing_recursion_limit():
	    """Return true if current stack depth is withing 100 of maximum limit."""
-	    return sys.getrecursionlimit() - _get_stack_depth() < 100
+	    return (sys.getrecursionlimit() - _get_stack_depth() > 100)
	
	
	"""

```  
Lines 175:181

```diff
	
	def nearing_recursion_limit():
	    """Return true if current stack depth is withing 100 of maximum limit."""
-	    return sys.getrecursionlimit() - _get_stack_depth() < 100
+	    return (sys.getrecursionlimit() % _get_stack_depth()) < 100
	
	
	"""

```  
Lines 175:181

```diff
	
	def nearing_recursion_limit():
	    """Return true if current stack depth is withing 100 of maximum limit."""
-	    return sys.getrecursionlimit() - _get_stack_depth() < 100
+	    return (sys.getrecursionlimit() / _get_stack_depth()) < 100
	
	
	"""

```  
Lines 175:181

```diff
	
	def nearing_recursion_limit():
	    """Return true if current stack depth is withing 100 of maximum limit."""
-	    return sys.getrecursionlimit() - _get_stack_depth() < 100
+	    return (sys.getrecursionlimit() // _get_stack_depth()) < 100
	
	
	"""

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
Lines 137:143

```diff
	       returns True or False. If preserve_none=True, returns True, False,
	       or None. If parsing was not successful, raises  ValueError, or, if
	       fail_on_errors=False, returns None."""
-	    if not isinstance(value, str):
+	    if True:
	        if preserve_none and value is None:
	            return value
	        return bool(value)

```  
Lines 138:144

```diff
	       or None. If parsing was not successful, raises  ValueError, or, if
	       fail_on_errors=False, returns None."""
	    if not isinstance(value, str):
-	        if preserve_none and value is None:
+	        if (preserve_none or value is None):
	            return value
	        return bool(value)
	    elif preserve_none and value.lower() == 'none':

```  
Lines 138:144

```diff
	       or None. If parsing was not successful, raises  ValueError, or, if
	       fail_on_errors=False, returns None."""
	    if not isinstance(value, str):
-	        if preserve_none and value is None:
+	        if False:
	            return value
	        return bool(value)
	    elif preserve_none and value.lower() == 'none':

```  
Lines 138:144

```diff
	       or None. If parsing was not successful, raises  ValueError, or, if
	       fail_on_errors=False, returns None."""
	    if not isinstance(value, str):
-	        if preserve_none and value is None:
+	        if True:
	            return value
	        return bool(value)
	    elif preserve_none and value.lower() == 'none':

```  
Lines 138:144

```diff
	       or None. If parsing was not successful, raises  ValueError, or, if
	       fail_on_errors=False, returns None."""
	    if not isinstance(value, str):
-	        if preserve_none and value is None:
+	        if preserve_none and (value is not None):
	            return value
	        return bool(value)
	    elif preserve_none and value.lower() == 'none':

```  
Lines 138:144

```diff
	       or None. If parsing was not successful, raises  ValueError, or, if
	       fail_on_errors=False, returns None."""
	    if not isinstance(value, str):
-	        if preserve_none and value is None:
+	        if preserve_none and value is (False):
	            return value
	        return bool(value)
	    elif preserve_none and value.lower() == 'none':

```  
Lines 138:144

```diff
	       or None. If parsing was not successful, raises  ValueError, or, if
	       fail_on_errors=False, returns None."""
	    if not isinstance(value, str):
-	        if preserve_none and value is None:
+	        if preserve_none and value is (True):
	            return value
	        return bool(value)
	    elif preserve_none and value.lower() == 'none':

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
+	    if True:
	        text = text.replace(">", "&gt;")
	    return text
	

```  
Lines 169:175

```diff
	
	    for size in count(size):
	        frame = frame.f_back
-	        if not frame:
+	        if True:
	            return size
	
	

```  
Lines 175:181

```diff
	
	def nearing_recursion_limit():
	    """Return true if current stack depth is withing 100 of maximum limit."""
-	    return sys.getrecursionlimit() - _get_stack_depth() < 100
+	    return (sys.getrecursionlimit() - _get_stack_depth() == 100)
	
	
	"""

```  
Lines 175:181

```diff
	
	def nearing_recursion_limit():
	    """Return true if current stack depth is withing 100 of maximum limit."""
-	    return sys.getrecursionlimit() - _get_stack_depth() < 100
+	    return (sys.getrecursionlimit() - _get_stack_depth() <= 100)
	
	
	"""

```  
Lines 175:181

```diff
	
	def nearing_recursion_limit():
	    """Return true if current stack depth is withing 100 of maximum limit."""
-	    return sys.getrecursionlimit() - _get_stack_depth() < 100
+	    return (sys.getrecursionlimit() + _get_stack_depth()) < 100
	
	
	"""

```  
Lines 175:181

```diff
	
	def nearing_recursion_limit():
	    """Return true if current stack depth is withing 100 of maximum limit."""
-	    return sys.getrecursionlimit() - _get_stack_depth() < 100
+	    return (sys.getrecursionlimit() ** _get_stack_depth()) < 100
	
	
	"""

```  
Lines 175:181

```diff
	
	def nearing_recursion_limit():
	    """Return true if current stack depth is withing 100 of maximum limit."""
-	    return sys.getrecursionlimit() - _get_stack_depth() < 100
+	    return (sys.getrecursionlimit() * _get_stack_depth()) < 100
	
	
	"""

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

### testWithAttrList_none_1
  
Lines 104:110

```diff
	            text = RE_AMP.sub('&amp;', text)
	        if "<" in text:
	            text = text.replace("<", "&lt;")
-	        if ">" in text:
+	        if ('>' not in text):
	            text = text.replace(">", "&gt;")
	        if "\"" in text:
	            text = text.replace("\"", "&quot;")

```  
Lines 104:110

```diff
	            text = RE_AMP.sub('&amp;', text)
	        if "<" in text:
	            text = text.replace("<", "&lt;")
-	        if ">" in text:
+	        if False:
	            text = text.replace(">", "&gt;")
	        if "\"" in text:
	            text = text.replace("\"", "&quot;")

```
### testWithAttrList_none_0_str_hlf_2_str_dbl_2
  
Lines 146:152

```diff
	                    v = v.text
	                else:
	                    v = _escape_attrib_html(v)
-	                if k == v and format == 'html':
+	                if (k == v or format == 'html'):
	                    # handle boolean attributes
	                    write(" %s" % v)
	                else:

```  
Lines 146:152

```diff
	                    v = v.text
	                else:
	                    v = _escape_attrib_html(v)
-	                if k == v and format == 'html':
+	                if k == v and (format >= 'html'):
	                    # handle boolean attributes
	                    write(" %s" % v)
	                else:

```  
Lines 146:152

```diff
	                    v = v.text
	                else:
	                    v = _escape_attrib_html(v)
-	                if k == v and format == 'html':
+	                if k == v and (format != 'html'):
	                    # handle boolean attributes
	                    write(" %s" % v)
	                else:

```  
Lines 146:152

```diff
	                    v = v.text
	                else:
	                    v = _escape_attrib_html(v)
-	                if k == v and format == 'html':
+	                if k == v and (format > 'html'):
	                    # handle boolean attributes
	                    write(" %s" % v)
	                else:

```
### testRawHtml_str_dbl_0_str_hlf_1
  
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
+	        if ('<' not in text):
	            text = text.replace("<", "&lt;")
	        if ">" in text:
	            text = text.replace(">", "&gt;")

```
## Alive Mutants
  
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
Lines 99:105

```diff
	def _escape_attrib_html(text):
	    # escape attribute value
	    try:
-	        if "&" in text:
+	        if False:
	            # Only replace & when not part of an entity
	            text = RE_AMP.sub('&amp;', text)
	        if "<" in text:

```  
Lines 99:105

```diff
	def _escape_attrib_html(text):
	    # escape attribute value
	    try:
-	        if "&" in text:
+	        if True:
	            # Only replace & when not part of an entity
	            text = RE_AMP.sub('&amp;', text)
	        if "<" in text:

```  
Lines 99:105

```diff
	def _escape_attrib_html(text):
	    # escape attribute value
	    try:
-	        if "&" in text:
+	        if ('&' not in text):
	            # Only replace & when not part of an entity
	            text = RE_AMP.sub('&amp;', text)
	        if "<" in text:

```  
Lines 102:108

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
Lines 102:108

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
Lines 102:108

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
Lines 104:110

```diff
	            text = RE_AMP.sub('&amp;', text)
	        if "<" in text:
	            text = text.replace("<", "&lt;")
-	        if ">" in text:
+	        if True:
	            text = text.replace(">", "&gt;")
	        if "\"" in text:
	            text = text.replace("\"", "&quot;")

```  
Lines 106:112

```diff
	            text = text.replace("<", "&lt;")
	        if ">" in text:
	            text = text.replace(">", "&gt;")
-	        if "\"" in text:
+	        if False:
	            text = text.replace("\"", "&quot;")
	        return text
	    except (TypeError, AttributeError):  # pragma: no cover

```  
Lines 106:112

```diff
	            text = text.replace("<", "&lt;")
	        if ">" in text:
	            text = text.replace(">", "&gt;")
-	        if "\"" in text:
+	        if True:
	            text = text.replace("\"", "&quot;")
	        return text
	    except (TypeError, AttributeError):  # pragma: no cover

```  
Lines 106:112

```diff
	            text = text.replace("<", "&lt;")
	        if ">" in text:
	            text = text.replace(">", "&gt;")
-	        if "\"" in text:
+	        if ('"' not in text):
	            text = text.replace("\"", "&quot;")
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
+	        if True:
	            items = sorted(items)  # lexical order
	            for k, v in items:
	                if isinstance(k, QName):

```  
Lines 138:144

```diff
	        if items:
	            items = sorted(items)  # lexical order
	            for k, v in items:
-	                if isinstance(k, QName):
+	                if False:
	                    # Assume a text only QName
	                    k = k.text
	                if isinstance(v, QName):

```  
Lines 141:147

```diff
	                if isinstance(k, QName):
	                    # Assume a text only QName
	                    k = k.text
-	                if isinstance(v, QName):
+	                if False:
	                    # Assume a text only QName
	                    v = v.text
	                else:

```  
Lines 146:152

```diff
	                    v = v.text
	                else:
	                    v = _escape_attrib_html(v)
-	                if k == v and format == 'html':
+	                if (k < v) and format == 'html':
	                    # handle boolean attributes
	                    write(" %s" % v)
	                else:

```  
Lines 146:152

```diff
	                    v = v.text
	                else:
	                    v = _escape_attrib_html(v)
-	                if k == v and format == 'html':
+	                if (k >= v) and format == 'html':
	                    # handle boolean attributes
	                    write(" %s" % v)
	                else:

```  
Lines 146:152

```diff
	                    v = v.text
	                else:
	                    v = _escape_attrib_html(v)
-	                if k == v and format == 'html':
+	                if (k != v) and format == 'html':
	                    # handle boolean attributes
	                    write(" %s" % v)
	                else:

```  
Lines 146:152

```diff
	                    v = v.text
	                else:
	                    v = _escape_attrib_html(v)
-	                if k == v and format == 'html':
+	                if (k > v) and format == 'html':
	                    # handle boolean attributes
	                    write(" %s" % v)
	                else:

```  
Lines 146:152

```diff
	                    v = v.text
	                else:
	                    v = _escape_attrib_html(v)
-	                if k == v and format == 'html':
+	                if (k <= v) and format == 'html':
	                    # handle boolean attributes
	                    write(" %s" % v)
	                else:

```  
Lines 146:152

```diff
	                    v = v.text
	                else:
	                    v = _escape_attrib_html(v)
-	                if k == v and format == 'html':
+	                if k == v and (format < 'html'):
	                    # handle boolean attributes
	                    write(" %s" % v)
	                else:

```  
Lines 146:152

```diff
	                    v = v.text
	                else:
	                    v = _escape_attrib_html(v)
-	                if k == v and format == 'html':
+	                if k == v and (format <= 'html'):
	                    # handle boolean attributes
	                    write(" %s" % v)
	                else:

```  
Lines 146:152

```diff
	                    v = v.text
	                else:
	                    v = _escape_attrib_html(v)
-	                if k == v and format == 'html':
+	                if False:
	                    # handle boolean attributes
	                    write(" %s" % v)
	                else:

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
+	        if (format <= 'xhtml') and tag.lower() in HTML_EMPTY:
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

### testWithAttrList_str_emp_2_none_1
  
Lines 127:133

```diff
	                    'Successfully loaded extension "%s.%s".'
	                    % (ext.__class__.__module__, ext.__class__.__name__)
	                )
-	            elif ext is not None:
+	            elif (ext is None):
	                raise TypeError(
	                    'Extension "{}.{}" must be of type: "{}.{}"'.format(
	                        ext.__class__.__module__, ext.__class__.__name__,

```  
Lines 127:133

```diff
	                    'Successfully loaded extension "%s.%s".'
	                    % (ext.__class__.__module__, ext.__class__.__name__)
	                )
-	            elif ext is not None:
+	            elif True:
	                raise TypeError(
	                    'Extension "{}.{}" must be of type: "{}.{}"'.format(
	                        ext.__class__.__module__, ext.__class__.__name__,

```  
Lines 127:133

```diff
	                    'Successfully loaded extension "%s.%s".'
	                    % (ext.__class__.__module__, ext.__class__.__name__)
	                )
-	            elif ext is not None:
+	            elif ext is not (False):
	                raise TypeError(
	                    'Extension "{}.{}" must be of type: "{}.{}"'.format(
	                        ext.__class__.__module__, ext.__class__.__name__,

```  
Lines 127:133

```diff
	                    'Successfully loaded extension "%s.%s".'
	                    % (ext.__class__.__module__, ext.__class__.__name__)
	                )
-	            elif ext is not None:
+	            elif ext is not (True):
	                raise TypeError(
	                    'Extension "{}.{}" must be of type: "{}.{}"'.format(
	                        ext.__class__.__module__, ext.__class__.__name__,

```
### testWithAttrList_str_dbl_1
  
Lines 164:170

```diff
	                'Successfully imported extension module "%s".' % ext_name
	            )
	        except ImportError as e:
-	            message = 'Failed loading extension "%s".' % ext_name
+	            message = ('Failed loading extension "%s".' - ext_name)
	            e.args = (message,) + e.args[1:]
	            raise
	

```  
Lines 164:170

```diff
	                'Successfully imported extension module "%s".' % ext_name
	            )
	        except ImportError as e:
-	            message = 'Failed loading extension "%s".' % ext_name
+	            message = ('Failed loading extension "%s".' / ext_name)
	            e.args = (message,) + e.args[1:]
	            raise
	

```  
Lines 164:170

```diff
	                'Successfully imported extension module "%s".' % ext_name
	            )
	        except ImportError as e:
-	            message = 'Failed loading extension "%s".' % ext_name
+	            message = ('Failed loading extension "%s".' + ext_name)
	            e.args = (message,) + e.args[1:]
	            raise
	

```  
Lines 164:170

```diff
	                'Successfully imported extension module "%s".' % ext_name
	            )
	        except ImportError as e:
-	            message = 'Failed loading extension "%s".' % ext_name
+	            message = ('Failed loading extension "%s".' ** ext_name)
	            e.args = (message,) + e.args[1:]
	            raise
	

```  
Lines 164:170

```diff
	                'Successfully imported extension module "%s".' % ext_name
	            )
	        except ImportError as e:
-	            message = 'Failed loading extension "%s".' % ext_name
+	            message = ('Failed loading extension "%s".' // ext_name)
	            e.args = (message,) + e.args[1:]
	            raise
	

```  
Lines 164:170

```diff
	                'Successfully imported extension module "%s".' % ext_name
	            )
	        except ImportError as e:
-	            message = 'Failed loading extension "%s".' % ext_name
+	            message = ('Failed loading extension "%s".' * ext_name)
	            e.args = (message,) + e.args[1:]
	            raise
	

```  
Lines 165:171

```diff
	            )
	        except ImportError as e:
	            message = 'Failed loading extension "%s".' % ext_name
-	            e.args = (message,) + e.args[1:]
+	            e.args = ((message,) % e.args[1:])
	            raise
	
	        if class_name:

```  
Lines 165:171

```diff
	            )
	        except ImportError as e:
	            message = 'Failed loading extension "%s".' % ext_name
-	            e.args = (message,) + e.args[1:]
+	            e.args = ((message,) - e.args[1:])
	            raise
	
	        if class_name:

```  
Lines 165:171

```diff
	            )
	        except ImportError as e:
	            message = 'Failed loading extension "%s".' % ext_name
-	            e.args = (message,) + e.args[1:]
+	            e.args = ((message,) / e.args[1:])
	            raise
	
	        if class_name:

```  
Lines 165:171

```diff
	            )
	        except ImportError as e:
	            message = 'Failed loading extension "%s".' % ext_name
-	            e.args = (message,) + e.args[1:]
+	            e.args = ((message,) ** e.args[1:])
	            raise
	
	        if class_name:

```  
Lines 165:171

```diff
	            )
	        except ImportError as e:
	            message = 'Failed loading extension "%s".' % ext_name
-	            e.args = (message,) + e.args[1:]
+	            e.args = ((message,) // e.args[1:])
	            raise
	
	        if class_name:

```  
Lines 165:171

```diff
	            )
	        except ImportError as e:
	            message = 'Failed loading extension "%s".' % ext_name
-	            e.args = (message,) + e.args[1:]
+	            e.args = ((message,) * e.args[1:])
	            raise
	
	        if class_name:

```  
Lines 165:171

```diff
	            )
	        except ImportError as e:
	            message = 'Failed loading extension "%s".' % ext_name
-	            e.args = (message,) + e.args[1:]
+	            e.args = (message,) + e.args[:1]
	            raise
	
	        if class_name:

```  
Lines 165:171

```diff
	            )
	        except ImportError as e:
	            message = 'Failed loading extension "%s".' % ext_name
-	            e.args = (message,) + e.args[1:]
+	            e.args = (message,) + e.args[:]
	            raise
	
	        if class_name:

```
### testWithAttrList_str_emp_1
  
Lines 156:162

```diff
	            return ext(**configs)
	
	        # Get class name (if provided): `path.to.module:ClassName`
-	        ext_name, class_name = ext_name.split(':', 1) if ':' in ext_name else (ext_name, '')
+	        ext_name, class_name = ext_name.split(':', 1) if (':' not in ext_name) else (ext_name, '')
	
	        try:
	            module = importlib.import_module(ext_name)

```
### testWithAttrList_str_emp_3_str_hlf_2
  
Lines 161:167

```diff
	        try:
	            module = importlib.import_module(ext_name)
	            logger.debug(
-	                'Successfully imported extension module "%s".' % ext_name
+	                ('Successfully imported extension module "%s".' - ext_name)
	            )
	        except ImportError as e:
	            message = 'Failed loading extension "%s".' % ext_name

```  
Lines 161:167

```diff
	        try:
	            module = importlib.import_module(ext_name)
	            logger.debug(
-	                'Successfully imported extension module "%s".' % ext_name
+	                ('Successfully imported extension module "%s".' / ext_name)
	            )
	        except ImportError as e:
	            message = 'Failed loading extension "%s".' % ext_name

```  
Lines 161:167

```diff
	        try:
	            module = importlib.import_module(ext_name)
	            logger.debug(
-	                'Successfully imported extension module "%s".' % ext_name
+	                ('Successfully imported extension module "%s".' ** ext_name)
	            )
	        except ImportError as e:
	            message = 'Failed loading extension "%s".' % ext_name

```  
Lines 161:167

```diff
	        try:
	            module = importlib.import_module(ext_name)
	            logger.debug(
-	                'Successfully imported extension module "%s".' % ext_name
+	                ('Successfully imported extension module "%s".' // ext_name)
	            )
	        except ImportError as e:
	            message = 'Failed loading extension "%s".' % ext_name

```  
Lines 161:167

```diff
	        try:
	            module = importlib.import_module(ext_name)
	            logger.debug(
-	                'Successfully imported extension module "%s".' % ext_name
+	                ('Successfully imported extension module "%s".' * ext_name)
	            )
	        except ImportError as e:
	            message = 'Failed loading extension "%s".' % ext_name

```  
Lines 168:174

```diff
	            e.args = (message,) + e.args[1:]
	            raise
	
-	        if class_name:
+	        if True:
	            # Load given class name from module.
	            return getattr(module, class_name)(**configs)
	        else:

```  
Lines 176:182

```diff
	            try:
	                return module.makeExtension(**configs)
	            except AttributeError as e:
-	                message = e.args[0]
+	                message = e.args[<_ast.Constant object at 0x7fe4142216a0>]
	                message = "Failed to initiate extension " \
	                          "'%s': %s" % (ext_name, message)
	                e.args = (message,) + e.args[1:]

```  
Lines 177:184

```diff
	                return module.makeExtension(**configs)
	            except AttributeError as e:
	                message = e.args[0]
-	                message = "Failed to initiate extension " \
-	                          "'%s': %s" % (ext_name, message)
+	                message = ("Failed to initiate extension '%s': %s" - (ext_name, message))
	                e.args = (message,) + e.args[1:]
	                raise
	

```  
Lines 177:184

```diff
	                return module.makeExtension(**configs)
	            except AttributeError as e:
	                message = e.args[0]
-	                message = "Failed to initiate extension " \
-	                          "'%s': %s" % (ext_name, message)
+	                message = ("Failed to initiate extension '%s': %s" / (ext_name, message))
	                e.args = (message,) + e.args[1:]
	                raise
	

```  
Lines 177:184

```diff
	                return module.makeExtension(**configs)
	            except AttributeError as e:
	                message = e.args[0]
-	                message = "Failed to initiate extension " \
-	                          "'%s': %s" % (ext_name, message)
+	                message = ("Failed to initiate extension '%s': %s" + (ext_name, message))
	                e.args = (message,) + e.args[1:]
	                raise
	

```  
Lines 177:184

```diff
	                return module.makeExtension(**configs)
	            except AttributeError as e:
	                message = e.args[0]
-	                message = "Failed to initiate extension " \
-	                          "'%s': %s" % (ext_name, message)
+	                message = ("Failed to initiate extension '%s': %s" ** (ext_name, message))
	                e.args = (message,) + e.args[1:]
	                raise
	

```  
Lines 177:184

```diff
	                return module.makeExtension(**configs)
	            except AttributeError as e:
	                message = e.args[0]
-	                message = "Failed to initiate extension " \
-	                          "'%s': %s" % (ext_name, message)
+	                message = ("Failed to initiate extension '%s': %s" // (ext_name, message))
	                e.args = (message,) + e.args[1:]
	                raise
	

```  
Lines 177:184

```diff
	                return module.makeExtension(**configs)
	            except AttributeError as e:
	                message = e.args[0]
-	                message = "Failed to initiate extension " \
-	                          "'%s': %s" % (ext_name, message)
+	                message = ("Failed to initiate extension '%s': %s" * (ext_name, message))
	                e.args = (message,) + e.args[1:]
	                raise
	

```  
Lines 179:185

```diff
	                message = e.args[0]
	                message = "Failed to initiate extension " \
	                          "'%s': %s" % (ext_name, message)
-	                e.args = (message,) + e.args[1:]
+	                e.args = (message,) + e.args[:1]
	                raise
	
	    def registerExtension(self, extension):

```  
Lines 179:185

```diff
	                message = e.args[0]
	                message = "Failed to initiate extension " \
	                          "'%s': %s" % (ext_name, message)
-	                e.args = (message,) + e.args[1:]
+	                e.args = (message,) + e.args[:]
	                raise
	
	    def registerExtension(self, extension):

```  
Lines 179:185

```diff
	                message = e.args[0]
	                message = "Failed to initiate extension " \
	                          "'%s': %s" % (ext_name, message)
-	                e.args = (message,) + e.args[1:]
+	                e.args = ((message,) % e.args[1:])
	                raise
	
	    def registerExtension(self, extension):

```  
Lines 179:185

```diff
	                message = e.args[0]
	                message = "Failed to initiate extension " \
	                          "'%s': %s" % (ext_name, message)
-	                e.args = (message,) + e.args[1:]
+	                e.args = ((message,) - e.args[1:])
	                raise
	
	    def registerExtension(self, extension):

```  
Lines 179:185

```diff
	                message = e.args[0]
	                message = "Failed to initiate extension " \
	                          "'%s': %s" % (ext_name, message)
-	                e.args = (message,) + e.args[1:]
+	                e.args = ((message,) / e.args[1:])
	                raise
	
	    def registerExtension(self, extension):

```  
Lines 179:185

```diff
	                message = e.args[0]
	                message = "Failed to initiate extension " \
	                          "'%s': %s" % (ext_name, message)
-	                e.args = (message,) + e.args[1:]
+	                e.args = ((message,) ** e.args[1:])
	                raise
	
	    def registerExtension(self, extension):

```  
Lines 179:185

```diff
	                message = e.args[0]
	                message = "Failed to initiate extension " \
	                          "'%s': %s" % (ext_name, message)
-	                e.args = (message,) + e.args[1:]
+	                e.args = ((message,) // e.args[1:])
	                raise
	
	    def registerExtension(self, extension):

```  
Lines 179:185

```diff
	                message = e.args[0]
	                message = "Failed to initiate extension " \
	                          "'%s': %s" % (ext_name, message)
-	                e.args = (message,) + e.args[1:]
+	                e.args = ((message,) * e.args[1:])
	                raise
	
	    def registerExtension(self, extension):

```
## Alive Mutants
  
Lines 127:133

```diff
	                    'Successfully loaded extension "%s.%s".'
	                    % (ext.__class__.__module__, ext.__class__.__name__)
	                )
-	            elif ext is not None:
+	            elif False:
	                raise TypeError(
	                    'Extension "{}.{}" must be of type: "{}.{}"'.format(
	                        ext.__class__.__module__, ext.__class__.__name__,

```  
Lines 161:167

```diff
	        try:
	            module = importlib.import_module(ext_name)
	            logger.debug(
-	                'Successfully imported extension module "%s".' % ext_name
+	                ('Successfully imported extension module "%s".' + ext_name)
	            )
	        except ImportError as e:
	            message = 'Failed loading extension "%s".' % ext_name

```  
Lines 168:174

```diff
	            e.args = (message,) + e.args[1:]
	            raise
	
-	        if class_name:
+	        if False:
	            # Load given class name from module.
	            return getattr(module, class_name)(**configs)
	        else:

```  
Lines 176:182

```diff
	            try:
	                return module.makeExtension(**configs)
	            except AttributeError as e:
-	                message = e.args[0]
+	                message = e.args[<_ast.Constant object at 0x7fe414221f40>]
	                message = "Failed to initiate extension " \
	                          "'%s': %s" % (ext_name, message)
	                e.args = (message,) + e.args[1:]

```
# /home/ubuntu/projects/markdown/markdown/htmlparser.py

## Newly Killed Mutants

### testWithAttrList_str_emp_2_none_1
  
Lines 124:130

```diff
	        Allows for up to three blank spaces at start of line.
	        """
	        if self.offset == 0:
-	            return True
+	            return (False)
	        if self.offset > 3:
	            return False
	        # Confirm up to first 3 chars are whitespace

```  
Lines 124:130

```diff
	        Allows for up to three blank spaces at start of line.
	        """
	        if self.offset == 0:
-	            return True
+	            return None
	        if self.offset > 3:
	            return False
	        # Confirm up to first 3 chars are whitespace

```  
Lines 128:134

```diff
	        if self.offset > 3:
	            return False
	        # Confirm up to first 3 chars are whitespace
-	        return self.rawdata[self.line_offset:self.line_offset + self.offset].strip() == ''
+	        return self.rawdata[self.line_offset:(self.line_offset % self.offset)].strip() == ''
	
	    def get_endtag_text(self, tag):
	        """

```  
Lines 128:134

```diff
	        if self.offset > 3:
	            return False
	        # Confirm up to first 3 chars are whitespace
-	        return self.rawdata[self.line_offset:self.line_offset + self.offset].strip() == ''
+	        return self.rawdata[self.line_offset:(self.line_offset - self.offset)].strip() == ''
	
	    def get_endtag_text(self, tag):
	        """

```  
Lines 128:134

```diff
	        if self.offset > 3:
	            return False
	        # Confirm up to first 3 chars are whitespace
-	        return self.rawdata[self.line_offset:self.line_offset + self.offset].strip() == ''
+	        return self.rawdata[self.line_offset:(self.line_offset ** self.offset)].strip() == ''
	
	    def get_endtag_text(self, tag):
	        """

```  
Lines 128:134

```diff
	        if self.offset > 3:
	            return False
	        # Confirm up to first 3 chars are whitespace
-	        return self.rawdata[self.line_offset:self.line_offset + self.offset].strip() == ''
+	        return self.rawdata[self.line_offset:(self.line_offset // self.offset)].strip() == ''
	
	    def get_endtag_text(self, tag):
	        """

```  
Lines 128:134

```diff
	        if self.offset > 3:
	            return False
	        # Confirm up to first 3 chars are whitespace
-	        return self.rawdata[self.line_offset:self.line_offset + self.offset].strip() == ''
+	        return self.rawdata[self.line_offset:(self.line_offset * self.offset)].strip() == ''
	
	    def get_endtag_text(self, tag):
	        """

```  
Lines 128:134

```diff
	        if self.offset > 3:
	            return False
	        # Confirm up to first 3 chars are whitespace
-	        return self.rawdata[self.line_offset:self.line_offset + self.offset].strip() == ''
+	        return (self.rawdata[self.line_offset:self.line_offset + self.offset].strip() < '')
	
	    def get_endtag_text(self, tag):
	        """

```  
Lines 128:134

```diff
	        if self.offset > 3:
	            return False
	        # Confirm up to first 3 chars are whitespace
-	        return self.rawdata[self.line_offset:self.line_offset + self.offset].strip() == ''
+	        return (self.rawdata[self.line_offset:self.line_offset + self.offset].strip() >= '')
	
	    def get_endtag_text(self, tag):
	        """

```  
Lines 128:134

```diff
	        if self.offset > 3:
	            return False
	        # Confirm up to first 3 chars are whitespace
-	        return self.rawdata[self.line_offset:self.line_offset + self.offset].strip() == ''
+	        return (self.rawdata[self.line_offset:self.line_offset + self.offset].strip() != '')
	
	    def get_endtag_text(self, tag):
	        """

```  
Lines 128:134

```diff
	        if self.offset > 3:
	            return False
	        # Confirm up to first 3 chars are whitespace
-	        return self.rawdata[self.line_offset:self.line_offset + self.offset].strip() == ''
+	        return (self.rawdata[self.line_offset:self.line_offset + self.offset].strip() > '')
	
	    def get_endtag_text(self, tag):
	        """

```  
Lines 128:134

```diff
	        if self.offset > 3:
	            return False
	        # Confirm up to first 3 chars are whitespace
-	        return self.rawdata[self.line_offset:self.line_offset + self.offset].strip() == ''
+	        return (self.rawdata[self.line_offset:self.line_offset + self.offset].strip() <= '')
	
	    def get_endtag_text(self, tag):
	        """

```
### testHtmlEntities_str_dbl_0_str_hlf_1
  
Lines 128:134

```diff
	        if self.offset > 3:
	            return False
	        # Confirm up to first 3 chars are whitespace
-	        return self.rawdata[self.line_offset:self.line_offset + self.offset].strip() == ''
+	        return self.rawdata[self.line_offset:(self.line_offset / self.offset)].strip() == ''
	
	    def get_endtag_text(self, tag):
	        """

```
## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/__main__.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/pep562.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/inlinepatterns.py

## Newly Killed Mutants

### testWithAttrList_str_emp_2_none_1
  
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
Lines 660:666

```diff
	                if c == '(':
	                    # Count nested (
	                    # Don't increment the bracket count if we are sure we're in a title.
-	                    if not ignore_matches:
+	                    if True:
	                        bracket_count += 1
	                    elif backtrack_count > 0:
	                        backtrack_count -= 1

```  
Lines 661:667

```diff
	                    # Count nested (
	                    # Don't increment the bracket count if we are sure we're in a title.
	                    if not ignore_matches:
-	                        bracket_count += 1
+	                        bracket_count /= 1
	                    elif backtrack_count > 0:
	                        backtrack_count -= 1
	                elif c == ')':

```  
Lines 661:667

```diff
	                    # Count nested (
	                    # Don't increment the bracket count if we are sure we're in a title.
	                    if not ignore_matches:
-	                        bracket_count += 1
+	                        bracket_count *= 1
	                    elif backtrack_count > 0:
	                        backtrack_count -= 1
	                elif c == ')':

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
### testHeaderInlineMarkup_str_hlf_1_str_dbl_1
  
Lines 660:666

```diff
	                if c == '(':
	                    # Count nested (
	                    # Don't increment the bracket count if we are sure we're in a title.
-	                    if not ignore_matches:
+	                    if False:
	                        bracket_count += 1
	                    elif backtrack_count > 0:
	                        backtrack_count -= 1

```  
Lines 661:667

```diff
	                    # Count nested (
	                    # Don't increment the bracket count if we are sure we're in a title.
	                    if not ignore_matches:
-	                        bracket_count += 1
+	                        bracket_count -= 1
	                    elif backtrack_count > 0:
	                        backtrack_count -= 1
	                elif c == ')':

```
## Alive Mutants
  
Lines 813:819

```diff
	        else:
	            id = m.group(1).lower()
	            end = m.end(0)
-	            if not id:
+	            if False:
	                id = text.lower()
	        return id, end, True
	

```  
Lines 813:819

```diff
	        else:
	            id = m.group(1).lower()
	            end = m.end(0)
-	            if not id:
+	            if True:
	                id = text.lower()
	        return id, end, True
	

```  
Lines 815:821

```diff
	            end = m.end(0)
	            if not id:
	                id = text.lower()
-	        return id, end, True
+	        return id, end, (False)
	
	    def makeTag(self, href, title, text):
	        el = etree.Element('a')

```  
Lines 815:821

```diff
	            end = m.end(0)
	            if not id:
	                id = text.lower()
-	        return id, end, True
+	        return id, end, None
	
	    def makeTag(self, href, title, text):
	        el = etree.Element('a')

```
# /home/ubuntu/projects/markdown/markdown/treeprocessors.py

## Newly Killed Mutants

### testWithAttrList_str_emp_2_none_1
  
Lines 187:193

```diff
	                    else:
	                        result[-1][0].tail = text
	                elif not isText:
-	                    if parent.tail:
+	                    if False:
	                        parent.tail += text
	                    else:
	                        parent.tail = text

```  
Lines 378:384

```diff
	                if child.tail:
	                    tail = self.__handleInline(child.tail)
	                    dumby = etree.Element('d')
-	                    child.tail = None
+	                    child.tail = (False)
	                    tailResult = self.__processPlaceholders(tail, dumby, False)
	                    if dumby.tail:
	                        child.tail = dumby.tail

```  
Lines 378:384

```diff
	                if child.tail:
	                    tail = self.__handleInline(child.tail)
	                    dumby = etree.Element('d')
-	                    child.tail = None
+	                    child.tail = (True)
	                    tailResult = self.__processPlaceholders(tail, dumby, False)
	                    if dumby.tail:
	                        child.tail = dumby.tail

```  
Lines 379:385

```diff
	                    tail = self.__handleInline(child.tail)
	                    dumby = etree.Element('d')
	                    child.tail = None
-	                    tailResult = self.__processPlaceholders(tail, dumby, False)
+	                    tailResult = self.__processPlaceholders(tail, dumby, None)
	                    if dumby.tail:
	                        child.tail = dumby.tail
	                    pos = list(currElement).index(child) + 1

```  
Lines 380:386

```diff
	                    dumby = etree.Element('d')
	                    child.tail = None
	                    tailResult = self.__processPlaceholders(tail, dumby, False)
-	                    if dumby.tail:
+	                    if True:
	                        child.tail = dumby.tail
	                    pos = list(currElement).index(child) + 1
	                    tailResult.reverse()

```  
Lines 382:388

```diff
	                    tailResult = self.__processPlaceholders(tail, dumby, False)
	                    if dumby.tail:
	                        child.tail = dumby.tail
-	                    pos = list(currElement).index(child) + 1
+	                    pos = (list(currElement).index(child) % 1)
	                    tailResult.reverse()
	                    for newChild in tailResult:
	                        self.parent_map[newChild[0]] = currElement

```  
Lines 382:388

```diff
	                    tailResult = self.__processPlaceholders(tail, dumby, False)
	                    if dumby.tail:
	                        child.tail = dumby.tail
-	                    pos = list(currElement).index(child) + 1
+	                    pos = (list(currElement).index(child) - 1)
	                    tailResult.reverse()
	                    for newChild in tailResult:
	                        self.parent_map[newChild[0]] = currElement

```  
Lines 382:388

```diff
	                    tailResult = self.__processPlaceholders(tail, dumby, False)
	                    if dumby.tail:
	                        child.tail = dumby.tail
-	                    pos = list(currElement).index(child) + 1
+	                    pos = (list(currElement).index(child) / 1)
	                    tailResult.reverse()
	                    for newChild in tailResult:
	                        self.parent_map[newChild[0]] = currElement

```  
Lines 382:388

```diff
	                    tailResult = self.__processPlaceholders(tail, dumby, False)
	                    if dumby.tail:
	                        child.tail = dumby.tail
-	                    pos = list(currElement).index(child) + 1
+	                    pos = (list(currElement).index(child) ** 1)
	                    tailResult.reverse()
	                    for newChild in tailResult:
	                        self.parent_map[newChild[0]] = currElement

```  
Lines 382:388

```diff
	                    tailResult = self.__processPlaceholders(tail, dumby, False)
	                    if dumby.tail:
	                        child.tail = dumby.tail
-	                    pos = list(currElement).index(child) + 1
+	                    pos = (list(currElement).index(child) // 1)
	                    tailResult.reverse()
	                    for newChild in tailResult:
	                        self.parent_map[newChild[0]] = currElement

```  
Lines 382:388

```diff
	                    tailResult = self.__processPlaceholders(tail, dumby, False)
	                    if dumby.tail:
	                        child.tail = dumby.tail
-	                    pos = list(currElement).index(child) + 1
+	                    pos = (list(currElement).index(child) * 1)
	                    tailResult.reverse()
	                    for newChild in tailResult:
	                        self.parent_map[newChild[0]] = currElement

```
### testHeaderInlineMarkup_str_dbl_1_str_hlf_1
  
Lines 165:171

```diff
	
	        childResult.reverse()
	        for newChild in childResult:
-	            node.insert(pos, newChild[0])
+	            node.insert(pos, newChild[<_ast.Constant object at 0x7fe4140d0f10>])
	
	    def __processPlaceholders(self, data, parent, isText=True):
	        """

```  
Lines 165:171

```diff
	
	        childResult.reverse()
	        for newChild in childResult:
-	            node.insert(pos, newChild[0])
+	            node.insert(pos, newChild[<_ast.Constant object at 0x7fe4140d00d0>])
	
	    def __processPlaceholders(self, data, parent, isText=True):
	        """

```  
Lines 187:193

```diff
	                    else:
	                        result[-1][0].tail = text
	                elif not isText:
-	                    if parent.tail:
+	                    if True:
	                        parent.tail += text
	                    else:
	                        parent.tail = text

```  
Lines 379:385

```diff
	                    tail = self.__handleInline(child.tail)
	                    dumby = etree.Element('d')
	                    child.tail = None
-	                    tailResult = self.__processPlaceholders(tail, dumby, False)
+	                    tailResult = self.__processPlaceholders(tail, dumby, (True))
	                    if dumby.tail:
	                        child.tail = dumby.tail
	                    pos = list(currElement).index(child) + 1

```  
Lines 380:386

```diff
	                    dumby = etree.Element('d')
	                    child.tail = None
	                    tailResult = self.__processPlaceholders(tail, dumby, False)
-	                    if dumby.tail:
+	                    if False:
	                        child.tail = dumby.tail
	                    pos = list(currElement).index(child) + 1
	                    tailResult.reverse()

```
## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/blockparser.py

## Newly Killed Mutants

### testHtmlSpecialChars_str_dbl_0_str_hlf_1
  
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
### testWithAttrList_str_emp_2_none_1
  
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
+	            return self[(-1)] == state
	        else:
	            return False
	

```
### testHeaderInlineMarkup_str_hlf_0_call_dup_0_str_hlf_1
  
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
## Alive Mutants

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

### testMarker_str_emp_0_call_dup_0_str_hlf_0
  
Lines 76:82

```diff
	        if len(parent):
	            return parent[-1]
	        else:
-	            return None
+	            return (False)
	
	    def detab(self, text, length=None):
	        """ Remove a tab from the front of each line of the given text. """

```  
Lines 76:82

```diff
	        if len(parent):
	            return parent[-1]
	        else:
-	            return None
+	            return (True)
	
	    def detab(self, text, length=None):
	        """ Remove a tab from the front of each line of the given text. """

```  
Lines 544:550

```diff
	            filler = '\n'
	            # Save the rest for later.
	            theRest = block[1:]
-	            if theRest:
+	            if False:
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)

```
### testWithAttrList_str_emp_2_none_1
  
Lines 284:290

```diff
	    def run(self, parent, blocks):
	        block = blocks.pop(0)
	        m = self.RE.search(block)
-	        if m:
+	        if True:
	            before = block[:m.start()]  # Lines before blockquote
	            # Pass lines before blockquote in recursively for parsing forst.
	            self.parser.parseBlocks(parent, [before])

```  
Lines 290:296

```diff
	            self.parser.parseBlocks(parent, [before])
	            # Remove ``> `` from beginning of each line.
	            block = '\n'.join(
-	                [self.clean(line) for line in block[m.start():].split('\n')]
+	                [self.clean(line) for line in block[:].split('\n')]
	            )
	        sibling = self.lastChild(parent)
	        if sibling is not None and sibling.tag == "blockquote":

```  
Lines 293:299

```diff
	                [self.clean(line) for line in block[m.start():].split('\n')]
	            )
	        sibling = self.lastChild(parent)
-	        if sibling is not None and sibling.tag == "blockquote":
+	        if False:
	            # Previous block was a blockquote so set that as this blocks parent
	            quote = sibling
	        else:

```  
Lines 293:299

```diff
	                [self.clean(line) for line in block[m.start():].split('\n')]
	            )
	        sibling = self.lastChild(parent)
-	        if sibling is not None and sibling.tag == "blockquote":
+	        if sibling is not None and (sibling.tag < 'blockquote'):
	            # Previous block was a blockquote so set that as this blocks parent
	            quote = sibling
	        else:

```  
Lines 293:299

```diff
	                [self.clean(line) for line in block[m.start():].split('\n')]
	            )
	        sibling = self.lastChild(parent)
-	        if sibling is not None and sibling.tag == "blockquote":
+	        if sibling is not None and (sibling.tag >= 'blockquote'):
	            # Previous block was a blockquote so set that as this blocks parent
	            quote = sibling
	        else:

```  
Lines 293:299

```diff
	                [self.clean(line) for line in block[m.start():].split('\n')]
	            )
	        sibling = self.lastChild(parent)
-	        if sibling is not None and sibling.tag == "blockquote":
+	        if sibling is not None and (sibling.tag != 'blockquote'):
	            # Previous block was a blockquote so set that as this blocks parent
	            quote = sibling
	        else:

```  
Lines 293:299

```diff
	                [self.clean(line) for line in block[m.start():].split('\n')]
	            )
	        sibling = self.lastChild(parent)
-	        if sibling is not None and sibling.tag == "blockquote":
+	        if sibling is not None and (sibling.tag > 'blockquote'):
	            # Previous block was a blockquote so set that as this blocks parent
	            quote = sibling
	        else:

```  
Lines 293:299

```diff
	                [self.clean(line) for line in block[m.start():].split('\n')]
	            )
	        sibling = self.lastChild(parent)
-	        if sibling is not None and sibling.tag == "blockquote":
+	        if sibling is not None and (sibling.tag <= 'blockquote'):
	            # Previous block was a blockquote so set that as this blocks parent
	            quote = sibling
	        else:

```  
Lines 308:314

```diff
	    def clean(self, line):
	        """ Remove ``>`` from beginning of a line. """
	        m = self.RE.match(line)
-	        if line.strip() == ">":
+	        if False:
	            return ""
	        elif m:
	            return m.group(2)

```  
Lines 308:314

```diff
	    def clean(self, line):
	        """ Remove ``>`` from beginning of a line. """
	        m = self.RE.match(line)
-	        if line.strip() == ">":
+	        if (line.strip() < '>'):
	            return ""
	        elif m:
	            return m.group(2)

```  
Lines 308:314

```diff
	    def clean(self, line):
	        """ Remove ``>`` from beginning of a line. """
	        m = self.RE.match(line)
-	        if line.strip() == ">":
+	        if (line.strip() <= '>'):
	            return ""
	        elif m:
	            return m.group(2)

```  
Lines 310:316

```diff
	        m = self.RE.match(line)
	        if line.strip() == ">":
	            return ""
-	        elif m:
+	        elif True:
	            return m.group(2)
	        else:
	            return line

```  
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
Lines 544:550

```diff
	            filler = '\n'
	            # Save the rest for later.
	            theRest = block[1:]
-	            if theRest:
+	            if True:
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)

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
### testHtmlSpecialChars_str_dbl_0_str_hlf_1
  
Lines 284:290

```diff
	    def run(self, parent, blocks):
	        block = blocks.pop(0)
	        m = self.RE.search(block)
-	        if m:
+	        if False:
	            before = block[:m.start()]  # Lines before blockquote
	            # Pass lines before blockquote in recursively for parsing forst.
	            self.parser.parseBlocks(parent, [before])

```  
Lines 285:291

```diff
	        block = blocks.pop(0)
	        m = self.RE.search(block)
	        if m:
-	            before = block[:m.start()]  # Lines before blockquote
+	            before = block[m.start():]  # Lines before blockquote
	            # Pass lines before blockquote in recursively for parsing forst.
	            self.parser.parseBlocks(parent, [before])
	            # Remove ``> `` from beginning of each line.

```  
Lines 285:291

```diff
	        block = blocks.pop(0)
	        m = self.RE.search(block)
	        if m:
-	            before = block[:m.start()]  # Lines before blockquote
+	            before = block[:]  # Lines before blockquote
	            # Pass lines before blockquote in recursively for parsing forst.
	            self.parser.parseBlocks(parent, [before])
	            # Remove ``> `` from beginning of each line.

```  
Lines 290:296

```diff
	            self.parser.parseBlocks(parent, [before])
	            # Remove ``> `` from beginning of each line.
	            block = '\n'.join(
-	                [self.clean(line) for line in block[m.start():].split('\n')]
+	                [self.clean(line) for line in block[:m.start()].split('\n')]
	            )
	        sibling = self.lastChild(parent)
	        if sibling is not None and sibling.tag == "blockquote":

```  
Lines 293:299

```diff
	                [self.clean(line) for line in block[m.start():].split('\n')]
	            )
	        sibling = self.lastChild(parent)
-	        if sibling is not None and sibling.tag == "blockquote":
+	        if True:
	            # Previous block was a blockquote so set that as this blocks parent
	            quote = sibling
	        else:

```  
Lines 293:299

```diff
	                [self.clean(line) for line in block[m.start():].split('\n')]
	            )
	        sibling = self.lastChild(parent)
-	        if sibling is not None and sibling.tag == "blockquote":
+	        if sibling is not (False) and sibling.tag == "blockquote":
	            # Previous block was a blockquote so set that as this blocks parent
	            quote = sibling
	        else:

```  
Lines 293:299

```diff
	                [self.clean(line) for line in block[m.start():].split('\n')]
	            )
	        sibling = self.lastChild(parent)
-	        if sibling is not None and sibling.tag == "blockquote":
+	        if sibling is not (True) and sibling.tag == "blockquote":
	            # Previous block was a blockquote so set that as this blocks parent
	            quote = sibling
	        else:

```  
Lines 293:299

```diff
	                [self.clean(line) for line in block[m.start():].split('\n')]
	            )
	        sibling = self.lastChild(parent)
-	        if sibling is not None and sibling.tag == "blockquote":
+	        if (sibling is not None or sibling.tag == 'blockquote'):
	            # Previous block was a blockquote so set that as this blocks parent
	            quote = sibling
	        else:

```  
Lines 293:299

```diff
	                [self.clean(line) for line in block[m.start():].split('\n')]
	            )
	        sibling = self.lastChild(parent)
-	        if sibling is not None and sibling.tag == "blockquote":
+	        if (sibling is None) and sibling.tag == "blockquote":
	            # Previous block was a blockquote so set that as this blocks parent
	            quote = sibling
	        else:

```  
Lines 308:314

```diff
	    def clean(self, line):
	        """ Remove ``>`` from beginning of a line. """
	        m = self.RE.match(line)
-	        if line.strip() == ">":
+	        if True:
	            return ""
	        elif m:
	            return m.group(2)

```  
Lines 308:314

```diff
	    def clean(self, line):
	        """ Remove ``>`` from beginning of a line. """
	        m = self.RE.match(line)
-	        if line.strip() == ">":
+	        if (line.strip() >= '>'):
	            return ""
	        elif m:
	            return m.group(2)

```  
Lines 308:314

```diff
	    def clean(self, line):
	        """ Remove ``>`` from beginning of a line. """
	        m = self.RE.match(line)
-	        if line.strip() == ">":
+	        if (line.strip() != '>'):
	            return ""
	        elif m:
	            return m.group(2)

```  
Lines 308:314

```diff
	    def clean(self, line):
	        """ Remove ``>`` from beginning of a line. """
	        m = self.RE.match(line)
-	        if line.strip() == ">":
+	        if (line.strip() > '>'):
	            return ""
	        elif m:
	            return m.group(2)

```  
Lines 310:316

```diff
	        m = self.RE.match(line)
	        if line.strip() == ">":
	            return ""
-	        elif m:
+	        elif False:
	            return m.group(2)
	        else:
	            return line

```
### testHeaderInlineMarkup_str_hlf_0_call_dup_0_str_hlf_1
  
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
