



# /home/ubuntu/projects/markdown/markdown/util.py

## Newly Killed Mutants

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
Lines 331:337

```diff
	        """
	        Return the index of the given name.
	        """
-	        if name in self:
+	        if True:
	            self._sort()
	            return self._priority.index(
	                [x for x in self._priority if x.name == name][0]

```  
Lines 334:340

```diff
	        if name in self:
	            self._sort()
	            return self._priority.index(
-	                [x for x in self._priority if x.name == name][0]
+	                [x for x in self._priority if x.name == name][<_ast.Constant object at 0x7fe41339ed60>]
	            )
	        raise ValueError('No item named "{}" exists.'.format(name))
	

```  
Lines 334:340

```diff
	        if name in self:
	            self._sort()
	            return self._priority.index(
-	                [x for x in self._priority if x.name == name][0]
+	                [x for x in self._priority if (x.name < name)][0]
	            )
	        raise ValueError('No item named "{}" exists.'.format(name))
	

```  
Lines 334:340

```diff
	        if name in self:
	            self._sort()
	            return self._priority.index(
-	                [x for x in self._priority if x.name == name][0]
+	                [x for x in self._priority if (x.name >= name)][0]
	            )
	        raise ValueError('No item named "{}" exists.'.format(name))
	

```  
Lines 334:340

```diff
	        if name in self:
	            self._sort()
	            return self._priority.index(
-	                [x for x in self._priority if x.name == name][0]
+	                [x for x in self._priority if (x.name != name)][0]
	            )
	        raise ValueError('No item named "{}" exists.'.format(name))
	

```  
Lines 334:340

```diff
	        if name in self:
	            self._sort()
	            return self._priority.index(
-	                [x for x in self._priority if x.name == name][0]
+	                [x for x in self._priority if (x.name > name)][0]
	            )
	        raise ValueError('No item named "{}" exists.'.format(name))
	

```  
Lines 334:340

```diff
	        if name in self:
	            self._sort()
	            return self._priority.index(
-	                [x for x in self._priority if x.name == name][0]
+	                [x for x in self._priority if (x.name <= name)][0]
	            )
	        raise ValueError('No item named "{}" exists.'.format(name))
	

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

### testCustomSubstitutions_call_add_0_str_hlf_0
  
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
Lines 157:163

```diff
	            write(" />")
	        else:
	            write(">")
-	            if text:
+	            if True:
	                if tag.lower() in ["script", "style"]:
	                    write(text)
	                else:

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
Lines 166:172

```diff
	                _serialize_html(write, e, format)
	            if tag.lower() not in HTML_EMPTY:
	                write("</" + tag + ">")
-	    if elem.tail:
+	    if False:
	        write(_escape_cdata(elem.tail))
	
	

```  
Lines 166:172

```diff
	                _serialize_html(write, e, format)
	            if tag.lower() not in HTML_EMPTY:
	                write("</" + tag + ">")
-	    if elem.tail:
+	    if True:
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

### testCustomSubstitutions_none_1_none_0
  
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
+	            ext = entry_points[<_ast.Constant object at 0x7fe4198f0cd0>].load()
	            return ext(**configs)
	
	        # Get class name (if provided): `path.to.module:ClassName`

```  
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

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/treeprocessors.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/blockparser.py

## Newly Killed Mutants

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

### testCustomSubstitutions_str_dbl_1_str_hlf_0
  
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
## Alive Mutants
