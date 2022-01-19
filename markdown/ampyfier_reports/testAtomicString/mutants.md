



# /home/ubuntu/projects/markdown/markdown/util.py

## Newly Killed Mutants

## Alive Mutants
  
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
Lines 29:35

```diff
	
	from .pep562 import Pep562
	
-	if sys.version_info >= (3, 10):
+	if False:
	    from importlib import metadata
	else:
	    # <PY310 use backport

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
Lines 382:388

```diff
	        This method is called internally and should never be explicitly called.
	        """
	        if not self._is_sorted:
-	            self._priority.sort(key=lambda item: item.priority, reverse=True)
+	            self._priority.sort(key=lambda item: item.priority, reverse=(False))
	            self._is_sorted = True
	
	    # Deprecated Methods which provide a smooth transition from OrderedDict

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

### testSimpleAtomicString_none_2
  
Lines 121:127

```diff
	    elif tag is ProcessingInstruction:
	        write("<?%s?>" % _escape_cdata(text))
	    elif tag is None:
-	        if text:
+	        if False:
	            write(_escape_cdata(text))
	        for e in elem:
	            _serialize_html(write, e, format)

```
### testString_none_3_none_2
  
Lines 121:127

```diff
	    elif tag is ProcessingInstruction:
	        write("<?%s?>" % _escape_cdata(text))
	    elif tag is None:
-	        if text:
+	        if True:
	            write(_escape_cdata(text))
	        for e in elem:
	            _serialize_html(write, e, format)

```
## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/core.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/htmlparser.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/__main__.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/pep562.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/inlinepatterns.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/treeprocessors.py

## Newly Killed Mutants

### testString_str_dbl_3
  
Lines 182:188

```diff
	        def linkText(text):
	            if text:
	                if result:
-	                    if result[-1][0].tail:
+	                    if result[(-1)][0].tail:
	                        result[-1][0].tail += text
	                    else:
	                        result[-1][0].tail = text

```  
Lines 182:188

```diff
	        def linkText(text):
	            if text:
	                if result:
-	                    if result[-1][0].tail:
+	                    if result[-1][<_ast.Constant object at 0x7fafc7edb7f0>].tail:
	                        result[-1][0].tail += text
	                    else:
	                        result[-1][0].tail = text

```  
Lines 182:188

```diff
	        def linkText(text):
	            if text:
	                if result:
-	                    if result[-1][0].tail:
+	                    if result[-1][<_ast.Constant object at 0x7fafc8f743d0>].tail:
	                        result[-1][0].tail += text
	                    else:
	                        result[-1][0].tail = text

```  
Lines 182:188

```diff
	        def linkText(text):
	            if text:
	                if result:
-	                    if result[-1][0].tail:
+	                    if True:
	                        result[-1][0].tail += text
	                    else:
	                        result[-1][0].tail = text

```  
Lines 185:191

```diff
	                    if result[-1][0].tail:
	                        result[-1][0].tail += text
	                    else:
-	                        result[-1][0].tail = text
+	                        result[(-1)][0].tail = text
	                elif not isText:
	                    if parent.tail:
	                        parent.tail += text

```  
Lines 185:191

```diff
	                    if result[-1][0].tail:
	                        result[-1][0].tail += text
	                    else:
-	                        result[-1][0].tail = text
+	                        result[-1][<_ast.Constant object at 0x7fafc04807c0>].tail = text
	                elif not isText:
	                    if parent.tail:
	                        parent.tail += text

```  
Lines 185:191

```diff
	                    if result[-1][0].tail:
	                        result[-1][0].tail += text
	                    else:
-	                        result[-1][0].tail = text
+	                        result[-1][<_ast.Constant object at 0x7fafc0480400>].tail = text
	                elif not isText:
	                    if parent.tail:
	                        parent.tail += text

```
### testString_str_dbl_3_str_dbl_3
  
Lines 182:188

```diff
	        def linkText(text):
	            if text:
	                if result:
-	                    if result[-1][0].tail:
+	                    if result[(-1)][0].tail:
	                        result[-1][0].tail += text
	                    else:
	                        result[-1][0].tail = text

```  
Lines 185:191

```diff
	                    if result[-1][0].tail:
	                        result[-1][0].tail += text
	                    else:
-	                        result[-1][0].tail = text
+	                        result[(-1)][0].tail = text
	                elif not isText:
	                    if parent.tail:
	                        parent.tail += text

```
### testString_none_3_none_2
  
Lines 182:188

```diff
	        def linkText(text):
	            if text:
	                if result:
-	                    if result[-1][0].tail:
+	                    if False:
	                        result[-1][0].tail += text
	                    else:
	                        result[-1][0].tail = text

```  
Lines 193:199

```diff
	                        parent.tail = text
	                else:
	                    if parent.text:
-	                        parent.text += text
+	                        parent.text *= text
	                    else:
	                        parent.text = text
	        result = []

```  
Lines 193:199

```diff
	                        parent.tail = text
	                else:
	                    if parent.text:
-	                        parent.text += text
+	                        parent.text -= text
	                    else:
	                        parent.text = text
	        result = []

```  
Lines 193:199

```diff
	                        parent.tail = text
	                else:
	                    if parent.text:
-	                        parent.text += text
+	                        parent.text /= text
	                    else:
	                        parent.text = text
	        result = []

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
### testString_str_hlf_3
  
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

## Alive Mutants
