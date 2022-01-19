"""
Python Markdown

A Python implementation of John Gruber's Markdown.

Documentation: https://python-markdown.github.io/
GitHub: https://github.com/Python-Markdown/markdown/
PyPI: https://pypi.org/project/Markdown/

Started by Manfred Stienstra (http://www.dwerg.net/).
Maintained for a few years by Yuri Takhteyev (http://www.freewisdom.org).
Currently maintained by Waylan Limberg (https://github.com/waylan),
Dmitry Shachnev (https://github.com/mitya57) and Isaac Muse (https://github.com/facelessuser).

Copyright 2007-2018 The Python Markdown Project (v. 1.7 and later)
Copyright 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b)
Copyright 2004 Manfred Stienstra (the original version)

License: BSD (see LICENSE.md for details).

Python-Markdown Extension Regression Tests
==========================================

A collection of regression tests to confirm that the included extensions
continue to work as advertised. This used to be accomplished by doctests.
"""
import unittest
import markdown


class TestExtensionClass(unittest.TestCase):
    """ Test markdown.extensions.Extension. """

    def setUp(self):


        class TestExtension(markdown.extensions.Extension):
            config = {'foo': ['bar', 'Description of foo'], 'bar': ['baz',
                'Description of bar']}
        self.ext = TestExtension()
        self.ExtKlass = TestExtension

    def testGetConfig(self):
        self.assertEqual(self.ext.getConfig('foo'), 'bar')

    def testGetConfigDefault(self):
        self.assertEqual(self.ext.getConfig('baz'), '')
        self.assertEqual(self.ext.getConfig('baz', default='missing'),
            'missing')

    def testGetConfigs(self):
        self.assertEqual(self.ext.getConfigs(), {'foo': 'bar', 'bar': 'baz'})

    def testGetConfigInfo(self):
        self.assertEqual(dict(self.ext.getConfigInfo()), dict([('foo',
            'Description of foo'), ('bar', 'Description of bar')]))

    def testSetConfig(self):
        self.ext.setConfig('foo', 'baz')
        self.assertEqual(self.ext.getConfigs(), {'foo': 'baz', 'bar': 'baz'})

    def testSetConfigWithBadKey(self):
        self.assertRaises(KeyError, self.ext.setConfig, 'bad', 'baz')

    def testConfigAsKwargsOnInit(self):
        ext = self.ExtKlass(foo='baz', bar='blah')
        self.assertEqual(ext.getConfigs(), {'foo': 'baz', 'bar': 'blah'})

    def testSetConfig_call_dup_0_none_1(self):
        self.ext.setConfig('foo', None)
        with self.assertRaises(ValueError) as excep_info:
            self.ext.setConfig('foo', 'baz')
        self.assertEqual(excep_info.exception.args, (
            "Cannot parse bool value: 'baz'",))
        self.ext.getConfigs()

    def testSetConfig_none_1_call_dup_0(self):
        self.ext.setConfig('foo', None)
        self.ext.setConfig('foo', None)
        self.ext.getConfigs()


class TestAbbr(unittest.TestCase):
    """ Test abbr extension. """

    def setUp(self):
        self.md = markdown.Markdown(extensions=['abbr'])

    def testSimpleAbbr(self):
        """ Test Abbreviations. """
        text = (
            'Some text with an ABBR and a REF. Ignore REFERENCE and ref.' +
            """

*[ABBR]: Abbreviation
""" + '*[REF]: Abbreviation Reference')
        self.assertEqual(self.md.convert(text),
            '<p>Some text with an <abbr title="Abbreviation">ABBR</abbr> and a <abbr title="Abbreviation Reference">REF</abbr>. Ignore REFERENCE and ref.</p>'
            )

    def testNestedAbbr(self):
        """ Test Nested Abbreviations. """
        text = '[ABBR](/foo) and _ABBR_\n\n' + '*[ABBR]: Abreviation'
        self.assertEqual(self.md.convert(text),
            '<p><a href="/foo"><abbr title="Abreviation">ABBR</abbr></a> and <em><abbr title="Abreviation">ABBR</abbr></em></p>'
            )

    def testSimpleAbbr_str_hlf_2(self):
        """ Test Abbreviations. """
        text = (
            'Some text with an ABBR and a REF. Ignore REFERENCE and ref.' +
            'BR]: Abbrevi' + '*[REF]: Abbreviation Reference')
        self.assertEqual(self.md.convert(text),
            '<p>Some text with an ABBR and a REF. Ignore REFERENCE and ref.BR]: Abbrevi*[REF]: Abbreviation Reference</p>'
            )

    def testSimpleAbbr_str_emp_1(self):
        """ Test Abbreviations. """
        text = ('' + '\n\n*[ABBR]: Abbreviation\n' +
            '*[REF]: Abbreviation Reference')
        self.assertEqual(self.md.convert(text), '')

    def testSimpleAbbr_str_dbl_2(self):
        """ Test Abbreviations. """
        text = (
            'Some text with an ABBR and a REF. Ignore REFERENCE and ref.' +
            """

*[ABBR]: Abbreviation


*[ABBR]: Abbreviation
""" +
            '*[REF]: Abbreviation Reference')
        self.assertEqual(self.md.convert(text),
            '<p>Some text with an <abbr title="Abbreviation">ABBR</abbr> and a <abbr title="Abbreviation Reference">REF</abbr>. Ignore REFERENCE and ref.</p>'
            )

    def testNestedAbbr_str_dbl_1_str_hlf_1(self):
        """ Test Nested Abbreviations. """
        text = 'BR](/foo) and _ABBR_\n\n[AB' + '*[ABBR]: Abreviation'
        self.assertEqual(self.md.convert(text),
            '<p>BR](/foo) and <em>ABBR</em></p>')

    def testNestedAbbr_str_dbl_2_call_dup_0_str_hlf_2(self):
        """ Test Nested Abbreviations. """
        text = '[ABBR](/foo) and _ABBR_\n\n' + 'ABBR]: Abreviation*['
        self.assertEqual(self.md.convert(text),
            """<p><a href="/foo">ABBR</a> and <em>ABBR</em></p>
<p>ABBR]: Abreviation*[</p>"""
            )
        self.assertEqual(self.md.convert(text),
            """<p><a href="/foo">ABBR</a> and <em>ABBR</em></p>
<p>ABBR]: Abreviation*[</p>"""
            )

    def testNestedAbbr_str_emp_2_str_emp_1(self):
        """ Test Nested Abbreviations. """
        text = '' + ''
        self.assertEqual(self.md.convert(text), '')


class TestMetaData(unittest.TestCase):
    """ Test MetaData extension. """

    def setUp(self):
        self.md = markdown.Markdown(extensions=['meta'])

    def testBasicMetaData(self):
        """ Test basic metadata. """
        text = """Title: A Test Doc.
Author: Waylan Limberg
        John Doe
Blank_Data:

The body. This is paragraph one."""
        self.assertEqual(self.md.convert(text),
            '<p>The body. This is paragraph one.</p>')
        self.assertEqual(self.md.Meta, {'author': ['Waylan Limberg',
            'John Doe'], 'blank_data': [''], 'title': ['A Test Doc.']})

    def testYamlMetaData(self):
        """ Test metadata specified as simple YAML. """
        text = """---
Title: A Test Doc.
Author: [Waylan Limberg, John Doe]
Blank_Data:
---

The body. This is paragraph one."""
        self.assertEqual(self.md.convert(text),
            '<p>The body. This is paragraph one.</p>')
        self.assertEqual(self.md.Meta, {'author': [
            '[Waylan Limberg, John Doe]'], 'blank_data': [''], 'title': [
            'A Test Doc.']})

    def testMissingMetaData(self):
        """ Test document without Meta Data. """
        text = '    Some Code - not extra lines of meta data.'
        self.assertEqual(self.md.convert(text),
            """<pre><code>Some Code - not extra lines of meta data.
</code></pre>"""
            )
        self.assertEqual(self.md.Meta, {})

    def testMetaDataWithoutNewline(self):
        """ Test doocument with only metadata and no newline at end."""
        text = 'title: No newline'
        self.assertEqual(self.md.convert(text), '')
        self.assertEqual(self.md.Meta, {'title': ['No newline']})

    def testMetaDataReset(self):
        """ Test that reset call remove Meta entirely """
        text = """Title: A Test Doc.
Author: Waylan Limberg
        John Doe
Blank_Data:

The body. This is paragraph one."""
        self.md.convert(text)
        self.md.reset()
        self.assertEqual(self.md.Meta, {})

    def testBasicMetaData_str_dbl_1(self):
        """ Test basic metadata. """
        text = """Title: A Test Doc.
Author: Waylan Limberg
        John Doe
Blank_Data:

The body. This is paragraph one.Title: A Test Doc.
Author: Waylan Limberg
        John Doe
Blank_Data:

The body. This is paragraph one."""
        self.assertEqual(self.md.convert(text),
            """<p>The body. This is paragraph one.Title: A Test Doc.
Author: Waylan Limberg
        John Doe
Blank_Data:</p>
<p>The body. This is paragraph one.</p>"""
            )
        self.assertEqual(self.md.Meta, {'title': ['A Test Doc.'], 'author':
            ['Waylan Limberg', 'John Doe'], 'blank_data': ['']})

    def testBasicMetaData_str_hlf_1(self):
        """ Test basic metadata. """
        text = '     John Doe\nBlank_Data:\n\nThe body. This is paragra'
        self.assertEqual(self.md.convert(text),
            """<pre><code> John Doe
</code></pre>
<p>Blank_Data:</p>
<p>The body. This is paragra</p>"""
            )
        self.assertEqual(self.md.Meta, {})

    def testBasicMetaData_str_emp_1(self):
        """ Test basic metadata. """
        text = ''
        self.assertEqual(self.md.convert(text), '')
        self.assertEqual(self.md.Meta, {})

    def testBasicMetaData_none_1(self):
        """ Test basic metadata. """
        text = None
        with self.assertRaises(AttributeError) as excep_info:
            self.md.convert(text)
        self.assertEqual(excep_info.exception.args, (
            "'NoneType' object has no attribute 'strip'",))
        self.assertEqual(self.md.Meta, {})

    def testYamlMetaData_str_hlf_1_str_hlf_1_str_dbl_1(self):
        """ Test metadata specified as simple YAML. """
        text = 'k_Data:\n---\n\nThe body. Thik_Data:\n---\n\nThe body. Thi'
        self.assertEqual(self.md.convert(text),
            """<h2>The body. Thik_Data:</h2>
<p>The body. Thi</p>""")
        self.assertEqual(self.md.Meta, {'k_data': ['']})

    def testYamlMetaData_str_dbl_1(self):
        """ Test metadata specified as simple YAML. """
        text = """---
Title: A Test Doc.
Author: [Waylan Limberg, John Doe]
Blank_Data:
---

The body. This is paragraph one.---
Title: A Test Doc.
Author: [Waylan Limberg, John Doe]
Blank_Data:
---

The body. This is paragraph one."""
        self.assertEqual(self.md.convert(text),
            """<p>The body. This is paragraph one.---
Title: A Test Doc.
Author: [Waylan Limberg, John Doe]
Blank_Data:</p>
<hr />
<p>The body. This is paragraph one.</p>"""
            )
        self.assertEqual(self.md.Meta, {'title': ['A Test Doc.'], 'author':
            ['[Waylan Limberg, John Doe]'], 'blank_data': ['']})

    def testYamlMetaData_str_hlf_0_str_hlf_1_str_dbl_1(self):
        """ specified as simple"""
        text = """
Title: A Test Doc.
Author: [Waylan Limberg, John Doe
Title: A Test Doc.
Author: [Waylan Limberg, John Doe"""
        self.assertEqual(self.md.convert(text),
            """<p>Title: A Test Doc.
Author: [Waylan Limberg, John Doe
Title: A Test Doc.
Author: [Waylan Limberg, John Doe</p>"""
            )
        self.assertEqual(self.md.Meta, {})

    def testYamlMetaData_str_hlf_0_str_hlf_1(self):
        """ specified as simple"""
        text = '\nTitle: A Test Doc.\nAuthor: [Waylan Limberg, John Doe'
        self.assertEqual(self.md.convert(text),
            """<p>Title: A Test Doc.
Author: [Waylan Limberg, John Doe</p>""")
        self.assertEqual(self.md.Meta, {})

    def testMissingMetaData_str_hlf_1_call_add_0_str_hlf_1(self):
        """ Test document without Meta Data. """
        text = ' - not extr'
        self.assertEqual(self.md.convert(text),
            '<ul>\n<li>not extr</li>\n</ul>')
        self.assertEqual(self.md.Meta, {})


class TestWikiLinks(unittest.TestCase):
    """ Test Wikilinks Extension. """

    def setUp(self):
        self.md = markdown.Markdown(extensions=['wikilinks'])
        self.text = 'Some text with a [[WikiLink]].'

    def testBasicWikilinks(self):
        """ Test [[wikilinks]]. """
        self.assertEqual(self.md.convert(self.text),
            '<p>Some text with a <a class="wikilink" href="/WikiLink/">WikiLink</a>.</p>'
            )

    def testWikilinkWhitespace(self):
        """ Test whitespace in wikilinks. """
        self.assertEqual(self.md.convert('[[ foo bar_baz ]]'),
            '<p><a class="wikilink" href="/foo_bar_baz/">foo bar_baz</a></p>')
        self.assertEqual(self.md.convert('foo [[ ]] bar'), '<p>foo  bar</p>')

    def testSimpleSettings(self):
        """ Test Simple Settings. """
        self.assertEqual(markdown.markdown(self.text, extensions=[markdown.
            extensions.wikilinks.WikiLinkExtension(base_url='/wiki/',
            end_url='.html', html_class='foo')]),
            '<p>Some text with a <a class="foo" href="/wiki/WikiLink.html">WikiLink</a>.</p>'
            )

    def testComplexSettings(self):
        """ Test Complex Settings. """
        md = markdown.Markdown(extensions=['wikilinks'], extension_configs=
            {'wikilinks': [('base_url', 'http://example.com/'), ('end_url',
            '.html'), ('html_class', '')]}, safe_mode=True)
        self.assertEqual(md.convert(self.text),
            '<p>Some text with a <a href="http://example.com/WikiLink.html">WikiLink</a>.</p>'
            )

    def testWikilinksMetaData(self):
        """ test MetaData with Wikilinks Extension. """
        text = """wiki_base_url: http://example.com/
wiki_end_url:   .html
wiki_html_class:

Some text with a [[WikiLink]]."""
        md = markdown.Markdown(extensions=['meta', 'wikilinks'])
        self.assertEqual(md.convert(text),
            '<p>Some text with a <a href="http://example.com/WikiLink.html">WikiLink</a>.</p>'
            )
        self.assertEqual(md.convert('No [[MetaData]] here.'),
            '<p>No <a class="wikilink" href="/MetaData/">MetaData</a> here.</p>'
            )

    def testURLCallback(self):
        """ Test used of a custom URL builder. """
        from markdown.extensions.wikilinks import WikiLinkExtension

        def my_url_builder(label, base, end):
            return '/bar/'
        md = markdown.Markdown(extensions=[WikiLinkExtension(build_url=
            my_url_builder)])
        self.assertEqual(md.convert('[[foo]]'),
            '<p><a class="wikilink" href="/bar/">foo</a></p>')

    def testWikilinkWhitespace_str_emp_1(self):
        """ Test whitespace in wikilinks. """
        self.assertEqual(self.md.convert(''), '')
        self.assertEqual(self.md.convert('foo [[ ]] bar'), '<p>foo  bar</p>')

    def testWikilinkWhitespace_str_dbl_1_str_hlf_1(self):
        """ Test whitespace in wikilinks. """
        self.assertEqual(self.md.convert('foo bar_baz ]][[ '),
            '<p>foo bar_baz ]][[ </p>')
        self.assertEqual(self.md.convert('foo [[ ]] bar'), '<p>foo  bar</p>')

    def testWikilinkWhitespace_str_dbl_1(self):
        """ Test whitespace in wikilinks. """
        self.assertEqual(self.md.convert(
            '[[ foo bar_baz ]][[ foo bar_baz ]]'),
            '<p><a class="wikilink" href="/foo_bar_baz/">foo bar_baz</a><a class="wikilink" href="/foo_bar_baz/">foo bar_baz</a></p>'
            )
        self.assertEqual(self.md.convert('foo [[ ]] bar'), '<p>foo  bar</p>')

    def testComplexSettings_str_dbl_1(self):
        """ Test Complex Settings. """
        with self.assertRaises(ModuleNotFoundError) as excep_info:
            md = markdown.Markdown(extensions=['wikilinkswikilinks'],
                extension_configs={'wikilinks': [('base_url',
                'http://example.com/'), ('end_url', '.html'), ('html_class',
                '')]}, safe_mode=True)
        self.assertEqual(excep_info.exception.args, (
            'Failed loading extension "wikilinkswikilinks".',))
        self.assertEqual(excep_info.exception.msg,
            "No module named 'wikilinkswikilinks'")
        self.assertEqual(excep_info.exception.name, 'wikilinkswikilinks')
        self.assertIsNone(excep_info.exception.path)

    def testComplexSettings_none_1(self):
        """ Test Complex Settings. """
        md = markdown.Markdown(extensions=[None], extension_configs={
            'wikilinks': [('base_url', 'http://example.com/'), ('end_url',
            '.html'), ('html_class', '')]}, safe_mode=True)
        self.assertEqual(md.convert(self.text),
            '<p>Some text with a [[WikiLink]].</p>')

    def testComplexSettings_str_emp_1(self):
        """ Test Complex Settings. """
        with self.assertRaises(ValueError) as excep_info:
            md = markdown.Markdown(extensions=[''], extension_configs={
                'wikilinks': [('base_url', 'http://example.com/'), (
                'end_url', '.html'), ('html_class', '')]}, safe_mode=True)
        self.assertEqual(excep_info.exception.args, ('Empty module name',))

    def testWikilinksMetaData_none_4_str_hlf_1(self):
        """ test MetaData with Wikilinks Extension. """
        text = 'base_url: http://example.com/\nwiki_end_url:   .html\n'
        md = markdown.Markdown(extensions=['meta', 'wikilinks'])
        self.assertEqual(md.convert(text), '')
        with self.assertRaises(AttributeError) as excep_info:
            md.convert(None)
        self.assertEqual(excep_info.exception.args, (
            "'NoneType' object has no attribute 'strip'",))


class TestAdmonition(unittest.TestCase):
    """ Test Admonition Extension. """

    def setUp(self):
        self.md = markdown.Markdown(extensions=['admonition'])

    def testRE(self):
        RE = self.md.parser.blockprocessors['admonition'].RE
        tests = [('!!! note', ('note', None)), ('!!! note "Please Note"', (
            'note', 'Please Note')), ('!!! note ""', ('note', ''))]
        for test, expected in tests:
            self.assertEqual(RE.match(test).groups(), expected)


class TestTOC(unittest.TestCase):
    """ Test TOC Extension. """

    def assertStartsWith(self, expectedPrefix, text, msg=None):
        if not text.startswith(expectedPrefix):
            if len(expectedPrefix) + 5 < len(text):
                text = text[:len(expectedPrefix) + 5] + '...'
            standardMsg = '{} not found at the start of {}'.format(repr(
                expectedPrefix), repr(text))
            self.fail(self._formatMessage(msg, standardMsg))

    def setUp(self):
        self.md = markdown.Markdown(extensions=['toc'])

    def testMarker(self):
        """ Test TOC with a Marker. """
        text = '[TOC]\n\n# Header 1\n\n## Header 2'
        self.assertEqual(self.md.convert(text),
            """<div class="toc">
<ul>
<li><a href="#header-1">Header 1</a><ul>
<li><a href="#header-2">Header 2</a></li>
</ul>
</li>
</ul>
</div>
<h1 id="header-1">Header 1</h1>
<h2 id="header-2">Header 2</h2>"""
            )

    def testNoMarker(self):
        """ Test TOC without a Marker. """
        text = '# Header 1\n\n## Header 2'
        self.assertEqual(self.md.convert(text),
            """<h1 id="header-1">Header 1</h1>
<h2 id="header-2">Header 2</h2>"""
            )
        self.assertEqual(self.md.toc,
            """<div class="toc">
<ul>
<li><a href="#header-1">Header 1</a><ul>
<li><a href="#header-2">Header 2</a></li>
</ul>
</li>
</ul>
</div>
"""
            )

    def testAlternateMarker(self):
        """ Test TOC with user defined marker. """
        md = markdown.Markdown(extensions=[markdown.extensions.toc.
            TocExtension(marker='{{marker}}')])
        text = '{{marker}}\n\n# Header 1\n\n## Header 2'
        self.assertEqual(md.convert(text),
            """<div class="toc">
<ul>
<li><a href="#header-1">Header 1</a><ul>
<li><a href="#header-2">Header 2</a></li>
</ul>
</li>
</ul>
</div>
<h1 id="header-1">Header 1</h1>
<h2 id="header-2">Header 2</h2>"""
            )

    def testDisabledMarker(self):
        """ Test TOC with disabled marker. """
        md = markdown.Markdown(extensions=[markdown.extensions.toc.
            TocExtension(marker='')])
        text = '[TOC]\n\n# Header 1\n\n## Header 2'
        self.assertEqual(md.convert(text),
            """<p>[TOC]</p>
<h1 id="header-1">Header 1</h1>
<h2 id="header-2">Header 2</h2>"""
            )
        self.assertStartsWith('<div class="toc">', md.toc)

    def testReset(self):
        """ Test TOC Reset. """
        self.assertEqual(self.md.toc, '')
        self.md.convert('# Header 1\n\n## Header 2')
        self.assertStartsWith('<div class="toc">', self.md.toc)
        self.md.reset()
        self.assertEqual(self.md.toc, '')
        self.assertEqual(self.md.toc_tokens, [])

    def testUniqueIds(self):
        """ Test Unique IDs. """
        text = '#Header\n#Header\n#Header'
        self.assertEqual(self.md.convert(text),
            """<h1 id="header">Header</h1>
<h1 id="header_1">Header</h1>
<h1 id="header_2">Header</h1>"""
            )
        self.assertEqual(self.md.toc,
            """<div class="toc">
<ul>
<li><a href="#header">Header</a></li>
<li><a href="#header_1">Header</a></li>
<li><a href="#header_2">Header</a></li>
</ul>
</div>
"""
            )
        self.assertEqual(self.md.toc_tokens, [{'level': 1, 'id': 'header',
            'name': 'Header', 'children': []}, {'level': 1, 'id':
            'header_1', 'name': 'Header', 'children': []}, {'level': 1,
            'id': 'header_2', 'name': 'Header', 'children': []}])

    def testHtmlEntities(self):
        """ Test Headers with HTML Entities. """
        text = '# Foo &amp; bar'
        self.assertEqual(self.md.convert(text),
            '<h1 id="foo-bar">Foo &amp; bar</h1>')
        self.assertEqual(self.md.toc,
            """<div class="toc">
<ul>
<li><a href="#foo-bar">Foo &amp; bar</a></li>
</ul>
</div>
"""
            )
        self.assertEqual(self.md.toc_tokens, [{'level': 1, 'id': 'foo-bar',
            'name': 'Foo &amp; bar', 'children': []}])

    def testHtmlSpecialChars(self):
        """ Test Headers with HTML special characters. """
        text = '# Foo > & bar'
        self.assertEqual(self.md.convert(text),
            '<h1 id="foo-bar">Foo &gt; &amp; bar</h1>')
        self.assertEqual(self.md.toc,
            """<div class="toc">
<ul>
<li><a href="#foo-bar">Foo &gt; &amp; bar</a></li>
</ul>
</div>
"""
            )
        self.assertEqual(self.md.toc_tokens, [{'level': 1, 'id': 'foo-bar',
            'name': 'Foo &gt; &amp; bar', 'children': []}])

    def testRawHtml(self):
        """ Test Headers with raw HTML. """
        text = '# Foo <b>Bar</b> Baz.'
        self.assertEqual(self.md.convert(text),
            '<h1 id="foo-bar-baz">Foo <b>Bar</b> Baz.</h1>')
        self.assertEqual(self.md.toc,
            """<div class="toc">
<ul>
<li><a href="#foo-bar-baz">Foo Bar Baz.</a></li>
</ul>
</div>
"""
            )
        self.assertEqual(self.md.toc_tokens, [{'level': 1, 'id':
            'foo-bar-baz', 'name': 'Foo Bar Baz.', 'children': []}])

    def testBaseLevel(self):
        """ Test Header Base Level. """
        md = markdown.Markdown(extensions=[markdown.extensions.toc.
            TocExtension(baselevel=5)])
        text = '# Some Header\n\n## Next Level\n\n### Too High'
        self.assertEqual(md.convert(text),
            """<h5 id="some-header">Some Header</h5>
<h6 id="next-level">Next Level</h6>
<h6 id="too-high">Too High</h6>"""
            )
        self.assertEqual(md.toc,
            """<div class="toc">
<ul>
<li><a href="#some-header">Some Header</a><ul>
<li><a href="#next-level">Next Level</a></li>
<li><a href="#too-high">Too High</a></li>
</ul>
</li>
</ul>
</div>
"""
            )
        self.assertEqual(md.toc_tokens, [{'level': 5, 'id': 'some-header',
            'name': 'Some Header', 'children': [{'level': 6, 'id':
            'next-level', 'name': 'Next Level', 'children': []}, {'level': 
            6, 'id': 'too-high', 'name': 'Too High', 'children': []}]}])

    def testHeaderInlineMarkup(self):
        """ Test Headers with inline markup. """
        text = '#Some *Header* with [markup](http://example.com).'
        self.assertEqual(self.md.convert(text),
            '<h1 id="some-header-with-markup">Some <em>Header</em> with <a href="http://example.com">markup</a>.</h1>'
            )
        self.assertEqual(self.md.toc,
            """<div class="toc">
<ul>
<li><a href="#some-header-with-markup">Some Header with markup.</a></li>
</ul>
</div>
"""
            )
        self.assertEqual(self.md.toc_tokens, [{'level': 1, 'id':
            'some-header-with-markup', 'name': 'Some Header with markup.',
            'children': []}])

    def testTitle(self):
        """ Test TOC Title. """
        md = markdown.Markdown(extensions=[markdown.extensions.toc.
            TocExtension(title='Table of Contents')])
        md.convert('# Header 1\n\n## Header 2')
        self.assertStartsWith(
            '<div class="toc"><span class="toctitle">Table of Contents</span><ul>'
            , md.toc)

    def testWithAttrList(self):
        """ Test TOC with attr_list Extension. """
        md = markdown.Markdown(extensions=['toc', 'attr_list'])
        text = """# Header 1

## Header 2 { #foo }

## Header 3 { data-toc-label="Foo Bar" }

# Header 4 { data-toc-label="Foo > Baz" }

# Header 5 { data-toc-label="Foo <b>Quux</b>" }"""
        self.assertEqual(md.convert(text),
            """<h1 id="header-1">Header 1</h1>
<h2 id="foo">Header 2</h2>
<h2 id="header-3">Header 3</h2>
<h1 id="header-4">Header 4</h1>
<h1 id="header-5">Header 5</h1>"""
            )
        self.assertEqual(md.toc,
            """<div class="toc">
<ul>
<li><a href="#header-1">Header 1</a><ul>
<li><a href="#foo">Header 2</a></li>
<li><a href="#header-3">Foo Bar</a></li>
</ul>
</li>
<li><a href="#header-4">Foo &gt; Baz</a></li>
<li><a href="#header-5">Foo Quux</a></li>
</ul>
</div>
"""
            )
        self.assertEqual(md.toc_tokens, [{'level': 1, 'id': 'header-1',
            'name': 'Header 1', 'children': [{'level': 2, 'id': 'foo',
            'name': 'Header 2', 'children': []}, {'level': 2, 'id':
            'header-3', 'name': 'Foo Bar', 'children': []}]}, {'level': 1,
            'id': 'header-4', 'name': 'Foo &gt; Baz', 'children': []}, {
            'level': 1, 'id': 'header-5', 'name': 'Foo Quux', 'children': []}])

    def testUniqueFunc(self):
        """ Test 'unique' function. """
        from markdown.extensions.toc import unique
        ids = {'foo'}
        self.assertEqual(unique('foo', ids), 'foo_1')
        self.assertEqual(ids, {'foo', 'foo_1'})

    def testTocInHeaders(self):
        text = '[TOC]\n#[TOC]'
        self.assertEqual(self.md.convert(text),
            """<div class="toc">
<ul>
<li><a href="#toc">[TOC]</a></li>
</ul>
</div>
<h1 id="toc">[TOC]</h1>"""
            )
        text = '#[TOC]\n[TOC]'
        self.assertEqual(self.md.convert(text),
            """<h1 id="toc">[TOC]</h1>
<div class="toc">
<ul>
<li><a href="#toc">[TOC]</a></li>
</ul>
</div>"""
            )
        text = '[TOC]\n# *[TOC]*'
        self.assertEqual(self.md.convert(text),
            """<div class="toc">
<ul>
<li><a href="#toc">[TOC]</a></li>
</ul>
</div>
<h1 id="toc"><em>[TOC]</em></h1>"""
            )

    def testMarker_str_emp_0_call_dup_0_str_hlf_0(self):
        """"""
        text = '\n# Header 1\n\n##'
        self.assertEqual(self.md.convert(text),
            """<h1 id="header-1">Header 1</h1>
<h2 id="_1"></h2>""")
        self.assertEqual(self.md.convert(text),
            """<h1 id="header-1">Header 1</h1>
<h2 id="_1"></h2>""")

    def testMarker_str_emp_1(self):
        """ Test TOC with a Marker. """
        text = ''
        self.assertEqual(self.md.convert(text), '')

    def testDisabledMarker_str_chr_0_str_dbl_2_str_hlf_2(self):
        """ Test TOC with disabled marker. """
        md = markdown.Markdown(extensions=[markdown.extensions.toc.
            TocExtension(marker='w')])
        text = 'C]\n\n# Header 1\n\n## Header 2[TO'
        self.assertEqual(md.convert(text),
            """<p>C]</p>
<h1 id="header-1">Header 1</h1>
<h2 id="header-2to">Header 2[TO</h2>"""
            )
        self.assertEqual(md.toc,
            """<div class="toc">
<ul>
<li><a href="#header-1">Header 1</a><ul>
<li><a href="#header-2to">Header 2[TO</a></li>
</ul>
</li>
</ul>
</div>
"""
            )

    def testHtmlEntities_str_dbl_0_str_hlf_1(self):
        """ Test Headers with HTML Entities.  Test Headers with HTML Entities. """
        text = ' &amp; '
        self.assertEqual(self.md.convert(text), '<p>&amp; </p>')
        self.assertEqual(self.md.toc, '<div class="toc">\n<ul></ul>\n</div>\n')
        self.assertEqual(self.md.toc_tokens, [])

    def testHtmlEntities_call_add_0_call_dup_0_str_hlf_1(self):
        """ Test Headers with HTML Entities. """
        text = '&amp; b'
        self.assertEqual(self.md.convert(text), '<p>&amp; b</p>')
        self.assertEqual(self.md.convert(text), '<p>&amp; b</p>')
        self.assertEqual(self.md.toc, '<div class="toc">\n<ul></ul>\n</div>\n')
        self.assertEqual(self.md.toc_tokens, [])

    def testHtmlSpecialChars_str_dbl_0_str_hlf_1(self):
        """ Test Headers with HTML special characters.  Test Headers with HTML special characters. """
        text = '> & ba'
        self.assertEqual(self.md.convert(text),
            '<blockquote>\n<p>&amp; ba</p>\n</blockquote>')
        self.assertEqual(self.md.toc, '<div class="toc">\n<ul></ul>\n</div>\n')
        self.assertEqual(self.md.toc_tokens, [])

    def testRawHtml_str_dbl_0_str_hlf_1(self):
        """ Test Headers with raw HTML.  Test Headers with raw HTML. """
        text = 'oo <b>Bar<'
        self.assertEqual(self.md.convert(text), '<p>oo <b>Bar&lt;</p>')
        self.assertEqual(self.md.toc, '<div class="toc">\n<ul></ul>\n</div>\n')
        self.assertEqual(self.md.toc_tokens, [])

    def testHeaderInlineMarkup_str_hlf_1_str_dbl_1(self):
        """ Test Headers with inline markup. """
        text = ' *Header* with [markup]( *Header* with [markup]('
        self.assertEqual(self.md.convert(text),
            '<p><em>Header</em> with [markup]( <em>Header</em> with [markup](</p>'
            )
        self.assertEqual(self.md.toc, '<div class="toc">\n<ul></ul>\n</div>\n')
        self.assertEqual(self.md.toc_tokens, [])

    def testHeaderInlineMarkup_str_dbl_1_str_hlf_1(self):
        """ Test Headers with inline markup. """
        text = 'er* with [markup](http://example.com).#Some *Head'
        self.assertEqual(self.md.convert(text),
            '<p>er<em> with <a href="http://example.com">markup</a>.#Some </em>Head</p>'
            )
        self.assertEqual(self.md.toc, '<div class="toc">\n<ul></ul>\n</div>\n')
        self.assertEqual(self.md.toc_tokens, [])

    def testHeaderInlineMarkup_str_hlf_0_call_dup_0_str_hlf_1(self):
        """ith inline markup"""
        text = '* with [markup](http://e'
        self.assertEqual(self.md.convert(text),
            '<ul>\n<li>with [markup](http://e</li>\n</ul>')
        self.assertEqual(self.md.convert(text),
            '<ul>\n<li>with [markup](http://e</li>\n</ul>')
        self.assertEqual(self.md.toc, '<div class="toc">\n<ul></ul>\n</div>\n')
        self.assertEqual(self.md.toc_tokens, [])

    def testWithAttrList_str_emp_1(self):
        """ Test TOC with attr_list Extension. """
        with self.assertRaises(ValueError) as excep_info:
            md = markdown.Markdown(extensions=['', 'attr_list'])
        self.assertEqual(excep_info.exception.args, ('Empty module name',))
        text = """# Header 1

## Header 2 { #foo }

## Header 3 { data-toc-label="Foo Bar" }

# Header 4 { data-toc-label="Foo > Baz" }

# Header 5 { data-toc-label="Foo <b>Quux</b>" }"""

    def testWithAttrList_str_emp_2_none_1(self):
        """ Test TOC with attr_list Extension. """
        with self.assertRaises(ValueError) as excep_info:
            md = markdown.Markdown(extensions=[None, ''])
        self.assertEqual(excep_info.exception.args, ('Empty module name',))
        text = """# Header 1

## Header 2 { #foo }

## Header 3 { data-toc-label="Foo Bar" }

# Header 4 { data-toc-label="Foo > Baz" }

# Header 5 { data-toc-label="Foo <b>Quux</b>" }"""

    def testWithAttrList_str_dbl_1(self):
        """ Test TOC with attr_list Extension. """
        with self.assertRaises(ModuleNotFoundError) as excep_info:
            md = markdown.Markdown(extensions=['toctoc', 'attr_list'])
        self.assertEqual(excep_info.exception.args, (
            'Failed loading extension "toctoc".',))
        self.assertEqual(excep_info.exception.msg, "No module named 'toctoc'")
        self.assertEqual(excep_info.exception.name, 'toctoc')
        self.assertIsNone(excep_info.exception.path)
        text = """# Header 1

## Header 2 { #foo }

## Header 3 { data-toc-label="Foo Bar" }

# Header 4 { data-toc-label="Foo > Baz" }

# Header 5 { data-toc-label="Foo <b>Quux</b>" }"""

    def testWithAttrList_str_emp_3_str_hlf_2(self):
        """ Test TOC with attr_list Extension. """
        with self.assertRaises(AttributeError) as excep_info:
            md = markdown.Markdown(extensions=['toc', 'attr'])
        self.assertEqual(excep_info.exception.args, (
            "Failed to initiate extension 'attr': module 'attr' has no attribute 'makeExtension'"
            ,))
        text = ''

    def testWithAttrList_none_1(self):
        """ Test TOC with attr_list Extension. """
        md = markdown.Markdown(extensions=[None, 'attr_list'])
        text = """# Header 1

## Header 2 { #foo }

## Header 3 { data-toc-label="Foo Bar" }

# Header 4 { data-toc-label="Foo > Baz" }

# Header 5 { data-toc-label="Foo <b>Quux</b>" }"""
        self.assertEqual(md.convert(text),
            """<h1>Header 1</h1>
<h2 id="foo">Header 2</h2>
<h2 data-toc-label="Foo Bar">Header 3</h2>
<h1 data-toc-label="Foo &gt; Baz">Header 4</h1>
<h1 data-toc-label="Foo <b>Quux</b>">Header 5</h1>"""
            )
        with self.assertRaises(AttributeError) as excep_info:
            md.toc
        self.assertEqual(excep_info.exception.args, (
            "'Markdown' object has no attribute 'toc'",))
        with self.assertRaises(AttributeError) as excep_info:
            md.toc_tokens
        self.assertEqual(excep_info.exception.args, (
            "'Markdown' object has no attribute 'toc_tokens'",))

    def testWithAttrList_none_0_str_hlf_2_str_dbl_2(self):
        None
        md = markdown.Markdown(extensions=['toc', 'attr_list'])
        text = """r 2 { #foo }

## Header 3 { data-toc-label="Foo Bar" }

# Header 4 { data-toc-labelr 2 { #foo }

## Header 3 { data-toc-label="Foo Bar" }

# Header 4 { data-toc-label"""
        self.assertEqual(md.convert(text),
            """<p>r 2 { #foo }</p>
<h2 id="header-3">Header 3</h2>
<h1 2="2" _="{" data-toc-labelr="data-toc-labelr" id="foo">Header 4</h1>
<h2 id="header-3_1">Header 3</h2>
<h1 id="header-4-data-toc-label">Header 4 { data-toc-label</h1>"""
            )
        self.assertEqual(md.toc,
            """<div class="toc">
<ul>
<li><a href="#header-3">Foo Bar</a></li>
<li><a href="#foo">Header 4</a><ul>
<li><a href="#header-3_1">Foo Bar</a></li>
</ul>
</li>
<li><a href="#header-4-data-toc-label">Header 4 { data-toc-label</a></li>
</ul>
</div>
"""
            )
        self.assertEqual(md.toc_tokens, [{'level': 2, 'id': 'header-3',
            'name': 'Foo Bar', 'children': []}, {'level': 1, 'id': 'foo',
            'name': 'Header 4', 'children': [{'level': 2, 'id':
            'header-3_1', 'name': 'Foo Bar', 'children': []}]}, {'level': 1,
            'id': 'header-4-data-toc-label', 'name':
            'Header 4 { data-toc-label', 'children': []}])

    def testTocInHeaders_str_hlf_2(self):
        text = '[TOC]\n#[TOC]'
        self.assertEqual(self.md.convert(text),
            """<div class="toc">
<ul>
<li><a href="#toc">[TOC]</a></li>
</ul>
</div>
<h1 id="toc">[TOC]</h1>"""
            )
        text = '#[TOC]\n[TOC]'
        self.assertEqual(self.md.convert(text),
            """<h1 id="toc">[TOC]</h1>
<div class="toc">
<ul>
<li><a href="#toc">[TOC]</a></li>
</ul>
</div>"""
            )
        text = 'OC]\n# *'
        self.assertEqual(self.md.convert(text),
            '<p>OC]</p>\n<h1 id="_1">*</h1>')

    def testTocInHeaders_str_dbl_0(self):
        text = '[TOC]\n#[TOC][TOC]\n#[TOC]'
        self.assertEqual(self.md.convert(text),
            """<div class="toc">
<ul>
<li><a href="#toctoc">[TOC][TOC]</a></li>
<li><a href="#toc">[TOC]</a></li>
</ul>
</div>
<h1 id="toctoc">[TOC][TOC]</h1>
<h1 id="toc">[TOC]</h1>"""
            )
        text = '#[TOC]\n[TOC]'
        self.assertEqual(self.md.convert(text),
            """<h1 id="toc">[TOC]</h1>
<div class="toc">
<ul>
<li><a href="#toc">[TOC]</a></li>
</ul>
</div>"""
            )
        text = '[TOC]\n# *[TOC]*'
        self.assertEqual(self.md.convert(text),
            """<div class="toc">
<ul>
<li><a href="#toc">[TOC]</a></li>
</ul>
</div>
<h1 id="toc"><em>[TOC]</em></h1>"""
            )


class TestSmarty(unittest.TestCase):

    def setUp(self):
        config = {'smarty': [('smart_angled_quotes', True), (
            'substitutions', {'ndash': '–', 'mdash': '—', 'ellipsis': '…',
            'left-single-quote': '&sbquo;', 'right-single-quote': '&lsquo;',
            'left-double-quote': '&bdquo;', 'right-double-quote': '&ldquo;',
            'left-angle-quote': '[', 'right-angle-quote': ']'})]}
        self.md = markdown.Markdown(extensions=['smarty'],
            extension_configs=config)

    def testCustomSubstitutions(self):
        text = """<< The "Unicode char of the year 2014"
is the 'mdash': ---
Must not be confused with 'ndash'  (--) ... >>
"""
        correct = """<p>[ The &bdquo;Unicode char of the year 2014&ldquo;
is the &sbquo;mdash&lsquo;: —
Must not be confused with &sbquo;ndash&lsquo;  (–) … ]</p>"""
        self.assertEqual(self.md.convert(text), correct)

    def testCustomSubstitutions_str_emp_0_str_chr_0_none_1(self):
        text = 'i'
        correct = None
        self.assertEqual(self.md.convert(text), '<p>i</p>')

    def testCustomSubstitutions_call_add_0_str_hlf_0(self):
        text = "h': ---\nMust not be confused with 'ndash'  (--) ... >"
        correct = """<p>[ The &bdquo;Unicode char of the year 2014&ldquo;
is the &sbquo;mdash&lsquo;: —
Must not be confused with &sbquo;ndash&lsquo;  (–) … ]</p>"""
        self.assertEqual(self.md.convert(text),
            """<p>h&lsquo;: —
Must not be confused with &sbquo;ndash&lsquo;  (–) … &gt;</p>"""
            )
        self.assertEqual(correct,
            """<p>[ The &bdquo;Unicode char of the year 2014&ldquo;
is the &sbquo;mdash&lsquo;: —
Must not be confused with &sbquo;ndash&lsquo;  (–) … ]</p>"""
            )

    def testCustomSubstitutions_str_dbl_1_str_hlf_0(self):
        text = "\nis the 'mdash': ---\nMust not be confused with 'ndash"
        correct = """<p>[ The &bdquo;Unicode char of the year 2014&ldquo;
is the &sbquo;mdash&lsquo;: —
Must not be confused with &sbquo;ndash&lsquo;  (–) … ]</p><p>[ The &bdquo;Unicode char of the year 2014&ldquo;
is the &sbquo;mdash&lsquo;: —
Must not be confused with &sbquo;ndash&lsquo;  (–) … ]</p>"""
        self.assertEqual(self.md.convert(text),
            """<p>is the &sbquo;mdash&lsquo;: —
Must not be confused with &sbquo;ndash</p>"""
            )
        self.assertEqual(correct,
            """<p>[ The &bdquo;Unicode char of the year 2014&ldquo;
is the &sbquo;mdash&lsquo;: —
Must not be confused with &sbquo;ndash&lsquo;  (–) … ]</p><p>[ The &bdquo;Unicode char of the year 2014&ldquo;
is the &sbquo;mdash&lsquo;: —
Must not be confused with &sbquo;ndash&lsquo;  (–) … ]</p>"""
            )

    def testCustomSubstitutions_none_1_str_emp_0(self):
        text = ''
        correct = None
        self.assertEqual(self.md.convert(text), '')

    def testCustomSubstitutions_none_1_none_0(self):
        text = None
        correct = None
        with self.assertRaises(AttributeError) as excep_info:
            self.md.convert(text)
        self.assertEqual(excep_info.exception.args, (
            "'NoneType' object has no attribute 'strip'",))
