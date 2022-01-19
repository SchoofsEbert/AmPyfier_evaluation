



# /home/ebert/projects/markdown/markdown/preprocessors.py

## Newly Killed Mutants

## Alive Mutants

# /home/ebert/projects/markdown/markdown/inlinepatterns.py

## Newly Killed Mutants

### testSimpleAbbr_str_emp_2
  
Lines 794:800

```diff
	
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)
-	        if id not in self.md.references:  # ignore undefined refs
+	        if (id in self.md.references):  # ignore undefined refs
	            return None, m.start(0), end
	
	        href, title = self.md.references[id]

```  
Lines 794:800

```diff
	
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)
-	        if id not in self.md.references:  # ignore undefined refs
+	        if False:  # ignore undefined refs
	            return None, m.start(0), end
	
	        href, title = self.md.references[id]

```  
Lines 795:801

```diff
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)
	        if id not in self.md.references:  # ignore undefined refs
-	            return None, m.start(0), end
+	            return (False), m.start(0), end
	
	        href, title = self.md.references[id]
	

```  
Lines 795:801

```diff
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)
	        if id not in self.md.references:  # ignore undefined refs
-	            return None, m.start(0), end
+	            return (True), m.start(0), end
	
	        href, title = self.md.references[id]
	

```
## Alive Mutants
  
Lines 606:612

```diff
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:
-	            return None, None, None
+	            return None, None, (False)
	
	        el = etree.Element("a")
	        el.text = text

```  
Lines 606:612

```diff
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:
-	            return None, None, None
+	            return None, None, (True)
	
	        el = etree.Element("a")
	        el.text = text

```  
Lines 606:612

```diff
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:
-	            return None, None, None
+	            return (False), None, None
	
	        el = etree.Element("a")
	        el.text = text

```  
Lines 606:612

```diff
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:
-	            return None, None, None
+	            return (True), None, None
	
	        el = etree.Element("a")
	        el.text = text

```  
Lines 606:612

```diff
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:
-	            return None, None, None
+	            return None, (False), None
	
	        el = etree.Element("a")
	        el.text = text

```  
Lines 606:612

```diff
	
	        href, title, index, handled = self.getLink(data, index)
	        if not handled:
-	            return None, None, None
+	            return None, (True), None
	
	        el = etree.Element("a")
	        el.text = text

```  
Lines 794:800

```diff
	
	        # Clean up linebreaks in id
	        id = self.NEWLINE_CLEANUP_RE.sub(' ', id)
-	        if id not in self.md.references:  # ignore undefined refs
+	        if True:  # ignore undefined refs
	            return None, m.start(0), end
	
	        href, title = self.md.references[id]

```  
Lines 833:839

```diff
	    def evalId(self, data, index, text):
	        """Evaluate the id from of [ref]  """
	
-	        return text.lower(), index, True
+	        return text.lower(), index, (False)
	
	
	class ImageReferenceInlineProcessor(ReferenceInlineProcessor):

```  
Lines 833:839

```diff
	    def evalId(self, data, index, text):
	        """Evaluate the id from of [ref]  """
	
-	        return text.lower(), index, True
+	        return text.lower(), index, None
	
	
	class ImageReferenceInlineProcessor(ReferenceInlineProcessor):

```
# /home/ebert/projects/markdown/markdown/blockparser.py

## Newly Killed Mutants

## Alive Mutants

# /home/ebert/projects/markdown/markdown/__meta__.py

## Newly Killed Mutants

## Alive Mutants

# /home/ebert/projects/markdown/markdown/__init__.py

## Newly Killed Mutants

## Alive Mutants

# /home/ebert/projects/markdown/markdown/treeprocessors.py

## Newly Killed Mutants

### testNestedAbbr_str_emp_2_str_hlf_1
  
Lines 193:199

```diff
	                        parent.tail = text
	                else:
	                    if parent.text:
-	                        parent.text += text
+	                        parent.text *= text
	                    else:
	                        parent.text = text
	        result = []

```  
Lines 193:199

```diff
	                        parent.tail = text
	                else:
	                    if parent.text:
-	                        parent.text += text
+	                        parent.text /= text
	                    else:
	                        parent.text = text
	        result = []

```  
Lines 193:199

```diff
	                        parent.tail = text
	                else:
	                    if parent.text:
-	                        parent.text += text
+	                        parent.text -= text
	                    else:
	                        parent.text = text
	        result = []

```
## Alive Mutants
  
Lines 288:294

```diff
	            end = match.end(0)
	
	        if node is None:
-	            return data, True, end
+	            return data, (False), end
	
	        if not isString(node):
	            if not isinstance(node.text, util.AtomicString):

```  
Lines 288:294

```diff
	            end = match.end(0)
	
	        if node is None:
-	            return data, True, end
+	            return data, None, end
	
	        if not isString(node):
	            if not isinstance(node.text, util.AtomicString):

```
# /home/ebert/projects/markdown/markdown/util.py

## Newly Killed Mutants

### testSimpleAbbr_str_dbl_2
  
Lines 331:337

```diff
	        """
	        Return the index of the given name.
	        """
-	        if name in self:
+	        if False:
	            self._sort()
	            return self._priority.index(
	                [x for x in self._priority if x.name == name][0]

```  
Lines 331:337

```diff
	        """
	        Return the index of the given name.
	        """
-	        if name in self:
+	        if (name not in self):
	            self._sort()
	            return self._priority.index(
	                [x for x in self._priority if x.name == name][0]

```  
Lines 334:340

```diff
	        if name in self:
	            self._sort()
	            return self._priority.index(
-	                [x for x in self._priority if x.name == name][0]
+	                [x for x in self._priority if (x.name < name)][0]
	            )
	        raise ValueError('No item named "{}" exists.'.format(name))
	

```
### testNestedAbbr_str_emp_2_str_hlf_1
  
Lines 331:337

```diff
	        """
	        Return the index of the given name.
	        """
-	        if name in self:
+	        if True:
	            self._sort()
	            return self._priority.index(
	                [x for x in self._priority if x.name == name][0]

```  
Lines 334:340

```diff
	        if name in self:
	            self._sort()
	            return self._priority.index(
-	                [x for x in self._priority if x.name == name][0]
+	                [x for x in self._priority if (x.name <= name)][0]
	            )
	        raise ValueError('No item named "{}" exists.'.format(name))
	

```  
Lines 334:340

```diff
	        if name in self:
	            self._sort()
	            return self._priority.index(
-	                [x for x in self._priority if x.name == name][0]
+	                [x for x in self._priority if (x.name >= name)][0]
	            )
	        raise ValueError('No item named "{}" exists.'.format(name))
	

```  
Lines 334:340

```diff
	        if name in self:
	            self._sort()
	            return self._priority.index(
-	                [x for x in self._priority if x.name == name][0]
+	                [x for x in self._priority if (x.name != name)][0]
	            )
	        raise ValueError('No item named "{}" exists.'.format(name))
	

```  
Lines 334:340

```diff
	        if name in self:
	            self._sort()
	            return self._priority.index(
-	                [x for x in self._priority if x.name == name][0]
+	                [x for x in self._priority if (x.name > name)][0]
	            )
	        raise ValueError('No item named "{}" exists.'.format(name))
	

```
## Alive Mutants

# /home/ebert/projects/markdown/markdown/core.py

## Newly Killed Mutants

## Alive Mutants

# /home/ebert/projects/markdown/markdown/pep562.py

## Newly Killed Mutants

## Alive Mutants

# /home/ebert/projects/markdown/markdown/htmlparser.py

## Newly Killed Mutants

## Alive Mutants

# /home/ebert/projects/markdown/markdown/postprocessors.py

## Newly Killed Mutants

## Alive Mutants

# /home/ebert/projects/markdown/markdown/serializers.py

## Newly Killed Mutants

## Alive Mutants

# /home/ebert/projects/markdown/markdown/blockprocessors.py

## Newly Killed Mutants

### testSimpleAbbr_str_dbl_2
  
Lines 76:82

```diff
	        if len(parent):
	            return parent[-1]
	        else:
-	            return None
+	            return (False)
	
	    def detab(self, text, length=None):
	        """ Remove a tab from the front of each line of the given text. """

```  
Lines 76:82

```diff
	        if len(parent):
	            return parent[-1]
	        else:
-	            return None
+	            return (True)
	
	    def detab(self, text, length=None):
	        """ Remove a tab from the front of each line of the given text. """

```  
Lines 544:550

```diff
	            filler = '\n'
	            # Save the rest for later.
	            theRest = block[1:]
-	            if theRest:
+	            if False:
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)

```  
Lines 544:550

```diff
	            filler = '\n'
	            # Save the rest for later.
	            theRest = block[1:]
-	            if theRest:
+	            if True:
	                # Add remaining lines to master blocks for later.
	                blocks.insert(0, theRest)
	        sibling = self.lastChild(parent)

```
### testNestedAbbr_str_emp_2_str_hlf_1
  
Lines 571:577

```diff
	        if m:
	            id = m.group(1).strip().lower()
	            link = m.group(2).lstrip('<').rstrip('>')
-	            title = m.group(5) or m.group(6)
+	            title = (m.group(5) and m.group(6))
	            self.parser.md.references[id] = (link, title)
	            if block[m.end():].strip():
	                # Add any content after match back to blocks as separate block

```  
Lines 573:579

```diff
	            link = m.group(2).lstrip('<').rstrip('>')
	            title = m.group(5) or m.group(6)
	            self.parser.md.references[id] = (link, title)
-	            if block[m.end():].strip():
+	            if False:
	                # Add any content after match back to blocks as separate block
	                blocks.insert(0, block[m.end():].lstrip('\n'))
	            if block[:m.start()].strip():

```  
Lines 573:579

```diff
	            link = m.group(2).lstrip('<').rstrip('>')
	            title = m.group(5) or m.group(6)
	            self.parser.md.references[id] = (link, title)
-	            if block[m.end():].strip():
+	            if True:
	                # Add any content after match back to blocks as separate block
	                blocks.insert(0, block[m.end():].lstrip('\n'))
	            if block[:m.start()].strip():

```  
Lines 573:579

```diff
	            link = m.group(2).lstrip('<').rstrip('>')
	            title = m.group(5) or m.group(6)
	            self.parser.md.references[id] = (link, title)
-	            if block[m.end():].strip():
+	            if block[:m.end()].strip():
	                # Add any content after match back to blocks as separate block
	                blocks.insert(0, block[m.end():].lstrip('\n'))
	            if block[:m.start()].strip():

```  
Lines 573:579

```diff
	            link = m.group(2).lstrip('<').rstrip('>')
	            title = m.group(5) or m.group(6)
	            self.parser.md.references[id] = (link, title)
-	            if block[m.end():].strip():
+	            if block[:].strip():
	                # Add any content after match back to blocks as separate block
	                blocks.insert(0, block[m.end():].lstrip('\n'))
	            if block[:m.start()].strip():

```  
Lines 576:582

```diff
	            if block[m.end():].strip():
	                # Add any content after match back to blocks as separate block
	                blocks.insert(0, block[m.end():].lstrip('\n'))
-	            if block[:m.start()].strip():
+	            if False:
	                # Add any content before match back to blocks as separate block
	                blocks.insert(0, block[:m.start()].rstrip('\n'))
	            return True

```  
Lines 576:582

```diff
	            if block[m.end():].strip():
	                # Add any content after match back to blocks as separate block
	                blocks.insert(0, block[m.end():].lstrip('\n'))
-	            if block[:m.start()].strip():
+	            if True:
	                # Add any content before match back to blocks as separate block
	                blocks.insert(0, block[:m.start()].rstrip('\n'))
	            return True

```  
Lines 576:582

```diff
	            if block[m.end():].strip():
	                # Add any content after match back to blocks as separate block
	                blocks.insert(0, block[m.end():].lstrip('\n'))
-	            if block[:m.start()].strip():
+	            if block[:].strip():
	                # Add any content before match back to blocks as separate block
	                blocks.insert(0, block[:m.start()].rstrip('\n'))
	            return True

```  
Lines 576:582

```diff
	            if block[m.end():].strip():
	                # Add any content after match back to blocks as separate block
	                blocks.insert(0, block[m.end():].lstrip('\n'))
-	            if block[:m.start()].strip():
+	            if block[m.start():].strip():
	                # Add any content before match back to blocks as separate block
	                blocks.insert(0, block[:m.start()].rstrip('\n'))
	            return True

```  
Lines 579:585

```diff
	            if block[:m.start()].strip():
	                # Add any content before match back to blocks as separate block
	                blocks.insert(0, block[:m.start()].rstrip('\n'))
-	            return True
+	            return (False)
	        # No match. Restore block.
	        blocks.insert(0, block)
	        return False

```  
Lines 579:585

```diff
	            if block[:m.start()].strip():
	                # Add any content before match back to blocks as separate block
	                blocks.insert(0, block[:m.start()].rstrip('\n'))
-	            return True
+	            return None
	        # No match. Restore block.
	        blocks.insert(0, block)
	        return False

```
## Alive Mutants

# /home/ebert/projects/markdown/markdown/__main__.py

## Newly Killed Mutants

## Alive Mutants

# /home/ebert/projects/markdown/markdown/test_tools.py

## Newly Killed Mutants

## Alive Mutants
