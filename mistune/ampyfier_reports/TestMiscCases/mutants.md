



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
Lines 21:27

```diff
	
	def escape_url(link):
	    safe = '/#:()*?=%@+,&'
-	    if html is None:
+	    if (html is not None):
	        return quote(link.encode('utf-8'), safe=safe)
	    return html.escape(quote(html.unescape(link), safe=safe))
	

```  
Lines 21:27

```diff
	
	def escape_url(link):
	    safe = '/#:()*?=%@+,&'
-	    if html is None:
+	    if False:
	        return quote(link.encode('utf-8'), safe=safe)
	    return html.escape(quote(html.unescape(link), safe=safe))
	

```  
Lines 21:27

```diff
	
	def escape_url(link):
	    safe = '/#:()*?=%@+,&'
-	    if html is None:
+	    if True:
	        return quote(link.encode('utf-8'), safe=safe)
	    return html.escape(quote(html.unescape(link), safe=safe))
	

```  
Lines 21:27

```diff
	
	def escape_url(link):
	    safe = '/#:()*?=%@+,&'
-	    if html is None:
+	    if html is (False):
	        return quote(link.encode('utf-8'), safe=safe)
	    return html.escape(quote(html.unescape(link), safe=safe))
	

```  
Lines 21:27

```diff
	
	def escape_url(link):
	    safe = '/#:()*?=%@+,&'
-	    if html is None:
+	    if html is (True):
	        return quote(link.encode('utf-8'), safe=safe)
	    return html.escape(quote(html.unescape(link), safe=safe))
	

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
  
Lines 6:12

```diff
	
	        pos = 0
	        for match in iter(sc.search, None):
-	            name, method = self.lexicon[match.lastindex - 1][1]
+	            name, method = self.lexicon[match.lastindex - 1][<_ast.Constant object at 0x7f23354c3340>]
	            hole = string[pos:match.start()]
	            if hole:
	                yield parse_text(hole, state)

```  
Lines 8:14

```diff
	        for match in iter(sc.search, None):
	            name, method = self.lexicon[match.lastindex - 1][1]
	            hole = string[pos:match.start()]
-	            if hole:
+	            if True:
	                yield parse_text(hole, state)
	
	            yield method(match, state)

```  
Lines 15:21

```diff
	            pos = match.end()
	
	        hole = string[pos:]
-	        if hole:
+	        if True:
	            yield parse_text(hole, state)
	
	

```  
Lines 38:44

```diff
	
	    def get_rule_method(self, name):
	        if name not in self.RULE_NAMES:
-	            return self.rule_methods[name][1]
+	            return self.rule_methods[name][<_ast.Constant object at 0x7f23351657f0>]
	        return getattr(self, 'parse_' + name)
	
	    def parse_text(self, text, state):

```  
Lines 38:44

```diff
	
	    def get_rule_method(self, name):
	        if name not in self.RULE_NAMES:
-	            return self.rule_methods[name][1]
+	            return self.rule_methods[name][<_ast.Constant object at 0x7f23351c7790>]
	        return getattr(self, 'parse_' + name)
	
	    def parse_text(self, text, state):

```  
Lines 50:56

```diff
	            if isinstance(tok, list):
	                for t in tok:
	                    yield t
-	            elif tok:
+	            elif True:
	                yield tok
	
	    def _create_scanner(self, rules):

```  
Lines 56:62

```diff
	    def _create_scanner(self, rules):
	        sc_key = '|'.join(rules)
	        sc = self._cached_sc.get(sc_key)
-	        if sc:
+	        if False:
	            return sc
	
	        lexicon = [

```  
Lines 83:89

```diff
	
	    def search_pos(self, string, pos):
	        m = self.PARAGRAPH_END.search(string, pos)
-	        if not m:
+	        if True:
	            return None
	        if set(m.group(0)) == {'\n'}:
	            return m.end()

```  
Lines 94:100

```diff
	        endpos = len(string)
	        last_end = 0
	        while 1:
-	            if pos >= endpos:
+	            if (pos < endpos):
	                break
	            for rule, (name, method) in self.lexicon:
	                match = rule.match(string, pos)

```  
Lines 94:100

```diff
	        endpos = len(string)
	        last_end = 0
	        while 1:
-	            if pos >= endpos:
+	            if (pos != endpos):
	                break
	            for rule, (name, method) in self.lexicon:
	                match = rule.match(string, pos)

```  
Lines 94:100

```diff
	        endpos = len(string)
	        last_end = 0
	        while 1:
-	            if pos >= endpos:
+	            if (pos > endpos):
	                break
	            for rule, (name, method) in self.lexicon:
	                match = rule.match(string, pos)

```  
Lines 94:100

```diff
	        endpos = len(string)
	        last_end = 0
	        while 1:
-	            if pos >= endpos:
+	            if (pos == endpos):
	                break
	            for rule, (name, method) in self.lexicon:
	                match = rule.match(string, pos)

```  
Lines 94:100

```diff
	        endpos = len(string)
	        last_end = 0
	        while 1:
-	            if pos >= endpos:
+	            if (pos <= endpos):
	                break
	            for rule, (name, method) in self.lexicon:
	                match = rule.match(string, pos)

```  
Lines 94:100

```diff
	        endpos = len(string)
	        last_end = 0
	        while 1:
-	            if pos >= endpos:
+	            if False:
	                break
	            for rule, (name, method) in self.lexicon:
	                match = rule.match(string, pos)

```  
Lines 94:100

```diff
	        endpos = len(string)
	        last_end = 0
	        while 1:
-	            if pos >= endpos:
+	            if True:
	                break
	            for rule, (name, method) in self.lexicon:
	                match = rule.match(string, pos)

```  
Lines 98:104

```diff
	                break
	            for rule, (name, method) in self.lexicon:
	                match = rule.match(string, pos)
-	                if match is not None:
+	                if False:
	                    start, end = match.span()
	                    if start > last_end:
	                        yield parse_text(string[last_end:start], state)

```  
Lines 100:106

```diff
	                match = rule.match(string, pos)
	                if match is not None:
	                    start, end = match.span()
-	                    if start > last_end:
+	                    if (start < last_end):
	                        yield parse_text(string[last_end:start], state)
	
	                    if name.endswith('_start'):

```  
Lines 100:106

```diff
	                match = rule.match(string, pos)
	                if match is not None:
	                    start, end = match.span()
-	                    if start > last_end:
+	                    if (start >= last_end):
	                        yield parse_text(string[last_end:start], state)
	
	                    if name.endswith('_start'):

```  
Lines 100:106

```diff
	                match = rule.match(string, pos)
	                if match is not None:
	                    start, end = match.span()
-	                    if start > last_end:
+	                    if (start != last_end):
	                        yield parse_text(string[last_end:start], state)
	
	                    if name.endswith('_start'):

```  
Lines 100:106

```diff
	                match = rule.match(string, pos)
	                if match is not None:
	                    start, end = match.span()
-	                    if start > last_end:
+	                    if (start == last_end):
	                        yield parse_text(string[last_end:start], state)
	
	                    if name.endswith('_start'):

```  
Lines 100:106

```diff
	                match = rule.match(string, pos)
	                if match is not None:
	                    start, end = match.span()
-	                    if start > last_end:
+	                    if (start <= last_end):
	                        yield parse_text(string[last_end:start], state)
	
	                    if name.endswith('_start'):

```  
Lines 100:106

```diff
	                match = rule.match(string, pos)
	                if match is not None:
	                    start, end = match.span()
-	                    if start > last_end:
+	                    if False:
	                        yield parse_text(string[last_end:start], state)
	
	                    if name.endswith('_start'):

```  
Lines 100:106

```diff
	                match = rule.match(string, pos)
	                if match is not None:
	                    start, end = match.span()
-	                    if start > last_end:
+	                    if True:
	                        yield parse_text(string[last_end:start], state)
	
	                    if name.endswith('_start'):

```  
Lines 103:109

```diff
	                    if start > last_end:
	                        yield parse_text(string[last_end:start], state)
	
-	                    if name.endswith('_start'):
+	                    if False:
	                        token = method(match, state, string)
	                        yield token[0]
	                        end = token[1]

```  
Lines 113:119

```diff
	                    break
	            else:
	                found = self.search_pos(string, pos)
-	                if found is None:
+	                if True:
	                    break
	                pos = found
	

```  
Lines 117:121

```diff
	                    break
	                pos = found
	
-	        if last_end < endpos:
+	        if (last_end != endpos):
	            yield parse_text(string[last_end:], state)

```  
Lines 117:121

```diff
	                    break
	                pos = found
	
-	        if last_end < endpos:
+	        if (last_end <= endpos):
	            yield parse_text(string[last_end:], state)

```  
Lines 117:121

```diff
	                    break
	                pos = found
	
-	        if last_end < endpos:
+	        if True:
	            yield parse_text(string[last_end:], state)

```  
Lines 118:121

```diff
	                pos = found
	
	        if last_end < endpos:
-	            yield parse_text(string[last_end:], state)
+	            yield parse_text(string[:], state)
	
```
# /home/ubuntu/projects/mistune/mistune/renderers.py

## Newly Killed Mutants

### test_escape_html_none_4_bool_inv_0
  
Lines 199:205

```diff
	
	    def block_html(self, html):
	        if not self._escape:
-	            return html + '\n'
+	            return (html * '\n')
	        return '<p>' + escape(html) + '</p>\n'
	
	    def block_error(self, html):

```  
Lines 199:205

```diff
	
	    def block_html(self, html):
	        if not self._escape:
-	            return html + '\n'
+	            return (html % '\n')
	        return '<p>' + escape(html) + '</p>\n'
	
	    def block_error(self, html):

```  
Lines 199:205

```diff
	
	    def block_html(self, html):
	        if not self._escape:
-	            return html + '\n'
+	            return (html - '\n')
	        return '<p>' + escape(html) + '</p>\n'
	
	    def block_error(self, html):

```  
Lines 199:205

```diff
	
	    def block_html(self, html):
	        if not self._escape:
-	            return html + '\n'
+	            return (html / '\n')
	        return '<p>' + escape(html) + '</p>\n'
	
	    def block_error(self, html):

```  
Lines 199:205

```diff
	
	    def block_html(self, html):
	        if not self._escape:
-	            return html + '\n'
+	            return (html ** '\n')
	        return '<p>' + escape(html) + '</p>\n'
	
	    def block_error(self, html):

```  
Lines 199:205

```diff
	
	    def block_html(self, html):
	        if not self._escape:
-	            return html + '\n'
+	            return (html // '\n')
	        return '<p>' + escape(html) + '</p>\n'
	
	    def block_error(self, html):

```
### test_escape_html_none_4_str_hlf_0
  
Lines 195:201

```diff
	        return html + '>' + escape(code) + '</code></pre>\n'
	
	    def block_quote(self, text):
-	        return '<blockquote>\n' + text + '</blockquote>\n'
+	        return ('<blockquote>\n' * text) + '</blockquote>\n'
	
	    def block_html(self, html):
	        if not self._escape:

```  
Lines 195:201

```diff
	        return html + '>' + escape(code) + '</code></pre>\n'
	
	    def block_quote(self, text):
-	        return '<blockquote>\n' + text + '</blockquote>\n'
+	        return ('<blockquote>\n' % text) + '</blockquote>\n'
	
	    def block_html(self, html):
	        if not self._escape:

```  
Lines 195:201

```diff
	        return html + '>' + escape(code) + '</code></pre>\n'
	
	    def block_quote(self, text):
-	        return '<blockquote>\n' + text + '</blockquote>\n'
+	        return ('<blockquote>\n' - text) + '</blockquote>\n'
	
	    def block_html(self, html):
	        if not self._escape:

```  
Lines 195:201

```diff
	        return html + '>' + escape(code) + '</code></pre>\n'
	
	    def block_quote(self, text):
-	        return '<blockquote>\n' + text + '</blockquote>\n'
+	        return ('<blockquote>\n' / text) + '</blockquote>\n'
	
	    def block_html(self, html):
	        if not self._escape:

```  
Lines 195:201

```diff
	        return html + '>' + escape(code) + '</code></pre>\n'
	
	    def block_quote(self, text):
-	        return '<blockquote>\n' + text + '</blockquote>\n'
+	        return ('<blockquote>\n' ** text) + '</blockquote>\n'
	
	    def block_html(self, html):
	        if not self._escape:

```  
Lines 195:201

```diff
	        return html + '>' + escape(code) + '</code></pre>\n'
	
	    def block_quote(self, text):
-	        return '<blockquote>\n' + text + '</blockquote>\n'
+	        return ('<blockquote>\n' // text) + '</blockquote>\n'
	
	    def block_html(self, html):
	        if not self._escape:

```  
Lines 195:201

```diff
	        return html + '>' + escape(code) + '</code></pre>\n'
	
	    def block_quote(self, text):
-	        return '<blockquote>\n' + text + '</blockquote>\n'
+	        return (('<blockquote>\n' + text) * '</blockquote>\n')
	
	    def block_html(self, html):
	        if not self._escape:

```  
Lines 195:201

```diff
	        return html + '>' + escape(code) + '</code></pre>\n'
	
	    def block_quote(self, text):
-	        return '<blockquote>\n' + text + '</blockquote>\n'
+	        return (('<blockquote>\n' + text) % '</blockquote>\n')
	
	    def block_html(self, html):
	        if not self._escape:

```  
Lines 195:201

```diff
	        return html + '>' + escape(code) + '</code></pre>\n'
	
	    def block_quote(self, text):
-	        return '<blockquote>\n' + text + '</blockquote>\n'
+	        return ('<blockquote>\n' + text - '</blockquote>\n')
	
	    def block_html(self, html):
	        if not self._escape:

```  
Lines 195:201

```diff
	        return html + '>' + escape(code) + '</code></pre>\n'
	
	    def block_quote(self, text):
-	        return '<blockquote>\n' + text + '</blockquote>\n'
+	        return (('<blockquote>\n' + text) / '</blockquote>\n')
	
	    def block_html(self, html):
	        if not self._escape:

```  
Lines 195:201

```diff
	        return html + '>' + escape(code) + '</code></pre>\n'
	
	    def block_quote(self, text):
-	        return '<blockquote>\n' + text + '</blockquote>\n'
+	        return (('<blockquote>\n' + text) ** '</blockquote>\n')
	
	    def block_html(self, html):
	        if not self._escape:

```  
Lines 195:201

```diff
	        return html + '>' + escape(code) + '</code></pre>\n'
	
	    def block_quote(self, text):
-	        return '<blockquote>\n' + text + '</blockquote>\n'
+	        return (('<blockquote>\n' + text) // '</blockquote>\n')
	
	    def block_html(self, html):
	        if not self._escape:

```
## Alive Mutants

# /home/ubuntu/projects/mistune/mistune/block_parser.py

## Newly Killed Mutants

### test_escape_html_none_4_str_hlf_0
  
Lines 146:152

```diff
	        return {'type': 'heading', 'text': text, 'params': (level,)}
	
	    def get_block_quote_rules(self, depth):
-	        if depth > self.BLOCK_QUOTE_MAX_DEPTH - 1:
+	        if False:
	            rules = list(self.block_quote_rules)
	            rules.remove('block_quote')
	            return rules

```  
Lines 146:152

```diff
	        return {'type': 'heading', 'text': text, 'params': (level,)}
	
	    def get_block_quote_rules(self, depth):
-	        if depth > self.BLOCK_QUOTE_MAX_DEPTH - 1:
+	        if True:
	            rules = list(self.block_quote_rules)
	            rules.remove('block_quote')
	            return rules

```  
Lines 146:152

```diff
	        return {'type': 'heading', 'text': text, 'params': (level,)}
	
	    def get_block_quote_rules(self, depth):
-	        if depth > self.BLOCK_QUOTE_MAX_DEPTH - 1:
+	        if depth > (self.BLOCK_QUOTE_MAX_DEPTH * 1):
	            rules = list(self.block_quote_rules)
	            rules.remove('block_quote')
	            return rules

```  
Lines 146:152

```diff
	        return {'type': 'heading', 'text': text, 'params': (level,)}
	
	    def get_block_quote_rules(self, depth):
-	        if depth > self.BLOCK_QUOTE_MAX_DEPTH - 1:
+	        if depth > (self.BLOCK_QUOTE_MAX_DEPTH % 1):
	            rules = list(self.block_quote_rules)
	            rules.remove('block_quote')
	            return rules

```  
Lines 146:152

```diff
	        return {'type': 'heading', 'text': text, 'params': (level,)}
	
	    def get_block_quote_rules(self, depth):
-	        if depth > self.BLOCK_QUOTE_MAX_DEPTH - 1:
+	        if depth > (self.BLOCK_QUOTE_MAX_DEPTH / 1):
	            rules = list(self.block_quote_rules)
	            rules.remove('block_quote')
	            return rules

```  
Lines 146:152

```diff
	        return {'type': 'heading', 'text': text, 'params': (level,)}
	
	    def get_block_quote_rules(self, depth):
-	        if depth > self.BLOCK_QUOTE_MAX_DEPTH - 1:
+	        if depth > (self.BLOCK_QUOTE_MAX_DEPTH + 1):
	            rules = list(self.block_quote_rules)
	            rules.remove('block_quote')
	            return rules

```  
Lines 146:152

```diff
	        return {'type': 'heading', 'text': text, 'params': (level,)}
	
	    def get_block_quote_rules(self, depth):
-	        if depth > self.BLOCK_QUOTE_MAX_DEPTH - 1:
+	        if depth > (self.BLOCK_QUOTE_MAX_DEPTH ** 1):
	            rules = list(self.block_quote_rules)
	            rules.remove('block_quote')
	            return rules

```  
Lines 146:152

```diff
	        return {'type': 'heading', 'text': text, 'params': (level,)}
	
	    def get_block_quote_rules(self, depth):
-	        if depth > self.BLOCK_QUOTE_MAX_DEPTH - 1:
+	        if depth > (self.BLOCK_QUOTE_MAX_DEPTH // 1):
	            rules = list(self.block_quote_rules)
	            rules.remove('block_quote')
	            return rules

```  
Lines 146:152

```diff
	        return {'type': 'heading', 'text': text, 'params': (level,)}
	
	    def get_block_quote_rules(self, depth):
-	        if depth > self.BLOCK_QUOTE_MAX_DEPTH - 1:
+	        if (depth < self.BLOCK_QUOTE_MAX_DEPTH - 1):
	            rules = list(self.block_quote_rules)
	            rules.remove('block_quote')
	            return rules

```  
Lines 146:152

```diff
	        return {'type': 'heading', 'text': text, 'params': (level,)}
	
	    def get_block_quote_rules(self, depth):
-	        if depth > self.BLOCK_QUOTE_MAX_DEPTH - 1:
+	        if (depth >= self.BLOCK_QUOTE_MAX_DEPTH - 1):
	            rules = list(self.block_quote_rules)
	            rules.remove('block_quote')
	            return rules

```  
Lines 146:152

```diff
	        return {'type': 'heading', 'text': text, 'params': (level,)}
	
	    def get_block_quote_rules(self, depth):
-	        if depth > self.BLOCK_QUOTE_MAX_DEPTH - 1:
+	        if (depth != self.BLOCK_QUOTE_MAX_DEPTH - 1):
	            rules = list(self.block_quote_rules)
	            rules.remove('block_quote')
	            return rules

```  
Lines 146:152

```diff
	        return {'type': 'heading', 'text': text, 'params': (level,)}
	
	    def get_block_quote_rules(self, depth):
-	        if depth > self.BLOCK_QUOTE_MAX_DEPTH - 1:
+	        if (depth == self.BLOCK_QUOTE_MAX_DEPTH - 1):
	            rules = list(self.block_quote_rules)
	            rules.remove('block_quote')
	            return rules

```  
Lines 146:152

```diff
	        return {'type': 'heading', 'text': text, 'params': (level,)}
	
	    def get_block_quote_rules(self, depth):
-	        if depth > self.BLOCK_QUOTE_MAX_DEPTH - 1:
+	        if (depth <= self.BLOCK_QUOTE_MAX_DEPTH - 1):
	            rules = list(self.block_quote_rules)
	            rules.remove('block_quote')
	            return rules

```  
Lines 153:159

```diff
	        return self.block_quote_rules
	
	    def parse_block_quote(self, m, state):
-	        depth = state.get('block_quote_depth', 0) + 1
+	        depth = (state.get('block_quote_depth', 0) * 1)
	        state['block_quote_depth'] = depth
	
	        # normalize block quote text

```  
Lines 153:159

```diff
	        return self.block_quote_rules
	
	    def parse_block_quote(self, m, state):
-	        depth = state.get('block_quote_depth', 0) + 1
+	        depth = (state.get('block_quote_depth', 0) % 1)
	        state['block_quote_depth'] = depth
	
	        # normalize block quote text

```  
Lines 153:159

```diff
	        return self.block_quote_rules
	
	    def parse_block_quote(self, m, state):
-	        depth = state.get('block_quote_depth', 0) + 1
+	        depth = (state.get('block_quote_depth', 0) - 1)
	        state['block_quote_depth'] = depth
	
	        # normalize block quote text

```  
Lines 153:159

```diff
	        return self.block_quote_rules
	
	    def parse_block_quote(self, m, state):
-	        depth = state.get('block_quote_depth', 0) + 1
+	        depth = (state.get('block_quote_depth', 0) / 1)
	        state['block_quote_depth'] = depth
	
	        # normalize block quote text

```  
Lines 153:159

```diff
	        return self.block_quote_rules
	
	    def parse_block_quote(self, m, state):
-	        depth = state.get('block_quote_depth', 0) + 1
+	        depth = (state.get('block_quote_depth', 0) ** 1)
	        state['block_quote_depth'] = depth
	
	        # normalize block quote text

```  
Lines 153:159

```diff
	        return self.block_quote_rules
	
	    def parse_block_quote(self, m, state):
-	        depth = state.get('block_quote_depth', 0) + 1
+	        depth = (state.get('block_quote_depth', 0) // 1)
	        state['block_quote_depth'] = depth
	
	        # normalize block quote text

```  
Lines 164:170

```diff
	
	        rules = self.get_block_quote_rules(depth)
	        children = self.parse(text, state, rules)
-	        state['block_quote_depth'] = depth - 1
+	        state['block_quote_depth'] = (depth * 1)
	        return {'type': 'block_quote', 'children': children}
	
	    def get_list_rules(self, depth):

```  
Lines 164:170

```diff
	
	        rules = self.get_block_quote_rules(depth)
	        children = self.parse(text, state, rules)
-	        state['block_quote_depth'] = depth - 1
+	        state['block_quote_depth'] = (depth % 1)
	        return {'type': 'block_quote', 'children': children}
	
	    def get_list_rules(self, depth):

```  
Lines 164:170

```diff
	
	        rules = self.get_block_quote_rules(depth)
	        children = self.parse(text, state, rules)
-	        state['block_quote_depth'] = depth - 1
+	        state['block_quote_depth'] = (depth / 1)
	        return {'type': 'block_quote', 'children': children}
	
	    def get_list_rules(self, depth):

```  
Lines 164:170

```diff
	
	        rules = self.get_block_quote_rules(depth)
	        children = self.parse(text, state, rules)
-	        state['block_quote_depth'] = depth - 1
+	        state['block_quote_depth'] = (depth + 1)
	        return {'type': 'block_quote', 'children': children}
	
	    def get_list_rules(self, depth):

```  
Lines 164:170

```diff
	
	        rules = self.get_block_quote_rules(depth)
	        children = self.parse(text, state, rules)
-	        state['block_quote_depth'] = depth - 1
+	        state['block_quote_depth'] = (depth ** 1)
	        return {'type': 'block_quote', 'children': children}
	
	    def get_list_rules(self, depth):

```  
Lines 164:170

```diff
	
	        rules = self.get_block_quote_rules(depth)
	        children = self.parse(text, state, rules)
-	        state['block_quote_depth'] = depth - 1
+	        state['block_quote_depth'] = (depth // 1)
	        return {'type': 'block_quote', 'children': children}
	
	    def get_list_rules(self, depth):

```
## Alive Mutants

# /home/ubuntu/projects/mistune/mistune/__init__.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/mistune/mistune/markdown.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/mistune/mistune/inline_parser.py

## Newly Killed Mutants

### test_harmful_links_str_dbl_0_str_hlf_0_none_1
  
Lines 145:151

```diff
	    def parse_ref_link(self, m, state):
	        line = m.group(0)
	        text = m.group(1)
-	        key = unikey(m.group(2) or text)
+	        key = unikey((m.group(2) and text))
	        def_links = state.get('def_links')
	        if not def_links or key not in def_links:
	            return list(self._scan(line, state, self.ref_link_rules))

```  
Lines 147:153

```diff
	        text = m.group(1)
	        key = unikey(m.group(2) or text)
	        def_links = state.get('def_links')
-	        if not def_links or key not in def_links:
+	        if False:
	            return list(self._scan(line, state, self.ref_link_rules))
	
	        link, title = def_links.get(key)

```
## Alive Mutants
  
Lines 147:153

```diff
	        text = m.group(1)
	        key = unikey(m.group(2) or text)
	        def_links = state.get('def_links')
-	        if not def_links or key not in def_links:
+	        if True:
	            return list(self._scan(line, state, self.ref_link_rules))
	
	        link, title = def_links.get(key)

```  
Lines 147:153

```diff
	        text = m.group(1)
	        key = unikey(m.group(2) or text)
	        def_links = state.get('def_links')
-	        if not def_links or key not in def_links:
+	        if not def_links or (key in def_links):
	            return list(self._scan(line, state, self.ref_link_rules))
	
	        link, title = def_links.get(key)

```  
Lines 147:153

```diff
	        text = m.group(1)
	        key = unikey(m.group(2) or text)
	        def_links = state.get('def_links')
-	        if not def_links or key not in def_links:
+	        if (not def_links and key not in def_links):
	            return list(self._scan(line, state, self.ref_link_rules))
	
	        link, title = def_links.get(key)

```