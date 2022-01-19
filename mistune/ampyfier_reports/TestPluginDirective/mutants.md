



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
Lines 27:33

```diff
	
	
	def escape_html(s):
-	    if html is not None:
+	    if html is not (False):
	        return html.escape(html.unescape(s)).replace('&#x27;', "'")
	    return escape(s)
	

```  
Lines 27:33

```diff
	
	
	def escape_html(s):
-	    if html is not None:
+	    if html is not (True):
	        return html.escape(html.unescape(s)).replace('&#x27;', "'")
	    return escape(s)
	

```  
Lines 27:33

```diff
	
	
	def escape_html(s):
-	    if html is not None:
+	    if False:
	        return html.escape(html.unescape(s)).replace('&#x27;', "'")
	    return escape(s)
	

```  
Lines 27:33

```diff
	
	
	def escape_html(s):
-	    if html is not None:
+	    if True:
	        return html.escape(html.unescape(s)).replace('&#x27;', "'")
	    return escape(s)
	

```  
Lines 27:33

```diff
	
	
	def escape_html(s):
-	    if html is not None:
+	    if (html is None):
	        return html.escape(html.unescape(s)).replace('&#x27;', "'")
	    return escape(s)
	

```
# /home/ubuntu/projects/mistune/mistune/scanner.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/mistune/mistune/renderers.py

## Newly Killed Mutants

### test_html_include_bool_inv_0_none_4
  
Lines 200:206

```diff
	    def block_html(self, html):
	        if not self._escape:
	            return html + '\n'
-	        return '<p>' + escape(html) + '</p>\n'
+	        return ('<p>' * escape(html)) + '</p>\n'
	
	    def block_error(self, html):
	        return '<div class="error">' + html + '</div>\n'

```  
Lines 200:206

```diff
	    def block_html(self, html):
	        if not self._escape:
	            return html + '\n'
-	        return '<p>' + escape(html) + '</p>\n'
+	        return ('<p>' % escape(html)) + '</p>\n'
	
	    def block_error(self, html):
	        return '<div class="error">' + html + '</div>\n'

```  
Lines 200:206

```diff
	    def block_html(self, html):
	        if not self._escape:
	            return html + '\n'
-	        return '<p>' + escape(html) + '</p>\n'
+	        return ('<p>' - escape(html)) + '</p>\n'
	
	    def block_error(self, html):
	        return '<div class="error">' + html + '</div>\n'

```  
Lines 200:206

```diff
	    def block_html(self, html):
	        if not self._escape:
	            return html + '\n'
-	        return '<p>' + escape(html) + '</p>\n'
+	        return ('<p>' / escape(html)) + '</p>\n'
	
	    def block_error(self, html):
	        return '<div class="error">' + html + '</div>\n'

```  
Lines 200:206

```diff
	    def block_html(self, html):
	        if not self._escape:
	            return html + '\n'
-	        return '<p>' + escape(html) + '</p>\n'
+	        return ('<p>' ** escape(html)) + '</p>\n'
	
	    def block_error(self, html):
	        return '<div class="error">' + html + '</div>\n'

```  
Lines 200:206

```diff
	    def block_html(self, html):
	        if not self._escape:
	            return html + '\n'
-	        return '<p>' + escape(html) + '</p>\n'
+	        return ('<p>' // escape(html)) + '</p>\n'
	
	    def block_error(self, html):
	        return '<div class="error">' + html + '</div>\n'

```  
Lines 200:206

```diff
	    def block_html(self, html):
	        if not self._escape:
	            return html + '\n'
-	        return '<p>' + escape(html) + '</p>\n'
+	        return (('<p>' + escape(html)) * '</p>\n')
	
	    def block_error(self, html):
	        return '<div class="error">' + html + '</div>\n'

```  
Lines 200:206

```diff
	    def block_html(self, html):
	        if not self._escape:
	            return html + '\n'
-	        return '<p>' + escape(html) + '</p>\n'
+	        return (('<p>' + escape(html)) % '</p>\n')
	
	    def block_error(self, html):
	        return '<div class="error">' + html + '</div>\n'

```  
Lines 200:206

```diff
	    def block_html(self, html):
	        if not self._escape:
	            return html + '\n'
-	        return '<p>' + escape(html) + '</p>\n'
+	        return ('<p>' + escape(html) - '</p>\n')
	
	    def block_error(self, html):
	        return '<div class="error">' + html + '</div>\n'

```  
Lines 200:206

```diff
	    def block_html(self, html):
	        if not self._escape:
	            return html + '\n'
-	        return '<p>' + escape(html) + '</p>\n'
+	        return (('<p>' + escape(html)) / '</p>\n')
	
	    def block_error(self, html):
	        return '<div class="error">' + html + '</div>\n'

```  
Lines 200:206

```diff
	    def block_html(self, html):
	        if not self._escape:
	            return html + '\n'
-	        return '<p>' + escape(html) + '</p>\n'
+	        return (('<p>' + escape(html)) ** '</p>\n')
	
	    def block_error(self, html):
	        return '<div class="error">' + html + '</div>\n'

```  
Lines 200:206

```diff
	    def block_html(self, html):
	        if not self._escape:
	            return html + '\n'
-	        return '<p>' + escape(html) + '</p>\n'
+	        return (('<p>' + escape(html)) // '</p>\n')
	
	    def block_error(self, html):
	        return '<div class="error">' + html + '</div>\n'

```
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
