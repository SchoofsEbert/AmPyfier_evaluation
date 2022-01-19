



# /home/ubuntu/projects/whois/whois/whois.py

## Newly Killed Mutants

## Alive Mutants
  
Lines 123:129

```diff
	                    break
	        return nhost
	
-	    def whois(self, query, hostname, flags, many_results=False, quiet=False):
+	    def whois(self, query, hostname, flags, many_results=(True), quiet=False):
	        """Perform initial lookup with TLD whois server
	        then, if the quick flag is false, search that result
	        for the region-specifc whois server and do a lookup

```  
Lines 123:129

```diff
	                    break
	        return nhost
	
-	    def whois(self, query, hostname, flags, many_results=False, quiet=False):
+	    def whois(self, query, hostname, flags, many_results=None, quiet=False):
	        """Perform initial lookup with TLD whois server
	        then, if the quick flag is false, search that result
	        for the region-specifc whois server and do a lookup

```  
Lines 123:129

```diff
	                    break
	        return nhost
	
-	    def whois(self, query, hostname, flags, many_results=False, quiet=False):
+	    def whois(self, query, hostname, flags, many_results=False, quiet=(True)):
	        """Perform initial lookup with TLD whois server
	        then, if the quick flag is false, search that result
	        for the region-specifc whois server and do a lookup

```  
Lines 123:129

```diff
	                    break
	        return nhost
	
-	    def whois(self, query, hostname, flags, many_results=False, quiet=False):
+	    def whois(self, query, hostname, flags, many_results=False, quiet=None):
	        """Perform initial lookup with TLD whois server
	        then, if the quick flag is false, search that result
	        for the region-specifc whois server and do a lookup

```  
Lines 374:380

```diff
	    return parser.parse_args(argv)
	
	
-	if __name__ == "__main__":
+	if (__name__ <= '__main__'):
	    flags = 0
	    nic_client = NICClient()
	    options, args = parse_command_line(sys.argv)

```  
Lines 374:380

```diff
	    return parser.parse_args(argv)
	
	
-	if __name__ == "__main__":
+	if (__name__ < '__main__'):
	    flags = 0
	    nic_client = NICClient()
	    options, args = parse_command_line(sys.argv)

```  
Lines 374:380

```diff
	    return parser.parse_args(argv)
	
	
-	if __name__ == "__main__":
+	if False:
	    flags = 0
	    nic_client = NICClient()
	    options, args = parse_command_line(sys.argv)

```
# /home/ubuntu/projects/whois/whois/parser.py

## Newly Killed Mutants

## Alive Mutants
  
Lines 24:30

```diff
	try:
	    import dateutil.parser as dp
	    from .time_zones import tz_data
-	    DATEUTIL = True
+	    DATEUTIL = (False)
	except ImportError:
	    DATEUTIL = False
	

```  
Lines 24:30

```diff
	try:
	    import dateutil.parser as dp
	    from .time_zones import tz_data
-	    DATEUTIL = True
+	    DATEUTIL = None
	except ImportError:
	    DATEUTIL = False
	

```  
Lines 88:94

```diff
	    return s
	
	
-	def cast_date(s, dayfirst=False, yearfirst=False):
+	def cast_date(s, dayfirst=False, yearfirst=(True)):
	    """Convert any date string found in WHOIS to a datetime object.
	    """
	    if DATEUTIL:

```  
Lines 88:94

```diff
	    return s
	
	
-	def cast_date(s, dayfirst=False, yearfirst=False):
+	def cast_date(s, dayfirst=False, yearfirst=None):
	    """Convert any date string found in WHOIS to a datetime object.
	    """
	    if DATEUTIL:

```  
Lines 88:94

```diff
	    return s
	
	
-	def cast_date(s, dayfirst=False, yearfirst=False):
+	def cast_date(s, dayfirst=(True), yearfirst=False):
	    """Convert any date string found in WHOIS to a datetime object.
	    """
	    if DATEUTIL:

```  
Lines 88:94

```diff
	    return s
	
	
-	def cast_date(s, dayfirst=False, yearfirst=False):
+	def cast_date(s, dayfirst=None, yearfirst=False):
	    """Convert any date string found in WHOIS to a datetime object.
	    """
	    if DATEUTIL:

```  
Lines 130:136

```diff
	        'zipcode':              r'Registrant Postal Code: *(.+)',
	        'country':              r'Registrant Country: *(.+)',
	    }
-	    dayfirst = False
+	    dayfirst = (True)
	    yearfirst = False
	
	    def __init__(self, domain, text, regex=None):

```  
Lines 130:136

```diff
	        'zipcode':              r'Registrant Postal Code: *(.+)',
	        'country':              r'Registrant Country: *(.+)',
	    }
-	    dayfirst = False
+	    dayfirst = None
	    yearfirst = False
	
	    def __init__(self, domain, text, regex=None):

```  
Lines 131:137

```diff
	        'country':              r'Registrant Country: *(.+)',
	    }
	    dayfirst = False
-	    yearfirst = False
+	    yearfirst = (True)
	
	    def __init__(self, domain, text, regex=None):
	        if 'This TLD has no whois server, but you can access the whois database at' in text:

```  
Lines 131:137

```diff
	        'country':              r'Registrant Country: *(.+)',
	    }
	    dayfirst = False
-	    yearfirst = False
+	    yearfirst = None
	
	    def __init__(self, domain, text, regex=None):
	        if 'This TLD has no whois server, but you can access the whois database at' in text:

```  
Lines 133:139

```diff
	    dayfirst = False
	    yearfirst = False
	
-	    def __init__(self, domain, text, regex=None):
+	    def __init__(self, domain, text, regex=(False)):
	        if 'This TLD has no whois server, but you can access the whois database at' in text:
	            raise PywhoisError(text)
	        else:

```  
Lines 133:139

```diff
	    dayfirst = False
	    yearfirst = False
	
-	    def __init__(self, domain, text, regex=None):
+	    def __init__(self, domain, text, regex=(True)):
	        if 'This TLD has no whois server, but you can access the whois database at' in text:
	            raise PywhoisError(text)
	        else:

```  
Lines 529:535

```diff
	        'registrar': r'registrar: *(.+)',
	        'creation_date': r'created: *(.+)',
	        'expiration_date': r'paid-till: *(.+)',
-	        'updated_date': None,
+	        'updated_date': (False),
	        'name_servers': r'nserver: *(.+)',  # list of name servers
	        'status': r'state: *(.+)',  # list of statuses
	        'emails': EMAIL_REGEX,  # list of email addresses

```  
Lines 529:535

```diff
	        'registrar': r'registrar: *(.+)',
	        'creation_date': r'created: *(.+)',
	        'expiration_date': r'paid-till: *(.+)',
-	        'updated_date': None,
+	        'updated_date': (True),
	        'name_servers': r'nserver: *(.+)',  # list of name servers
	        'status': r'state: *(.+)',  # list of statuses
	        'emails': EMAIL_REGEX,  # list of email addresses

```  
Lines 552:558

```diff
	        'updated_date':        r'Updated\sDate:\s*(.+)',
	        'creation_date':       r'Creation\sDate:\s*(.+)',
	        'status':              r'Status: *(.+)',  # list of statuses
-	        'name':                None,
+	        'name':                (False),
	        'registrar':           r'Registrar:\s*(.*\n)',
	        'registrar_address':   r'Registrar:\s*(?:.*\n){1}\s*(.*)',
	        'registrar_zip_code':  r'Registrar:\s*(?:.*\n){2}\s*(\S*)\s(?:.*)',

```  
Lines 552:558

```diff
	        'updated_date':        r'Updated\sDate:\s*(.+)',
	        'creation_date':       r'Creation\sDate:\s*(.+)',
	        'status':              r'Status: *(.+)',  # list of statuses
-	        'name':                None,
+	        'name':                (True),
	        'registrar':           r'Registrar:\s*(.*\n)',
	        'registrar_address':   r'Registrar:\s*(?:.*\n){1}\s*(.*)',
	        'registrar_zip_code':  r'Registrar:\s*(?:.*\n){2}\s*(\S*)\s(?:.*)',

```  
Lines 865:871

```diff
	
	    }
	
-	    dayfirst = True
+	    dayfirst = (False)
	
	    def __init__(self, domain, text):
	        if 'Domain not ' in text:

```  
Lines 865:871

```diff
	
	    }
	
-	    dayfirst = True
+	    dayfirst = None
	
	    def __init__(self, domain, text):
	        if 'Domain not ' in text:

```  
Lines 1051:1057

```diff
	        'status': r'Domain Status: *(.+)',  # list of statuses
	        'emails': EMAIL_REGEX,  # list of email addresses
	    }
-	    dayfirst = True
+	    dayfirst = (False)
	
	    def __init__(self, domain, text):
	        if text.strip() == 'No entries found':

```  
Lines 1051:1057

```diff
	        'status': r'Domain Status: *(.+)',  # list of statuses
	        'emails': EMAIL_REGEX,  # list of email addresses
	    }
-	    dayfirst = True
+	    dayfirst = None
	
	    def __init__(self, domain, text):
	        if text.strip() == 'No entries found':

```  
Lines 1068:1074

```diff
	        'status': r'registration status: s*(.+)',
	        'expiration_date': r'expires at: *(.+)',
	    }
-	    dayfirst = True
+	    dayfirst = (False)
	
	    def __init__(self, domain, text):
	        if 'does not exist in database!' in text:

```  
Lines 1068:1074

```diff
	        'status': r'registration status: s*(.+)',
	        'expiration_date': r'expires at: *(.+)',
	    }
-	    dayfirst = True
+	    dayfirst = None
	
	    def __init__(self, domain, text):
	        if 'does not exist in database!' in text:

```  
Lines 1925:1931

```diff
	        'registrar':          r'registrar name: *(.+)',
	        'referral_url':       r'registrar info: *(.+)',
	    }
-	    dayfirst = True
+	    dayfirst = (False)
	
	    def __init__(self, domain, text):
	        if 'No data was found' in text:

```  
Lines 1925:1931

```diff
	        'registrar':          r'registrar name: *(.+)',
	        'referral_url':       r'registrar info: *(.+)',
	    }
-	    dayfirst = True
+	    dayfirst = None
	
	    def __init__(self, domain, text):
	        if 'No data was found' in text:

```  
Lines 2187:2193

```diff
	        'expiration_date':                r'[Registrant Contact Information\w\W]+Expiry Date: (.+)',
	        'name_servers':                   r'Name Servers Information:\s+((?:.+\n)*)'
	    }
-	    dayfirst = True
+	    dayfirst = (False)
	
	    def __init__(self, domain, text):
	        if 'ERROR: No entries found' in text or 'The domain has not been registered' in text:

```  
Lines 2187:2193

```diff
	        'expiration_date':                r'[Registrant Contact Information\w\W]+Expiry Date: (.+)',
	        'name_servers':                   r'Name Servers Information:\s+((?:.+\n)*)'
	    }
-	    dayfirst = True
+	    dayfirst = None
	
	    def __init__(self, domain, text):
	        if 'ERROR: No entries found' in text or 'The domain has not been registered' in text:

```
# /home/ubuntu/projects/whois/whois/time_zones.py

## Newly Killed Mutants

## Alive Mutants
  
Lines 47:52

```diff
	tz_data = {}
	
	for tz_descr in (tz_spec.split() for tz_spec in _tz_string.split('\n')):
-	    tz_offset = int(float(tz_descr[0]) * 3600)
+	    tz_offset = int((float(tz_descr[0]) - 3600))
	    for tz_code in tz_descr[1:]:
	        tz_data[tz_code] = tz_offset

```  
Lines 47:52

```diff
	tz_data = {}
	
	for tz_descr in (tz_spec.split() for tz_spec in _tz_string.split('\n')):
-	    tz_offset = int(float(tz_descr[0]) * 3600)
+	    tz_offset = int((float(tz_descr[0]) / 3600))
	    for tz_code in tz_descr[1:]:
	        tz_data[tz_code] = tz_offset

```  
Lines 47:52

```diff
	tz_data = {}
	
	for tz_descr in (tz_spec.split() for tz_spec in _tz_string.split('\n')):
-	    tz_offset = int(float(tz_descr[0]) * 3600)
+	    tz_offset = int((float(tz_descr[0]) + 3600))
	    for tz_code in tz_descr[1:]:
	        tz_data[tz_code] = tz_offset

```  
Lines 47:52

```diff
	tz_data = {}
	
	for tz_descr in (tz_spec.split() for tz_spec in _tz_string.split('\n')):
-	    tz_offset = int(float(tz_descr[0]) * 3600)
+	    tz_offset = int((float(tz_descr[0]) // 3600))
	    for tz_code in tz_descr[1:]:
	        tz_data[tz_code] = tz_offset

```  
Lines 47:52

```diff
	tz_data = {}
	
	for tz_descr in (tz_spec.split() for tz_spec in _tz_string.split('\n')):
-	    tz_offset = int(float(tz_descr[0]) * 3600)
+	    tz_offset = int((float(tz_descr[0]) % 3600))
	    for tz_code in tz_descr[1:]:
	        tz_data[tz_code] = tz_offset

```  
Lines 48:52

```diff
	
	for tz_descr in (tz_spec.split() for tz_spec in _tz_string.split('\n')):
	    tz_offset = int(float(tz_descr[0]) * 3600)
-	    for tz_code in tz_descr[1:]:
+	    for tz_code in tz_descr[:]:
	        tz_data[tz_code] = tz_offset

```  
Lines 48:52

```diff
	
	for tz_descr in (tz_spec.split() for tz_spec in _tz_string.split('\n')):
	    tz_offset = int(float(tz_descr[0]) * 3600)
-	    for tz_code in tz_descr[1:]:
+	    for tz_code in tz_descr[:1]:
	        tz_data[tz_code] = tz_offset

```
# /home/ubuntu/projects/whois/whois/__init__.py

## Newly Killed Mutants

### test_simple_ascii_domain_str_hlf_0
  
Lines 89:95

```diff
	        # downloaded from https://publicsuffix.org/list/public_suffix_list.dat
	        tlds_path = os.path.join(os.getcwd(), os.path.dirname(__file__), 'data', 'public_suffix_list.dat')
	        with open(tlds_path, encoding='utf-8') as tlds_fp:
-	            suffixes = set(line.encode('utf-8') for line in tlds_fp.read().splitlines() if line and not line.startswith('//'))
+	            suffixes = set(line.encode('utf-8') for line in tlds_fp.read().splitlines() if (line or not line.startswith('//')))
	
	    if not isinstance(url, str):
	        url = url.decode('utf-8')

```  
Lines 109:115

```diff
	                # match the first two sections - if that works, keep going
	                # See https://github.com/richardpenman/whois/issues/50
	                second_order_tld = '.'.join([split_url[-2], split_url[-1]])
-	                if not second_order_tld.encode('utf-8') in suffixes:
+	                if False:
	                    break
	            else:
	                break

```
### test_simple_ascii_domain_str_emp_0
  
Lines 104:110

```diff
	            domain = b'.' + domain
	        domain = section.encode('utf-8') + domain
	        if domain not in suffixes:
-	            if not b'.' in domain and len(split_url) >= 2:
+	            if True:
	                # If this is the first section and there wasn't a match, try to
	                # match the first two sections - if that works, keep going
	                # See https://github.com/richardpenman/whois/issues/50

```  
Lines 104:110

```diff
	            domain = b'.' + domain
	        domain = section.encode('utf-8') + domain
	        if domain not in suffixes:
-	            if not b'.' in domain and len(split_url) >= 2:
+	            if (not b'.' in domain or len(split_url) >= 2):
	                # If this is the first section and there wasn't a match, try to
	                # match the first two sections - if that works, keep going
	                # See https://github.com/richardpenman/whois/issues/50

```  
Lines 104:110

```diff
	            domain = b'.' + domain
	        domain = section.encode('utf-8') + domain
	        if domain not in suffixes:
-	            if not b'.' in domain and len(split_url) >= 2:
+	            if not b'.' in domain and (len(split_url) != 2):
	                # If this is the first section and there wasn't a match, try to
	                # match the first two sections - if that works, keep going
	                # See https://github.com/richardpenman/whois/issues/50

```
## Alive Mutants
  
Lines 28:34

```diff
	IPV4_OR_V6 = re.compile(r"((^\s*((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))\s*$)|(^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$))")
	
	
-	def whois(url, command=False, flags=0, executable="whois"):
+	def whois(url, command=(True), flags=0, executable="whois"):
	    # clean domain to expose netloc
	    ip_match = IPV4_OR_V6.match(url)
	    if ip_match:

```  
Lines 28:34

```diff
	IPV4_OR_V6 = re.compile(r"((^\s*((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))\s*$)|(^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$))")
	
	
-	def whois(url, command=False, flags=0, executable="whois"):
+	def whois(url, command=None, flags=0, executable="whois"):
	    # clean domain to expose netloc
	    ip_match = IPV4_OR_V6.match(url)
	    if ip_match:

```  
Lines 52:58

```diff
	    return WhoisEntry.load(domain, text)
	
	
-	suffixes = None
+	suffixes = (False)
	def extract_domain(url):
	    """Extract the domain from the given URL
	

```  
Lines 85:91

```diff
	
	    # load known TLD suffixes
	    global suffixes
-	    if not suffixes:
+	    if True:
	        # downloaded from https://publicsuffix.org/list/public_suffix_list.dat
	        tlds_path = os.path.join(os.getcwd(), os.path.dirname(__file__), 'data', 'public_suffix_list.dat')
	        with open(tlds_path, encoding='utf-8') as tlds_fp:

```  
Lines 91:97

```diff
	        with open(tlds_path, encoding='utf-8') as tlds_fp:
	            suffixes = set(line.encode('utf-8') for line in tlds_fp.read().splitlines() if line and not line.startswith('//'))
	
-	    if not isinstance(url, str):
+	    if False:
	        url = url.decode('utf-8')
	    url = re.sub('^.*://', '', url)
	    url = url.split('/')[0].lower()

```  
Lines 104:110

```diff
	            domain = b'.' + domain
	        domain = section.encode('utf-8') + domain
	        if domain not in suffixes:
-	            if not b'.' in domain and len(split_url) >= 2:
+	            if not b'.' in domain and (len(split_url) > 2):
	                # If this is the first section and there wasn't a match, try to
	                # match the first two sections - if that works, keep going
	                # See https://github.com/richardpenman/whois/issues/50

```  
Lines 108:114

```diff
	                # If this is the first section and there wasn't a match, try to
	                # match the first two sections - if that works, keep going
	                # See https://github.com/richardpenman/whois/issues/50
-	                second_order_tld = '.'.join([split_url[-2], split_url[-1]])
+	                second_order_tld = '.'.join([split_url[(-2)], split_url[-1]])
	                if not second_order_tld.encode('utf-8') in suffixes:
	                    break
	            else:

```  
Lines 116:122

```diff
	    return domain.decode('utf-8')
	
	
-	if __name__ == '__main__':
+	if False:
	    try:
	        url = sys.argv[1]
	    except IndexError:

```  
Lines 116:122

```diff
	    return domain.decode('utf-8')
	
	
-	if __name__ == '__main__':
+	if (__name__ <= '__main__'):
	    try:
	        url = sys.argv[1]
	    except IndexError:

```  
Lines 116:122

```diff
	    return domain.decode('utf-8')
	
	
-	if __name__ == '__main__':
+	if (__name__ < '__main__'):
	    try:
	        url = sys.argv[1]
	    except IndexError:

```