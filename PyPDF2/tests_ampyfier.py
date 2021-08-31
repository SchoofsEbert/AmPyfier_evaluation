import os
import sys
import unittest
import binascii
from PyPDF2 import PdfFileReader, PdfFileWriter
TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(TESTS_ROOT)
RESOURCE_ROOT = os.path.join(PROJECT_ROOT, 'Resources')
sys.path.append(PROJECT_ROOT)


class PdfReaderTestCases(unittest.TestCase):

    def test_PdfReaderFileLoad(self):
        """
        Test loading and parsing of a file. Extract text of the file and compare to expected
        textual output. Expected outcome: file loads, text matches expected.
        """
        with open(os.path.join(RESOURCE_ROOT, 'crazyones.pdf'), 'rb'
            ) as inputfile:
            ipdf = PdfFileReader(inputfile)
            ipdf_p1 = ipdf.getPage(0)
            with open(os.path.join(RESOURCE_ROOT, 'crazyones.txt'), 'rb'
                ) as pdftext_file:
                pdftext = pdftext_file.read()
            ipdf_p1_text = ipdf_p1.extractText().replace('\n', '').encode(
                'utf-8')
            self.assertEqual(ipdf_p1_text, pdftext, msg=
                """PDF extracted text differs from expected value.

Expected:

%r

Extracted:

%r

"""
                 % (pdftext, ipdf_p1_text))

    def test_PdfReaderJpegImage(self):
        """
        Test loading and parsing of a file. Extract the image of the file and compare to expected
        textual output. Expected outcome: file loads, image matches expected.
        """
        with open(os.path.join(RESOURCE_ROOT, 'jpeg.pdf'), 'rb') as inputfile:
            ipdf = PdfFileReader(inputfile)
            with open(os.path.join(RESOURCE_ROOT, 'jpeg.txt'), 'r'
                ) as pdftext_file:
                imagetext = pdftext_file.read()
            ipdf_p0 = ipdf.getPage(0)
            xObject = ipdf_p0['/Resources']['/XObject'].getObject()
            data = xObject['/Im4'].getData()
            self.assertEqual(binascii.hexlify(data).decode(), imagetext,
                msg=
                """PDF extracted image differs from expected value.

Expected:

%r

Extracted:

%r

"""
                 % (imagetext, binascii.hexlify(data).decode()))

    def test_PdfReaderFileLoad_amp_str_dbl_5(self):
        """
        Test loading and parsing of a file. Extract text of the file and compare to expected
        textual output. Expected outcome: file loads, text matches expected.
        """
        with open(os.path.join(RESOURCE_ROOT, 'crazyones.pdf'), 'rb'
            ) as inputfile:
            ipdf = PdfFileReader(inputfile)
            ipdf_p1 = ipdf.getPage(0)
            with open(os.path.join(RESOURCE_ROOT, 'crazyones.txt'), 'rb'
                ) as pdftext_file:
                pdftext = pdftext_file.read()
            ipdf_p1_text = ipdf_p1.extractText().replace('\n\n', '').encode(
                'utf-8')
            self.assertEqual(ipdf_p1_text,
                b'TheCrazyOnes\nOctober14,1998\nHerestothecrazyones.Themis\xcb\x9dts.Therebels.Thetroublemakers.\nTheroundpegsinthesquareholes.\nTheoneswhoseethingsdi\xcb\x99erently.Theyrenotfondofrules.And\ntheyhavenorespectforthestatusquo.Youcanquotethem,\ndisagreewiththem,glorifyorvilifythem.\nAbouttheonlythingyoucantdoisignorethem.Becausetheychange\nthings.Theyinvent.Theyimagine.Theyheal.Theyexplore.They\ncreate.Theyinspire.Theypushthehumanraceforward.\nMaybetheyhavetobecrazy.\nHowelsecanyoustareatanemptycanvasandseeaworkofart?Or\nsitinsilenceandhearasongthatsneverbeenwritten?Orgazeat\naredplanetandseealaboratoryonwheels?\nWemaketoolsforthesekindsofpeople.\nWhilesomeseethemasthecrazyones,weseegenius.Becausethe\npeoplewhoarecrazyenoughtothinktheycanchangetheworld,\naretheoneswhodo.\n'
                )
            self.assertEqual(pdftext,
                b'TheCrazyOnesOctober14,1998Herestothecrazyones.Themis\xcb\x9dts.Therebels.Thetroublemakers.Theroundpegsinthesquareholes.Theoneswhoseethingsdi\xcb\x99erently.Theyrenotfondofrules.Andtheyhavenorespectforthestatusquo.Youcanquotethem,disagreewiththem,glorifyorvilifythem.Abouttheonlythingyoucantdoisignorethem.Becausetheychangethings.Theyinvent.Theyimagine.Theyheal.Theyexplore.Theycreate.Theyinspire.Theypushthehumanraceforward.Maybetheyhavetobecrazy.Howelsecanyoustareatanemptycanvasandseeaworkofart?Orsitinsilenceandhearasongthatsneverbeenwritten?Orgazeataredplanetandseealaboratoryonwheels?Wemaketoolsforthesekindsofpeople.Whilesomeseethemasthecrazyones,weseegenius.Becausethepeoplewhoarecrazyenoughtothinktheycanchangetheworld,aretheoneswhodo.'
                )

    def test_PdfReaderFileLoad_amp_str_hlf_2(self):
        from io import UnsupportedOperation
        """
        Test loading and parsing of a file. Extract text of the file and compare to expected
        textual output. Expected outcome: file loads, text matches expected.
        """
        with open(os.path.join(RESOURCE_ROOT, 'crazyones.pdf'), 'r'
            ) as inputfile:
            with self.assertRaises(UnsupportedOperation):
                ipdf = PdfFileReader(inputfile)
            with open(os.path.join(RESOURCE_ROOT, 'crazyones.txt'), 'rb'
                ) as pdftext_file:
                pdftext = pdftext_file.read()
            self.assertEqual(pdftext,
                b'TheCrazyOnesOctober14,1998Herestothecrazyones.Themis\xcb\x9dts.Therebels.Thetroublemakers.Theroundpegsinthesquareholes.Theoneswhoseethingsdi\xcb\x99erently.Theyrenotfondofrules.Andtheyhavenorespectforthestatusquo.Youcanquotethem,disagreewiththem,glorifyorvilifythem.Abouttheonlythingyoucantdoisignorethem.Becausetheychangethings.Theyinvent.Theyimagine.Theyheal.Theyexplore.Theycreate.Theyinspire.Theypushthehumanraceforward.Maybetheyhavetobecrazy.Howelsecanyoustareatanemptycanvasandseeaworkofart?Orsitinsilenceandhearasongthatsneverbeenwritten?Orgazeataredplanetandseealaboratoryonwheels?Wemaketoolsforthesekindsofpeople.Whilesomeseethemasthecrazyones,weseegenius.Becausethepeoplewhoarecrazyenoughtothinktheycanchangetheworld,aretheoneswhodo.'
                )


class AddJsTestCase(unittest.TestCase):

    def setUp(self):
        ipdf = PdfFileReader(os.path.join(RESOURCE_ROOT, 'crazyones.pdf'))
        self.pdf_file_writer = PdfFileWriter()
        self.pdf_file_writer.appendPagesFromReader(ipdf)

    def get_javascript_name(self):
        self.assertIn('/Names', self.pdf_file_writer._root_object)
        self.assertIn('/JavaScript', self.pdf_file_writer._root_object[
            '/Names'])
        self.assertIn('/Names', self.pdf_file_writer._root_object['/Names']
            ['/JavaScript'])
        return self.pdf_file_writer._root_object['/Names']['/JavaScript'][
            '/Names'][0]

    def test_add(self):
        self.pdf_file_writer.addJS(
            'this.print({bUI:true,bSilent:false,bShrinkToFit:true});')
        self.assertIn('/Names', self.pdf_file_writer._root_object,
            'addJS should add a name catalog in the root object.')
        self.assertIn('/JavaScript', self.pdf_file_writer._root_object[
            '/Names'],
            'addJS should add a JavaScript name tree under the name catalog.')
        self.assertIn('/OpenAction', self.pdf_file_writer._root_object,
            'addJS should add an OpenAction to the catalog.')

    def test_overwrite(self):
        self.pdf_file_writer.addJS(
            'this.print({bUI:true,bSilent:false,bShrinkToFit:true});')
        first_js = self.get_javascript_name()
        self.pdf_file_writer.addJS(
            'this.print({bUI:true,bSilent:false,bShrinkToFit:true});')
        second_js = self.get_javascript_name()
        self.assertNotEqual(first_js, second_js,
            'addJS should overwrite the previous script in the catalog.')
