



# /home/ubuntu/projects/pj/pj/constants.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/pj/pj/parser.py

## Newly Killed Mutants

### test_nested_object_call_add_0_str_hlf_0_str_dbl_0
  
Lines 45:51

```diff
	        json_object[json_key] = json_value
	
	        t = tokens[0]
-	        if t == JSON_RIGHTBRACE:
+	        if True:
	            return json_object, tokens[1:]
	        elif t != JSON_COMMA:
	            raise Exception('Expected comma after pair in object, got: {}'.format(t))

```  
Lines 45:51

```diff
	        json_object[json_key] = json_value
	
	        t = tokens[0]
-	        if t == JSON_RIGHTBRACE:
+	        if (t <= JSON_RIGHTBRACE):
	            return json_object, tokens[1:]
	        elif t != JSON_COMMA:
	            raise Exception('Expected comma after pair in object, got: {}'.format(t))

```
### test_empty_object_str_hlf_0
  
Lines 57:63

```diff
	def parse(tokens, is_root=False):
	    t = tokens[0]
	
-	    if is_root and t != JSON_LEFTBRACE:
+	    if is_root and (t < JSON_LEFTBRACE):
	        raise Exception('Root must be an object')
	
	    if t == JSON_LEFTBRACKET:

```  
Lines 57:63

```diff
	def parse(tokens, is_root=False):
	    t = tokens[0]
	
-	    if is_root and t != JSON_LEFTBRACE:
+	    if False:
	        raise Exception('Root must be an object')
	
	    if t == JSON_LEFTBRACKET:

```
### test_basic_object_call_add_0_call_add_1_str_hlf_0
  
Lines 57:63

```diff
	def parse(tokens, is_root=False):
	    t = tokens[0]
	
-	    if is_root and t != JSON_LEFTBRACE:
+	    if is_root and (t > JSON_LEFTBRACE):
	        raise Exception('Root must be an object')
	
	    if t == JSON_LEFTBRACKET:

```
## Alive Mutants
  
Lines 13:19

```diff
	        json_array.append(json)
	
	        t = tokens[0]
-	        if t == JSON_RIGHTBRACKET:
+	        if (t >= JSON_RIGHTBRACKET):
	            return json_array, tokens[1:]
	        elif t != JSON_COMMA:
	            raise Exception('Expected comma after object in array')

```  
Lines 15:21

```diff
	        t = tokens[0]
	        if t == JSON_RIGHTBRACKET:
	            return json_array, tokens[1:]
-	        elif t != JSON_COMMA:
+	        elif (t < JSON_COMMA):
	            raise Exception('Expected comma after object in array')
	        else:
	            tokens = tokens[1:]

```  
Lines 15:21

```diff
	        t = tokens[0]
	        if t == JSON_RIGHTBRACKET:
	            return json_array, tokens[1:]
-	        elif t != JSON_COMMA:
+	        elif (t > JSON_COMMA):
	            raise Exception('Expected comma after object in array')
	        else:
	            tokens = tokens[1:]

```  
Lines 15:21

```diff
	        t = tokens[0]
	        if t == JSON_RIGHTBRACKET:
	            return json_array, tokens[1:]
-	        elif t != JSON_COMMA:
+	        elif False:
	            raise Exception('Expected comma after object in array')
	        else:
	            tokens = tokens[1:]

```  
Lines 27:33

```diff
	    json_object = {}
	
	    t = tokens[0]
-	    if t == JSON_RIGHTBRACE:
+	    if (t >= JSON_RIGHTBRACE):
	        return json_object, tokens[1:]
	
	    while True:

```  
Lines 28:34

```diff
	
	    t = tokens[0]
	    if t == JSON_RIGHTBRACE:
-	        return json_object, tokens[1:]
+	        return json_object, tokens[:]
	
	    while True:
	        json_key = tokens[0]

```  
Lines 28:34

```diff
	
	    t = tokens[0]
	    if t == JSON_RIGHTBRACE:
-	        return json_object, tokens[1:]
+	        return json_object, tokens[:1]
	
	    while True:
	        json_key = tokens[0]

```  
Lines 32:38

```diff
	
	    while True:
	        json_key = tokens[0]
-	        if type(json_key) is str:
+	        if True:
	            tokens = tokens[1:]
	        else:
	            raise Exception('Expected string key, got: {}'.format(json_key))

```  
Lines 37:43

```diff
	        else:
	            raise Exception('Expected string key, got: {}'.format(json_key))
	
-	        if tokens[0] != JSON_COLON:
+	        if (tokens[0] < JSON_COLON):
	            raise Exception('Expected colon after key in object, got: {}'.format(t))
	
	        json_value, tokens = parse(tokens[1:])

```  
Lines 37:43

```diff
	        else:
	            raise Exception('Expected string key, got: {}'.format(json_key))
	
-	        if tokens[0] != JSON_COLON:
+	        if (tokens[0] > JSON_COLON):
	            raise Exception('Expected colon after key in object, got: {}'.format(t))
	
	        json_value, tokens = parse(tokens[1:])

```  
Lines 37:43

```diff
	        else:
	            raise Exception('Expected string key, got: {}'.format(json_key))
	
-	        if tokens[0] != JSON_COLON:
+	        if False:
	            raise Exception('Expected colon after key in object, got: {}'.format(t))
	
	        json_value, tokens = parse(tokens[1:])

```  
Lines 44:50

```diff
	
	        json_object[json_key] = json_value
	
-	        t = tokens[0]
+	        t = tokens[<_ast.UnaryOp object at 0x7f14055737c0>]
	        if t == JSON_RIGHTBRACE:
	            return json_object, tokens[1:]
	        elif t != JSON_COMMA:

```  
Lines 45:51

```diff
	        json_object[json_key] = json_value
	
	        t = tokens[0]
-	        if t == JSON_RIGHTBRACE:
+	        if (t >= JSON_RIGHTBRACE):
	            return json_object, tokens[1:]
	        elif t != JSON_COMMA:
	            raise Exception('Expected comma after pair in object, got: {}'.format(t))

```  
Lines 46:52

```diff
	
	        t = tokens[0]
	        if t == JSON_RIGHTBRACE:
-	            return json_object, tokens[1:]
+	            return json_object, tokens[:]
	        elif t != JSON_COMMA:
	            raise Exception('Expected comma after pair in object, got: {}'.format(t))
	

```  
Lines 46:52

```diff
	
	        t = tokens[0]
	        if t == JSON_RIGHTBRACE:
-	            return json_object, tokens[1:]
+	            return json_object, tokens[:1]
	        elif t != JSON_COMMA:
	            raise Exception('Expected comma after pair in object, got: {}'.format(t))
	

```  
Lines 47:53

```diff
	        t = tokens[0]
	        if t == JSON_RIGHTBRACE:
	            return json_object, tokens[1:]
-	        elif t != JSON_COMMA:
+	        elif (t < JSON_COMMA):
	            raise Exception('Expected comma after pair in object, got: {}'.format(t))
	
	        tokens = tokens[1:]

```  
Lines 47:53

```diff
	        t = tokens[0]
	        if t == JSON_RIGHTBRACE:
	            return json_object, tokens[1:]
-	        elif t != JSON_COMMA:
+	        elif (t >= JSON_COMMA):
	            raise Exception('Expected comma after pair in object, got: {}'.format(t))
	
	        tokens = tokens[1:]

```  
Lines 47:53

```diff
	        t = tokens[0]
	        if t == JSON_RIGHTBRACE:
	            return json_object, tokens[1:]
-	        elif t != JSON_COMMA:
+	        elif (t > JSON_COMMA):
	            raise Exception('Expected comma after pair in object, got: {}'.format(t))
	
	        tokens = tokens[1:]

```  
Lines 47:53

```diff
	        t = tokens[0]
	        if t == JSON_RIGHTBRACE:
	            return json_object, tokens[1:]
-	        elif t != JSON_COMMA:
+	        elif (t == JSON_COMMA):
	            raise Exception('Expected comma after pair in object, got: {}'.format(t))
	
	        tokens = tokens[1:]

```  
Lines 47:53

```diff
	        t = tokens[0]
	        if t == JSON_RIGHTBRACE:
	            return json_object, tokens[1:]
-	        elif t != JSON_COMMA:
+	        elif (t <= JSON_COMMA):
	            raise Exception('Expected comma after pair in object, got: {}'.format(t))
	
	        tokens = tokens[1:]

```  
Lines 47:53

```diff
	        t = tokens[0]
	        if t == JSON_RIGHTBRACE:
	            return json_object, tokens[1:]
-	        elif t != JSON_COMMA:
+	        elif True:
	            raise Exception('Expected comma after pair in object, got: {}'.format(t))
	
	        tokens = tokens[1:]

```  
Lines 47:53

```diff
	        t = tokens[0]
	        if t == JSON_RIGHTBRACE:
	            return json_object, tokens[1:]
-	        elif t != JSON_COMMA:
+	        elif False:
	            raise Exception('Expected comma after pair in object, got: {}'.format(t))
	
	        tokens = tokens[1:]

```  
Lines 54:60

```diff
	
	    raise Exception('Expected end-of-object bracket')
	
-	def parse(tokens, is_root=False):
+	def parse(tokens, is_root=None):
	    t = tokens[0]
	
	    if is_root and t != JSON_LEFTBRACE:

```
# /home/ubuntu/projects/pj/pj/lexer.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/pj/pj/__init__.py

## Newly Killed Mutants

## Alive Mutants
