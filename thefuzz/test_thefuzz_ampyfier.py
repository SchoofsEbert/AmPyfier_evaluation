from __future__ import unicode_literals
import unittest
import re
import sys
import pycodestyle
from thefuzz import fuzz
from thefuzz import process
from thefuzz import utils
from thefuzz.string_processing import StringProcessor
if sys.version_info[0] == 3:
    unicode = str


class StringProcessingTest(unittest.TestCase):

    def test_replace_non_letters_non_numbers_with_whitespace(self):
        strings = ['new york mets - atlanta braves', 'Cães danados',
            'New York //// Mets $$$', 'Ça va?']
        for string in strings:
            proc_string = (StringProcessor.
                replace_non_letters_non_numbers_with_whitespace(string))
            regex = re.compile('(?ui)[\\W]')
            for expr in regex.finditer(proc_string):
                self.assertEqual(expr.group(), ' ')

    def test_dont_condense_whitespace(self):
        s1 = 'new york mets - atlanta braves'
        s2 = 'new york mets atlanta braves'
        p1 = StringProcessor.replace_non_letters_non_numbers_with_whitespace(s1
            )
        p2 = StringProcessor.replace_non_letters_non_numbers_with_whitespace(s2
            )
        self.assertNotEqual(p1, p2)


class UtilsTest(unittest.TestCase):

    def setUp(self):
        self.s1 = 'new york mets'
        self.s1a = 'new york mets'
        self.s2 = 'new YORK mets'
        self.s3 = 'the wonderful new york mets'
        self.s4 = 'new york mets vs atlanta braves'
        self.s5 = 'atlanta braves vs new york mets'
        self.s6 = 'new york mets - atlanta braves'
        self.mixed_strings = [
            'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
            , "C'est la vie", 'Ça va?', 'Cães danados', '¬Camarões assados',
            'a¬ሴ€耀', 'Á']

    def tearDown(self):
        pass

    def test_asciidammit(self):
        for s in self.mixed_strings:
            utils.asciidammit(s)

    def test_asciionly(self):
        for s in self.mixed_strings:
            s = utils.asciidammit(s)
            utils.asciionly(s)

    def test_fullProcess(self):
        for s in self.mixed_strings:
            utils.full_process(s)

    def test_fullProcessForceAscii(self):
        for s in self.mixed_strings:
            utils.full_process(s, force_ascii=True)


class RatioTest(unittest.TestCase):

    def setUp(self):
        self.s1 = 'new york mets'
        self.s1a = 'new york mets'
        self.s2 = 'new YORK mets'
        self.s3 = 'the wonderful new york mets'
        self.s4 = 'new york mets vs atlanta braves'
        self.s5 = 'atlanta braves vs new york mets'
        self.s6 = 'new york mets - atlanta braves'
        self.s7 = 'new york city mets - atlanta braves'
        self.s8 = '{'
        self.s8a = '{'
        self.s9 = '{a'
        self.s9a = '{a'
        self.s10 = 'a{'
        self.s10a = '{b'
        self.cirque_strings = ['cirque du soleil - zarkana - las vegas',
            'cirque du soleil ', 'cirque du soleil las vegas',
            'zarkana las vegas',
            'las vegas cirque du soleil at the bellagio',
            'zarakana - cirque du soleil - bellagio']
        self.baseball_strings = ['new york mets vs chicago cubs',
            'chicago cubs vs chicago white sox',
            'philladelphia phillies vs atlanta braves', 'braves vs mets']

    def tearDown(self):
        pass

    def testEqual(self):
        self.assertEqual(fuzz.ratio(self.s1, self.s1a), 100)
        self.assertEqual(fuzz.ratio(self.s8, self.s8a), 100)
        self.assertEqual(fuzz.ratio(self.s9, self.s9a), 100)

    def testCaseInsensitive(self):
        self.assertNotEqual(fuzz.ratio(self.s1, self.s2), 100)
        self.assertEqual(fuzz.ratio(utils.full_process(self.s1), utils.
            full_process(self.s2)), 100)

    def testPartialRatio(self):
        self.assertEqual(fuzz.partial_ratio(self.s1, self.s3), 100)

    def testTokenSortRatio(self):
        self.assertEqual(fuzz.token_sort_ratio(self.s1, self.s1a), 100)

    def testPartialTokenSortRatio(self):
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s1, self.s1a), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s4, self.s5), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s8, self.s8a,
            full_process=False), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s9, self.s9a,
            full_process=True), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s9, self.s9a,
            full_process=False), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s10, self.s10a,
            full_process=False), 50)

    def testTokenSetRatio(self):
        self.assertEqual(fuzz.token_set_ratio(self.s4, self.s5), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s8, self.s8a,
            full_process=False), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s9, self.s9a,
            full_process=True), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s9, self.s9a,
            full_process=False), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s10, self.s10a,
            full_process=False), 50)

    def testPartialTokenSetRatio(self):
        self.assertEqual(fuzz.partial_token_set_ratio(self.s4, self.s7), 100)

    def testQuickRatioEqual(self):
        self.assertEqual(fuzz.QRatio(self.s1, self.s1a), 100)

    def testQuickRatioCaseInsensitive(self):
        self.assertEqual(fuzz.QRatio(self.s1, self.s2), 100)

    def testQuickRatioNotEqual(self):
        self.assertNotEqual(fuzz.QRatio(self.s1, self.s3), 100)

    def testWRatioEqual(self):
        self.assertEqual(fuzz.WRatio(self.s1, self.s1a), 100)

    def testWRatioCaseInsensitive(self):
        self.assertEqual(fuzz.WRatio(self.s1, self.s2), 100)

    def testWRatioPartialMatch(self):
        self.assertEqual(fuzz.WRatio(self.s1, self.s3), 90)

    def testWRatioMisorderedMatch(self):
        self.assertEqual(fuzz.WRatio(self.s4, self.s5), 95)

    def testWRatioUnicode(self):
        self.assertEqual(fuzz.WRatio(unicode(self.s1), unicode(self.s1a)), 100)

    def testQRatioUnicode(self):
        self.assertEqual(fuzz.WRatio(unicode(self.s1), unicode(self.s1a)), 100)

    def testEmptyStringsScore100(self):
        self.assertEqual(fuzz.ratio('', ''), 100)
        self.assertEqual(fuzz.partial_ratio('', ''), 100)

    def testIssueSeven(self):
        s1 = 'HSINCHUANG'
        s2 = 'SINJHUAN'
        s3 = 'LSINJHUANG DISTRIC'
        s4 = 'SINJHUANG DISTRICT'
        self.assertTrue(fuzz.partial_ratio(s1, s2) > 75)
        self.assertTrue(fuzz.partial_ratio(s1, s3) > 75)
        self.assertTrue(fuzz.partial_ratio(s1, s4) > 75)

    def testRatioUnicodeString(self):
        s1 = 'Á'
        s2 = 'ABCD'
        score = fuzz.ratio(s1, s2)
        self.assertEqual(0, score)

    def testPartialRatioUnicodeString(self):
        s1 = 'Á'
        s2 = 'ABCD'
        score = fuzz.partial_ratio(s1, s2)
        self.assertEqual(0, score)

    def testWRatioUnicodeString(self):
        s1 = 'Á'
        s2 = 'ABCD'
        score = fuzz.WRatio(s1, s2)
        self.assertEqual(0, score)
        s1 = 'психолог'
        s2 = 'психотерапевт'
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)
        s1 = '我了解数学'
        s2 = '我学数学'
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)

    def testQRatioUnicodeString(self):
        s1 = 'Á'
        s2 = 'ABCD'
        score = fuzz.QRatio(s1, s2)
        self.assertEqual(0, score)
        s1 = 'психолог'
        s2 = 'психотерапевт'
        score = fuzz.QRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)
        s1 = '我了解数学'
        s2 = '我学数学'
        score = fuzz.QRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)

    def testQratioForceAscii(self):
        s1 = 'ABCDÁ'
        s2 = 'ABCD'
        score = fuzz.QRatio(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)
        score = fuzz.QRatio(s1, s2, force_ascii=False)
        self.assertLess(score, 100)

    def testQRatioForceAscii(self):
        s1 = 'ABCDÁ'
        s2 = 'ABCD'
        score = fuzz.WRatio(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertLess(score, 100)

    def testTokenSetForceAscii(self):
        s1 = 'ABCDÁ HELPÁ'
        s2 = 'ABCD HELP'
        score = fuzz._token_set(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)
        score = fuzz._token_set(s1, s2, force_ascii=False)
        self.assertLess(score, 100)

    def testTokenSortForceAscii(self):
        s1 = 'ABCDÁ HELPÁ'
        s2 = 'ABCD HELP'
        score = fuzz._token_sort(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)
        score = fuzz._token_sort(s1, s2, force_ascii=False)
        self.assertLess(score, 100)

    def testTokenSetRatio_bool_inv_0(self):
        self.assertEqual(fuzz.token_set_ratio(self.s4, self.s5), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s8, self.s8a,
            full_process=True), 0)
        self.assertEqual(fuzz.token_set_ratio(self.s9, self.s9a,
            full_process=True), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s9, self.s9a,
            full_process=False), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s10, self.s10a,
            full_process=False), 50)

    def testEmptyStringsScore100_none_0(self):
        fuzz.ratio(None, '')
        fuzz.partial_ratio('', '')

    def testEmptyStringsScore100_none_1_str_chr_0(self):
        fuzz.ratio('w', None)
        fuzz.partial_ratio('', '')

    def testIssueSeven_none_6_str_emp_1_str_chr_0(self):
        s1 = 'HSINCHUANG'
        s2 = 'I'
        s3 = 'LSINJHUANG DISTRIC'
        s4 = 'SINJHUANG DISTRICT'
        self.assertTrue(fuzz.partial_ratio(s1, s2) > 75)
        self.assertTrue(fuzz.partial_ratio(s1, s3) > 75)

    def testIssueSeven_str_dbl_0_none_5(self):
        s1 = 'HSINCHUANGHSINCHUANG'
        s2 = 'SINJHUAN'
        s3 = 'LSINJHUANG DISTRIC'
        s4 = 'SINJHUANG DISTRICT'
        self.assertTrue(fuzz.partial_ratio(s1, s2) > 75)
        self.assertFalse(fuzz.partial_ratio(s1, s4) > 75)

    def testIssueSeven_none_6_str_emp_1(self):
        s1 = 'HSINCHUANG'
        s2 = ''
        s3 = 'LSINJHUANG DISTRIC'
        s4 = 'SINJHUANG DISTRICT'
        self.assertFalse(fuzz.partial_ratio(s1, s2) > 75)
        self.assertTrue(fuzz.partial_ratio(s1, s3) > 75)

    def testIssueSeven_str_hlf_0(self):
        s1 = 'CHUAN'
        s2 = 'SINJHUAN'
        s3 = 'LSINJHUANG DISTRIC'
        s4 = 'SINJHUANG DISTRICT'
        self.assertTrue(fuzz.partial_ratio(s1, s2) > 75)
        self.assertTrue(fuzz.partial_ratio(s1, s3) > 75)
        self.assertTrue(fuzz.partial_ratio(s1, s4) > 75)

    def testWRatioUnicodeString_amp(self):
        s1 = 'Á'
        s2 = 'ABCD'
        score = fuzz.WRatio(s1, s2)
        self.assertEqual(score, 0)
        self.assertEqual(score, 0)
        s1 = 'психолог'
        s2 = 'психотерапевт'
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 56)
        self.assertEqual(score, 56)
        s1 = '我了解数学'
        s2 = '我学数学'
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 67)
        self.assertEqual(score, 67)

    def testWRatioUnicodeString_none_6_none_0(self):
        s1 = None
        s2 = 'ABCD'
        score = fuzz.WRatio(s1, s2)
        self.assertEqual(score, 0)
        self.assertEqual(score, 0)
        s1 = 'психолог'
        s2 = 'психотерапевт'
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 56)
        self.assertEqual(score, 56)
        s1 = '我了解数学'
        s2 = None
        self.assertEqual(score, 56)

    def testWRatioUnicodeString_str_emp_2_str_chr_0(self):
        s1 = 'Á'
        s2 = 'ABCD'
        score = fuzz.WRatio(s1, s2)
        self.assertEqual(score, 0)
        self.assertEqual(score, 0)
        s1 = 'Y'
        s2 = 'психотерапевт'
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 0)
        self.assertEqual(score, 0)
        s1 = '我了解数学'
        s2 = '我学数学'
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 67)
        self.assertEqual(score, 67)

    def testWRatioUnicodeString_str_emp_3(self):
        s1 = 'Á'
        s2 = 'ABCD'
        score = fuzz.WRatio(s1, s2)
        self.assertEqual(score, 0)
        self.assertEqual(score, 0)
        s1 = 'психолог'
        s2 = ''
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 0)
        self.assertEqual(score, 0)
        s1 = '我了解数学'
        s2 = '我学数学'
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 67)
        self.assertEqual(score, 67)

    def testWRatioUnicodeString_str_dbl_5_str_hlf_4_str_dbl_5(self):
        s1 = 'Á'
        s2 = 'ABCD'
        score = fuzz.WRatio(s1, s2)
        self.assertEqual(score, 0)
        self.assertEqual(score, 0)
        s1 = 'психолог'
        s2 = 'психотерапевт'
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 56)
        self.assertEqual(score, 56)
        s1 = '解数'
        s2 = '我学数学我学数学我学数学我学数学'
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 45)
        self.assertEqual(score, 45)

    def testWRatioUnicodeString_str_dbl_5_str_hlf_4_none_3(self):
        s1 = 'Á'
        s2 = 'ABCD'
        score = fuzz.WRatio(s1, s2)
        self.assertEqual(score, 0)
        self.assertEqual(score, 0)
        s1 = 'психолог'
        s2 = None
        self.assertEqual(score, 0)
        s1 = '解数'
        s2 = '我学数学我学数学'
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 45)
        self.assertEqual(score, 45)

    def testWRatioUnicodeString_none_6_str_hlf_3(self):
        s1 = 'Á'
        s2 = 'ABCD'
        score = fuzz.WRatio(s1, s2)
        self.assertEqual(score, 0)
        self.assertEqual(score, 0)
        s1 = 'психолог'
        s2 = 'сихоте'
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 57)
        self.assertEqual(score, 57)
        s1 = '我了解数学'
        s2 = None
        self.assertEqual(score, 57)

    def testQRatioUnicodeString_str_emp_3_none_5(self):
        s1 = 'Á'
        s2 = 'ABCD'
        score = fuzz.QRatio(s1, s2)
        self.assertEqual(score, 0)
        self.assertEqual(score, 0)
        s1 = 'психолог'
        s2 = ''
        score = fuzz.QRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 0)
        self.assertEqual(score, 0)
        s1 = None
        s2 = '我学数学'
        self.assertEqual(score, 0)

    def testQRatioUnicodeString_none_3_none_1_none_3(self):
        s1 = 'Á'
        s2 = None
        score = fuzz.QRatio(s1, s2)
        self.assertEqual(score, 0)
        self.assertEqual(score, 0)
        s1 = 'психолог'
        s2 = None
        self.assertEqual(score, 0)
        s1 = None
        s2 = '我学数学'
        self.assertEqual(score, 0)

    def testQratioForceAscii_str_dbl_0(self):
        s1 = 'ABCDÁABCDÁ'
        s2 = 'ABCD'
        score = fuzz.QRatio(s1, s2, force_ascii=True)
        self.assertEqual(score, 67)
        self.assertEqual(score, 67)
        score = fuzz.QRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 57)
        self.assertEqual(score, 57)

    def testQRatioForceAscii_amp(self):
        s1 = 'ABCDÁ'
        s2 = 'ABCD'
        score = fuzz.WRatio(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)
        self.assertEqual(score, 100)
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 89)
        self.assertEqual(score, 89)

    def testQRatioForceAscii_str_dbl_1(self):
        s1 = 'ABCDÁ'
        s2 = 'ABCDABCD'
        score = fuzz.WRatio(s1, s2, force_ascii=True)
        self.assertEqual(score, 90)
        self.assertEqual(score, 90)
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 72)
        self.assertEqual(score, 72)

    def testQRatioForceAscii_str_dbl_0_str_hlf_1_str_dbl_0(self):
        s1 = 'ABCDÁABCDÁABCDÁABCDÁ'
        s2 = 'CD'
        score = fuzz.WRatio(s1, s2, force_ascii=True)
        self.assertEqual(score, 90)
        self.assertEqual(score, 90)
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertEqual(score, 60)
        self.assertEqual(score, 60)

    def testTokenSetForceAscii_amp(self):
        s1 = 'ABCDÁ HELPÁ'
        s2 = 'ABCD HELP'
        score = fuzz._token_set(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)
        score = fuzz._token_set(s1, s2, force_ascii=False)
        self.assertEqual(score, 89)

    def testTokenSetForceAscii_str_emp_1(self):
        s1 = 'ABCDÁ HELPÁ'
        s2 = ''
        score = fuzz._token_set(s1, s2, force_ascii=True)
        self.assertEqual(score, 0)
        score = fuzz._token_set(s1, s2, force_ascii=False)
        self.assertEqual(score, 0)

    def testTokenSetForceAscii_str_emp_0(self):
        s1 = ''
        s2 = 'ABCD HELP'
        score = fuzz._token_set(s1, s2, force_ascii=True)
        self.assertEqual(score, 0)
        score = fuzz._token_set(s1, s2, force_ascii=False)
        self.assertEqual(score, 0)

    def testTokenSortForceAscii_amp(self):
        s1 = 'ABCDÁ HELPÁ'
        s2 = 'ABCD HELP'
        score = fuzz._token_sort(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)
        score = fuzz._token_sort(s1, s2, force_ascii=False)
        self.assertEqual(score, 89)


class ValidatorTest(unittest.TestCase):

    def setUp(self):
        self.testFunc = lambda *args, **kwargs: (args, kwargs)

    def testCheckForNone(self):
        invalid_input = [(None, None), ('Some', None), (None, 'Some')]
        decorated_func = utils.check_for_none(self.testFunc)
        for i in invalid_input:
            self.assertEqual(decorated_func(*i), 0)
        valid_input = 'Some', 'Some'
        actual = decorated_func(*valid_input)
        self.assertNotEqual(actual, 0)

    def testCheckEmptyString(self):
        invalid_input = [('', ''), ('Some', ''), ('', 'Some')]
        decorated_func = utils.check_empty_string(self.testFunc)
        for i in invalid_input:
            self.assertEqual(decorated_func(*i), 0)
        valid_input = 'Some', 'Some'
        actual = decorated_func(*valid_input)
        self.assertNotEqual(actual, 0)


class ProcessTest(unittest.TestCase):

    def setUp(self):
        self.s1 = 'new york mets'
        self.s1a = 'new york mets'
        self.s2 = 'new YORK mets'
        self.s3 = 'the wonderful new york mets'
        self.s4 = 'new york mets vs atlanta braves'
        self.s5 = 'atlanta braves vs new york mets'
        self.s6 = 'new york mets - atlanta braves'
        self.cirque_strings = ['cirque du soleil - zarkana - las vegas',
            'cirque du soleil ', 'cirque du soleil las vegas',
            'zarkana las vegas',
            'las vegas cirque du soleil at the bellagio',
            'zarakana - cirque du soleil - bellagio']
        self.baseball_strings = ['new york mets vs chicago cubs',
            'chicago cubs vs chicago white sox',
            'philladelphia phillies vs atlanta braves', 'braves vs mets']

    def testGetBestChoice1(self):
        query = 'new york mets at atlanta braves'
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best[0], 'braves vs mets')

    def testGetBestChoice2(self):
        query = 'philadelphia phillies at atlanta braves'
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best[0], self.baseball_strings[2])

    def testGetBestChoice3(self):
        query = 'atlanta braves at philadelphia phillies'
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best[0], self.baseball_strings[2])

    def testGetBestChoice4(self):
        query = 'chicago cubs vs new york mets'
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best[0], self.baseball_strings[0])

    def testWithProcessor(self):
        events = [['chicago cubs vs new york mets', 'CitiField',
            '2011-05-11', '8pm'], ['new york yankees vs boston red sox',
            'Fenway Park', '2011-05-11', '8pm'], [
            'atlanta braves vs pittsburgh pirates', 'PNC Park',
            '2011-05-11', '8pm']]
        query = ['new york mets vs chicago cubs', 'CitiField', '2017-03-19',
            '8pm'],
        best = process.extractOne(query, events, processor=lambda event:
            event[0])
        self.assertEqual(best[0], events[0])

    def testWithScorer(self):
        choices = ['new york mets vs chicago cubs',
            'chicago cubs at new york mets',
            'atlanta braves vs pittsbugh pirates',
            'new york yankees vs boston red sox']
        choices_dict = {(1): 'new york mets vs chicago cubs', (2):
            'chicago cubs vs chicago white sox', (3):
            'philladelphia phillies vs atlanta braves', (4): 'braves vs mets'}
        query = 'new york mets at chicago cubs'
        scorer = fuzz.QRatio
        best = process.extractOne(query, choices)
        self.assertEqual(best[0], choices[1])
        best = process.extractOne(query, choices, scorer=scorer)
        self.assertEqual(best[0], choices[0])
        best = process.extractOne(query, choices_dict)
        self.assertEqual(best[0], choices_dict[1])

    def testWithCutoff(self):
        choices = ['new york mets vs chicago cubs',
            'chicago cubs at new york mets',
            'atlanta braves vs pittsbugh pirates',
            'new york yankees vs boston red sox']
        query = 'los angeles dodgers vs san francisco giants'
        best = process.extractOne(query, choices, score_cutoff=50)
        self.assertTrue(best is None)

    def testWithCutoff2(self):
        choices = ['new york mets vs chicago cubs',
            'chicago cubs at new york mets',
            'atlanta braves vs pittsbugh pirates',
            'new york yankees vs boston red sox']
        query = 'new york mets vs chicago cubs'
        res = process.extractOne(query, choices, score_cutoff=100)
        self.assertTrue(res is not None)
        best_match, score = res
        self.assertTrue(best_match is choices[0])

    def testEmptyStrings(self):
        choices = ['', 'new york mets vs chicago cubs',
            'new york yankees vs boston red sox', '', '']
        query = 'new york mets at chicago cubs'
        best = process.extractOne(query, choices)
        self.assertEqual(best[0], choices[1])

    def testNullStrings(self):
        choices = [None, 'new york mets vs chicago cubs',
            'new york yankees vs boston red sox', None, None]
        query = 'new york mets at chicago cubs'
        best = process.extractOne(query, choices)
        self.assertEqual(best[0], choices[1])

    def test_list_like_extract(self):
        """We should be able to use a list-like object for choices."""

        def generate_choices():
            choices = ['a', 'Bb', 'CcC']
            for choice in choices:
                yield choice
        search = 'aaa'
        result = [(value, confidence) for value, confidence in process.
            extract(search, generate_choices())]
        self.assertTrue(len(result) > 0)

    def test_dict_like_extract(self):
        """We should be able to use a dict-like object for choices, not only a
        dict, and still get dict-like output.
        """
        try:
            from UserDict import UserDict
        except ImportError:
            from collections import UserDict
        choices = UserDict({'aa': 'bb', 'a1': None})
        search = 'aaa'
        result = process.extract(search, choices)
        self.assertTrue(len(result) > 0)
        for value, confidence, key in result:
            self.assertTrue(value in choices.values())

    def test_dedupe(self):
        """We should be able to use a list-like object for contains_dupes
        """
        contains_dupes = ['Frodo Baggins', 'Tom Sawyer', 'Bilbo Baggin',
            'Samuel L. Jackson', 'F. Baggins', 'Frody Baggins', 'Bilbo Baggins'
            ]
        result = process.dedupe(contains_dupes)
        self.assertTrue(len(result) < len(contains_dupes))
        contains_dupes = ['Tom', 'Dick', 'Harry']
        deduped_list = ['Tom', 'Dick', 'Harry']
        result = process.dedupe(contains_dupes)
        self.assertEqual(result, deduped_list)

    def test_simplematch(self):
        basic_string = 'a, b'
        match_strings = ['a, b']
        result = process.extractOne(basic_string, match_strings, scorer=
            fuzz.ratio)
        part_result = process.extractOne(basic_string, match_strings,
            scorer=fuzz.partial_ratio)
        self.assertEqual(result, ('a, b', 100))
        self.assertEqual(part_result, ('a, b', 100))

    def testGetBestChoice1_amp(self):
        query = 'new york mets at atlanta braves'
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best, ('braves vs mets', 86))
        self.assertEqual(best[0], 'braves vs mets')

    def testGetBestChoice1_none_1_str_emp_0(self):
        query = ''
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best, ('new york mets vs chicago cubs', 0))

    def testGetBestChoice1_str_dbl_0_none_1_str_dbl_0(self):
        query = (
            'new york mets at atlanta bravesnew york mets at atlanta bravesnew york mets at atlanta bravesnew york mets at atlanta braves'
            )
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best, ('new york mets vs chicago cubs', 86))

    def testGetBestChoice1_str_hlf_0_none_1_str_hlf_0(self):
        query = 't atlan'
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best, ('philladelphia phillies vs atlanta braves', 77)
            )

    def testGetBestChoice1_str_emp_0_none_1_str_chr_0(self):
        query = 'g'
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best, ('new york mets vs chicago cubs', 60))

    def testGetBestChoice1_numb_add_0_str_hlf_0_str_hlf_0(self):
        query = 'york me'
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best, ('new york mets vs chicago cubs', 90))
        self.assertEqual(best[1], 90)

    def testGetBestChoice1_none_1_str_hlf_0(self):
        query = 'york mets at at'
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best, ('new york mets vs chicago cubs', 86))

    def testGetBestChoice1_str_hlf_0_none_1(self):
        query = 'ets at atlanta '
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best, ('philladelphia phillies vs atlanta braves', 86)
            )

    def testGetBestChoice1_str_hlf_0_none_1_str_dbl_0(self):
        query = 'ets at atlanta ets at atlanta '
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best, ('philladelphia phillies vs atlanta braves', 64)
            )

    def testGetBestChoice2_amp(self):
        query = 'philadelphia phillies at atlanta braves'
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best, ('philladelphia phillies vs atlanta braves', 94)
            )
        self.assertEqual(best[0], 'philladelphia phillies vs atlanta braves')
        self.assertEqual(self.baseball_strings[2],
            'philladelphia phillies vs atlanta braves')

    def testGetBestChoice2_none_2_str_hlf_0_str_dbl_0(self):
        query = 'es at atlanta bravees at atlanta brave'
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best, ('braves vs mets', 64))
        self.assertEqual(best[0], 'braves vs mets')

    def testGetBestChoice2_str_dbl_0_str_hlf_0(self):
        query = ' phillies at atlanta bravesphiladelphia'
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best, ('philladelphia phillies vs atlanta braves', 86)
            )
        self.assertEqual(best[0], 'philladelphia phillies vs atlanta braves')
        self.assertEqual(self.baseball_strings[2],
            'philladelphia phillies vs atlanta braves')

    def testGetBestChoice3_numb_sub_0_none_2_str_hlf_0(self):
        query = ' at philadelphia ph'
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best, ('philladelphia phillies vs atlanta braves', 75)
            )
        self.assertEqual(best[-1], 75)

    def testWithProcessor_none_12_none_17_str_dbl_4(self):
        events = [['chicago cubs vs new york mets', 'CitiField',
            '2011-05-11', '8pm'], [
            'new york yankees vs boston red soxnew york yankees vs boston red sox'
            , 'Fenway Park', '2011-05-11', '8pm'], [
            'atlanta braves vs pittsburgh pirates', 'PNC Park',
            '2011-05-11', '8pm']]
        query = [None, 'CitiField', '2017-03-19', '8pm'],
        best = process.extractOne(query, events, processor=lambda event:
            event[0])
        self.assertEqual(best, ([
            'new york yankees vs boston red soxnew york yankees vs boston red sox'
            , 'Fenway Park', '2011-05-11', '8pm'], 27))
        self.assertEqual(best[0], [
            'new york yankees vs boston red soxnew york yankees vs boston red sox'
            , 'Fenway Park', '2011-05-11', '8pm'])

    def testWithScorer_amp(self):
        choices = ['new york mets vs chicago cubs',
            'chicago cubs at new york mets',
            'atlanta braves vs pittsbugh pirates',
            'new york yankees vs boston red sox']
        choices_dict = {(1): 'new york mets vs chicago cubs', (2):
            'chicago cubs vs chicago white sox', (3):
            'philladelphia phillies vs atlanta braves', (4): 'braves vs mets'}
        query = 'new york mets at chicago cubs'
        scorer = fuzz.QRatio
        best = process.extractOne(query, choices)
        self.assertEqual(best, ('chicago cubs at new york mets', 95))
        self.assertEqual(best[0], 'chicago cubs at new york mets')
        self.assertEqual(choices[1], 'chicago cubs at new york mets')
        best = process.extractOne(query, choices, scorer=scorer)
        self.assertEqual(best, ('new york mets vs chicago cubs', 93))
        self.assertEqual(best[0], 'new york mets vs chicago cubs')
        self.assertEqual(choices[0], 'new york mets vs chicago cubs')
        best = process.extractOne(query, choices_dict)
        self.assertEqual(best, ('new york mets vs chicago cubs', 93, 1))
        self.assertEqual(best[0], 'new york mets vs chicago cubs')
        self.assertEqual(choices_dict[1], 'new york mets vs chicago cubs')

    def testWithScorer_str_emp_1_none_17(self):
        choices = ['new york mets vs chicago cubs', '',
            'atlanta braves vs pittsbugh pirates',
            'new york yankees vs boston red sox']
        choices_dict = {(1): 'new york mets vs chicago cubs', (2):
            'chicago cubs vs chicago white sox', (3):
            'philladelphia phillies vs atlanta braves', (4): 'braves vs mets'}
        query = 'new york mets at chicago cubs'
        scorer = fuzz.QRatio
        best = process.extractOne(query, choices)
        self.assertEqual(best, ('new york mets vs chicago cubs', 93))
        self.assertEqual(best[0], 'new york mets vs chicago cubs')
        self.assertEqual(choices[1], '')
        best = process.extractOne(query, choices, scorer=scorer)
        self.assertEqual(best, ('new york mets vs chicago cubs', 93))
        self.assertEqual(best[0], 'new york mets vs chicago cubs')
        self.assertEqual(choices[0], 'new york mets vs chicago cubs')
        best = process.extractOne(query, choices_dict)
        self.assertEqual(best, ('new york mets vs chicago cubs', 93, 1))
        self.assertEqual(choices_dict[1], 'new york mets vs chicago cubs')

    def testWithScorer_str_emp_8_none_8(self):
        choices = ['new york mets vs chicago cubs',
            'chicago cubs at new york mets',
            'atlanta braves vs pittsbugh pirates',
            'new york yankees vs boston red sox']
        choices_dict = {(1): None, (2): 'chicago cubs vs chicago white sox',
            (3): 'philladelphia phillies vs atlanta braves', (4):
            'braves vs mets'}
        query = ''
        scorer = fuzz.QRatio
        best = process.extractOne(query, choices)
        self.assertEqual(best, ('new york mets vs chicago cubs', 0))
        self.assertEqual(best[0], 'new york mets vs chicago cubs')
        self.assertEqual(choices[1], 'chicago cubs at new york mets')
        best = process.extractOne(query, choices, scorer=scorer)
        self.assertEqual(best, ('new york mets vs chicago cubs', 0))
        self.assertEqual(best[0], 'new york mets vs chicago cubs')
        self.assertEqual(choices[0], 'new york mets vs chicago cubs')
        best = process.extractOne(query, choices_dict)
        self.assertEqual(best, (None, 0, 1))

    def testWithCutoff_str_hlf_0_str_hlf_1_str_hlf_4(self):
        choices = ['s vs chicago c', 'chicago cubs a',
            'atlanta braves vs pittsbugh pirates',
            'new york yankees vs boston red sox']
        query = 'les dodgers vs san fr'
        best = process.extractOne(query, choices, score_cutoff=50)
        self.assertEqual(best, ('s vs chicago c', 86))
        self.assertFalse(best is None)

    def testNullStrings_str_dbl_0_str_dbl_0_str_dbl_0(self):
        choices = [None,
            'new york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubs'
            , 'new york yankees vs boston red sox', None, None]
        query = 'new york mets at chicago cubs'
        best = process.extractOne(query, choices)
        self.assertEqual(best, (
            'new york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubs'
            , 86))
        self.assertEqual(best[0],
            'new york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubs'
            )
        self.assertEqual(choices[1],
            'new york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubsnew york mets vs chicago cubs'
            )

    def testNullStrings_none_0_str_hlf_1_str_dbl_1(self):
        choices = [None, None, 'new york yankees vs boston red sox', None, None
            ]
        query = 'ts at chicago ts at chicago '
        best = process.extractOne(query, choices)
        self.assertEqual(best, ('new york yankees vs boston red sox', 25))
        self.assertEqual(best[0], 'new york yankees vs boston red sox')

    def test_dedupe_none_10_str_emp_1(self):
        """We should be able to use a list-like object for contains_dupes
        """
        contains_dupes = ['', 'Tom Sawyer', 'Bilbo Baggin',
            'Samuel L. Jackson', 'F. Baggins', 'Frody Baggins', 'Bilbo Baggins'
            ]
        result = process.dedupe(contains_dupes)
        self.assertTrue(len(result) < len(contains_dupes))
        contains_dupes = ['Tom', 'Dick', None]
        deduped_list = ['Tom', 'Dick', 'Harry']
        self.assertEqual(deduped_list, ['Tom', 'Dick', 'Harry'])

    def test_dedupe_str_emp_8_none_3(self):
        """We should be able to use a list-like object for contains_dupes
        """
        contains_dupes = ['Frodo Baggins', 'Tom Sawyer', None,
            'Samuel L. Jackson', 'F. Baggins', 'Frody Baggins', 'Bilbo Baggins'
            ]
        contains_dupes = ['', 'Dick', 'Harry']
        deduped_list = ['Tom', 'Dick', 'Harry']
        result = process.dedupe(contains_dupes)
        self.assertEqual(result, ['', 'Dick', 'Harry'])
        self.assertEqual(result, ['', 'Dick', 'Harry'])
        self.assertEqual(deduped_list, ['Tom', 'Dick', 'Harry'])


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        pep8style = pycodestyle.StyleGuide(quiet=False)
        pep8style.options.ignore = pep8style.options.ignore + tuple(['E501'])
        pep8style.input_dir('thefuzz')
        result = pep8style.check_files()
        self.assertEqual(result.total_errors, 0,
            'PEP8 POLICE - WOOOOOWOOOOOOOOOO')


if __name__ == '__main__':
    unittest.main()
