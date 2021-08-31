from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
import unittest
from whois import extract_domain


class TestExtractDomain(unittest.TestCase):

    def test_simple_ascii_domain(self):
        url = 'google.com'
        domain = url
        self.assertEqual(domain, extract_domain(url))

    def test_ascii_with_schema_path_and_query(self):
        url = 'https://www.google.com/search?q=why+is+domain+whois+such+a+mess'
        domain = 'google.com'
        self.assertEqual(domain, extract_domain(url))

    def test_simple_unicode_domain(self):
        url = 'http://нарояци.com/'
        domain = 'нарояци.com'
        self.assertEqual(domain, extract_domain(url))

    def test_unicode_domain_and_tld(self):
        url = 'http://россия.рф/'
        domain = 'россия.рф'
        self.assertEqual(domain, extract_domain(url))

    def test_ipv6(self):
        """ Verify that ipv6 addresses work """
        url = '2607:f8b0:4006:802::200e'
        domain = '1e100.net'
        self.assertEqual(domain, extract_domain(extract_domain(url)))

    def test_ipv4(self):
        """ Verify that ipv4 addresses work """
        url = '172.217.3.110'
        domain = '1e100.net'
        self.assertEqual(domain, extract_domain(extract_domain(url)))

    def test_second_level_domain(self):
        """Verify that TLDs which only have second-level domains parse correctly"""
        url = 'google.co.za'
        domain = url
        self.assertEqual(domain, extract_domain(url))

    def test_simple_ascii_domain_amp_str_hlf_0(self):
        url = 'gle.c'
        domain = url
        self.assertEqual(domain, 'gle.c')
        self.assertEqual(extract_domain(url), 'c')

    def test_simple_ascii_domain_amp_str_emp_0(self):
        url = ''
        domain = url
        self.assertEqual(domain, '')
        self.assertEqual(extract_domain(url), '')

    def test_simple_ascii_domain_amp_call_dup_0_call_dup_0_str_hlf_0(self):
        url = 'ogle.'
        domain = url
        self.assertEqual(domain, 'ogle.')
        self.assertEqual(extract_domain(url), '')
        self.assertEqual(extract_domain(url), '')
        self.assertEqual(extract_domain(url), '')

    def test_ipv6_amp_str_dbl_1_str_dbl_0_str_hlf_2(self):
        """ Verify that ipv6 addresses work """
        url = (
            '2607:f8b0:4006:802::200e2607:f8b0:4006:802::200e2607:f8b0:4006:802::200e2607:f8b0:4006:802::200e'
            )
        domain = '1e10'
        self.assertEqual(domain, '1e10')
        self.assertEqual(extract_domain(extract_domain(url)),
            '2607:f8b0:4006:802::200e2607:f8b0:4006:802::200e2607:f8b0:4006:802::200e2607:f8b0:4006:802::200e'
            )
