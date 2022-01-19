



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

### test_ancestors_none_2_str_hlf_1
  
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
### test_ancestors_str_hlf_1_str_dbl_1_none_2
  
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
### test_ancestors_tail_str_hlf_1_none_2
  
Lines 460:466

```diff
	        """Return single tag."""
	        el1 = etree.Element(tag)
	        text = m.group(2)
-	        self.parse_sub_patterns(text, el1, None, idx)
+	        self.parse_sub_patterns(text, el1, (False), idx)
	        return el1
	
	    def build_double(self, m, tags, idx):

```  
Lines 460:466

```diff
	        """Return single tag."""
	        el1 = etree.Element(tag)
	        text = m.group(2)
-	        self.parse_sub_patterns(text, el1, None, idx)
+	        self.parse_sub_patterns(text, el1, (True), idx)
	        return el1
	
	    def build_double(self, m, tags, idx):

```
## Alive Mutants
  
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
+	                        bracket_count *= 1
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
+	                        bracket_count /= 1
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
Lines 794:800

```diff
	
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)
-	        if id not in self.md.references:  # ignore undefined refs
+	        if True:  # ignore undefined refs
	            return None, m.start(0), end
	
	        href, title = self.md.references[id]

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

### test_ancestors_tail_str_hlf_1_none_2
  
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
## Alive Mutants

# /home/ubuntu/projects/markdown/markdown/blockparser.py

## Newly Killed Mutants

### test_ancestors_str_dbl_2_str_hlf_1
  
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
+	            return self[(-1)] == state
	        else:
	            return False
	

```
### test_ancestors_tail_str_hlf_1_none_2
  
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

### test_ancestors_str_dbl_2_str_hlf_1
  
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
+	                if (sibling is None):
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
### test_ancestors_tail_str_hlf_1_none_2
  
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
+	            if False:
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
+	                if False:
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
## Alive Mutants
