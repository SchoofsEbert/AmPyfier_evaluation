import re
import mistune
from mistune.util import html
from tests import BaseTestCase
IGNORE_CASES = {'setext_headings_002', 'setext_headings_015',
    'setext_headings_003', 'setext_headings_007', 'setext_headings_013',
    'html_blocks_039', 'link_reference_definitions_019', 'block_quotes_008',
    'list_items_005', 'list_items_024', 'list_items_028', 'list_items_039',
    'list_items_040', 'list_items_041', 'lists_007', 'lists_016',
    'lists_017', 'lists_018', 'lists_019', 'block_quotes_005',
    'block_quotes_006', 'block_quotes_011', 'block_quotes_020',
    'block_quotes_023', 'block_quotes_024', 'code_spans_009',
    'code_spans_010', 'entity_and_numeric_character_references_004',
    'entity_and_numeric_character_references_005', 'links_029', 'links_031',
    'links_034', 'links_037', 'links_038', 'links_039', 'links_043',
    'links_045', 'links_046', 'links_047', 'links_049', 'links_050',
    'links_051', 'links_064', 'links_065', 'links_077', 'images_002',
    'images_003', 'images_004', 'images_005', 'images_006', 'images_014',
    'images_018', 'autolinks_002'}
INSANE_CASES = {'fenced_code_blocks_013', 'fenced_code_blocks_015',
    'list_items_033', 'list_items_038', 'link_reference_definitions_002',
    'link_reference_definitions_003', 'link_reference_definitions_004',
    'link_reference_definitions_005', 'link_reference_definitions_007',
    'link_reference_definitions_021', 'links_025', 'links_032', 'links_033',
    'links_041', 'links_060', 'links_082', 'links_084'}
if html is None:
    PY2_IGNORES = {'entity_and_numeric_character_references_001',
        'entity_and_numeric_character_references_002',
        'entity_and_numeric_character_references_003',
        'entity_and_numeric_character_references_008',
        'entity_and_numeric_character_references_009',
        'entity_and_numeric_character_references_010', 'links_016', 'links_019'
        }
else:
    PY2_IGNORES = []
DIFFERENCES = {'tabs_005': lambda s: s.replace('<code>  ', '<code>'),
    'tabs_006': lambda s: s.replace('<code>  ', '<code>'), 'tabs_007': lambda
    s: s.replace('<code>  ', '<code>')}
PASSED = {'tabs', 'thematic', 'atx', 'setext', 'indented', 'fenced',
    'html_blocks', 'link_ref', 'paragraphs', 'blank_lines', 'block_quotes',
    'list_items', 'lists', 'backslash', 'entity', 'code_spans', 'links',
    'images', 'autolinks', 'raw_html', 'hard_line', 'soft_line', 'textual'}


class TestCommonMark(BaseTestCase):

    @classmethod
    def ignore_case(cls, n):
        if n.startswith('emphasis'):
            return True
        if PY2_IGNORES and n in PY2_IGNORES:
            return True
        return n in IGNORE_CASES or n in INSANE_CASES

    def assert_case(self, n, text, html):
        result = mistune.html(text)
        result = re.sub('\\s*\\n+\\s*', '\n', result)
        result = re.sub('>\\n', '>', result)
        result = re.sub('\\n<', '<', result)
        expect = re.sub('\\s*\\n+\\s*', '\n', html)
        expect = re.sub('>\\n', '>', expect)
        expect = re.sub('\\n<', '<', expect)
        if n in DIFFERENCES:
            expect = DIFFERENCES[n](expect)
        self.assertEqual(result, expect)


TestCommonMark.load_fixtures('commonmark.txt')
