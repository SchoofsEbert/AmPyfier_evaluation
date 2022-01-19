



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

### testParseChunk_none_1
  
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

### testParseChunk_none_1
  
Lines 538:544

```diff
	    def run(self, parent, blocks):
	        block = blocks.pop(0)
	        filler = '\n\n'
-	        if block:
+	        if False:
	            # Starts with empty line
	            # Only replace a single line.
	            filler = '\n'

```  
Lines 538:544

```diff
	    def run(self, parent, blocks):
	        block = blocks.pop(0)
	        filler = '\n\n'
-	        if block:
+	        if True:
	            # Starts with empty line
	            # Only replace a single line.
	            filler = '\n'

```  
Lines 548:554

```diff
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)
-	        if (sibling is not None and sibling.tag == 'pre' and
+	        if (sibling is not None and (sibling.tag != 'pre') and
	           len(sibling) and sibling[0].tag == 'code'):
	            # Last block is a codeblock. Append to preserve whitespace.
	            sibling[0].text = util.AtomicString(

```  
Lines 548:554

```diff
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)
-	        if (sibling is not None and sibling.tag == 'pre' and
+	        if (sibling is not None and (sibling.tag > 'pre') and
	           len(sibling) and sibling[0].tag == 'code'):
	            # Last block is a codeblock. Append to preserve whitespace.
	            sibling[0].text = util.AtomicString(

```  
Lines 548:554

```diff
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)
-	        if (sibling is not None and sibling.tag == 'pre' and
+	        if (sibling is not None and (sibling.tag <= 'pre') and
	           len(sibling) and sibling[0].tag == 'code'):
	            # Last block is a codeblock. Append to preserve whitespace.
	            sibling[0].text = util.AtomicString(

```  
Lines 548:554

```diff
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)
-	        if (sibling is not None and sibling.tag == 'pre' and
+	        if (sibling is not None and (sibling.tag < 'pre') and
	           len(sibling) and sibling[0].tag == 'code'):
	            # Last block is a codeblock. Append to preserve whitespace.
	            sibling[0].text = util.AtomicString(

```  
Lines 548:554

```diff
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)
-	        if (sibling is not None and sibling.tag == 'pre' and
+	        if (sibling is not None and (sibling.tag >= 'pre') and
	           len(sibling) and sibling[0].tag == 'code'):
	            # Last block is a codeblock. Append to preserve whitespace.
	            sibling[0].text = util.AtomicString(

```  
Lines 548:555

```diff
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)
-	        if (sibling is not None and sibling.tag == 'pre' and
-	           len(sibling) and sibling[0].tag == 'code'):
+	        if False:
	            # Last block is a codeblock. Append to preserve whitespace.
	            sibling[0].text = util.AtomicString(
	                '{}{}'.format(sibling[0].text, filler)

```
### testParseChunk_str_emp_2
  
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
Lines 548:555

```diff
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)
-	        if (sibling is not None and sibling.tag == 'pre' and
-	           len(sibling) and sibling[0].tag == 'code'):
+	        if ((sibling is not None or sibling.tag == 'pre' or len(sibling) or sibling[0].
    tag == 'code')):
	            # Last block is a codeblock. Append to preserve whitespace.
	            sibling[0].text = util.AtomicString(
	                '{}{}'.format(sibling[0].text, filler)

```  
Lines 548:554

```diff
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)
-	        if (sibling is not None and sibling.tag == 'pre' and
+	        if ((sibling is None) and sibling.tag == 'pre' and
	           len(sibling) and sibling[0].tag == 'code'):
	            # Last block is a codeblock. Append to preserve whitespace.
	            sibling[0].text = util.AtomicString(

```  
Lines 548:554

```diff
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)
-	        if (sibling is not None and sibling.tag == 'pre' and
+	        if (sibling is not (False) and sibling.tag == 'pre' and
	           len(sibling) and sibling[0].tag == 'code'):
	            # Last block is a codeblock. Append to preserve whitespace.
	            sibling[0].text = util.AtomicString(

```  
Lines 548:554

```diff
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)
-	        if (sibling is not None and sibling.tag == 'pre' and
+	        if (sibling is not (True) and sibling.tag == 'pre' and
	           len(sibling) and sibling[0].tag == 'code'):
	            # Last block is a codeblock. Append to preserve whitespace.
	            sibling[0].text = util.AtomicString(

```  
Lines 548:555

```diff
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)
-	        if (sibling is not None and sibling.tag == 'pre' and
-	           len(sibling) and sibling[0].tag == 'code'):
+	        if True:
	            # Last block is a codeblock. Append to preserve whitespace.
	            sibling[0].text = util.AtomicString(
	                '{}{}'.format(sibling[0].text, filler)

```
### testParseDocument_str_chr_0_str_emp_1
  
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
## Alive Mutants
  
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