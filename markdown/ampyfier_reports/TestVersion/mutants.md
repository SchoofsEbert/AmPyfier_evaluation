



# /home/ubuntu/projects/markdown/markdown/__meta__.py

## Newly Killed Mutants

### test_get_version_numb_sub_10
  
Lines 34:40

```diff
	    assert len(version_info) == 5
	    assert version_info[3] in ('dev', 'alpha', 'beta', 'rc', 'final')
	
-	    parts = 2 if version_info[2] == 0 else 3
+	    parts = 2 if (version_info[2] <= 0) else 3
	    v = '.'.join(map(str, version_info[:parts]))
	
	    if version_info[3] == 'dev':

```
## Alive Mutants
  
Lines 31:37

```diff
	
	def _get_version(version_info):
	    " Returns a PEP 440-compliant version number from version_info. "
-	    assert len(version_info) == 5
+	    assert (len(version_info) <= 5)
	    assert version_info[3] in ('dev', 'alpha', 'beta', 'rc', 'final')
	
	    parts = 2 if version_info[2] == 0 else 3

```  
Lines 31:37

```diff
	
	def _get_version(version_info):
	    " Returns a PEP 440-compliant version number from version_info. "
-	    assert len(version_info) == 5
+	    assert (len(version_info) >= 5)
	    assert version_info[3] in ('dev', 'alpha', 'beta', 'rc', 'final')
	
	    parts = 2 if version_info[2] == 0 else 3

```  
Lines 38:44

```diff
	    v = '.'.join(map(str, version_info[:parts]))
	
	    if version_info[3] == 'dev':
-	        v += '.dev' + str(version_info[4])
+	        v += '.dev' + str(version_info[<_ast.Constant object at 0x7fa90c89f2b0>])
	    elif version_info[3] != 'final':
	        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'rc'}
	        v += mapping[version_info[3]] + str(version_info[4])

```  
Lines 41:47

```diff
	        v += '.dev' + str(version_info[4])
	    elif version_info[3] != 'final':
	        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'rc'}
-	        v += mapping[version_info[3]] + str(version_info[4])
+	        v += mapping[version_info[3]] + str(version_info[<_ast.Constant object at 0x7fa90b2d1fd0>])
	
	    return v
	

```