



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
# /home/ubuntu/projects/mistune/mistune/scanner.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/mistune/mistune/renderers.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/mistune/mistune/block_parser.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/mistune/mistune/__init__.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/mistune/mistune/markdown.py

## Newly Killed Mutants

## Alive Mutants

# /home/ubuntu/projects/mistune/mistune/inline_parser.py

## Newly Killed Mutants

## Alive Mutants
