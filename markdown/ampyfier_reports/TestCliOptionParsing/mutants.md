



# /home/ubuntu/projects/markdown/markdown/__main__.py

## Newly Killed Mutants

### testQuietOption_amp
  
Lines 79:85

```diff
	                      "`--extension` option.",
	                      metavar="CONFIG_FILE")
	    parser.add_option("-q", "--quiet", default=CRITICAL,
-	                      action="store_const", const=CRITICAL+10, dest="verbose",
+	                      action="store_const", const=(CRITICAL ** 10), dest="verbose",
	                      help="Suppress all warnings.")
	    parser.add_option("-v", "--verbose",
	                      action="store_const", const=WARNING, dest="verbose",

```  
Lines 79:85

```diff
	                      "`--extension` option.",
	                      metavar="CONFIG_FILE")
	    parser.add_option("-q", "--quiet", default=CRITICAL,
-	                      action="store_const", const=CRITICAL+10, dest="verbose",
+	                      action="store_const", const=(CRITICAL * 10), dest="verbose",
	                      help="Suppress all warnings.")
	    parser.add_option("-v", "--verbose",
	                      action="store_const", const=WARNING, dest="verbose",

```
### testOutputFileOption_str_hlf_0
  
Lines 93:99

```diff
	    if len(args) == 0:
	        input_file = None
	    else:
-	        input_file = args[0]
+	        input_file = args[<_ast.Constant object at 0x7fafbba90eb0>]
	
	    if not options.extensions:
	        options.extensions = []

```
## Alive Mutants
  
Lines 43:49

```diff
	logger = logging.getLogger('MARKDOWN')
	
	
-	def parse_options(args=None, values=None):
+	def parse_options(args=(False), values=None):
	    """
	    Define and parse `optparse` options for command-line usage.
	    """

```  
Lines 43:49

```diff
	logger = logging.getLogger('MARKDOWN')
	
	
-	def parse_options(args=None, values=None):
+	def parse_options(args=(True), values=None):
	    """
	    Define and parse `optparse` options for command-line usage.
	    """

```  
Lines 51:57

```diff
	       (STDIN is assumed if no INPUTFILE is given)"""
	    desc = "A Python implementation of John Gruber's Markdown. " \
	           "https://Python-Markdown.github.io/"
-	    ver = "%%prog %s" % markdown.__version__
+	    ver = ('%%prog %s' + markdown.__version__)
	
	    parser = optparse.OptionParser(usage=usage, description=desc, version=ver)
	    parser.add_option("-f", "--file", dest="filename", default=None,

```  
Lines 68:74

```diff
	    parser.add_option("-x", "--extension", action="append", dest="extensions",
	                      help="Load extension EXTENSION.", metavar="EXTENSION")
	    parser.add_option("-c", "--extension_configs",
-	                      dest="configfile", default=None,
+	                      dest="configfile", default=(False),
	                      help="Read extension configurations from CONFIG_FILE. "
	                      "CONFIG_FILE must be of JSON or YAML format. YAML "
	                      "format requires that a python YAML library be "

```  
Lines 90:96

```diff
	
	    (options, args) = parser.parse_args(args, values)
	
-	    if len(args) == 0:
+	    if (len(args) <= 0):
	        input_file = None
	    else:
	        input_file = args[0]

```  
Lines 106:113

```diff
	            try:
	                extension_configs = yaml_load(fp)
	            except Exception as e:
-	                message = "Failed parsing extension config file: %s" % \
-	                          options.configfile
+	                message = ('Failed parsing extension config file: %s' + options.configfile)
	                e.args = (message,) + e.args[1:]
	                raise
	

```  
Lines 108:114

```diff
	            except Exception as e:
	                message = "Failed parsing extension config file: %s" % \
	                          options.configfile
-	                e.args = (message,) + e.args[1:]
+	                e.args = (message,) + e.args[:]
	                raise
	
	    opts = {

```  
Lines 108:114

```diff
	            except Exception as e:
	                message = "Failed parsing extension config file: %s" % \
	                          options.configfile
-	                e.args = (message,) + e.args[1:]
+	                e.args = (message,) + e.args[:1]
	                raise
	
	    opts = {

```  
Lines 145:151

```diff
	    markdown.markdownFromFile(**options)
	
	
-	if __name__ == '__main__':  # pragma: no cover
+	if (__name__ <= '__main__'):  # pragma: no cover
	    # Support running module as a commandline command.
	    # `python -m markdown [options] [args]`.
	    run()

```  
Lines 145:151

```diff
	    markdown.markdownFromFile(**options)
	
	
-	if __name__ == '__main__':  # pragma: no cover
+	if (__name__ < '__main__'):  # pragma: no cover
	    # Support running module as a commandline command.
	    # `python -m markdown [options] [args]`.
	    run()

```  
Lines 145:151

```diff
	    markdown.markdownFromFile(**options)
	
	
-	if __name__ == '__main__':  # pragma: no cover
+	if False: no cover
	    # Support running module as a commandline command.
	    # `python -m markdown [options] [args]`.
	    run()

```