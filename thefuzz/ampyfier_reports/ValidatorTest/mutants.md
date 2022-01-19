



# /home/ubuntu/projects/thefuzz/thefuzz/fuzz.py

## Newly Killed Mutants

## Alive Mutants
  
Lines 7:13

```diff
	try:
	    from .StringMatcher import StringMatcher as SequenceMatcher
	except ImportError:
-	    if platform.python_implementation() != "PyPy":
+	    if False:
	        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
	    from difflib import SequenceMatcher
	

```  
Lines 7:13

```diff
	try:
	    from .StringMatcher import StringMatcher as SequenceMatcher
	except ImportError:
-	    if platform.python_implementation() != "PyPy":
+	    if True:
	        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
	    from difflib import SequenceMatcher
	

```  
Lines 7:13

```diff
	try:
	    from .StringMatcher import StringMatcher as SequenceMatcher
	except ImportError:
-	    if platform.python_implementation() != "PyPy":
+	    if (platform.python_implementation() < 'PyPy'):
	        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
	    from difflib import SequenceMatcher
	

```  
Lines 7:13

```diff
	try:
	    from .StringMatcher import StringMatcher as SequenceMatcher
	except ImportError:
-	    if platform.python_implementation() != "PyPy":
+	    if (platform.python_implementation() >= 'PyPy'):
	        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
	    from difflib import SequenceMatcher
	

```  
Lines 7:13

```diff
	try:
	    from .StringMatcher import StringMatcher as SequenceMatcher
	except ImportError:
-	    if platform.python_implementation() != "PyPy":
+	    if (platform.python_implementation() > 'PyPy'):
	        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
	    from difflib import SequenceMatcher
	

```  
Lines 7:13

```diff
	try:
	    from .StringMatcher import StringMatcher as SequenceMatcher
	except ImportError:
-	    if platform.python_implementation() != "PyPy":
+	    if (platform.python_implementation() == 'PyPy'):
	        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
	    from difflib import SequenceMatcher
	

```  
Lines 7:13

```diff
	try:
	    from .StringMatcher import StringMatcher as SequenceMatcher
	except ImportError:
-	    if platform.python_implementation() != "PyPy":
+	    if (platform.python_implementation() <= 'PyPy'):
	        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
	    from difflib import SequenceMatcher
	

```  
Lines 72:78

```diff
	# Advanced Scoring Functions #
	##############################
	
-	def _process_and_sort(s, force_ascii, full_process=True):
+	def _process_and_sort(s, force_ascii, full_process=(False)):
	    """Return a cleaned string with token sorted."""
	    # pull tokens
	    ts = utils.full_process(s, force_ascii=force_ascii) if full_process else s

```  
Lines 72:78

```diff
	# Advanced Scoring Functions #
	##############################
	
-	def _process_and_sort(s, force_ascii, full_process=True):
+	def _process_and_sort(s, force_ascii, full_process=None):
	    """Return a cleaned string with token sorted."""
	    # pull tokens
	    ts = utils.full_process(s, force_ascii=force_ascii) if full_process else s

```  
Lines 88:94

```diff
	#   sort those tokens and take ratio of resulting joined strings
	#   controls for unordered string elements
	@utils.check_for_none
-	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_sort(s1, s2, partial=(False), force_ascii=True, full_process=True):
	    sorted1 = _process_and_sort(s1, force_ascii, full_process=full_process)
	    sorted2 = _process_and_sort(s2, force_ascii, full_process=full_process)
	

```  
Lines 88:94

```diff
	#   sort those tokens and take ratio of resulting joined strings
	#   controls for unordered string elements
	@utils.check_for_none
-	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_sort(s1, s2, partial=None, force_ascii=True, full_process=True):
	    sorted1 = _process_and_sort(s1, force_ascii, full_process=full_process)
	    sorted2 = _process_and_sort(s2, force_ascii, full_process=full_process)
	

```  
Lines 88:94

```diff
	#   sort those tokens and take ratio of resulting joined strings
	#   controls for unordered string elements
	@utils.check_for_none
-	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_sort(s1, s2, partial=True, force_ascii=(False), full_process=True):
	    sorted1 = _process_and_sort(s1, force_ascii, full_process=full_process)
	    sorted2 = _process_and_sort(s2, force_ascii, full_process=full_process)
	

```  
Lines 88:94

```diff
	#   sort those tokens and take ratio of resulting joined strings
	#   controls for unordered string elements
	@utils.check_for_none
-	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_sort(s1, s2, partial=True, force_ascii=None, full_process=True):
	    sorted1 = _process_and_sort(s1, force_ascii, full_process=full_process)
	    sorted2 = _process_and_sort(s2, force_ascii, full_process=full_process)
	

```  
Lines 88:94

```diff
	#   sort those tokens and take ratio of resulting joined strings
	#   controls for unordered string elements
	@utils.check_for_none
-	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=(False)):
	    sorted1 = _process_and_sort(s1, force_ascii, full_process=full_process)
	    sorted2 = _process_and_sort(s2, force_ascii, full_process=full_process)
	

```  
Lines 88:94

```diff
	#   sort those tokens and take ratio of resulting joined strings
	#   controls for unordered string elements
	@utils.check_for_none
-	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_sort(s1, s2, partial=True, force_ascii=True, full_process=None):
	    sorted1 = _process_and_sort(s1, force_ascii, full_process=full_process)
	    sorted2 = _process_and_sort(s2, force_ascii, full_process=full_process)
	

```  
Lines 98:104

```diff
	        return ratio(sorted1, sorted2)
	
	
-	def token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_sort_ratio(s1, s2, force_ascii=(False), full_process=True):
	    """Return a measure of the sequences' similarity between 0 and 100
	    but sorting the token before comparing.
	    """

```  
Lines 98:104

```diff
	        return ratio(sorted1, sorted2)
	
	
-	def token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_sort_ratio(s1, s2, force_ascii=None, full_process=True):
	    """Return a measure of the sequences' similarity between 0 and 100
	    but sorting the token before comparing.
	    """

```  
Lines 98:104

```diff
	        return ratio(sorted1, sorted2)
	
	
-	def token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_sort_ratio(s1, s2, force_ascii=True, full_process=(False)):
	    """Return a measure of the sequences' similarity between 0 and 100
	    but sorting the token before comparing.
	    """

```  
Lines 98:104

```diff
	        return ratio(sorted1, sorted2)
	
	
-	def token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_sort_ratio(s1, s2, force_ascii=True, full_process=None):
	    """Return a measure of the sequences' similarity between 0 and 100
	    but sorting the token before comparing.
	    """

```  
Lines 105:111

```diff
	    return _token_sort(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=(False)):
	    """Return the ratio of the most similar substring as a number between
	    0 and 100 but sorting the token before comparing.
	    """

```  
Lines 105:111

```diff
	    return _token_sort(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=None):
	    """Return the ratio of the most similar substring as a number between
	    0 and 100 but sorting the token before comparing.
	    """

```  
Lines 105:111

```diff
	    return _token_sort(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_sort_ratio(s1, s2, force_ascii=(False), full_process=True):
	    """Return the ratio of the most similar substring as a number between
	    0 and 100 but sorting the token before comparing.
	    """

```  
Lines 105:111

```diff
	    return _token_sort(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_sort_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_sort_ratio(s1, s2, force_ascii=None, full_process=True):
	    """Return the ratio of the most similar substring as a number between
	    0 and 100 but sorting the token before comparing.
	    """

```  
Lines 113:119

```diff
	
	
	@utils.check_for_none
-	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=(False)):
	    """Find all alphanumeric tokens in each string...
	        - treat them as a set
	        - construct two strings of the form:

```  
Lines 113:119

```diff
	
	
	@utils.check_for_none
-	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=None):
	    """Find all alphanumeric tokens in each string...
	        - treat them as a set
	        - construct two strings of the form:

```  
Lines 113:119

```diff
	
	
	@utils.check_for_none
-	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_set(s1, s2, partial=True, force_ascii=(False), full_process=True):
	    """Find all alphanumeric tokens in each string...
	        - treat them as a set
	        - construct two strings of the form:

```  
Lines 113:119

```diff
	
	
	@utils.check_for_none
-	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_set(s1, s2, partial=True, force_ascii=None, full_process=True):
	    """Find all alphanumeric tokens in each string...
	        - treat them as a set
	        - construct two strings of the form:

```  
Lines 113:119

```diff
	
	
	@utils.check_for_none
-	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_set(s1, s2, partial=(False), force_ascii=True, full_process=True):
	    """Find all alphanumeric tokens in each string...
	        - treat them as a set
	        - construct two strings of the form:

```  
Lines 113:119

```diff
	
	
	@utils.check_for_none
-	def _token_set(s1, s2, partial=True, force_ascii=True, full_process=True):
+	def _token_set(s1, s2, partial=None, force_ascii=True, full_process=True):
	    """Find all alphanumeric tokens in each string...
	        - treat them as a set
	        - construct two strings of the form:

```  
Lines 165:171

```diff
	    return max(pairwise)
	
	
-	def token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_set_ratio(s1, s2, force_ascii=True, full_process=(False)):
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 165:171

```diff
	    return max(pairwise)
	
	
-	def token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_set_ratio(s1, s2, force_ascii=True, full_process=None):
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 165:171

```diff
	    return max(pairwise)
	
	
-	def token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_set_ratio(s1, s2, force_ascii=(False), full_process=True):
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 165:171

```diff
	    return max(pairwise)
	
	
-	def token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def token_set_ratio(s1, s2, force_ascii=None, full_process=True):
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 169:175

```diff
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_set_ratio(s1, s2, force_ascii=(False), full_process=True):
	    return _token_set(s1, s2, partial=True, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 169:175

```diff
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_set_ratio(s1, s2, force_ascii=None, full_process=True):
	    return _token_set(s1, s2, partial=True, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 169:175

```diff
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=(False)):
	    return _token_set(s1, s2, partial=True, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 169:175

```diff
	    return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)
	
	
-	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=True):
+	def partial_token_set_ratio(s1, s2, force_ascii=True, full_process=None):
	    return _token_set(s1, s2, partial=True, force_ascii=force_ascii, full_process=full_process)
	
	

```  
Lines 178:184

```diff
	###################
	
	# q is for quick
-	def QRatio(s1, s2, force_ascii=True, full_process=True):
+	def QRatio(s1, s2, force_ascii=True, full_process=(False)):
	    """
	    Quick ratio comparison between two strings.
	

```  
Lines 178:184

```diff
	###################
	
	# q is for quick
-	def QRatio(s1, s2, force_ascii=True, full_process=True):
+	def QRatio(s1, s2, force_ascii=True, full_process=None):
	    """
	    Quick ratio comparison between two strings.
	

```  
Lines 178:184

```diff
	###################
	
	# q is for quick
-	def QRatio(s1, s2, force_ascii=True, full_process=True):
+	def QRatio(s1, s2, force_ascii=(False), full_process=True):
	    """
	    Quick ratio comparison between two strings.
	

```  
Lines 178:184

```diff
	###################
	
	# q is for quick
-	def QRatio(s1, s2, force_ascii=True, full_process=True):
+	def QRatio(s1, s2, force_ascii=None, full_process=True):
	    """
	    Quick ratio comparison between two strings.
	

```  
Lines 207:213

```diff
	    return ratio(p1, p2)
	
	
-	def UQRatio(s1, s2, full_process=True):
+	def UQRatio(s1, s2, full_process=(False)):
	    """
	    Unicode quick ratio
	

```  
Lines 207:213

```diff
	    return ratio(p1, p2)
	
	
-	def UQRatio(s1, s2, full_process=True):
+	def UQRatio(s1, s2, full_process=None):
	    """
	    Unicode quick ratio
	

```  
Lines 221:227

```diff
	
	
	# w is for weighted
-	def WRatio(s1, s2, force_ascii=True, full_process=True):
+	def WRatio(s1, s2, force_ascii=(False), full_process=True):
	    """
	    Return a measure of the sequences' similarity between 0 and 100, using different algorithms.
	

```  
Lines 221:227

```diff
	
	
	# w is for weighted
-	def WRatio(s1, s2, force_ascii=True, full_process=True):
+	def WRatio(s1, s2, force_ascii=None, full_process=True):
	    """
	    Return a measure of the sequences' similarity between 0 and 100, using different algorithms.
	

```  
Lines 221:227

```diff
	
	
	# w is for weighted
-	def WRatio(s1, s2, force_ascii=True, full_process=True):
+	def WRatio(s1, s2, force_ascii=True, full_process=(False)):
	    """
	    Return a measure of the sequences' similarity between 0 and 100, using different algorithms.
	

```  
Lines 221:227

```diff
	
	
	# w is for weighted
-	def WRatio(s1, s2, force_ascii=True, full_process=True):
+	def WRatio(s1, s2, force_ascii=True, full_process=None):
	    """
	    Return a measure of the sequences' similarity between 0 and 100, using different algorithms.
	

```  
Lines 299:306

```diff
	        return utils.intr(max(base, tsor, tser))
	
	
-	def UWRatio(s1, s2, full_process=True):
+	def UWRatio(s1, s2, full_process=(False)):
	    """Return a measure of the sequences' similarity between 0 and 100,
	    using different algorithms. Same as WRatio but preserving unicode.
	    """
	    return WRatio(s1, s2, force_ascii=False, full_process=full_process)

```  
Lines 299:306

```diff
	        return utils.intr(max(base, tsor, tser))
	
	
-	def UWRatio(s1, s2, full_process=True):
+	def UWRatio(s1, s2, full_process=None):
	    """Return a measure of the sequences' similarity between 0 and 100,
	    using different algorithms. Same as WRatio but preserving unicode.
	    """
	    return WRatio(s1, s2, force_ascii=False, full_process=full_process)

```
# /home/ubuntu/projects/thefuzz/thefuzz/utils.py

## Newly Killed Mutants

## Alive Mutants
  
Lines 5:11

```diff
	from thefuzz.string_processing import StringProcessor
	
	
-	PY3 = sys.version_info[0] == 3
+	PY3 = (sys.version_info[0] < 3)
	
	
	def validate_string(s):

```  
Lines 5:11

```diff
	from thefuzz.string_processing import StringProcessor
	
	
-	PY3 = sys.version_info[0] == 3
+	PY3 = (sys.version_info[0] >= 3)
	
	
	def validate_string(s):

```  
Lines 5:11

```diff
	from thefuzz.string_processing import StringProcessor
	
	
-	PY3 = sys.version_info[0] == 3
+	PY3 = (sys.version_info[0] != 3)
	
	
	def validate_string(s):

```  
Lines 5:11

```diff
	from thefuzz.string_processing import StringProcessor
	
	
-	PY3 = sys.version_info[0] == 3
+	PY3 = (sys.version_info[0] > 3)
	
	
	def validate_string(s):

```  
Lines 5:11

```diff
	from thefuzz.string_processing import StringProcessor
	
	
-	PY3 = sys.version_info[0] == 3
+	PY3 = (sys.version_info[0] <= 3)
	
	
	def validate_string(s):

```  
Lines 5:11

```diff
	from thefuzz.string_processing import StringProcessor
	
	
-	PY3 = sys.version_info[0] == 3
+	PY3 = sys.version_info[<_ast.Constant object at 0x7f3fd8770820>] == 3
	
	
	def validate_string(s):

```  
Lines 5:11

```diff
	from thefuzz.string_processing import StringProcessor
	
	
-	PY3 = sys.version_info[0] == 3
+	PY3 = sys.version_info[<_ast.Constant object at 0x7f3fd87700a0>] == 3
	
	
	def validate_string(s):

```  
Lines 33:39

```diff
	def check_for_none(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if args[0] is None or args[1] is None:
+	        if args[0] is None or args[<_ast.Constant object at 0x7f3fc8d3c250>] is None:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 42:48

```diff
	def check_empty_string(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if len(args[0]) == 0 or len(args[1]) == 0:
+	        if len(args[0]) == 0 or (len(args[1]) <= 0):
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 42:48

```diff
	def check_empty_string(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if len(args[0]) == 0 or len(args[1]) == 0:
+	        if (len(args[0]) <= 0) or len(args[1]) == 0:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 42:48

```diff
	def check_empty_string(func):
	    @functools.wraps(func)
	    def decorator(*args, **kwargs):
-	        if len(args[0]) == 0 or len(args[1]) == 0:
+	        if len(args[0]) == 0 or len(args[<_ast.Constant object at 0x7f3fc8d3cc10>]) == 0:
	            return 0
	        return func(*args, **kwargs)
	    return decorator

```  
Lines 49:55

```diff
	
	
	bad_chars = str("").join([chr(i) for i in range(128, 256)])  # ascii dammit!
-	if PY3:
+	if False:
	    translation_table = dict((ord(c), None) for c in bad_chars)
	    unicode = str
	

```  
Lines 49:55

```diff
	
	
	bad_chars = str("").join([chr(i) for i in range(128, 256)])  # ascii dammit!
-	if PY3:
+	if True:
	    translation_table = dict((ord(c), None) for c in bad_chars)
	    unicode = str
	

```  
Lines 50:56

```diff
	
	bad_chars = str("").join([chr(i) for i in range(128, 256)])  # ascii dammit!
	if PY3:
-	    translation_table = dict((ord(c), None) for c in bad_chars)
+	    translation_table = dict((ord(c), (False)) for c in bad_chars)
	    unicode = str
	
	

```  
Lines 50:56

```diff
	
	bad_chars = str("").join([chr(i) for i in range(128, 256)])  # ascii dammit!
	if PY3:
-	    translation_table = dict((ord(c), None) for c in bad_chars)
+	    translation_table = dict((ord(c), (True)) for c in bad_chars)
	    unicode = str
	
	

```  
Lines 82:88

```diff
	        return unicode(s1), unicode(s2)
	
	
-	def full_process(s, force_ascii=False):
+	def full_process(s, force_ascii=(True)):
	    """Process string by
	        -- removing all but letters and numbers
	        -- trim whitespace

```  
Lines 82:88

```diff
	        return unicode(s1), unicode(s2)
	
	
-	def full_process(s, force_ascii=False):
+	def full_process(s, force_ascii=None):
	    """Process string by
	        -- removing all but letters and numbers
	        -- trim whitespace

```
# /home/ubuntu/projects/thefuzz/thefuzz/string_processing.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/thefuzz/thefuzz/StringMatcher.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/thefuzz/thefuzz/__init__.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/thefuzz/thefuzz/process.py

## Newly Killed Mutants

## Alive Mutants
