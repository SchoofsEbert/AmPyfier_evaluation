



# /home/ubuntu/projects/whois/whois/parser.py

## Newly Killed Mutants

### test_com_expiration_str_hlf_2_str_hlf_0
  
Lines 162:168

```diff
	                    values = values[-1]  # ignore junk
	                if len(values) == 1:
	                    values = values[0]
-	                elif not values:
+	                elif False:
	                    values = None
	
	                self[attr] = values

```  
Lines 163:169

```diff
	                if len(values) == 1:
	                    values = values[0]
	                elif not values:
-	                    values = None
+	                    values = (False)
	
	                self[attr] = values
	

```  
Lines 163:169

```diff
	                if len(values) == 1:
	                    values = values[0]
	                elif not values:
-	                    values = None
+	                    values = (True)
	
	                self[attr] = values
	

```
### test_com_expiration_str_hlf_1
  
Lines 315:321

```diff
	            return WhoisCz(domain, text)
	        elif domain.endswith('.online'):
	            return WhoisOnline(domain, text)
-	        elif domain.endswith('.cn'):
+	        elif True:
	            return WhoisCn(domain, text)
	        elif domain.endswith('.app'):
	            return WhoisApp(domain, text)

```  
Lines 321:327

```diff
	            return WhoisApp(domain, text)
	        elif domain.endswith('.money'):
	            return WhoisMoney(domain, text)
-	        elif domain.endswith('.cl'):
+	        elif True:
	            return WhoisCl(domain, text)
	        elif domain.endswith('.ar'):
	            return WhoisAr(domain, text)

```  
Lines 323:329

```diff
	            return WhoisMoney(domain, text)
	        elif domain.endswith('.cl'):
	            return WhoisCl(domain, text)
-	        elif domain.endswith('.ar'):
+	        elif True:
	            return WhoisAr(domain, text)
	        elif domain.endswith('.by'):
	            return WhoisBy(domain, text)

```  
Lines 325:331

```diff
	            return WhoisCl(domain, text)
	        elif domain.endswith('.ar'):
	            return WhoisAr(domain, text)
-	        elif domain.endswith('.by'):
+	        elif True:
	            return WhoisBy(domain, text)
	        elif domain.endswith('.cr'):
	            return WhoisCr(domain, text)

```  
Lines 327:333

```diff
	            return WhoisAr(domain, text)
	        elif domain.endswith('.by'):
	            return WhoisBy(domain, text)
-	        elif domain.endswith('.cr'):
+	        elif True:
	            return WhoisCr(domain, text)
	        elif domain.endswith('.do'):
	            return WhoisDo(domain, text)

```  
Lines 335:341

```diff
	            return WhoisJobs(domain, text)
	        elif domain.endswith('.lat'):
	            return WhoisLat(domain, text)
-	        elif domain.endswith('.pe'):
+	        elif True:
	            return WhoisPe(domain, text)
	        elif domain.endswith('.ro'):
	            return WhoisRo(domain, text)

```  
Lines 337:343

```diff
	            return WhoisLat(domain, text)
	        elif domain.endswith('.pe'):
	            return WhoisPe(domain, text)
-	        elif domain.endswith('.ro'):
+	        elif True:
	            return WhoisRo(domain, text)
	        elif domain.endswith('.sa'):
	            return WhoisSa(domain, text)

```  
Lines 339:345

```diff
	            return WhoisPe(domain, text)
	        elif domain.endswith('.ro'):
	            return WhoisRo(domain, text)
-	        elif domain.endswith('.sa'):
+	        elif True:
	            return WhoisSa(domain, text)
	        elif domain.endswith('.tw'):
	            return WhoisTw(domain, text)

```  
Lines 341:347

```diff
	            return WhoisRo(domain, text)
	        elif domain.endswith('.sa'):
	            return WhoisSa(domain, text)
-	        elif domain.endswith('.tw'):
+	        elif True:
	            return WhoisTw(domain, text)
	        elif domain.endswith('.tr'):
	            return WhoisTr(domain, text)

```  
Lines 343:349

```diff
	            return WhoisSa(domain, text)
	        elif domain.endswith('.tw'):
	            return WhoisTw(domain, text)
-	        elif domain.endswith('.tr'):
+	        elif True:
	            return WhoisTr(domain, text)
	        elif domain.endswith('.ve'):
	            return WhoisVe(domain, text)

```  
Lines 345:351

```diff
	            return WhoisTw(domain, text)
	        elif domain.endswith('.tr'):
	            return WhoisTr(domain, text)
-	        elif domain.endswith('.ve'):
+	        elif True:
	            return WhoisVe(domain, text)
	        elif domain.endswith('.ua'):
	            return WhoisUA(domain, text)

```  
Lines 347:353

```diff
	            return WhoisTr(domain, text)
	        elif domain.endswith('.ve'):
	            return WhoisVe(domain, text)
-	        elif domain.endswith('.ua'):
+	        elif True:
	            return WhoisUA(domain, text)
	        elif domain.endswith('.kz'):
	            return WhoisKZ(domain, text)

```  
Lines 349:355

```diff
	            return WhoisVe(domain, text)
	        elif domain.endswith('.ua'):
	            return WhoisUA(domain, text)
-	        elif domain.endswith('.kz'):
+	        elif True:
	            return WhoisKZ(domain, text)
	        elif domain.endswith('.ir'):
	            return WhoisIR(domain, text)

```  
Lines 351:357

```diff
	            return WhoisUA(domain, text)
	        elif domain.endswith('.kz'):
	            return WhoisKZ(domain, text)
-	        elif domain.endswith('.ir'):
+	        elif True:
	            return WhoisIR(domain, text)
	        elif domain.endswith('.中国'):
	            return WhoisZhongGuo(domain, text)

```  
Lines 353:359

```diff
	            return WhoisKZ(domain, text)
	        elif domain.endswith('.ir'):
	            return WhoisIR(domain, text)
-	        elif domain.endswith('.中国'):
+	        elif True:
	            return WhoisZhongGuo(domain, text)
	        elif domain.endswith('.website'):
	            return WhoisWebsite(domain, text)

```  
Lines 357:363

```diff
	            return WhoisZhongGuo(domain, text)
	        elif domain.endswith('.website'):
	            return WhoisWebsite(domain, text)
-	        elif domain.endswith('.sg'):
+	        elif True:
	            return WhoisSG(domain, text)
	        elif domain.endswith('.ml'):
	            return WhoisML(domain, text)

```  
Lines 359:365

```diff
	            return WhoisWebsite(domain, text)
	        elif domain.endswith('.sg'):
	            return WhoisSG(domain, text)
-	        elif domain.endswith('.ml'):
+	        elif True:
	            return WhoisML(domain, text)
	        elif domain.endswith('.ooo'):
	            return WhoisOOO(domain, text)

```
### test_com_expiration_str_dbl_2_str_hlf_2_str_hlf_0
  
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
Lines 91:97

```diff
	def cast_date(s, dayfirst=False, yearfirst=False):
	    """Convert any date string found in WHOIS to a datetime object.
	    """
-	    if DATEUTIL:
+	    if False:
	        try:
	            return dp.parse(
	                s,

```  
Lines 98:104

```diff
	                tzinfos=tz_data,
	                dayfirst=dayfirst,
	                yearfirst=yearfirst
-	            ).replace(tzinfo=None)
+	            ).replace(tzinfo=(False))
	        except Exception:
	            return datetime_parse(s)
	    else:

```  
Lines 98:104

```diff
	                tzinfos=tz_data,
	                dayfirst=dayfirst,
	                yearfirst=yearfirst
-	            ).replace(tzinfo=None)
+	            ).replace(tzinfo=(True))
	        except Exception:
	            return datetime_parse(s)
	    else:

```
### test_cn_parse_str_emp_16_str_hlf_0
  
Lines 2398:2404

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if text.strip() == 'No matching record.':
+	        if (text.strip() >= 'No matching record.'):
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text, self.regex)

```  
Lines 2398:2404

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if text.strip() == 'No matching record.':
+	        if (text.strip() > 'No matching record.'):
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text, self.regex)

```
### test_com_expiration_none_0
  
Lines 198:204

```diff
	        """Given whois output in ``text``, return an instance of ``WhoisEntry``
	        that represents its parsed contents.
	        """
-	        if text.strip() == 'No whois server is known for this kind of object.':
+	        if False:
	            raise PywhoisError(text)
	
	        if domain.endswith('.com'):

```
### test_com_expiration_none_2_str_hlf_1
  
Lines 361:367

```diff
	            return WhoisSG(domain, text)
	        elif domain.endswith('.ml'):
	            return WhoisML(domain, text)
-	        elif domain.endswith('.ooo'):
+	        elif True:
	            return WhoisOOO(domain, text)
	        elif domain.endswith('.market'):
	            return WhoisMarket(domain, text)

```
### test_com_expiration_str_hlf_0_str_hlf_1_str_hlf_0
  
Lines 319:325

```diff
	            return WhoisCn(domain, text)
	        elif domain.endswith('.app'):
	            return WhoisApp(domain, text)
-	        elif domain.endswith('.money'):
+	        elif True:
	            return WhoisMoney(domain, text)
	        elif domain.endswith('.cl'):
	            return WhoisCl(domain, text)

```  
Lines 329:335

```diff
	            return WhoisBy(domain, text)
	        elif domain.endswith('.cr'):
	            return WhoisCr(domain, text)
-	        elif domain.endswith('.do'):
+	        elif True:
	            return WhoisDo(domain, text)
	        elif domain.endswith('.jobs'):
	            return WhoisJobs(domain, text)

```  
Lines 331:337

```diff
	            return WhoisCr(domain, text)
	        elif domain.endswith('.do'):
	            return WhoisDo(domain, text)
-	        elif domain.endswith('.jobs'):
+	        elif True:
	            return WhoisJobs(domain, text)
	        elif domain.endswith('.lat'):
	            return WhoisLat(domain, text)

```  
Lines 333:339

```diff
	            return WhoisDo(domain, text)
	        elif domain.endswith('.jobs'):
	            return WhoisJobs(domain, text)
-	        elif domain.endswith('.lat'):
+	        elif True:
	            return WhoisLat(domain, text)
	        elif domain.endswith('.pe'):
	            return WhoisPe(domain, text)

```
### test_com_expiration_str_emp_0_str_hlf_0
  
Lines 317:323

```diff
	            return WhoisOnline(domain, text)
	        elif domain.endswith('.cn'):
	            return WhoisCn(domain, text)
-	        elif domain.endswith('.app'):
+	        elif True:
	            return WhoisApp(domain, text)
	        elif domain.endswith('.money'):
	            return WhoisMoney(domain, text)

```
### test_il_parse_str_hlf_27
  
Lines 491:497

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if text.strip() == 'NOT FOUND':
+	        if True:
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text)

```  
Lines 491:497

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if text.strip() == 'NOT FOUND':
+	        if (text.strip() >= 'NOT FOUND'):
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text)

```  
Lines 491:497

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if text.strip() == 'NOT FOUND':
+	        if (text.strip() != 'NOT FOUND'):
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text)

```  
Lines 491:497

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if text.strip() == 'NOT FOUND':
+	        if (text.strip() > 'NOT FOUND'):
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text)

```
### test_il_parse_str_hlf_27_str_emp_0
  
Lines 491:497

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if text.strip() == 'NOT FOUND':
+	        if (text.strip() < 'NOT FOUND'):
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text)

```  
Lines 491:497

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if text.strip() == 'NOT FOUND':
+	        if (text.strip() <= 'NOT FOUND'):
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text)

```
## Alive Mutants
  
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
Lines 91:97

```diff
	def cast_date(s, dayfirst=False, yearfirst=False):
	    """Convert any date string found in WHOIS to a datetime object.
	    """
-	    if DATEUTIL:
+	    if True:
	        try:
	            return dp.parse(
	                s,

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
Lines 134:140

```diff
	    yearfirst = False
	
	    def __init__(self, domain, text, regex=None):
-	        if 'This TLD has no whois server, but you can access the whois database at' in text:
+	        if False:
	            raise PywhoisError(text)
	        else:
	            self.domain = domain

```  
Lines 150:156

```diff
	        for attr, regex in list(self._regex.items()):
	            if regex:
	                values = []
-	                for data in re.findall(regex, self.text, re.IGNORECASE | re.M):
+	                for data in re.findall(regex, self.text, (re.IGNORECASE ^ re.M)):
	
	                    matches = data if isinstance(data, tuple) else [data]
	                    for value in matches:

```  
Lines 158:164

```diff
	                        if value and value not in values:
	                            # avoid duplicates
	                            values.append(value)
-	                if values and attr in ('registrar', 'whois_server', 'referral_url'):
+	                if False:
	                    values = values[-1]  # ignore junk
	                if len(values) == 1:
	                    values = values[0]

```  
Lines 159:165

```diff
	                            # avoid duplicates
	                            values.append(value)
	                if values and attr in ('registrar', 'whois_server', 'referral_url'):
-	                    values = values[-1]  # ignore junk
+	                    values = values[(-1)]  # ignore junk
	                if len(values) == 1:
	                    values = values[0]
	                elif not values:

```  
Lines 161:167

```diff
	                if values and attr in ('registrar', 'whois_server', 'referral_url'):
	                    values = values[-1]  # ignore junk
	                if len(values) == 1:
-	                    values = values[0]
+	                    values = values[<_ast.Constant object at 0x7f2cbf50fb50>]
	                elif not values:
	                    values = None
	

```  
Lines 201:207

```diff
	        if text.strip() == 'No whois server is known for this kind of object.':
	            raise PywhoisError(text)
	
-	        if domain.endswith('.com'):
+	        if False:
	            return WhoisCom(domain, text)
	        elif domain.endswith('.net'):
	            return WhoisNet(domain, text)

```  
Lines 203:209

```diff
	
	        if domain.endswith('.com'):
	            return WhoisCom(domain, text)
-	        elif domain.endswith('.net'):
+	        elif False:
	            return WhoisNet(domain, text)
	        elif domain.endswith('.org'):
	            return WhoisOrg(domain, text)

```  
Lines 205:211

```diff
	            return WhoisCom(domain, text)
	        elif domain.endswith('.net'):
	            return WhoisNet(domain, text)
-	        elif domain.endswith('.org'):
+	        elif False:
	            return WhoisOrg(domain, text)
	        elif domain.endswith('.name'):
	            return WhoisName(domain, text)

```  
Lines 207:213

```diff
	            return WhoisNet(domain, text)
	        elif domain.endswith('.org'):
	            return WhoisOrg(domain, text)
-	        elif domain.endswith('.name'):
+	        elif False:
	            return WhoisName(domain, text)
	        elif domain.endswith('.me'):
	            return WhoisMe(domain, text)

```  
Lines 209:215

```diff
	            return WhoisOrg(domain, text)
	        elif domain.endswith('.name'):
	            return WhoisName(domain, text)
-	        elif domain.endswith('.me'):
+	        elif False:
	            return WhoisMe(domain, text)
	        elif domain.endswith('ae'):
	            return WhoisAe(domain, text)

```  
Lines 211:217

```diff
	            return WhoisName(domain, text)
	        elif domain.endswith('.me'):
	            return WhoisMe(domain, text)
-	        elif domain.endswith('ae'):
+	        elif False:
	            return WhoisAe(domain, text)
	        elif domain.endswith('.au'):
	            return WhoisAU(domain, text)

```  
Lines 213:219

```diff
	            return WhoisMe(domain, text)
	        elif domain.endswith('ae'):
	            return WhoisAe(domain, text)
-	        elif domain.endswith('.au'):
+	        elif False:
	            return WhoisAU(domain, text)
	        elif domain.endswith('.ru'):
	            return WhoisRu(domain, text)

```  
Lines 215:221

```diff
	            return WhoisAe(domain, text)
	        elif domain.endswith('.au'):
	            return WhoisAU(domain, text)
-	        elif domain.endswith('.ru'):
+	        elif False:
	            return WhoisRu(domain, text)
	        elif domain.endswith('.us'):
	            return WhoisUs(domain, text)

```  
Lines 217:223

```diff
	            return WhoisAU(domain, text)
	        elif domain.endswith('.ru'):
	            return WhoisRu(domain, text)
-	        elif domain.endswith('.us'):
+	        elif False:
	            return WhoisUs(domain, text)
	        elif domain.endswith('.uk'):
	            return WhoisUk(domain, text)

```  
Lines 219:225

```diff
	            return WhoisRu(domain, text)
	        elif domain.endswith('.us'):
	            return WhoisUs(domain, text)
-	        elif domain.endswith('.uk'):
+	        elif False:
	            return WhoisUk(domain, text)
	        elif domain.endswith('.fr'):
	            return WhoisFr(domain, text)

```  
Lines 221:227

```diff
	            return WhoisUs(domain, text)
	        elif domain.endswith('.uk'):
	            return WhoisUk(domain, text)
-	        elif domain.endswith('.fr'):
+	        elif False:
	            return WhoisFr(domain, text)
	        elif domain.endswith('.nl'):
	            return WhoisNl(domain, text)

```  
Lines 225:231

```diff
	            return WhoisFr(domain, text)
	        elif domain.endswith('.nl'):
	            return WhoisNl(domain, text)
-	        elif domain.endswith('.fi'):
+	        elif False:
	            return WhoisFi(domain, text)
	        elif domain.endswith('.hr'):
	            return WhoisHr(domain, text)

```  
Lines 227:233

```diff
	            return WhoisNl(domain, text)
	        elif domain.endswith('.fi'):
	            return WhoisFi(domain, text)
-	        elif domain.endswith('.hr'):
+	        elif False:
	            return WhoisHr(domain, text)
	        elif domain.endswith('.hn'):
	            return WhoisHn(domain, text)

```  
Lines 229:235

```diff
	            return WhoisFi(domain, text)
	        elif domain.endswith('.hr'):
	            return WhoisHr(domain, text)
-	        elif domain.endswith('.hn'):
+	        elif False:
	            return WhoisHn(domain, text)
	        elif domain.endswith('.hk'):
	            return WhoisHk(domain, text)

```  
Lines 231:237

```diff
	            return WhoisHr(domain, text)
	        elif domain.endswith('.hn'):
	            return WhoisHn(domain, text)
-	        elif domain.endswith('.hk'):
+	        elif False:
	            return WhoisHk(domain, text)
	        elif domain.endswith('.jp'):
	            return WhoisJp(domain, text)

```  
Lines 233:239

```diff
	            return WhoisHn(domain, text)
	        elif domain.endswith('.hk'):
	            return WhoisHk(domain, text)
-	        elif domain.endswith('.jp'):
+	        elif False:
	            return WhoisJp(domain, text)
	        elif domain.endswith('.pl'):
	            return WhoisPl(domain, text)

```  
Lines 235:241

```diff
	            return WhoisHk(domain, text)
	        elif domain.endswith('.jp'):
	            return WhoisJp(domain, text)
-	        elif domain.endswith('.pl'):
+	        elif False:
	            return WhoisPl(domain, text)
	        elif domain.endswith('.br'):
	            return WhoisBr(domain, text)

```  
Lines 237:243

```diff
	            return WhoisJp(domain, text)
	        elif domain.endswith('.pl'):
	            return WhoisPl(domain, text)
-	        elif domain.endswith('.br'):
+	        elif False:
	            return WhoisBr(domain, text)
	        elif domain.endswith('.eu'):
	            return WhoisEu(domain, text)

```  
Lines 239:245

```diff
	            return WhoisPl(domain, text)
	        elif domain.endswith('.br'):
	            return WhoisBr(domain, text)
-	        elif domain.endswith('.eu'):
+	        elif False:
	            return WhoisEu(domain, text)
	        elif domain.endswith('.ee'):
	            return WhoisEe(domain, text)

```  
Lines 241:247

```diff
	            return WhoisBr(domain, text)
	        elif domain.endswith('.eu'):
	            return WhoisEu(domain, text)
-	        elif domain.endswith('.ee'):
+	        elif False:
	            return WhoisEe(domain, text)
	        elif domain.endswith('.kr'):
	            return WhoisKr(domain, text)

```  
Lines 243:249

```diff
	            return WhoisEu(domain, text)
	        elif domain.endswith('.ee'):
	            return WhoisEe(domain, text)
-	        elif domain.endswith('.kr'):
+	        elif False:
	            return WhoisKr(domain, text)
	        elif domain.endswith('.pt'):
	            return WhoisPt(domain, text)

```  
Lines 245:251

```diff
	            return WhoisEe(domain, text)
	        elif domain.endswith('.kr'):
	            return WhoisKr(domain, text)
-	        elif domain.endswith('.pt'):
+	        elif False:
	            return WhoisPt(domain, text)
	        elif domain.endswith('.bg'):
	            return WhoisBg(domain, text)

```  
Lines 247:253

```diff
	            return WhoisKr(domain, text)
	        elif domain.endswith('.pt'):
	            return WhoisPt(domain, text)
-	        elif domain.endswith('.bg'):
+	        elif False:
	            return WhoisBg(domain, text)
	        elif domain.endswith('.de'):
	            return WhoisDe(domain, text)

```  
Lines 249:255

```diff
	            return WhoisPt(domain, text)
	        elif domain.endswith('.bg'):
	            return WhoisBg(domain, text)
-	        elif domain.endswith('.de'):
+	        elif False:
	            return WhoisDe(domain, text)
	        elif domain.endswith('.at'):
	            return WhoisAt(domain, text)

```  
Lines 251:257

```diff
	            return WhoisBg(domain, text)
	        elif domain.endswith('.de'):
	            return WhoisDe(domain, text)
-	        elif domain.endswith('.at'):
+	        elif False:
	            return WhoisAt(domain, text)
	        elif domain.endswith('.ca'):
	            return WhoisCa(domain, text)

```  
Lines 255:261

```diff
	            return WhoisAt(domain, text)
	        elif domain.endswith('.ca'):
	            return WhoisCa(domain, text)
-	        elif domain.endswith('.be'):
+	        elif False:
	            return WhoisBe(domain, text)
	        elif domain.endswith('.рф'):
	            return WhoisRf(domain, text)

```  
Lines 257:263

```diff
	            return WhoisCa(domain, text)
	        elif domain.endswith('.be'):
	            return WhoisBe(domain, text)
-	        elif domain.endswith('.рф'):
+	        elif False:
	            return WhoisRf(domain, text)
	        elif domain.endswith('.info'):
	            return WhoisInfo(domain, text)

```  
Lines 259:265

```diff
	            return WhoisBe(domain, text)
	        elif domain.endswith('.рф'):
	            return WhoisRf(domain, text)
-	        elif domain.endswith('.info'):
+	        elif False:
	            return WhoisInfo(domain, text)
	        elif domain.endswith('.su'):
	            return WhoisSu(domain, text)

```  
Lines 261:267

```diff
	            return WhoisRf(domain, text)
	        elif domain.endswith('.info'):
	            return WhoisInfo(domain, text)
-	        elif domain.endswith('.su'):
+	        elif False:
	            return WhoisSu(domain, text)
	        elif domain.endswith('si'):
	            return WhoisSi(domain, text)

```  
Lines 263:269

```diff
	            return WhoisInfo(domain, text)
	        elif domain.endswith('.su'):
	            return WhoisSu(domain, text)
-	        elif domain.endswith('si'):
+	        elif False:
	            return WhoisSi(domain, text)
	        elif domain.endswith('.kg'):
	            return WhoisKg(domain, text)

```  
Lines 265:271

```diff
	            return WhoisSu(domain, text)
	        elif domain.endswith('si'):
	            return WhoisSi(domain, text)
-	        elif domain.endswith('.kg'):
+	        elif False:
	            return WhoisKg(domain, text)
	        elif domain.endswith('.io'):
	            return WhoisIo(domain, text)

```  
Lines 267:273

```diff
	            return WhoisSi(domain, text)
	        elif domain.endswith('.kg'):
	            return WhoisKg(domain, text)
-	        elif domain.endswith('.io'):
+	        elif False:
	            return WhoisIo(domain, text)
	        elif domain.endswith('.biz'):
	            return WhoisBiz(domain, text)

```  
Lines 269:275

```diff
	            return WhoisKg(domain, text)
	        elif domain.endswith('.io'):
	            return WhoisIo(domain, text)
-	        elif domain.endswith('.biz'):
+	        elif False:
	            return WhoisBiz(domain, text)
	        elif domain.endswith('.mobi'):
	            return WhoisMobi(domain, text)

```  
Lines 271:277

```diff
	            return WhoisIo(domain, text)
	        elif domain.endswith('.biz'):
	            return WhoisBiz(domain, text)
-	        elif domain.endswith('.mobi'):
+	        elif False:
	            return WhoisMobi(domain, text)
	        elif domain.endswith('.ch'):
	            return WhoisChLi(domain, text)

```  
Lines 273:279

```diff
	            return WhoisBiz(domain, text)
	        elif domain.endswith('.mobi'):
	            return WhoisMobi(domain, text)
-	        elif domain.endswith('.ch'):
+	        elif False:
	            return WhoisChLi(domain, text)
	        elif domain.endswith('.li'):
	            return WhoisChLi(domain, text)

```  
Lines 275:281

```diff
	            return WhoisMobi(domain, text)
	        elif domain.endswith('.ch'):
	            return WhoisChLi(domain, text)
-	        elif domain.endswith('.li'):
+	        elif False:
	            return WhoisChLi(domain, text)
	        elif domain.endswith('.id'):
	            return WhoisID(domain, text)

```  
Lines 277:283

```diff
	            return WhoisChLi(domain, text)
	        elif domain.endswith('.li'):
	            return WhoisChLi(domain, text)
-	        elif domain.endswith('.id'):
+	        elif False:
	            return WhoisID(domain, text)
	        elif domain.endswith('.sk'):
	            return WhoisSK(domain, text)

```  
Lines 281:287

```diff
	            return WhoisID(domain, text)
	        elif domain.endswith('.sk'):
	            return WhoisSK(domain, text)
-	        elif domain.endswith('.se'):
+	        elif False:
	            return WhoisSe(domain, text)
	        elif domain.endswith('no'):
	            return WhoisNo(domain, text)

```  
Lines 283:289

```diff
	            return WhoisSK(domain, text)
	        elif domain.endswith('.se'):
	            return WhoisSe(domain, text)
-	        elif domain.endswith('no'):
+	        elif False:
	            return WhoisNo(domain, text)
	        elif domain.endswith('.nu'):
	            return WhoisSe(domain, text)

```  
Lines 285:291

```diff
	            return WhoisSe(domain, text)
	        elif domain.endswith('no'):
	            return WhoisNo(domain, text)
-	        elif domain.endswith('.nu'):
+	        elif False:
	            return WhoisSe(domain, text)
	        elif domain.endswith('.is'):
	            return WhoisIs(domain, text)

```  
Lines 287:293

```diff
	            return WhoisNo(domain, text)
	        elif domain.endswith('.nu'):
	            return WhoisSe(domain, text)
-	        elif domain.endswith('.is'):
+	        elif False:
	            return WhoisIs(domain, text)
	        elif domain.endswith('.dk'):
	            return WhoisDk(domain, text)

```  
Lines 291:297

```diff
	            return WhoisIs(domain, text)
	        elif domain.endswith('.dk'):
	            return WhoisDk(domain, text)
-	        elif domain.endswith('.it'):
+	        elif False:
	            return WhoisIt(domain, text)
	        elif domain.endswith('.mx'):
	            return WhoisMx(domain, text)

```  
Lines 293:299

```diff
	            return WhoisDk(domain, text)
	        elif domain.endswith('.it'):
	            return WhoisIt(domain, text)
-	        elif domain.endswith('.mx'):
+	        elif False:
	            return WhoisMx(domain, text)
	        elif domain.endswith('.ai'):
	            return WhoisAi(domain, text)

```  
Lines 295:301

```diff
	            return WhoisIt(domain, text)
	        elif domain.endswith('.mx'):
	            return WhoisMx(domain, text)
-	        elif domain.endswith('.ai'):
+	        elif False:
	            return WhoisAi(domain, text)
	        elif domain.endswith('.il'):
	            return WhoisIl(domain, text)

```  
Lines 299:305

```diff
	            return WhoisAi(domain, text)
	        elif domain.endswith('.il'):
	            return WhoisIl(domain, text)
-	        elif domain.endswith('.in'):
+	        elif False:
	            return WhoisIn(domain, text)
	        elif domain.endswith('.cat'):
	            return WhoisCat(domain, text)

```  
Lines 301:307

```diff
	            return WhoisIl(domain, text)
	        elif domain.endswith('.in'):
	            return WhoisIn(domain, text)
-	        elif domain.endswith('.cat'):
+	        elif False:
	            return WhoisCat(domain, text)
	        elif domain.endswith('.ie'):
	            return WhoisIe(domain, text)

```  
Lines 305:311

```diff
	            return WhoisCat(domain, text)
	        elif domain.endswith('.ie'):
	            return WhoisIe(domain, text)
-	        elif domain.endswith('.nz'):
+	        elif False:
	            return WhoisNz(domain, text)
	        elif domain.endswith('.space'):
	            return WhoisSpace(domain, text)

```  
Lines 307:313

```diff
	            return WhoisIe(domain, text)
	        elif domain.endswith('.nz'):
	            return WhoisNz(domain, text)
-	        elif domain.endswith('.space'):
+	        elif False:
	            return WhoisSpace(domain, text)
	        elif domain.endswith('.lu'):
	            return WhoisLu(domain, text)

```  
Lines 309:315

```diff
	            return WhoisNz(domain, text)
	        elif domain.endswith('.space'):
	            return WhoisSpace(domain, text)
-	        elif domain.endswith('.lu'):
+	        elif False:
	            return WhoisLu(domain, text)
	        elif domain.endswith('.cz'):
	            return WhoisCz(domain, text)

```  
Lines 311:317

```diff
	            return WhoisSpace(domain, text)
	        elif domain.endswith('.lu'):
	            return WhoisLu(domain, text)
-	        elif domain.endswith('.cz'):
+	        elif False:
	            return WhoisCz(domain, text)
	        elif domain.endswith('.online'):
	            return WhoisOnline(domain, text)

```  
Lines 313:319

```diff
	            return WhoisLu(domain, text)
	        elif domain.endswith('.cz'):
	            return WhoisCz(domain, text)
-	        elif domain.endswith('.online'):
+	        elif False:
	            return WhoisOnline(domain, text)
	        elif domain.endswith('.cn'):
	            return WhoisCn(domain, text)

```  
Lines 317:323

```diff
	            return WhoisOnline(domain, text)
	        elif domain.endswith('.cn'):
	            return WhoisCn(domain, text)
-	        elif domain.endswith('.app'):
+	        elif False:
	            return WhoisApp(domain, text)
	        elif domain.endswith('.money'):
	            return WhoisMoney(domain, text)

```  
Lines 319:325

```diff
	            return WhoisCn(domain, text)
	        elif domain.endswith('.app'):
	            return WhoisApp(domain, text)
-	        elif domain.endswith('.money'):
+	        elif False:
	            return WhoisMoney(domain, text)
	        elif domain.endswith('.cl'):
	            return WhoisCl(domain, text)

```  
Lines 321:327

```diff
	            return WhoisApp(domain, text)
	        elif domain.endswith('.money'):
	            return WhoisMoney(domain, text)
-	        elif domain.endswith('.cl'):
+	        elif False:
	            return WhoisCl(domain, text)
	        elif domain.endswith('.ar'):
	            return WhoisAr(domain, text)

```  
Lines 323:329

```diff
	            return WhoisMoney(domain, text)
	        elif domain.endswith('.cl'):
	            return WhoisCl(domain, text)
-	        elif domain.endswith('.ar'):
+	        elif False:
	            return WhoisAr(domain, text)
	        elif domain.endswith('.by'):
	            return WhoisBy(domain, text)

```  
Lines 325:331

```diff
	            return WhoisCl(domain, text)
	        elif domain.endswith('.ar'):
	            return WhoisAr(domain, text)
-	        elif domain.endswith('.by'):
+	        elif False:
	            return WhoisBy(domain, text)
	        elif domain.endswith('.cr'):
	            return WhoisCr(domain, text)

```  
Lines 327:333

```diff
	            return WhoisAr(domain, text)
	        elif domain.endswith('.by'):
	            return WhoisBy(domain, text)
-	        elif domain.endswith('.cr'):
+	        elif False:
	            return WhoisCr(domain, text)
	        elif domain.endswith('.do'):
	            return WhoisDo(domain, text)

```  
Lines 329:335

```diff
	            return WhoisBy(domain, text)
	        elif domain.endswith('.cr'):
	            return WhoisCr(domain, text)
-	        elif domain.endswith('.do'):
+	        elif False:
	            return WhoisDo(domain, text)
	        elif domain.endswith('.jobs'):
	            return WhoisJobs(domain, text)

```  
Lines 331:337

```diff
	            return WhoisCr(domain, text)
	        elif domain.endswith('.do'):
	            return WhoisDo(domain, text)
-	        elif domain.endswith('.jobs'):
+	        elif False:
	            return WhoisJobs(domain, text)
	        elif domain.endswith('.lat'):
	            return WhoisLat(domain, text)

```  
Lines 333:339

```diff
	            return WhoisDo(domain, text)
	        elif domain.endswith('.jobs'):
	            return WhoisJobs(domain, text)
-	        elif domain.endswith('.lat'):
+	        elif False:
	            return WhoisLat(domain, text)
	        elif domain.endswith('.pe'):
	            return WhoisPe(domain, text)

```  
Lines 335:341

```diff
	            return WhoisJobs(domain, text)
	        elif domain.endswith('.lat'):
	            return WhoisLat(domain, text)
-	        elif domain.endswith('.pe'):
+	        elif False:
	            return WhoisPe(domain, text)
	        elif domain.endswith('.ro'):
	            return WhoisRo(domain, text)

```  
Lines 337:343

```diff
	            return WhoisLat(domain, text)
	        elif domain.endswith('.pe'):
	            return WhoisPe(domain, text)
-	        elif domain.endswith('.ro'):
+	        elif False:
	            return WhoisRo(domain, text)
	        elif domain.endswith('.sa'):
	            return WhoisSa(domain, text)

```  
Lines 339:345

```diff
	            return WhoisPe(domain, text)
	        elif domain.endswith('.ro'):
	            return WhoisRo(domain, text)
-	        elif domain.endswith('.sa'):
+	        elif False:
	            return WhoisSa(domain, text)
	        elif domain.endswith('.tw'):
	            return WhoisTw(domain, text)

```  
Lines 341:347

```diff
	            return WhoisRo(domain, text)
	        elif domain.endswith('.sa'):
	            return WhoisSa(domain, text)
-	        elif domain.endswith('.tw'):
+	        elif False:
	            return WhoisTw(domain, text)
	        elif domain.endswith('.tr'):
	            return WhoisTr(domain, text)

```  
Lines 343:349

```diff
	            return WhoisSa(domain, text)
	        elif domain.endswith('.tw'):
	            return WhoisTw(domain, text)
-	        elif domain.endswith('.tr'):
+	        elif False:
	            return WhoisTr(domain, text)
	        elif domain.endswith('.ve'):
	            return WhoisVe(domain, text)

```  
Lines 345:351

```diff
	            return WhoisTw(domain, text)
	        elif domain.endswith('.tr'):
	            return WhoisTr(domain, text)
-	        elif domain.endswith('.ve'):
+	        elif False:
	            return WhoisVe(domain, text)
	        elif domain.endswith('.ua'):
	            return WhoisUA(domain, text)

```  
Lines 347:353

```diff
	            return WhoisTr(domain, text)
	        elif domain.endswith('.ve'):
	            return WhoisVe(domain, text)
-	        elif domain.endswith('.ua'):
+	        elif False:
	            return WhoisUA(domain, text)
	        elif domain.endswith('.kz'):
	            return WhoisKZ(domain, text)

```  
Lines 349:355

```diff
	            return WhoisVe(domain, text)
	        elif domain.endswith('.ua'):
	            return WhoisUA(domain, text)
-	        elif domain.endswith('.kz'):
+	        elif False:
	            return WhoisKZ(domain, text)
	        elif domain.endswith('.ir'):
	            return WhoisIR(domain, text)

```  
Lines 351:357

```diff
	            return WhoisUA(domain, text)
	        elif domain.endswith('.kz'):
	            return WhoisKZ(domain, text)
-	        elif domain.endswith('.ir'):
+	        elif False:
	            return WhoisIR(domain, text)
	        elif domain.endswith('.中国'):
	            return WhoisZhongGuo(domain, text)

```  
Lines 353:359

```diff
	            return WhoisKZ(domain, text)
	        elif domain.endswith('.ir'):
	            return WhoisIR(domain, text)
-	        elif domain.endswith('.中国'):
+	        elif False:
	            return WhoisZhongGuo(domain, text)
	        elif domain.endswith('.website'):
	            return WhoisWebsite(domain, text)

```  
Lines 355:361

```diff
	            return WhoisIR(domain, text)
	        elif domain.endswith('.中国'):
	            return WhoisZhongGuo(domain, text)
-	        elif domain.endswith('.website'):
+	        elif True:
	            return WhoisWebsite(domain, text)
	        elif domain.endswith('.sg'):
	            return WhoisSG(domain, text)

```  
Lines 355:361

```diff
	            return WhoisIR(domain, text)
	        elif domain.endswith('.中国'):
	            return WhoisZhongGuo(domain, text)
-	        elif domain.endswith('.website'):
+	        elif False:
	            return WhoisWebsite(domain, text)
	        elif domain.endswith('.sg'):
	            return WhoisSG(domain, text)

```  
Lines 357:363

```diff
	            return WhoisZhongGuo(domain, text)
	        elif domain.endswith('.website'):
	            return WhoisWebsite(domain, text)
-	        elif domain.endswith('.sg'):
+	        elif False:
	            return WhoisSG(domain, text)
	        elif domain.endswith('.ml'):
	            return WhoisML(domain, text)

```  
Lines 359:365

```diff
	            return WhoisWebsite(domain, text)
	        elif domain.endswith('.sg'):
	            return WhoisSG(domain, text)
-	        elif domain.endswith('.ml'):
+	        elif False:
	            return WhoisML(domain, text)
	        elif domain.endswith('.ooo'):
	            return WhoisOOO(domain, text)

```  
Lines 361:367

```diff
	            return WhoisSG(domain, text)
	        elif domain.endswith('.ml'):
	            return WhoisML(domain, text)
-	        elif domain.endswith('.ooo'):
+	        elif False:
	            return WhoisOOO(domain, text)
	        elif domain.endswith('.market'):
	            return WhoisMarket(domain, text)

```  
Lines 363:369

```diff
	            return WhoisML(domain, text)
	        elif domain.endswith('.ooo'):
	            return WhoisOOO(domain, text)
-	        elif domain.endswith('.market'):
+	        elif True:
	            return WhoisMarket(domain, text)
	        else:
	            return WhoisEntry(domain, text)

```  
Lines 363:369

```diff
	            return WhoisML(domain, text)
	        elif domain.endswith('.ooo'):
	            return WhoisOOO(domain, text)
-	        elif domain.endswith('.market'):
+	        elif False:
	            return WhoisMarket(domain, text)
	        else:
	            return WhoisEntry(domain, text)

```  
Lines 457:463

```diff
	    """
	
	    def __init__(self, domain, text):
-	        if 'No match for "' in text:
+	        if False:
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text)

```  
Lines 491:497

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if text.strip() == 'NOT FOUND':
+	        if False:
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text)

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
Lines 562:568

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if text.endswith('is free'):
+	        if False:
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text, self.regex)

```  
Lines 570:576

```diff
	        match = re.compile(r'Domain nameservers:(.*?)Record maintained by', re.DOTALL).search(text)
	        if match:
	            duplicate_nameservers_with_ip = [line.strip()
-	                                             for line in match.groups()[0].strip().splitlines()]
+	                                             for line in match.groups()[<_ast.Constant object at 0x7f2cbeaff4f0>].strip().splitlines()]
	            duplicate_nameservers_without_ip = [nameserver.split(' ')[0]
	                                                for nameserver in duplicate_nameservers_with_ip]
	            self['name_servers'] = sorted(list(set(duplicate_nameservers_without_ip)))

```  
Lines 720:726

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if 'Domain status:         available' in text or 'Not found:' in text:
+	        if ('Domain status:         available' in text and 'Not found:' in text):
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text, self.regex)

```  
Lines 720:726

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if 'Domain status:         available' in text or 'Not found:' in text:
+	        if False:
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text, self.regex)

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
Lines 1702:1708

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if 'not found.' in text:
+	        if False:
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text, self.regex)

```  
Lines 1872:1878

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if 'No match for ' in text:
+	        if False:
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text, self.regex)

```  
Lines 1880:1886

```diff
	    def _preprocess(self, attr, value):
	        if attr == 'name_servers':
	            return [
-	                line.split(":")[-1].strip()
+	                line.split(":")[(-1)].strip()
	                for line in value.split("\n")
	                if line.startswith("Hostname")
	            ]

```  
Lines 1928:1934

```diff
	    dayfirst = True
	
	    def __init__(self, domain, text):
-	        if 'No data was found' in text:
+	        if False:
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text, self.regex)

```  
Lines 1934:1940

```diff
	            WhoisEntry.__init__(self, domain, text, self.regex)
	
	    def _preprocess(self, attr, value):
-	        if attr == 'emails':
+	        if True:
	            value = value.replace(' AT ', '@')
	        return super(WhoisIl, self)._preprocess(attr, value)
	

```  
Lines 1934:1940

```diff
	            WhoisEntry.__init__(self, domain, text, self.regex)
	
	    def _preprocess(self, attr, value):
-	        if attr == 'emails':
+	        if (attr >= 'emails'):
	            value = value.replace(' AT ', '@')
	        return super(WhoisIl, self)._preprocess(attr, value)
	

```  
Lines 1934:1940

```diff
	            WhoisEntry.__init__(self, domain, text, self.regex)
	
	    def _preprocess(self, attr, value):
-	        if attr == 'emails':
+	        if (attr <= 'emails'):
	            value = value.replace(' AT ', '@')
	        return super(WhoisIl, self)._preprocess(attr, value)
	

```  
Lines 2006:2012

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if 'no matching objects' in text:
+	        if False:
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text, self.regex)

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
Lines 2398:2404

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if text.strip() == 'No matching record.':
+	        if False:
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text, self.regex)

```