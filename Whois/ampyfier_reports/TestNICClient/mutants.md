



# /home/ubuntu/projects/whois/whois/whois.py

## Newly Killed Mutants

### test_choose_server_str_dbl_0
  
Lines 210:216

```diff
	            return NICClient.HR_HOST
	
	        domain = domain.split('.')
-	        if len(domain) < 2:
+	        if (len(domain) != 2):
	            return None
	        tld = domain[-1]
	        if tld[0].isdigit():

```  
Lines 212:218

```diff
	        domain = domain.split('.')
	        if len(domain) < 2:
	            return None
-	        tld = domain[-1]
+	        tld = domain[(-1)]
	        if tld[0].isdigit():
	            return NICClient.ANICHOST
	        elif tld == 'ai':

```
### test_choose_server_str_hlf_0_str_hlf_0
  
Lines 213:219

```diff
	        if len(domain) < 2:
	            return None
	        tld = domain[-1]
-	        if tld[0].isdigit():
+	        if False:
	            return NICClient.ANICHOST
	        elif tld == 'ai':
	            return NICClient.AI_HOST

```
### test_choose_server_str_uni_0_str_hlf_0
  
Lines 221:227

```diff
	            return NICClient.APP_HOST
	        elif tld == 'dev':
	            return NICClient.DEV_HOST
-	        elif tld == 'games':
+	        elif (tld < 'games'):
	            return NICClient.GAMES_HOST
	        elif tld == 'page':
	            return NICClient.PAGE_HOST

```  
Lines 221:227

```diff
	            return NICClient.APP_HOST
	        elif tld == 'dev':
	            return NICClient.DEV_HOST
-	        elif tld == 'games':
+	        elif (tld <= 'games'):
	            return NICClient.GAMES_HOST
	        elif tld == 'page':
	            return NICClient.PAGE_HOST

```  
Lines 223:229

```diff
	            return NICClient.DEV_HOST
	        elif tld == 'games':
	            return NICClient.GAMES_HOST
-	        elif tld == 'page':
+	        elif (tld < 'page'):
	            return NICClient.PAGE_HOST
	        elif tld == 'money':
	            return NICClient.MONEY_HOST

```  
Lines 223:229

```diff
	            return NICClient.DEV_HOST
	        elif tld == 'games':
	            return NICClient.GAMES_HOST
-	        elif tld == 'page':
+	        elif (tld <= 'page'):
	            return NICClient.PAGE_HOST
	        elif tld == 'money':
	            return NICClient.MONEY_HOST

```  
Lines 225:231

```diff
	            return NICClient.GAMES_HOST
	        elif tld == 'page':
	            return NICClient.PAGE_HOST
-	        elif tld == 'money':
+	        elif (tld < 'money'):
	            return NICClient.MONEY_HOST
	        elif tld == 'online':
	            return NICClient.ONLINE_HOST

```  
Lines 225:231

```diff
	            return NICClient.GAMES_HOST
	        elif tld == 'page':
	            return NICClient.PAGE_HOST
-	        elif tld == 'money':
+	        elif (tld <= 'money'):
	            return NICClient.MONEY_HOST
	        elif tld == 'online':
	            return NICClient.ONLINE_HOST

```  
Lines 227:233

```diff
	            return NICClient.PAGE_HOST
	        elif tld == 'money':
	            return NICClient.MONEY_HOST
-	        elif tld == 'online':
+	        elif (tld < 'online'):
	            return NICClient.ONLINE_HOST
	        elif tld == 'cl':
	            return NICClient.CL_HOST

```  
Lines 227:233

```diff
	            return NICClient.PAGE_HOST
	        elif tld == 'money':
	            return NICClient.MONEY_HOST
-	        elif tld == 'online':
+	        elif (tld <= 'online'):
	            return NICClient.ONLINE_HOST
	        elif tld == 'cl':
	            return NICClient.CL_HOST

```  
Lines 243:249

```diff
	            return NICClient.DO_HOST
	        elif tld == 'de':
	            return NICClient.DE_HOST
-	        elif tld == 'hk':
+	        elif (tld < 'hk'):
	            return NICClient.HK_HOST
	        elif tld == 'hn':
	            return NICClient.HN_HOST

```  
Lines 243:249

```diff
	            return NICClient.DO_HOST
	        elif tld == 'de':
	            return NICClient.DE_HOST
-	        elif tld == 'hk':
+	        elif (tld <= 'hk'):
	            return NICClient.HK_HOST
	        elif tld == 'hn':
	            return NICClient.HN_HOST

```  
Lines 245:251

```diff
	            return NICClient.DE_HOST
	        elif tld == 'hk':
	            return NICClient.HK_HOST
-	        elif tld == 'hn':
+	        elif (tld < 'hn'):
	            return NICClient.HN_HOST
	        elif tld == 'jobs':
	            return NICClient.JOBS_HOST

```  
Lines 245:251

```diff
	            return NICClient.DE_HOST
	        elif tld == 'hk':
	            return NICClient.HK_HOST
-	        elif tld == 'hn':
+	        elif (tld <= 'hn'):
	            return NICClient.HN_HOST
	        elif tld == 'jobs':
	            return NICClient.JOBS_HOST

```  
Lines 247:253

```diff
	            return NICClient.HK_HOST
	        elif tld == 'hn':
	            return NICClient.HN_HOST
-	        elif tld == 'jobs':
+	        elif (tld < 'jobs'):
	            return NICClient.JOBS_HOST
	        elif tld == 'lat':
	            return NICClient.LAT_HOST

```  
Lines 247:253

```diff
	            return NICClient.HK_HOST
	        elif tld == 'hn':
	            return NICClient.HN_HOST
-	        elif tld == 'jobs':
+	        elif (tld <= 'jobs'):
	            return NICClient.JOBS_HOST
	        elif tld == 'lat':
	            return NICClient.LAT_HOST

```  
Lines 249:255

```diff
	            return NICClient.HN_HOST
	        elif tld == 'jobs':
	            return NICClient.JOBS_HOST
-	        elif tld == 'lat':
+	        elif (tld < 'lat'):
	            return NICClient.LAT_HOST
	        elif tld == 'li':
	            return NICClient.LI_HOST

```  
Lines 249:255

```diff
	            return NICClient.HN_HOST
	        elif tld == 'jobs':
	            return NICClient.JOBS_HOST
-	        elif tld == 'lat':
+	        elif (tld <= 'lat'):
	            return NICClient.LAT_HOST
	        elif tld == 'li':
	            return NICClient.LI_HOST

```  
Lines 251:257

```diff
	            return NICClient.JOBS_HOST
	        elif tld == 'lat':
	            return NICClient.LAT_HOST
-	        elif tld == 'li':
+	        elif (tld < 'li'):
	            return NICClient.LI_HOST
	        elif tld == 'mx':
	            return NICClient.MX_HOST

```  
Lines 251:257

```diff
	            return NICClient.JOBS_HOST
	        elif tld == 'lat':
	            return NICClient.LAT_HOST
-	        elif tld == 'li':
+	        elif (tld <= 'li'):
	            return NICClient.LI_HOST
	        elif tld == 'mx':
	            return NICClient.MX_HOST

```  
Lines 253:259

```diff
	            return NICClient.LAT_HOST
	        elif tld == 'li':
	            return NICClient.LI_HOST
-	        elif tld == 'mx':
+	        elif (tld < 'mx'):
	            return NICClient.MX_HOST
	        elif tld == 'pe':
	            return NICClient.PE_HOST

```  
Lines 253:259

```diff
	            return NICClient.LAT_HOST
	        elif tld == 'li':
	            return NICClient.LI_HOST
-	        elif tld == 'mx':
+	        elif (tld <= 'mx'):
	            return NICClient.MX_HOST
	        elif tld == 'pe':
	            return NICClient.PE_HOST

```  
Lines 255:261

```diff
	            return NICClient.LI_HOST
	        elif tld == 'mx':
	            return NICClient.MX_HOST
-	        elif tld == 'pe':
+	        elif (tld < 'pe'):
	            return NICClient.PE_HOST
	        elif tld == 'ist':
	            return NICClient.IST_HOST

```  
Lines 255:261

```diff
	            return NICClient.LI_HOST
	        elif tld == 'mx':
	            return NICClient.MX_HOST
-	        elif tld == 'pe':
+	        elif (tld <= 'pe'):
	            return NICClient.PE_HOST
	        elif tld == 'ist':
	            return NICClient.IST_HOST

```  
Lines 257:263

```diff
	            return NICClient.MX_HOST
	        elif tld == 'pe':
	            return NICClient.PE_HOST
-	        elif tld == 'ist':
+	        elif (tld < 'ist'):
	            return NICClient.IST_HOST
	        elif tld == 'kz':
	            return NICClient.KZ_HOST

```  
Lines 257:263

```diff
	            return NICClient.MX_HOST
	        elif tld == 'pe':
	            return NICClient.PE_HOST
-	        elif tld == 'ist':
+	        elif (tld <= 'ist'):
	            return NICClient.IST_HOST
	        elif tld == 'kz':
	            return NICClient.KZ_HOST

```  
Lines 259:265

```diff
	            return NICClient.PE_HOST
	        elif tld == 'ist':
	            return NICClient.IST_HOST
-	        elif tld == 'kz':
+	        elif (tld < 'kz'):
	            return NICClient.KZ_HOST
	        elif tld == 'chat':
	            return NICClient.CHAT_HOST

```  
Lines 259:265

```diff
	            return NICClient.PE_HOST
	        elif tld == 'ist':
	            return NICClient.IST_HOST
-	        elif tld == 'kz':
+	        elif (tld <= 'kz'):
	            return NICClient.KZ_HOST
	        elif tld == 'chat':
	            return NICClient.CHAT_HOST

```  
Lines 263:269

```diff
	            return NICClient.KZ_HOST
	        elif tld == 'chat':
	            return NICClient.CHAT_HOST
-	        elif tld == 'website':
+	        elif (tld < 'website'):
	            return NICClient.WEBSITE_HOST
	        elif tld == 'ooo':
	            return NICClient.OOO_HOST

```  
Lines 263:269

```diff
	            return NICClient.KZ_HOST
	        elif tld == 'chat':
	            return NICClient.CHAT_HOST
-	        elif tld == 'website':
+	        elif (tld <= 'website'):
	            return NICClient.WEBSITE_HOST
	        elif tld == 'ooo':
	            return NICClient.OOO_HOST

```  
Lines 265:271

```diff
	            return NICClient.CHAT_HOST
	        elif tld == 'website':
	            return NICClient.WEBSITE_HOST
-	        elif tld == 'ooo':
+	        elif (tld < 'ooo'):
	            return NICClient.OOO_HOST
	        elif tld == 'market':
	            return NICClient.MARKET_HOST

```  
Lines 265:271

```diff
	            return NICClient.CHAT_HOST
	        elif tld == 'website':
	            return NICClient.WEBSITE_HOST
-	        elif tld == 'ooo':
+	        elif (tld <= 'ooo'):
	            return NICClient.OOO_HOST
	        elif tld == 'market':
	            return NICClient.MARKET_HOST

```  
Lines 267:273

```diff
	            return NICClient.WEBSITE_HOST
	        elif tld == 'ooo':
	            return NICClient.OOO_HOST
-	        elif tld == 'market':
+	        elif (tld < 'market'):
	            return NICClient.MARKET_HOST
	        elif tld == 'nl':
	            return NICClient.NL_HOST    

```  
Lines 267:273

```diff
	            return NICClient.WEBSITE_HOST
	        elif tld == 'ooo':
	            return NICClient.OOO_HOST
-	        elif tld == 'market':
+	        elif (tld <= 'market'):
	            return NICClient.MARKET_HOST
	        elif tld == 'nl':
	            return NICClient.NL_HOST    

```  
Lines 269:275

```diff
	            return NICClient.OOO_HOST
	        elif tld == 'market':
	            return NICClient.MARKET_HOST
-	        elif tld == 'nl':
+	        elif (tld < 'nl'):
	            return NICClient.NL_HOST    
	        else:
	            return tld + NICClient.QNICHOST_TAIL

```  
Lines 269:275

```diff
	            return NICClient.OOO_HOST
	        elif tld == 'market':
	            return NICClient.MARKET_HOST
-	        elif tld == 'nl':
+	        elif (tld <= 'nl'):
	            return NICClient.NL_HOST    
	        else:
	            return tld + NICClient.QNICHOST_TAIL

```
### test_choose_server_str_uni_0_str_dbl_1_str_hlf_0
  
Lines 215:221

```diff
	        tld = domain[-1]
	        if tld[0].isdigit():
	            return NICClient.ANICHOST
-	        elif tld == 'ai':
+	        elif (tld < 'ai'):
	            return NICClient.AI_HOST
	        elif tld == 'app':
	            return NICClient.APP_HOST

```  
Lines 215:221

```diff
	        tld = domain[-1]
	        if tld[0].isdigit():
	            return NICClient.ANICHOST
-	        elif tld == 'ai':
+	        elif (tld <= 'ai'):
	            return NICClient.AI_HOST
	        elif tld == 'app':
	            return NICClient.APP_HOST

```  
Lines 217:223

```diff
	            return NICClient.ANICHOST
	        elif tld == 'ai':
	            return NICClient.AI_HOST
-	        elif tld == 'app':
+	        elif (tld < 'app'):
	            return NICClient.APP_HOST
	        elif tld == 'dev':
	            return NICClient.DEV_HOST

```  
Lines 217:223

```diff
	            return NICClient.ANICHOST
	        elif tld == 'ai':
	            return NICClient.AI_HOST
-	        elif tld == 'app':
+	        elif (tld <= 'app'):
	            return NICClient.APP_HOST
	        elif tld == 'dev':
	            return NICClient.DEV_HOST

```  
Lines 219:225

```diff
	            return NICClient.AI_HOST
	        elif tld == 'app':
	            return NICClient.APP_HOST
-	        elif tld == 'dev':
+	        elif (tld < 'dev'):
	            return NICClient.DEV_HOST
	        elif tld == 'games':
	            return NICClient.GAMES_HOST

```  
Lines 219:225

```diff
	            return NICClient.AI_HOST
	        elif tld == 'app':
	            return NICClient.APP_HOST
-	        elif tld == 'dev':
+	        elif (tld <= 'dev'):
	            return NICClient.DEV_HOST
	        elif tld == 'games':
	            return NICClient.GAMES_HOST

```  
Lines 229:235

```diff
	            return NICClient.MONEY_HOST
	        elif tld == 'online':
	            return NICClient.ONLINE_HOST
-	        elif tld == 'cl':
+	        elif (tld < 'cl'):
	            return NICClient.CL_HOST
	        elif tld == 'ar':
	            return NICClient.AR_HOST

```  
Lines 229:235

```diff
	            return NICClient.MONEY_HOST
	        elif tld == 'online':
	            return NICClient.ONLINE_HOST
-	        elif tld == 'cl':
+	        elif (tld <= 'cl'):
	            return NICClient.CL_HOST
	        elif tld == 'ar':
	            return NICClient.AR_HOST

```  
Lines 231:237

```diff
	            return NICClient.ONLINE_HOST
	        elif tld == 'cl':
	            return NICClient.CL_HOST
-	        elif tld == 'ar':
+	        elif (tld < 'ar'):
	            return NICClient.AR_HOST
	        elif tld == 'by':
	            return NICClient.BY_HOST

```  
Lines 231:237

```diff
	            return NICClient.ONLINE_HOST
	        elif tld == 'cl':
	            return NICClient.CL_HOST
-	        elif tld == 'ar':
+	        elif (tld <= 'ar'):
	            return NICClient.AR_HOST
	        elif tld == 'by':
	            return NICClient.BY_HOST

```  
Lines 233:239

```diff
	            return NICClient.CL_HOST
	        elif tld == 'ar':
	            return NICClient.AR_HOST
-	        elif tld == 'by':
+	        elif (tld < 'by'):
	            return NICClient.BY_HOST
	        elif tld == 'cr':
	            return NICClient.CR_HOST

```  
Lines 233:239

```diff
	            return NICClient.CL_HOST
	        elif tld == 'ar':
	            return NICClient.AR_HOST
-	        elif tld == 'by':
+	        elif (tld <= 'by'):
	            return NICClient.BY_HOST
	        elif tld == 'cr':
	            return NICClient.CR_HOST

```  
Lines 235:241

```diff
	            return NICClient.AR_HOST
	        elif tld == 'by':
	            return NICClient.BY_HOST
-	        elif tld == 'cr':
+	        elif (tld < 'cr'):
	            return NICClient.CR_HOST
	        elif tld == 'ca':
	            return NICClient.CA_HOST

```  
Lines 235:241

```diff
	            return NICClient.AR_HOST
	        elif tld == 'by':
	            return NICClient.BY_HOST
-	        elif tld == 'cr':
+	        elif (tld <= 'cr'):
	            return NICClient.CR_HOST
	        elif tld == 'ca':
	            return NICClient.CA_HOST

```  
Lines 237:243

```diff
	            return NICClient.BY_HOST
	        elif tld == 'cr':
	            return NICClient.CR_HOST
-	        elif tld == 'ca':
+	        elif (tld < 'ca'):
	            return NICClient.CA_HOST
	        elif tld == 'do':
	            return NICClient.DO_HOST

```  
Lines 237:243

```diff
	            return NICClient.BY_HOST
	        elif tld == 'cr':
	            return NICClient.CR_HOST
-	        elif tld == 'ca':
+	        elif (tld <= 'ca'):
	            return NICClient.CA_HOST
	        elif tld == 'do':
	            return NICClient.DO_HOST

```  
Lines 239:245

```diff
	            return NICClient.CR_HOST
	        elif tld == 'ca':
	            return NICClient.CA_HOST
-	        elif tld == 'do':
+	        elif (tld < 'do'):
	            return NICClient.DO_HOST
	        elif tld == 'de':
	            return NICClient.DE_HOST

```  
Lines 239:245

```diff
	            return NICClient.CR_HOST
	        elif tld == 'ca':
	            return NICClient.CA_HOST
-	        elif tld == 'do':
+	        elif (tld <= 'do'):
	            return NICClient.DO_HOST
	        elif tld == 'de':
	            return NICClient.DE_HOST

```  
Lines 241:247

```diff
	            return NICClient.CA_HOST
	        elif tld == 'do':
	            return NICClient.DO_HOST
-	        elif tld == 'de':
+	        elif (tld < 'de'):
	            return NICClient.DE_HOST
	        elif tld == 'hk':
	            return NICClient.HK_HOST

```  
Lines 241:247

```diff
	            return NICClient.CA_HOST
	        elif tld == 'do':
	            return NICClient.DO_HOST
-	        elif tld == 'de':
+	        elif (tld <= 'de'):
	            return NICClient.DE_HOST
	        elif tld == 'hk':
	            return NICClient.HK_HOST

```  
Lines 261:267

```diff
	            return NICClient.IST_HOST
	        elif tld == 'kz':
	            return NICClient.KZ_HOST
-	        elif tld == 'chat':
+	        elif (tld < 'chat'):
	            return NICClient.CHAT_HOST
	        elif tld == 'website':
	            return NICClient.WEBSITE_HOST

```  
Lines 261:267

```diff
	            return NICClient.IST_HOST
	        elif tld == 'kz':
	            return NICClient.KZ_HOST
-	        elif tld == 'chat':
+	        elif (tld <= 'chat'):
	            return NICClient.CHAT_HOST
	        elif tld == 'website':
	            return NICClient.WEBSITE_HOST

```
### test_choose_server_amp
  
Lines 102:108

```diff
	    ip_whois = [LNICHOST, RNICHOST, PNICHOST, BNICHOST, PANDIHOST]
	
	    def __init__(self):
-	        self.use_qnichost = False
+	        self.use_qnichost = (True)
	
	    def findwhois_server(self, buf, hostname, query):
	        """Search the initial TLD lookup results for the regional-specifc

```
### test_choose_server_str_emp_0
  
Lines 210:216

```diff
	            return NICClient.HR_HOST
	
	        domain = domain.split('.')
-	        if len(domain) < 2:
+	        if (len(domain) > 2):
	            return None
	        tld = domain[-1]
	        if tld[0].isdigit():

```  
Lines 210:216

```diff
	            return NICClient.HR_HOST
	
	        domain = domain.split('.')
-	        if len(domain) < 2:
+	        if False:
	            return None
	        tld = domain[-1]
	        if tld[0].isdigit():

```
## Alive Mutants
  
Lines 102:108

```diff
	    ip_whois = [LNICHOST, RNICHOST, PNICHOST, BNICHOST, PANDIHOST]
	
	    def __init__(self):
-	        self.use_qnichost = False
+	        self.use_qnichost = None
	
	    def findwhois_server(self, buf, hostname, query):
	        """Search the initial TLD lookup results for the regional-specifc

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
Lines 202:208

```diff
	            domain = domain.decode('utf-8').encode('idna').decode('utf-8')
	        except AttributeError:
	            domain = domain.decode('utf-8').encode('idna').decode('utf-8')
-	        if domain.endswith("-NORID"):
+	        if False:
	            return NICClient.NORIDHOST
	        if domain.endswith("id"):
	            return NICClient.PANDIHOST

```  
Lines 204:210

```diff
	            domain = domain.decode('utf-8').encode('idna').decode('utf-8')
	        if domain.endswith("-NORID"):
	            return NICClient.NORIDHOST
-	        if domain.endswith("id"):
+	        if False:
	            return NICClient.PANDIHOST
	        if domain.endswith("hr"):
	            return NICClient.HR_HOST

```  
Lines 206:212

```diff
	            return NICClient.NORIDHOST
	        if domain.endswith("id"):
	            return NICClient.PANDIHOST
-	        if domain.endswith("hr"):
+	        if False:
	            return NICClient.HR_HOST
	
	        domain = domain.split('.')

```  
Lines 211:217

```diff
	
	        domain = domain.split('.')
	        if len(domain) < 2:
-	            return None
+	            return (False)
	        tld = domain[-1]
	        if tld[0].isdigit():
	            return NICClient.ANICHOST

```  
Lines 211:217

```diff
	
	        domain = domain.split('.')
	        if len(domain) < 2:
-	            return None
+	            return (True)
	        tld = domain[-1]
	        if tld[0].isdigit():
	            return NICClient.ANICHOST

```  
Lines 213:219

```diff
	        if len(domain) < 2:
	            return None
	        tld = domain[-1]
-	        if tld[0].isdigit():
+	        if tld[<_ast.UnaryOp object at 0x7f8db2849970>].isdigit():
	            return NICClient.ANICHOST
	        elif tld == 'ai':
	            return NICClient.AI_HOST

```  
Lines 213:219

```diff
	        if len(domain) < 2:
	            return None
	        tld = domain[-1]
-	        if tld[0].isdigit():
+	        if tld[<_ast.Constant object at 0x7f8db26ed1c0>].isdigit():
	            return NICClient.ANICHOST
	        elif tld == 'ai':
	            return NICClient.AI_HOST

```  
Lines 215:221

```diff
	        tld = domain[-1]
	        if tld[0].isdigit():
	            return NICClient.ANICHOST
-	        elif tld == 'ai':
+	        elif False:
	            return NICClient.AI_HOST
	        elif tld == 'app':
	            return NICClient.APP_HOST

```  
Lines 217:223

```diff
	            return NICClient.ANICHOST
	        elif tld == 'ai':
	            return NICClient.AI_HOST
-	        elif tld == 'app':
+	        elif False:
	            return NICClient.APP_HOST
	        elif tld == 'dev':
	            return NICClient.DEV_HOST

```  
Lines 219:225

```diff
	            return NICClient.AI_HOST
	        elif tld == 'app':
	            return NICClient.APP_HOST
-	        elif tld == 'dev':
+	        elif False:
	            return NICClient.DEV_HOST
	        elif tld == 'games':
	            return NICClient.GAMES_HOST

```  
Lines 221:227

```diff
	            return NICClient.APP_HOST
	        elif tld == 'dev':
	            return NICClient.DEV_HOST
-	        elif tld == 'games':
+	        elif False:
	            return NICClient.GAMES_HOST
	        elif tld == 'page':
	            return NICClient.PAGE_HOST

```  
Lines 223:229

```diff
	            return NICClient.DEV_HOST
	        elif tld == 'games':
	            return NICClient.GAMES_HOST
-	        elif tld == 'page':
+	        elif False:
	            return NICClient.PAGE_HOST
	        elif tld == 'money':
	            return NICClient.MONEY_HOST

```  
Lines 225:231

```diff
	            return NICClient.GAMES_HOST
	        elif tld == 'page':
	            return NICClient.PAGE_HOST
-	        elif tld == 'money':
+	        elif False:
	            return NICClient.MONEY_HOST
	        elif tld == 'online':
	            return NICClient.ONLINE_HOST

```  
Lines 227:233

```diff
	            return NICClient.PAGE_HOST
	        elif tld == 'money':
	            return NICClient.MONEY_HOST
-	        elif tld == 'online':
+	        elif False:
	            return NICClient.ONLINE_HOST
	        elif tld == 'cl':
	            return NICClient.CL_HOST

```  
Lines 229:235

```diff
	            return NICClient.MONEY_HOST
	        elif tld == 'online':
	            return NICClient.ONLINE_HOST
-	        elif tld == 'cl':
+	        elif False:
	            return NICClient.CL_HOST
	        elif tld == 'ar':
	            return NICClient.AR_HOST

```  
Lines 231:237

```diff
	            return NICClient.ONLINE_HOST
	        elif tld == 'cl':
	            return NICClient.CL_HOST
-	        elif tld == 'ar':
+	        elif False:
	            return NICClient.AR_HOST
	        elif tld == 'by':
	            return NICClient.BY_HOST

```  
Lines 233:239

```diff
	            return NICClient.CL_HOST
	        elif tld == 'ar':
	            return NICClient.AR_HOST
-	        elif tld == 'by':
+	        elif False:
	            return NICClient.BY_HOST
	        elif tld == 'cr':
	            return NICClient.CR_HOST

```  
Lines 235:241

```diff
	            return NICClient.AR_HOST
	        elif tld == 'by':
	            return NICClient.BY_HOST
-	        elif tld == 'cr':
+	        elif False:
	            return NICClient.CR_HOST
	        elif tld == 'ca':
	            return NICClient.CA_HOST

```  
Lines 237:243

```diff
	            return NICClient.BY_HOST
	        elif tld == 'cr':
	            return NICClient.CR_HOST
-	        elif tld == 'ca':
+	        elif False:
	            return NICClient.CA_HOST
	        elif tld == 'do':
	            return NICClient.DO_HOST

```  
Lines 239:245

```diff
	            return NICClient.CR_HOST
	        elif tld == 'ca':
	            return NICClient.CA_HOST
-	        elif tld == 'do':
+	        elif False:
	            return NICClient.DO_HOST
	        elif tld == 'de':
	            return NICClient.DE_HOST

```  
Lines 241:247

```diff
	            return NICClient.CA_HOST
	        elif tld == 'do':
	            return NICClient.DO_HOST
-	        elif tld == 'de':
+	        elif False:
	            return NICClient.DE_HOST
	        elif tld == 'hk':
	            return NICClient.HK_HOST

```  
Lines 243:249

```diff
	            return NICClient.DO_HOST
	        elif tld == 'de':
	            return NICClient.DE_HOST
-	        elif tld == 'hk':
+	        elif False:
	            return NICClient.HK_HOST
	        elif tld == 'hn':
	            return NICClient.HN_HOST

```  
Lines 245:251

```diff
	            return NICClient.DE_HOST
	        elif tld == 'hk':
	            return NICClient.HK_HOST
-	        elif tld == 'hn':
+	        elif False:
	            return NICClient.HN_HOST
	        elif tld == 'jobs':
	            return NICClient.JOBS_HOST

```  
Lines 247:253

```diff
	            return NICClient.HK_HOST
	        elif tld == 'hn':
	            return NICClient.HN_HOST
-	        elif tld == 'jobs':
+	        elif False:
	            return NICClient.JOBS_HOST
	        elif tld == 'lat':
	            return NICClient.LAT_HOST

```  
Lines 249:255

```diff
	            return NICClient.HN_HOST
	        elif tld == 'jobs':
	            return NICClient.JOBS_HOST
-	        elif tld == 'lat':
+	        elif False:
	            return NICClient.LAT_HOST
	        elif tld == 'li':
	            return NICClient.LI_HOST

```  
Lines 251:257

```diff
	            return NICClient.JOBS_HOST
	        elif tld == 'lat':
	            return NICClient.LAT_HOST
-	        elif tld == 'li':
+	        elif False:
	            return NICClient.LI_HOST
	        elif tld == 'mx':
	            return NICClient.MX_HOST

```  
Lines 253:259

```diff
	            return NICClient.LAT_HOST
	        elif tld == 'li':
	            return NICClient.LI_HOST
-	        elif tld == 'mx':
+	        elif False:
	            return NICClient.MX_HOST
	        elif tld == 'pe':
	            return NICClient.PE_HOST

```  
Lines 255:261

```diff
	            return NICClient.LI_HOST
	        elif tld == 'mx':
	            return NICClient.MX_HOST
-	        elif tld == 'pe':
+	        elif False:
	            return NICClient.PE_HOST
	        elif tld == 'ist':
	            return NICClient.IST_HOST

```  
Lines 257:263

```diff
	            return NICClient.MX_HOST
	        elif tld == 'pe':
	            return NICClient.PE_HOST
-	        elif tld == 'ist':
+	        elif False:
	            return NICClient.IST_HOST
	        elif tld == 'kz':
	            return NICClient.KZ_HOST

```  
Lines 259:265

```diff
	            return NICClient.PE_HOST
	        elif tld == 'ist':
	            return NICClient.IST_HOST
-	        elif tld == 'kz':
+	        elif False:
	            return NICClient.KZ_HOST
	        elif tld == 'chat':
	            return NICClient.CHAT_HOST

```  
Lines 261:267

```diff
	            return NICClient.IST_HOST
	        elif tld == 'kz':
	            return NICClient.KZ_HOST
-	        elif tld == 'chat':
+	        elif False:
	            return NICClient.CHAT_HOST
	        elif tld == 'website':
	            return NICClient.WEBSITE_HOST

```  
Lines 263:269

```diff
	            return NICClient.KZ_HOST
	        elif tld == 'chat':
	            return NICClient.CHAT_HOST
-	        elif tld == 'website':
+	        elif False:
	            return NICClient.WEBSITE_HOST
	        elif tld == 'ooo':
	            return NICClient.OOO_HOST

```  
Lines 265:271

```diff
	            return NICClient.CHAT_HOST
	        elif tld == 'website':
	            return NICClient.WEBSITE_HOST
-	        elif tld == 'ooo':
+	        elif False:
	            return NICClient.OOO_HOST
	        elif tld == 'market':
	            return NICClient.MARKET_HOST

```  
Lines 267:273

```diff
	            return NICClient.WEBSITE_HOST
	        elif tld == 'ooo':
	            return NICClient.OOO_HOST
-	        elif tld == 'market':
+	        elif False:
	            return NICClient.MARKET_HOST
	        elif tld == 'nl':
	            return NICClient.NL_HOST    

```  
Lines 269:275

```diff
	            return NICClient.OOO_HOST
	        elif tld == 'market':
	            return NICClient.MARKET_HOST
-	        elif tld == 'nl':
+	        elif False:
	            return NICClient.NL_HOST    
	        else:
	            return tld + NICClient.QNICHOST_TAIL

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
+	if (__name__ <= '__main__'):
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