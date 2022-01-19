




```diff
	try:
	    from urllib.parse import quote
	    import html
-	except ImportError:
-	    from urllib import quote
-	    html = None
	
	
	PUNCTUATION = r'''\\!"#$%&'()*+,./:;<=>?@\[\]^`{}|_~-'''
	ESCAPE_TEXT = r'\\[' + PUNCTUATION + ']'
	
	
	def escape(s, quote=True):
+	    s = s.replace("&", "&amp;")	#test_html_include_bool_inv_0_none_4
+	    s = s.replace("<", "&lt;")	#test_html_include_bool_inv_0_none_4
+	    s = s.replace(">", "&gt;")	#test_html_include_bool_inv_0_none_4
+	    if quote:	#test_html_include_bool_inv_0_none_4
+	        s = s.replace('"', "&quot;")	#test_html_include_bool_inv_0_none_4
+	    return s	#test_html_include_bool_inv_0_none_4
	
	
	def escape_url(link):
-	    safe = '/#:()*?=%@+,&'
-	    if html is None:
-	        return quote(link.encode('utf-8'), safe=safe)
-	    return html.escape(quote(html.unescape(link), safe=safe))
	
	
	def escape_html(s):
	    if html is not None:
	        return html.escape(html.unescape(s)).replace('&#x27;', "'")
-	    return escape(s)
	
	
	def unikey(s):
-	    return ' '.join(s.split()).lower()

```