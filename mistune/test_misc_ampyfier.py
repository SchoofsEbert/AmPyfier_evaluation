import mistune
from unittest import TestCase


class TestMiscCases(TestCase):

    def test_none(self):
        self.assertEqual(mistune.html(None), '')

    def test_before_parse_hooks(self):

        def _add_name(md, s, state):
            state['name'] = 'test'
            return s, state
        md = mistune.create_markdown()
        md.before_parse_hooks.append(_add_name)
        state = {}
        md.parse('', state)
        self.assertEqual(state['name'], 'test')

    def test_hard_wrap(self):
        renderer = mistune.HTMLRenderer()
        inline = mistune.InlineParser(renderer, hard_wrap=True)
        md = mistune.Markdown(renderer, inline=inline)
        result = md('foo\nbar')
        expected = '<p>foo<br />\nbar</p>'
        self.assertEqual(result.strip(), expected)

    def test_escape_html(self):
        md = mistune.create_markdown(escape=True)
        result = md('<div>1</div>')
        expected = '<p>&lt;div&gt;1&lt;/div&gt;</p>'
        self.assertEqual(result.strip(), expected)
        result = md('<em>1</em>')
        expected = '<p>&lt;em&gt;1&lt;/em&gt;</p>'
        self.assertEqual(result.strip(), expected)

    def test_emphasis(self):
        md = mistune.create_markdown(escape=True)
        result = md('_em_ **strong**')
        expected = '<p><em>em</em> <strong>strong</strong></p>'
        self.assertEqual(result.strip(), expected)

    def test_harmful_links(self):
        result = mistune.html('[h](javAscript:alert)')
        expected = '<p><a href="#harmful-link">h</a></p>'
        self.assertEqual(result.strip(), expected)

    def test_allow_harmful_protocols(self):
        renderer = mistune.HTMLRenderer(allow_harmful_protocols=True)
        md = mistune.Markdown(renderer)
        result = md('[h](javascript:alert)')
        expected = '<p><a href="javascript:alert">h</a></p>'
        self.assertEqual(result.strip(), expected)

    def test_allow_data_protocols(self):
        renderer = mistune.HTMLRenderer(allow_harmful_protocols=['data:'])
        md = mistune.Markdown(renderer)
        result = md('[h](data:alert)')
        expected = '<p><a href="data:alert">h</a></p>'
        self.assertEqual(result.strip(), expected)

    def test_use_plugin(self):
        from mistune.plugins import plugin_url
        md = mistune.Markdown(mistune.HTMLRenderer())
        md.use(plugin_url)

    def test_escape_html_none_4_str_hlf_0(self):
        md = mistune.create_markdown(escape=True)
        result = md('>1</di')
        expected = '<p>&lt;div&gt;1&lt;/div&gt;</p>'
        result.strip()
        self.assertEqual(expected, '<p>&lt;div&gt;1&lt;/div&gt;</p>')
        result = md('<em>1</em>')
        expected = None
        result.strip()

    def test_escape_html_none_4_bool_inv_0(self):
        md = mistune.create_markdown(escape=False)
        result = md('<div>1</div>')
        expected = '<p>&lt;div&gt;1&lt;/div&gt;</p>'
        result.strip()
        self.assertEqual(expected, '<p>&lt;div&gt;1&lt;/div&gt;</p>')
        result = md('<em>1</em>')
        expected = None
        result.strip()

    def test_harmful_links_str_dbl_0_str_hlf_0_none_1(self):
        result = mistune.html('avAscript:alert)[h](j')
        expected = None
        result.strip()
