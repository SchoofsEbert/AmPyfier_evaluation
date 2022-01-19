



# /home/ubuntu/projects/mistune/mistune/util.py

## Newly Killed Mutants

## Alive Mutants
  
Lines 10:16

```diff
	ESCAPE_TEXT = r'\\[' + PUNCTUATION + ']'
	
	
-	def escape(s, quote=True):
+	def escape(s, quote=(False)):
	    s = s.replace("&", "&amp;")
	    s = s.replace("<", "&lt;")
	    s = s.replace(">", "&gt;")

```  
Lines 10:16

```diff
	ESCAPE_TEXT = r'\\[' + PUNCTUATION + ']'
	
	
-	def escape(s, quote=True):
+	def escape(s, quote=None):
	    s = s.replace("&", "&amp;")
	    s = s.replace("<", "&lt;")
	    s = s.replace(">", "&gt;")

```  
Lines 14:20

```diff
	    s = s.replace("&", "&amp;")
	    s = s.replace("<", "&lt;")
	    s = s.replace(">", "&gt;")
-	    if quote:
+	    if False:
	        s = s.replace('"', "&quot;")
	    return s
	

```  
Lines 14:20

```diff
	    s = s.replace("&", "&amp;")
	    s = s.replace("<", "&lt;")
	    s = s.replace(">", "&gt;")
-	    if quote:
+	    if True:
	        s = s.replace('"', "&quot;")
	    return s
	

```
# /home/ubuntu/projects/mistune/mistune/scanner.py

## Newly Killed Mutants

## Alive Mutants
  
Lines 85:91

```diff
	        m = self.PARAGRAPH_END.search(string, pos)
	        if not m:
	            return None
-	        if set(m.group(0)) == {'\n'}:
+	        if (set(m.group(0)) < {'\n'}):
	            return m.end()
	        return m.start() + 1
	

```  
Lines 85:91

```diff
	        m = self.PARAGRAPH_END.search(string, pos)
	        if not m:
	            return None
-	        if set(m.group(0)) == {'\n'}:
+	        if (set(m.group(0)) >= {'\n'}):
	            return m.end()
	        return m.start() + 1
	

```  
Lines 85:91

```diff
	        m = self.PARAGRAPH_END.search(string, pos)
	        if not m:
	            return None
-	        if set(m.group(0)) == {'\n'}:
+	        if (set(m.group(0)) != {'\n'}):
	            return m.end()
	        return m.start() + 1
	

```  
Lines 85:91

```diff
	        m = self.PARAGRAPH_END.search(string, pos)
	        if not m:
	            return None
-	        if set(m.group(0)) == {'\n'}:
+	        if (set(m.group(0)) > {'\n'}):
	            return m.end()
	        return m.start() + 1
	

```  
Lines 85:91

```diff
	        m = self.PARAGRAPH_END.search(string, pos)
	        if not m:
	            return None
-	        if set(m.group(0)) == {'\n'}:
+	        if (set(m.group(0)) <= {'\n'}):
	            return m.end()
	        return m.start() + 1
	

```  
Lines 85:91

```diff
	        m = self.PARAGRAPH_END.search(string, pos)
	        if not m:
	            return None
-	        if set(m.group(0)) == {'\n'}:
+	        if False:
	            return m.end()
	        return m.start() + 1
	

```  
Lines 85:91

```diff
	        m = self.PARAGRAPH_END.search(string, pos)
	        if not m:
	            return None
-	        if set(m.group(0)) == {'\n'}:
+	        if True:
	            return m.end()
	        return m.start() + 1
	

```
# /home/ubuntu/projects/mistune/mistune/renderers.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/mistune/mistune/block_parser.py

## Newly Killed Mutants

## Alive Mutants
  
Lines 102:108

```diff
	        self.list_rules = list(self.RULE_NAMES)
	
	    def parse_newline(self, m, state):
-	        return {'type': 'newline', 'blank': True}
+	        return {'type': 'newline', 'blank': (False)}
	
	    def parse_thematic_break(self, m, state):
	        return {'type': 'thematic_break', 'blank': True}

```  
Lines 102:108

```diff
	        self.list_rules = list(self.RULE_NAMES)
	
	    def parse_newline(self, m, state):
-	        return {'type': 'newline', 'blank': True}
+	        return {'type': 'newline', 'blank': None}
	
	    def parse_thematic_break(self, m, state):
	        return {'type': 'thematic_break', 'blank': True}

```
# /home/ubuntu/projects/mistune/mistune/__init__.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/mistune/mistune/markdown.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/mistune/mistune/inline_parser.py

## Newly Killed Mutants

## Alive Mutants
