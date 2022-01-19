



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

## Alive Mutants
