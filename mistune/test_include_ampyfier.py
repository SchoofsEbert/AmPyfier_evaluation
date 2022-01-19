import os
from mistune import create_markdown
from mistune.directives import DirectiveInclude
from tests.fixtures import ROOT
from unittest import TestCase


class TestPluginDirective(TestCase):

    def test_html_include(self):
        md = create_markdown(escape=False, plugins=[DirectiveInclude()])
        html = md.read(os.path.join(ROOT, 'include/text.md'))
        self.assertIn('Could not include self', html)
        self.assertIn('Could not find file', html)
        self.assertIn('<div>include html</div>', html)
        self.assertIn('<blockquote>', html)
        self.assertIn('# Table of Contents', html)

    def test_include_missing_source(self):
        md = create_markdown(plugins=[DirectiveInclude()])
        s = '.. include:: foo.txt'
        html = md(s)
        self.assertIn('Missing source file', html)

    def test_ast_include(self):
        md = create_markdown(renderer='ast', plugins=[DirectiveInclude()])
        filepath = os.path.join(ROOT, 'include/foo.txt')
        s = '.. include:: hello.txt'
        tokens = md.parse(s, {'__file__': filepath})
        token = tokens[0]
        self.assertEqual(token['type'], 'include')
        self.assertEqual(token['text'], 'hello\n')
        self.assertEqual(token['relpath'], 'hello.txt')

    def test_html_include_bool_inv_0_none_4(self):
        md = create_markdown(escape=True, plugins=[DirectiveInclude()])
        html = md.read(os.path.join(ROOT, 'include/text.md'))
        self.assertEqual(html,
            """<h1>Include</h1>
<h1>Include</h1>
<div class="error">Could not include self: ./text.md</div>
<div class="error">Could not find file: ./not-exist.md</div>
<p>&amp;lt;div&amp;gt;include html&amp;lt;/div&amp;gt;
</p>
<blockquote>
<p>hello</p>
</blockquote>
<section class="directive-include" data-relpath="../toc.txt">
# Table of Contents

## No TOC

```````````````````````````````` example
none
.
<p>none</p>
````````````````````````````````

```````````````````````````````` example
# H1
## H2
.
<h1 id="toc_1">H1</h1>
<h2 id="toc_2">H2</h2>
````````````````````````````````


## Simple TOC

```````````````````````````````` example
.. toc::

# H1
## H2
.
<section class="toc">
<ul>
<li><a href="#toc_1">H1</a>
<ul>
<li><a href="#toc_2">H2</a></li>
</ul>
</li>
</ul>
</section>
<h1 id="toc_1">H1</h1>
<h2 id="toc_2">H2</h2>
````````````````````````````````

## Invalid Option

```````````````````````````````` example
# H1
## H2
.. toc::
   :depth: s
.
<h1 id="toc_1">H1</h1>
<h2 id="toc_2">H2</h2>
<div class="error">TOC depth MUST be integer</div>
````````````````````````````````

## Complex

```````````````````````````````` example
# H1
## H2
### H3
#### H4
# H1 B
# H1 `C`

.. toc:: Table of Contents
   :depth: 3
.
<h1 id="toc_1">H1</h1>
<h2 id="toc_2">H2</h2>
<h3 id="toc_3">H3</h3>
<h4 id="toc_4">H4</h4>
<h1 id="toc_5">H1 B</h1>
<h1 id="toc_6">H1 <code>C</code></h1>
<section class="toc">
<h1>Table of Contents</h1>
<ul>
<li><a href="#toc_1">H1</a>
<ul>
<li><a href="#toc_2">H2</a>
<ul>
<li><a href="#toc_3">H3</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#toc_5">H1 B</a></li>
<li><a href="#toc_6">H1 C</a></li>
</ul>
</section>
````````````````````````````````

## Insane

```````````````````````````````` example
# H1
### H3
## H2
#### H4
### H3 B
# H1 B
.. toc::
.
<h1 id="toc_1">H1</h1>
<h3 id="toc_2">H3</h3>
<h2 id="toc_3">H2</h2>
<h4 id="toc_4">H4</h4>
<h3 id="toc_5">H3 B</h3>
<h1 id="toc_6">H1 B</h1>
<section class="toc">
<ul>
<li><a href="#toc_1">H1</a>
<ul>
<li><a href="#toc_2">H3</a></li>
<li><a href="#toc_3">H2</a>
<ul>
<li><a href="#toc_5">H3 B</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#toc_6">H1 B</a></li>
</ul>
</section>
````````````````````````````````

```````````````````````````````` example
### H3
## H2
# H1
.. toc::
.
<h3 id="toc_1">H3</h3>
<h2 id="toc_2">H2</h2>
<h1 id="toc_3">H1</h1>
<section class="toc">
<ul>
<li><a href="#toc_1">H3</a></li>
<li><a href="#toc_2">H2</a></li>
<li><a href="#toc_3">H1</a></li>
</ul>
</section>
````````````````````````````````

## Link in Heading


```````````````````````````````` example
# [foo](/bar)
.. toc::
.
<h1 id="toc_1"><a href="/bar">foo</a></h1>
<section class="toc">
<ul>
<li><a href="#toc_1">foo</a></li>
</ul>
</section>
````````````````````````````````

## HTML in Heading

```````````````````````````````` example
# <em>H1</em>
.. toc::
.
<h1 id="toc_1"><em>H1</em></h1>
<section class="toc">
<ul>
<li><a href="#toc_1">H1</a></li>
</ul>
</section>
````````````````````````````````
</section>
<div class="error">Could not find file: ./not-exist.md</div>
<p>&amp;lt;div&amp;gt;include html&amp;lt;/div&amp;gt;
</p>
<blockquote>
<p>hello</p>
</blockquote>
<section class="directive-include" data-relpath="../toc.txt">
# Table of Contents

## No TOC

```````````````````````````````` example
none
.
<p>none</p>
````````````````````````````````

```````````````````````````````` example
# H1
## H2
.
<h1 id="toc_1">H1</h1>
<h2 id="toc_2">H2</h2>
````````````````````````````````


## Simple TOC

```````````````````````````````` example
.. toc::

# H1
## H2
.
<section class="toc">
<ul>
<li><a href="#toc_1">H1</a>
<ul>
<li><a href="#toc_2">H2</a></li>
</ul>
</li>
</ul>
</section>
<h1 id="toc_1">H1</h1>
<h2 id="toc_2">H2</h2>
````````````````````````````````

## Invalid Option

```````````````````````````````` example
# H1
## H2
.. toc::
   :depth: s
.
<h1 id="toc_1">H1</h1>
<h2 id="toc_2">H2</h2>
<div class="error">TOC depth MUST be integer</div>
````````````````````````````````

## Complex

```````````````````````````````` example
# H1
## H2
### H3
#### H4
# H1 B
# H1 `C`

.. toc:: Table of Contents
   :depth: 3
.
<h1 id="toc_1">H1</h1>
<h2 id="toc_2">H2</h2>
<h3 id="toc_3">H3</h3>
<h4 id="toc_4">H4</h4>
<h1 id="toc_5">H1 B</h1>
<h1 id="toc_6">H1 <code>C</code></h1>
<section class="toc">
<h1>Table of Contents</h1>
<ul>
<li><a href="#toc_1">H1</a>
<ul>
<li><a href="#toc_2">H2</a>
<ul>
<li><a href="#toc_3">H3</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#toc_5">H1 B</a></li>
<li><a href="#toc_6">H1 C</a></li>
</ul>
</section>
````````````````````````````````

## Insane

```````````````````````````````` example
# H1
### H3
## H2
#### H4
### H3 B
# H1 B
.. toc::
.
<h1 id="toc_1">H1</h1>
<h3 id="toc_2">H3</h3>
<h2 id="toc_3">H2</h2>
<h4 id="toc_4">H4</h4>
<h3 id="toc_5">H3 B</h3>
<h1 id="toc_6">H1 B</h1>
<section class="toc">
<ul>
<li><a href="#toc_1">H1</a>
<ul>
<li><a href="#toc_2">H3</a></li>
<li><a href="#toc_3">H2</a>
<ul>
<li><a href="#toc_5">H3 B</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#toc_6">H1 B</a></li>
</ul>
</section>
````````````````````````````````

```````````````````````````````` example
### H3
## H2
# H1
.. toc::
.
<h3 id="toc_1">H3</h3>
<h2 id="toc_2">H2</h2>
<h1 id="toc_3">H1</h1>
<section class="toc">
<ul>
<li><a href="#toc_1">H3</a></li>
<li><a href="#toc_2">H2</a></li>
<li><a href="#toc_3">H1</a></li>
</ul>
</section>
````````````````````````````````

## Link in Heading


```````````````````````````````` example
# [foo](/bar)
.. toc::
.
<h1 id="toc_1"><a href="/bar">foo</a></h1>
<section class="toc">
<ul>
<li><a href="#toc_1">foo</a></li>
</ul>
</section>
````````````````````````````````

## HTML in Heading

```````````````````````````````` example
# <em>H1</em>
.. toc::
.
<h1 id="toc_1"><em>H1</em></h1>
<section class="toc">
<ul>
<li><a href="#toc_1">H1</a></li>
</ul>
</section>
````````````````````````````````
</section>
"""
            )
        self.assertTrue('Could not include self' in html)
        self.assertTrue('Could not find file' in html)
        self.assertTrue('<blockquote>' in html)
        self.assertTrue('# Table of Contents' in html)

    def test_include_missing_source_none_1_str_emp_0(self):
        md = create_markdown(plugins=[DirectiveInclude()])
        s = ''
        html = md(s)

    def test_include_missing_source_none_1_none_0(self):
        md = create_markdown(plugins=[DirectiveInclude()])
        s = None
        html = md(s)

    def test_ast_include_str_emp_1_none_4(self):
        md = create_markdown(renderer='ast', plugins=[DirectiveInclude()])
        filepath = os.path.join(ROOT, '')
        s = '.. include:: hello.txt'
        tokens = md.parse(s, {'__file__': filepath})
        self.assertEqual(tokens, [{'type': 'block_error', 'children':
            'Could not find file: hello.txt'}])

    def test_ast_include_none_7_str_hlf_2_numb_add_0(self):
        md = create_markdown(renderer='ast', plugins=[DirectiveInclude()])
        filepath = os.path.join(ROOT, 'include/foo.txt')
        s = '. include::'
        tokens = md.parse(s, {'__file__': filepath})
        self.assertEqual(tokens, [{'type': 'paragraph', 'children': [{
            'type': 'text', 'text': '. include::'}]}])
        with self.assertRaises(IndexError) as excep_info:
            token = tokens[1]
        self.assertEqual(excep_info.exception.args, (
            'list index out of range',))

    def test_ast_include_none_2_str_dbl_5_none_3(self):
        md = create_markdown(renderer='ast', plugins=[DirectiveInclude()])
        filepath = os.path.join(ROOT, 'include/foo.txt')
        s = None
        tokens = md.parse(s, {'__file__': filepath})
        self.assertEqual(tokens, [{'type': 'newline'}])
