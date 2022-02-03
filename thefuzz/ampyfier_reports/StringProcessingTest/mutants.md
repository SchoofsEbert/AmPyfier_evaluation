



# /home/ebert/projects/thefuzz/thefuzz/string_processing.py

## Newly Killed Mutants

## Alive Mutants
  
Lines 3:9

```diff
	import string
	import sys
	
-	PY3 = sys.version_info[0] == 3
+	PY3 = (sys.version_info[0] >= 3)
	if PY3:
	    string = str
	

```  
Lines 3:9

```diff
	import string
	import sys
	
-	PY3 = sys.version_info[0] == 3
+	PY3 = (sys.version_info[0] <= 3)
	if PY3:
	    string = str
	

```  
Lines 4:10

```diff
	import sys
	
	PY3 = sys.version_info[0] == 3
-	if PY3:
+	if True:
	    string = str
	
	

```