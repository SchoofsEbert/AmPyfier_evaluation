



# /home/ubuntu/projects/whois/whois/whois.py

## Newly Killed Mutants

### test_unicode_domain_and_tld_call_dup_0_call_add_0_none_1
  
Lines 114:120

```diff
	            nhost = match.groups()[0]
	            # if the whois address is domain.tld/something then
	            # s.connect((hostname, 43)) does not work
-	            if nhost.count('/') > 0:
+	            if (nhost.count('/') == 0):
	                nhost = None
	        elif hostname == NICClient.ANICHOST:
	            for nichost in NICClient.ip_whois:

```  
Lines 116:122

```diff
	            # s.connect((hostname, 43)) does not work
	            if nhost.count('/') > 0:
	                nhost = None
-	        elif hostname == NICClient.ANICHOST:
+	        elif (hostname <= NICClient.ANICHOST):
	            for nichost in NICClient.ip_whois:
	                if buf.find(nichost) != -1:
	                    nhost = nichost

```  
Lines 183:189

```diff
	            response = response.decode('utf-8', 'replace')
	            if 'with "=xxx"' in response:
	                return self.whois(query, hostname, flags, True)
-	            if flags & NICClient.WHOIS_RECURSE and nhost is None:
+	            if (flags | NICClient.WHOIS_RECURSE) and nhost is None:
	                nhost = self.findwhois_server(response, hostname, query)
	            if nhost is not None:
	                response += self.whois(query, nhost, 0, quiet=True)

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
### test_unicode_domain_and_tld_str_dbl_0_call_add_0_call_rem_1
  
Lines 114:120

```diff
	            nhost = match.groups()[0]
	            # if the whois address is domain.tld/something then
	            # s.connect((hostname, 43)) does not work
-	            if nhost.count('/') > 0:
+	            if (nhost.count('/') <= 0):
	                nhost = None
	        elif hostname == NICClient.ANICHOST:
	            for nichost in NICClient.ip_whois:

```
### test_unicode_domain_and_tld_str_dbl_0
  
Lines 102:108

```diff
	    ip_whois = [LNICHOST, RNICHOST, PNICHOST, BNICHOST, PANDIHOST]
	
	    def __init__(self):
-	        self.use_qnichost = False
+	        self.use_qnichost = (True)
	
	    def findwhois_server(self, buf, hostname, query):
	        """Search the initial TLD lookup results for the regional-specifc

```  
Lines 102:108

```diff
	    ip_whois = [LNICHOST, RNICHOST, PNICHOST, BNICHOST, PANDIHOST]
	
	    def __init__(self):
-	        self.use_qnichost = False
+	        self.use_qnichost = None
	
	    def findwhois_server(self, buf, hostname, query):
	        """Search the initial TLD lookup results for the regional-specifc

```  
Lines 109:115

```diff
	        whois server for getting contact details.
	        """
	        nhost = None
-	        match = re.compile(r'Domain Name: {}\s*.*?Whois Server: (.*?)\s'.format(query), flags=re.IGNORECASE | re.DOTALL).search(buf)
+	        match = re.compile(r'Domain Name: {}\s*.*?Whois Server: (.*?)\s'.format(query), flags=(re.IGNORECASE & re.DOTALL)).search(buf)
	        if match:
	            nhost = match.groups()[0]
	            # if the whois address is domain.tld/something then

```  
Lines 109:115

```diff
	        whois server for getting contact details.
	        """
	        nhost = None
-	        match = re.compile(r'Domain Name: {}\s*.*?Whois Server: (.*?)\s'.format(query), flags=re.IGNORECASE | re.DOTALL).search(buf)
+	        match = re.compile(r'Domain Name: {}\s*.*?Whois Server: (.*?)\s'.format(query), flags=(re.IGNORECASE ^ re.DOTALL)).search(buf)
	        if match:
	            nhost = match.groups()[0]
	            # if the whois address is domain.tld/something then

```  
Lines 110:116

```diff
	        """
	        nhost = None
	        match = re.compile(r'Domain Name: {}\s*.*?Whois Server: (.*?)\s'.format(query), flags=re.IGNORECASE | re.DOTALL).search(buf)
-	        if match:
+	        if False:
	            nhost = match.groups()[0]
	            # if the whois address is domain.tld/something then
	            # s.connect((hostname, 43)) does not work

```  
Lines 111:117

```diff
	        nhost = None
	        match = re.compile(r'Domain Name: {}\s*.*?Whois Server: (.*?)\s'.format(query), flags=re.IGNORECASE | re.DOTALL).search(buf)
	        if match:
-	            nhost = match.groups()[0]
+	            nhost = match.groups()[<_ast.UnaryOp object at 0x7f58758a3d00>]
	            # if the whois address is domain.tld/something then
	            # s.connect((hostname, 43)) does not work
	            if nhost.count('/') > 0:

```  
Lines 114:120

```diff
	            nhost = match.groups()[0]
	            # if the whois address is domain.tld/something then
	            # s.connect((hostname, 43)) does not work
-	            if nhost.count('/') > 0:
+	            if (nhost.count('/') < 0):
	                nhost = None
	        elif hostname == NICClient.ANICHOST:
	            for nichost in NICClient.ip_whois:

```  
Lines 114:120

```diff
	            nhost = match.groups()[0]
	            # if the whois address is domain.tld/something then
	            # s.connect((hostname, 43)) does not work
-	            if nhost.count('/') > 0:
+	            if (nhost.count('/') >= 0):
	                nhost = None
	        elif hostname == NICClient.ANICHOST:
	            for nichost in NICClient.ip_whois:

```  
Lines 114:120

```diff
	            nhost = match.groups()[0]
	            # if the whois address is domain.tld/something then
	            # s.connect((hostname, 43)) does not work
-	            if nhost.count('/') > 0:
+	            if (nhost.count('/') != 0):
	                nhost = None
	        elif hostname == NICClient.ANICHOST:
	            for nichost in NICClient.ip_whois:

```  
Lines 114:120

```diff
	            nhost = match.groups()[0]
	            # if the whois address is domain.tld/something then
	            # s.connect((hostname, 43)) does not work
-	            if nhost.count('/') > 0:
+	            if False:
	                nhost = None
	        elif hostname == NICClient.ANICHOST:
	            for nichost in NICClient.ip_whois:

```  
Lines 114:120

```diff
	            nhost = match.groups()[0]
	            # if the whois address is domain.tld/something then
	            # s.connect((hostname, 43)) does not work
-	            if nhost.count('/') > 0:
+	            if True:
	                nhost = None
	        elif hostname == NICClient.ANICHOST:
	            for nichost in NICClient.ip_whois:

```  
Lines 116:122

```diff
	            # s.connect((hostname, 43)) does not work
	            if nhost.count('/') > 0:
	                nhost = None
-	        elif hostname == NICClient.ANICHOST:
+	        elif (hostname >= NICClient.ANICHOST):
	            for nichost in NICClient.ip_whois:
	                if buf.find(nichost) != -1:
	                    nhost = nichost

```  
Lines 116:122

```diff
	            # s.connect((hostname, 43)) does not work
	            if nhost.count('/') > 0:
	                nhost = None
-	        elif hostname == NICClient.ANICHOST:
+	        elif (hostname != NICClient.ANICHOST):
	            for nichost in NICClient.ip_whois:
	                if buf.find(nichost) != -1:
	                    nhost = nichost

```  
Lines 116:122

```diff
	            # s.connect((hostname, 43)) does not work
	            if nhost.count('/') > 0:
	                nhost = None
-	        elif hostname == NICClient.ANICHOST:
+	        elif (hostname > NICClient.ANICHOST):
	            for nichost in NICClient.ip_whois:
	                if buf.find(nichost) != -1:
	                    nhost = nichost

```  
Lines 116:122

```diff
	            # s.connect((hostname, 43)) does not work
	            if nhost.count('/') > 0:
	                nhost = None
-	        elif hostname == NICClient.ANICHOST:
+	        elif False:
	            for nichost in NICClient.ip_whois:
	                if buf.find(nichost) != -1:
	                    nhost = nichost

```  
Lines 116:122

```diff
	            # s.connect((hostname, 43)) does not work
	            if nhost.count('/') > 0:
	                nhost = None
-	        elif hostname == NICClient.ANICHOST:
+	        elif True:
	            for nichost in NICClient.ip_whois:
	                if buf.find(nichost) != -1:
	                    nhost = nichost

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
Lines 132:138

```diff
	        is encountered.
	        """
	        response = b''
-	        if "SOCKS" in os.environ:
+	        if False:
	            try:
	                import socks
	            except ImportError as e:

```  
Lines 162:168

```diff
	            except AttributeError:
	                pass  # Already Unicode (python3's error)
	
-	            if hostname == NICClient.DENICHOST:
+	            if False:
	                query_bytes = "-T dn,ace -C UTF-8 " + query
	            elif hostname == NICClient.DK_HOST:
	                query_bytes = " --show-handles " + query

```  
Lines 164:170

```diff
	
	            if hostname == NICClient.DENICHOST:
	                query_bytes = "-T dn,ace -C UTF-8 " + query
-	            elif hostname == NICClient.DK_HOST:
+	            elif False:
	                query_bytes = " --show-handles " + query
	            elif hostname.endswith(NICClient.QNICHOST_TAIL) and many_results:
	                query_bytes = '=' + query

```  
Lines 166:172

```diff
	                query_bytes = "-T dn,ace -C UTF-8 " + query
	            elif hostname == NICClient.DK_HOST:
	                query_bytes = " --show-handles " + query
-	            elif hostname.endswith(NICClient.QNICHOST_TAIL) and many_results:
+	            elif False:
	                query_bytes = '=' + query
	            else:
	                query_bytes = query

```  
Lines 166:172

```diff
	                query_bytes = "-T dn,ace -C UTF-8 " + query
	            elif hostname == NICClient.DK_HOST:
	                query_bytes = " --show-handles " + query
-	            elif hostname.endswith(NICClient.QNICHOST_TAIL) and many_results:
+	            elif (hostname.endswith(NICClient.QNICHOST_TAIL) or many_results):
	                query_bytes = '=' + query
	            else:
	                query_bytes = query

```  
Lines 175:181

```diff
	            while True:
	                d = s.recv(4096)
	                response += d
-	                if not d:
+	                if True:
	                    break
	            s.close()
	

```  
Lines 181:187

```diff
	
	            nhost = None
	            response = response.decode('utf-8', 'replace')
-	            if 'with "=xxx"' in response:
+	            if False:
	                return self.whois(query, hostname, flags, True)
	            if flags & NICClient.WHOIS_RECURSE and nhost is None:
	                nhost = self.findwhois_server(response, hostname, query)

```  
Lines 183:189

```diff
	            response = response.decode('utf-8', 'replace')
	            if 'with "=xxx"' in response:
	                return self.whois(query, hostname, flags, True)
-	            if flags & NICClient.WHOIS_RECURSE and nhost is None:
+	            if (flags & NICClient.WHOIS_RECURSE or nhost is None):
	                nhost = self.findwhois_server(response, hostname, query)
	            if nhost is not None:
	                response += self.whois(query, nhost, 0, quiet=True)

```  
Lines 183:189

```diff
	            response = response.decode('utf-8', 'replace')
	            if 'with "=xxx"' in response:
	                return self.whois(query, hostname, flags, True)
-	            if flags & NICClient.WHOIS_RECURSE and nhost is None:
+	            if flags & NICClient.WHOIS_RECURSE and (nhost is not None):
	                nhost = self.findwhois_server(response, hostname, query)
	            if nhost is not None:
	                response += self.whois(query, nhost, 0, quiet=True)

```  
Lines 183:189

```diff
	            response = response.decode('utf-8', 'replace')
	            if 'with "=xxx"' in response:
	                return self.whois(query, hostname, flags, True)
-	            if flags & NICClient.WHOIS_RECURSE and nhost is None:
+	            if False:
	                nhost = self.findwhois_server(response, hostname, query)
	            if nhost is not None:
	                response += self.whois(query, nhost, 0, quiet=True)

```  
Lines 183:189

```diff
	            response = response.decode('utf-8', 'replace')
	            if 'with "=xxx"' in response:
	                return self.whois(query, hostname, flags, True)
-	            if flags & NICClient.WHOIS_RECURSE and nhost is None:
+	            if True:
	                nhost = self.findwhois_server(response, hostname, query)
	            if nhost is not None:
	                response += self.whois(query, nhost, 0, quiet=True)

```  
Lines 183:189

```diff
	            response = response.decode('utf-8', 'replace')
	            if 'with "=xxx"' in response:
	                return self.whois(query, hostname, flags, True)
-	            if flags & NICClient.WHOIS_RECURSE and nhost is None:
+	            if flags & NICClient.WHOIS_RECURSE and nhost is (False):
	                nhost = self.findwhois_server(response, hostname, query)
	            if nhost is not None:
	                response += self.whois(query, nhost, 0, quiet=True)

```  
Lines 183:189

```diff
	            response = response.decode('utf-8', 'replace')
	            if 'with "=xxx"' in response:
	                return self.whois(query, hostname, flags, True)
-	            if flags & NICClient.WHOIS_RECURSE and nhost is None:
+	            if flags & NICClient.WHOIS_RECURSE and nhost is (True):
	                nhost = self.findwhois_server(response, hostname, query)
	            if nhost is not None:
	                response += self.whois(query, nhost, 0, quiet=True)

```  
Lines 185:191

```diff
	                return self.whois(query, hostname, flags, True)
	            if flags & NICClient.WHOIS_RECURSE and nhost is None:
	                nhost = self.findwhois_server(response, hostname, query)
-	            if nhost is not None:
+	            if False:
	                response += self.whois(query, nhost, 0, quiet=True)
	        except socket.error as exc: # 'response' is assigned a value (also a str) even on socket timeout
	            if not quiet:

```  
Lines 186:192

```diff
	            if flags & NICClient.WHOIS_RECURSE and nhost is None:
	                nhost = self.findwhois_server(response, hostname, query)
	            if nhost is not None:
-	                response += self.whois(query, nhost, 0, quiet=True)
+	                response += self.whois(query, nhost, 0, quiet=(False))
	        except socket.error as exc: # 'response' is assigned a value (also a str) even on socket timeout
	            if not quiet:
	                print("Error trying to connect to socket: closing socket - {}".format(exc))

```  
Lines 186:192

```diff
	            if flags & NICClient.WHOIS_RECURSE and nhost is None:
	                nhost = self.findwhois_server(response, hostname, query)
	            if nhost is not None:
-	                response += self.whois(query, nhost, 0, quiet=True)
+	                response += self.whois(query, nhost, 0, quiet=None)
	        except socket.error as exc: # 'response' is assigned a value (also a str) even on socket timeout
	            if not quiet:
	                print("Error trying to connect to socket: closing socket - {}".format(exc))

```  
Lines 188:194

```diff
	            if nhost is not None:
	                response += self.whois(query, nhost, 0, quiet=True)
	        except socket.error as exc: # 'response' is assigned a value (also a str) even on socket timeout
-	            if not quiet:
+	            if False:
	                print("Error trying to connect to socket: closing socket - {}".format(exc))
	            s.close()
	            response = "Socket not responding: {}".format(exc)

```  
Lines 188:194

```diff
	            if nhost is not None:
	                response += self.whois(query, nhost, 0, quiet=True)
	        except socket.error as exc: # 'response' is assigned a value (also a str) even on socket timeout
-	            if not quiet:
+	            if True:
	                print("Error trying to connect to socket: closing socket - {}".format(exc))
	            s.close()
	            response = "Socket not responding: {}".format(exc)

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
Lines 213:219

```diff
	        if len(domain) < 2:
	            return None
	        tld = domain[-1]
-	        if tld[0].isdigit():
+	        if tld[<_ast.Constant object at 0x7f5875cb41f0>].isdigit():
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
+	        if tld[<_ast.UnaryOp object at 0x7f5875cc8c10>].isdigit():
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
+	        if False:
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
+	        elif (tld <= 'ai'):
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
+	        elif (tld >= 'page'):
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
+	        elif (tld > 'page'):
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
Lines 227:233

```diff
	            return NICClient.PAGE_HOST
	        elif tld == 'money':
	            return NICClient.MONEY_HOST
-	        elif tld == 'online':
+	        elif (tld >= 'online'):
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
+	        elif (tld > 'online'):
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
+	        elif (tld <= 'cl'):
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
+	        elif (tld <= 'ar'):
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
+	        elif (tld < 'ar'):
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
+	        elif (tld <= 'by'):
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
+	        elif (tld >= 'pe'):
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
+	        elif (tld > 'pe'):
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
+	        elif False:
	            return NICClient.PE_HOST
	        elif tld == 'ist':
	            return NICClient.IST_HOST

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
+	        elif (tld <= 'chat'):
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
+	        elif (tld >= 'website'):
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
+	        elif (tld > 'website'):
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
+	        elif (tld >= 'ooo'):
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
+	        elif (tld > 'ooo'):
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
+	        elif (tld >= 'nl'):
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
+	        elif (tld > 'nl'):
	            return NICClient.NL_HOST    
	        else:
	            return tld + NICClient.QNICHOST_TAIL

```  
Lines 280:286

```diff
	        or other server to get region-specific whois server, then if quick
	        flag is false, perform a second lookup on the region-specific
	        server for contact records"""
-	        nichost = None
+	        nichost = (False)
	        # whoud happen when this function is called by other than main
	        if options is None:
	            options = {}

```  
Lines 280:286

```diff
	        or other server to get region-specific whois server, then if quick
	        flag is false, perform a second lookup on the region-specific
	        server for contact records"""
-	        nichost = None
+	        nichost = (True)
	        # whoud happen when this function is called by other than main
	        if options is None:
	            options = {}

```  
Lines 282:288

```diff
	        server for contact records"""
	        nichost = None
	        # whoud happen when this function is called by other than main
-	        if options is None:
+	        if True:
	            options = {}
	
	        if ('whoishost' not in options or options['whoishost'] is None) \

```  
Lines 285:292

```diff
	        if options is None:
	            options = {}
	
-	        if ('whoishost' not in options or options['whoishost'] is None) \
-	                and ('country' not in options or options['country'] is None):
+	        if (('whoishost' not in options or options['whoishost'] is None) or ('country'
     not in options or options['country'] is None)):
	            self.use_qnichost = True
	            options['whoishost'] = NICClient.NICHOST
	            if not (flags & NICClient.WHOIS_QUICK):

```  
Lines 285:292

```diff
	        if options is None:
	            options = {}
	
-	        if ('whoishost' not in options or options['whoishost'] is None) \
-	                and ('country' not in options or options['country'] is None):
+	        if True:
	            self.use_qnichost = True
	            options['whoishost'] = NICClient.NICHOST
	            if not (flags & NICClient.WHOIS_QUICK):

```  
Lines 285:291

```diff
	        if options is None:
	            options = {}
	
-	        if ('whoishost' not in options or options['whoishost'] is None) \
+	        if ('whoishost' not in options or options['whoishost'] is (False)) \
	                and ('country' not in options or options['country'] is None):
	            self.use_qnichost = True
	            options['whoishost'] = NICClient.NICHOST

```  
Lines 285:291

```diff
	        if options is None:
	            options = {}
	
-	        if ('whoishost' not in options or options['whoishost'] is None) \
+	        if ('whoishost' not in options or options['whoishost'] is (True)) \
	                and ('country' not in options or options['country'] is None):
	            self.use_qnichost = True
	            options['whoishost'] = NICClient.NICHOST

```  
Lines 285:291

```diff
	        if options is None:
	            options = {}
	
-	        if ('whoishost' not in options or options['whoishost'] is None) \
+	        if ('whoishost' not in options or (options['whoishost'] is not None)) \
	                and ('country' not in options or options['country'] is None):
	            self.use_qnichost = True
	            options['whoishost'] = NICClient.NICHOST

```  
Lines 286:292

```diff
	            options = {}
	
	        if ('whoishost' not in options or options['whoishost'] is None) \
-	                and ('country' not in options or options['country'] is None):
+	                and ('country' not in options or (options['country'] is not None)):
	            self.use_qnichost = True
	            options['whoishost'] = NICClient.NICHOST
	            if not (flags & NICClient.WHOIS_QUICK):

```  
Lines 286:292

```diff
	            options = {}
	
	        if ('whoishost' not in options or options['whoishost'] is None) \
-	                and ('country' not in options or options['country'] is None):
+	                and ('country' not in options or options['country'] is (False)):
	            self.use_qnichost = True
	            options['whoishost'] = NICClient.NICHOST
	            if not (flags & NICClient.WHOIS_QUICK):

```  
Lines 286:292

```diff
	            options = {}
	
	        if ('whoishost' not in options or options['whoishost'] is None) \
-	                and ('country' not in options or options['country'] is None):
+	                and ('country' not in options or options['country'] is (True)):
	            self.use_qnichost = True
	            options['whoishost'] = NICClient.NICHOST
	            if not (flags & NICClient.WHOIS_QUICK):

```  
Lines 289:295

```diff
	                and ('country' not in options or options['country'] is None):
	            self.use_qnichost = True
	            options['whoishost'] = NICClient.NICHOST
-	            if not (flags & NICClient.WHOIS_QUICK):
+	            if False:
	                flags |= NICClient.WHOIS_RECURSE
	
	        if 'country' in options and options['country'] is not None:

```  
Lines 289:295

```diff
	                and ('country' not in options or options['country'] is None):
	            self.use_qnichost = True
	            options['whoishost'] = NICClient.NICHOST
-	            if not (flags & NICClient.WHOIS_QUICK):
+	            if True:
	                flags |= NICClient.WHOIS_RECURSE
	
	        if 'country' in options and options['country'] is not None:

```  
Lines 289:295

```diff
	                and ('country' not in options or options['country'] is None):
	            self.use_qnichost = True
	            options['whoishost'] = NICClient.NICHOST
-	            if not (flags & NICClient.WHOIS_QUICK):
+	            if not ((flags | NICClient.WHOIS_QUICK)):
	                flags |= NICClient.WHOIS_RECURSE
	
	        if 'country' in options and options['country'] is not None:

```  
Lines 289:295

```diff
	                and ('country' not in options or options['country'] is None):
	            self.use_qnichost = True
	            options['whoishost'] = NICClient.NICHOST
-	            if not (flags & NICClient.WHOIS_QUICK):
+	            if not ((flags ^ NICClient.WHOIS_QUICK)):
	                flags |= NICClient.WHOIS_RECURSE
	
	        if 'country' in options and options['country'] is not None:

```  
Lines 292:298

```diff
	            if not (flags & NICClient.WHOIS_QUICK):
	                flags |= NICClient.WHOIS_RECURSE
	
-	        if 'country' in options and options['country'] is not None:
+	        if 'country' in options and (options['country'] is None):
	            result = self.whois(
	                query_arg,
	                options['country'] + NICClient.QNICHOST_TAIL,

```  
Lines 292:298

```diff
	            if not (flags & NICClient.WHOIS_QUICK):
	                flags |= NICClient.WHOIS_RECURSE
	
-	        if 'country' in options and options['country'] is not None:
+	        if 'country' in options and options['country'] is not (False):
	            result = self.whois(
	                query_arg,
	                options['country'] + NICClient.QNICHOST_TAIL,

```  
Lines 292:298

```diff
	            if not (flags & NICClient.WHOIS_QUICK):
	                flags |= NICClient.WHOIS_RECURSE
	
-	        if 'country' in options and options['country'] is not None:
+	        if 'country' in options and options['country'] is not (True):
	            result = self.whois(
	                query_arg,
	                options['country'] + NICClient.QNICHOST_TAIL,

```  
Lines 292:298

```diff
	            if not (flags & NICClient.WHOIS_QUICK):
	                flags |= NICClient.WHOIS_RECURSE
	
-	        if 'country' in options and options['country'] is not None:
+	        if False:
	            result = self.whois(
	                query_arg,
	                options['country'] + NICClient.QNICHOST_TAIL,

```  
Lines 298:304

```diff
	                options['country'] + NICClient.QNICHOST_TAIL,
	                flags
	            )
-	        elif self.use_qnichost:
+	        elif True:
	            nichost = self.choose_server(query_arg)
	            if nichost is not None:
	                result = self.whois(query_arg, nichost, flags)

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
### test_simple_ascii_domain_str_emp_0
  
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
Lines 287:293

```diff
	
	        if ('whoishost' not in options or options['whoishost'] is None) \
	                and ('country' not in options or options['country'] is None):
-	            self.use_qnichost = True
+	            self.use_qnichost = (False)
	            options['whoishost'] = NICClient.NICHOST
	            if not (flags & NICClient.WHOIS_QUICK):
	                flags |= NICClient.WHOIS_RECURSE

```  
Lines 287:293

```diff
	
	        if ('whoishost' not in options or options['whoishost'] is None) \
	                and ('country' not in options or options['country'] is None):
-	            self.use_qnichost = True
+	            self.use_qnichost = None
	            options['whoishost'] = NICClient.NICHOST
	            if not (flags & NICClient.WHOIS_QUICK):
	                flags |= NICClient.WHOIS_RECURSE

```  
Lines 298:304

```diff
	                options['country'] + NICClient.QNICHOST_TAIL,
	                flags
	            )
-	        elif self.use_qnichost:
+	        elif False:
	            nichost = self.choose_server(query_arg)
	            if nichost is not None:
	                result = self.whois(query_arg, nichost, flags)

```
### test_simple_unicode_domain_str_dbl_0
  
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
### test_simple_unicode_domain_call_add_0_call_add_0
  
Lines 166:172

```diff
	                query_bytes = "-T dn,ace -C UTF-8 " + query
	            elif hostname == NICClient.DK_HOST:
	                query_bytes = " --show-handles " + query
-	            elif hostname.endswith(NICClient.QNICHOST_TAIL) and many_results:
+	            elif True:
	                query_bytes = '=' + query
	            else:
	                query_bytes = query

```
### test_unicode_domain_and_tld_str_dbl_0_call_add_0_numb_sub_0
  
Lines 116:122

```diff
	            # s.connect((hostname, 43)) does not work
	            if nhost.count('/') > 0:
	                nhost = None
-	        elif hostname == NICClient.ANICHOST:
+	        elif (hostname < NICClient.ANICHOST):
	            for nichost in NICClient.ip_whois:
	                if buf.find(nichost) != -1:
	                    nhost = nichost

```
### test_unicode_domain_and_tld_str_dbl_0_str_dbl_0_str_dbl_0
  
Lines 183:189

```diff
	            response = response.decode('utf-8', 'replace')
	            if 'with "=xxx"' in response:
	                return self.whois(query, hostname, flags, True)
-	            if flags & NICClient.WHOIS_RECURSE and nhost is None:
+	            if (flags ^ NICClient.WHOIS_RECURSE) and nhost is None:
	                nhost = self.findwhois_server(response, hostname, query)
	            if nhost is not None:
	                response += self.whois(query, nhost, 0, quiet=True)

```
### test_simple_ascii_domain_str_hlf_0
  
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
Lines 300:306

```diff
	            )
	        elif self.use_qnichost:
	            nichost = self.choose_server(query_arg)
-	            if nichost is not None:
+	            if True:
	                result = self.whois(query_arg, nichost, flags)
	            else:
	                result = ''

```  
Lines 300:306

```diff
	            )
	        elif self.use_qnichost:
	            nichost = self.choose_server(query_arg)
-	            if nichost is not None:
+	            if nichost is not (False):
	                result = self.whois(query_arg, nichost, flags)
	            else:
	                result = ''

```  
Lines 300:306

```diff
	            )
	        elif self.use_qnichost:
	            nichost = self.choose_server(query_arg)
-	            if nichost is not None:
+	            if nichost is not (True):
	                result = self.whois(query_arg, nichost, flags)
	            else:
	                result = ''

```
### test_simple_unicode_domain_call_dup_0
  
Lines 162:168

```diff
	            except AttributeError:
	                pass  # Already Unicode (python3's error)
	
-	            if hostname == NICClient.DENICHOST:
+	            if (hostname > NICClient.DENICHOST):
	                query_bytes = "-T dn,ace -C UTF-8 " + query
	            elif hostname == NICClient.DK_HOST:
	                query_bytes = " --show-handles " + query

```
## Alive Mutants

# /home/ubuntu/projects/whois/whois/parser.py

## Newly Killed Mutants

### test_simple_ascii_domain_str_dbl_0_str_hlf_0
  
Lines 198:204

```diff
	        """Given whois output in ``text``, return an instance of ``WhoisEntry``
	        that represents its parsed contents.
	        """
-	        if text.strip() == 'No whois server is known for this kind of object.':
+	        if (text.strip() >= 'No whois server is known for this kind of object.'):
	            raise PywhoisError(text)
	
	        if domain.endswith('.com'):

```  
Lines 198:204

```diff
	        """Given whois output in ``text``, return an instance of ``WhoisEntry``
	        that represents its parsed contents.
	        """
-	        if text.strip() == 'No whois server is known for this kind of object.':
+	        if (text.strip() > 'No whois server is known for this kind of object.'):
	            raise PywhoisError(text)
	
	        if domain.endswith('.com'):

```  
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
### test_simple_ascii_domain_str_hlf_0
  
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
Lines 139:145

```diff
	        else:
	            self.domain = domain
	            self.text = text
-	            if regex is not None:
+	            if False:
	                self._regex = regex
	            self.parse()
	

```  
Lines 150:156

```diff
	        for attr, regex in list(self._regex.items()):
	            if regex:
	                values = []
-	                for data in re.findall(regex, self.text, re.IGNORECASE | re.M):
+	                for data in re.findall(regex, self.text, (re.IGNORECASE & re.M)):
	
	                    matches = data if isinstance(data, tuple) else [data]
	                    for value in matches:

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
Lines 155:161

```diff
	                    matches = data if isinstance(data, tuple) else [data]
	                    for value in matches:
	                        value = self._preprocess(attr, value)
-	                        if value and value not in values:
+	                        if True:
	                            # avoid duplicates
	                            values.append(value)
	                if values and attr in ('registrar', 'whois_server', 'referral_url'):

```  
Lines 155:161

```diff
	                    matches = data if isinstance(data, tuple) else [data]
	                    for value in matches:
	                        value = self._preprocess(attr, value)
-	                        if value and value not in values:
+	                        if (value or value not in values):
	                            # avoid duplicates
	                            values.append(value)
	                if values and attr in ('registrar', 'whois_server', 'referral_url'):

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
Lines 160:166

```diff
	                            values.append(value)
	                if values and attr in ('registrar', 'whois_server', 'referral_url'):
	                    values = values[-1]  # ignore junk
-	                if len(values) == 1:
+	                if False:
	                    values = values[0]
	                elif not values:
	                    values = None

```  
Lines 161:167

```diff
	                if values and attr in ('registrar', 'whois_server', 'referral_url'):
	                    values = values[-1]  # ignore junk
	                if len(values) == 1:
-	                    values = values[0]
+	                    values = values[<_ast.UnaryOp object at 0x7f5875b451f0>]
	                elif not values:
	                    values = None
	

```  
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
Lines 169:175

```diff
	
	    def _preprocess(self, attr, value):
	        value = value.strip()
-	        if value and isinstance(value, basestring) and not value.isdigit() and '_date' in attr:
+	        if (value or isinstance(value, basestring) or not value.isdigit() or '_date' in
    attr):
	            # try casting to date format
	            value = cast_date(
	                value,

```  
Lines 169:175

```diff
	
	    def _preprocess(self, attr, value):
	        value = value.strip()
-	        if value and isinstance(value, basestring) and not value.isdigit() and '_date' in attr:
+	        if False:
	            # try casting to date format
	            value = cast_date(
	                value,

```  
Lines 169:175

```diff
	
	    def _preprocess(self, attr, value):
	        value = value.strip()
-	        if value and isinstance(value, basestring) and not value.isdigit() and '_date' in attr:
+	        if True:
	            # try casting to date format
	            value = cast_date(
	                value,

```  
Lines 169:175

```diff
	
	    def _preprocess(self, attr, value):
	        value = value.strip()
-	        if value and isinstance(value, basestring) and not value.isdigit() and '_date' in attr:
+	        if value and isinstance(value, basestring) and not value.isdigit() and ('_date' not in attr):
	            # try casting to date format
	            value = cast_date(
	                value,

```  
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
Lines 201:207

```diff
	        if text.strip() == 'No whois server is known for this kind of object.':
	            raise PywhoisError(text)
	
-	        if domain.endswith('.com'):
+	        if True:
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
Lines 203:209

```diff
	
	        if domain.endswith('.com'):
	            return WhoisCom(domain, text)
-	        elif domain.endswith('.net'):
+	        elif True:
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
Lines 205:211

```diff
	            return WhoisCom(domain, text)
	        elif domain.endswith('.net'):
	            return WhoisNet(domain, text)
-	        elif domain.endswith('.org'):
+	        elif True:
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
Lines 207:213

```diff
	            return WhoisNet(domain, text)
	        elif domain.endswith('.org'):
	            return WhoisOrg(domain, text)
-	        elif domain.endswith('.name'):
+	        elif True:
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
Lines 209:215

```diff
	            return WhoisOrg(domain, text)
	        elif domain.endswith('.name'):
	            return WhoisName(domain, text)
-	        elif domain.endswith('.me'):
+	        elif True:
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
Lines 211:217

```diff
	            return WhoisName(domain, text)
	        elif domain.endswith('.me'):
	            return WhoisMe(domain, text)
-	        elif domain.endswith('ae'):
+	        elif True:
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
Lines 213:219

```diff
	            return WhoisMe(domain, text)
	        elif domain.endswith('ae'):
	            return WhoisAe(domain, text)
-	        elif domain.endswith('.au'):
+	        elif True:
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
Lines 215:221

```diff
	            return WhoisAe(domain, text)
	        elif domain.endswith('.au'):
	            return WhoisAU(domain, text)
-	        elif domain.endswith('.ru'):
+	        elif True:
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
Lines 217:223

```diff
	            return WhoisAU(domain, text)
	        elif domain.endswith('.ru'):
	            return WhoisRu(domain, text)
-	        elif domain.endswith('.us'):
+	        elif True:
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
Lines 219:225

```diff
	            return WhoisRu(domain, text)
	        elif domain.endswith('.us'):
	            return WhoisUs(domain, text)
-	        elif domain.endswith('.uk'):
+	        elif True:
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
Lines 221:227

```diff
	            return WhoisUs(domain, text)
	        elif domain.endswith('.uk'):
	            return WhoisUk(domain, text)
-	        elif domain.endswith('.fr'):
+	        elif True:
	            return WhoisFr(domain, text)
	        elif domain.endswith('.nl'):
	            return WhoisNl(domain, text)

```  
Lines 223:229

```diff
	            return WhoisUk(domain, text)
	        elif domain.endswith('.fr'):
	            return WhoisFr(domain, text)
-	        elif domain.endswith('.nl'):
+	        elif False:
	            return WhoisNl(domain, text)
	        elif domain.endswith('.fi'):
	            return WhoisFi(domain, text)

```  
Lines 223:229

```diff
	            return WhoisUk(domain, text)
	        elif domain.endswith('.fr'):
	            return WhoisFr(domain, text)
-	        elif domain.endswith('.nl'):
+	        elif True:
	            return WhoisNl(domain, text)
	        elif domain.endswith('.fi'):
	            return WhoisFi(domain, text)

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
Lines 225:231

```diff
	            return WhoisFr(domain, text)
	        elif domain.endswith('.nl'):
	            return WhoisNl(domain, text)
-	        elif domain.endswith('.fi'):
+	        elif True:
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
Lines 227:233

```diff
	            return WhoisNl(domain, text)
	        elif domain.endswith('.fi'):
	            return WhoisFi(domain, text)
-	        elif domain.endswith('.hr'):
+	        elif True:
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
Lines 229:235

```diff
	            return WhoisFi(domain, text)
	        elif domain.endswith('.hr'):
	            return WhoisHr(domain, text)
-	        elif domain.endswith('.hn'):
+	        elif True:
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
Lines 231:237

```diff
	            return WhoisHr(domain, text)
	        elif domain.endswith('.hn'):
	            return WhoisHn(domain, text)
-	        elif domain.endswith('.hk'):
+	        elif True:
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
Lines 233:239

```diff
	            return WhoisHn(domain, text)
	        elif domain.endswith('.hk'):
	            return WhoisHk(domain, text)
-	        elif domain.endswith('.jp'):
+	        elif True:
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
Lines 235:241

```diff
	            return WhoisHk(domain, text)
	        elif domain.endswith('.jp'):
	            return WhoisJp(domain, text)
-	        elif domain.endswith('.pl'):
+	        elif True:
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
Lines 237:243

```diff
	            return WhoisJp(domain, text)
	        elif domain.endswith('.pl'):
	            return WhoisPl(domain, text)
-	        elif domain.endswith('.br'):
+	        elif True:
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
Lines 239:245

```diff
	            return WhoisPl(domain, text)
	        elif domain.endswith('.br'):
	            return WhoisBr(domain, text)
-	        elif domain.endswith('.eu'):
+	        elif True:
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
Lines 241:247

```diff
	            return WhoisBr(domain, text)
	        elif domain.endswith('.eu'):
	            return WhoisEu(domain, text)
-	        elif domain.endswith('.ee'):
+	        elif True:
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
Lines 243:249

```diff
	            return WhoisEu(domain, text)
	        elif domain.endswith('.ee'):
	            return WhoisEe(domain, text)
-	        elif domain.endswith('.kr'):
+	        elif True:
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
Lines 245:251

```diff
	            return WhoisEe(domain, text)
	        elif domain.endswith('.kr'):
	            return WhoisKr(domain, text)
-	        elif domain.endswith('.pt'):
+	        elif True:
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
Lines 247:253

```diff
	            return WhoisKr(domain, text)
	        elif domain.endswith('.pt'):
	            return WhoisPt(domain, text)
-	        elif domain.endswith('.bg'):
+	        elif True:
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
Lines 249:255

```diff
	            return WhoisPt(domain, text)
	        elif domain.endswith('.bg'):
	            return WhoisBg(domain, text)
-	        elif domain.endswith('.de'):
+	        elif True:
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
Lines 251:257

```diff
	            return WhoisBg(domain, text)
	        elif domain.endswith('.de'):
	            return WhoisDe(domain, text)
-	        elif domain.endswith('.at'):
+	        elif True:
	            return WhoisAt(domain, text)
	        elif domain.endswith('.ca'):
	            return WhoisCa(domain, text)

```  
Lines 253:259

```diff
	            return WhoisDe(domain, text)
	        elif domain.endswith('.at'):
	            return WhoisAt(domain, text)
-	        elif domain.endswith('.ca'):
+	        elif False:
	            return WhoisCa(domain, text)
	        elif domain.endswith('.be'):
	            return WhoisBe(domain, text)

```  
Lines 253:259

```diff
	            return WhoisDe(domain, text)
	        elif domain.endswith('.at'):
	            return WhoisAt(domain, text)
-	        elif domain.endswith('.ca'):
+	        elif True:
	            return WhoisCa(domain, text)
	        elif domain.endswith('.be'):
	            return WhoisBe(domain, text)

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
Lines 255:261

```diff
	            return WhoisAt(domain, text)
	        elif domain.endswith('.ca'):
	            return WhoisCa(domain, text)
-	        elif domain.endswith('.be'):
+	        elif True:
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
Lines 257:263

```diff
	            return WhoisCa(domain, text)
	        elif domain.endswith('.be'):
	            return WhoisBe(domain, text)
-	        elif domain.endswith('.рф'):
+	        elif True:
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
Lines 259:265

```diff
	            return WhoisBe(domain, text)
	        elif domain.endswith('.рф'):
	            return WhoisRf(domain, text)
-	        elif domain.endswith('.info'):
+	        elif True:
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
Lines 261:267

```diff
	            return WhoisRf(domain, text)
	        elif domain.endswith('.info'):
	            return WhoisInfo(domain, text)
-	        elif domain.endswith('.su'):
+	        elif True:
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
Lines 263:269

```diff
	            return WhoisInfo(domain, text)
	        elif domain.endswith('.su'):
	            return WhoisSu(domain, text)
-	        elif domain.endswith('si'):
+	        elif True:
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
Lines 265:271

```diff
	            return WhoisSu(domain, text)
	        elif domain.endswith('si'):
	            return WhoisSi(domain, text)
-	        elif domain.endswith('.kg'):
+	        elif True:
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
Lines 267:273

```diff
	            return WhoisSi(domain, text)
	        elif domain.endswith('.kg'):
	            return WhoisKg(domain, text)
-	        elif domain.endswith('.io'):
+	        elif True:
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
Lines 269:275

```diff
	            return WhoisKg(domain, text)
	        elif domain.endswith('.io'):
	            return WhoisIo(domain, text)
-	        elif domain.endswith('.biz'):
+	        elif True:
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
Lines 271:277

```diff
	            return WhoisIo(domain, text)
	        elif domain.endswith('.biz'):
	            return WhoisBiz(domain, text)
-	        elif domain.endswith('.mobi'):
+	        elif True:
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
Lines 273:279

```diff
	            return WhoisBiz(domain, text)
	        elif domain.endswith('.mobi'):
	            return WhoisMobi(domain, text)
-	        elif domain.endswith('.ch'):
+	        elif True:
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
Lines 275:281

```diff
	            return WhoisMobi(domain, text)
	        elif domain.endswith('.ch'):
	            return WhoisChLi(domain, text)
-	        elif domain.endswith('.li'):
+	        elif True:
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
Lines 277:283

```diff
	            return WhoisChLi(domain, text)
	        elif domain.endswith('.li'):
	            return WhoisChLi(domain, text)
-	        elif domain.endswith('.id'):
+	        elif True:
	            return WhoisID(domain, text)
	        elif domain.endswith('.sk'):
	            return WhoisSK(domain, text)

```  
Lines 279:285

```diff
	            return WhoisChLi(domain, text)
	        elif domain.endswith('.id'):
	            return WhoisID(domain, text)
-	        elif domain.endswith('.sk'):
+	        elif False:
	            return WhoisSK(domain, text)
	        elif domain.endswith('.se'):
	            return WhoisSe(domain, text)

```  
Lines 279:285

```diff
	            return WhoisChLi(domain, text)
	        elif domain.endswith('.id'):
	            return WhoisID(domain, text)
-	        elif domain.endswith('.sk'):
+	        elif True:
	            return WhoisSK(domain, text)
	        elif domain.endswith('.se'):
	            return WhoisSe(domain, text)

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
Lines 281:287

```diff
	            return WhoisID(domain, text)
	        elif domain.endswith('.sk'):
	            return WhoisSK(domain, text)
-	        elif domain.endswith('.se'):
+	        elif True:
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
Lines 283:289

```diff
	            return WhoisSK(domain, text)
	        elif domain.endswith('.se'):
	            return WhoisSe(domain, text)
-	        elif domain.endswith('no'):
+	        elif True:
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
Lines 285:291

```diff
	            return WhoisSe(domain, text)
	        elif domain.endswith('no'):
	            return WhoisNo(domain, text)
-	        elif domain.endswith('.nu'):
+	        elif True:
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
Lines 287:293

```diff
	            return WhoisNo(domain, text)
	        elif domain.endswith('.nu'):
	            return WhoisSe(domain, text)
-	        elif domain.endswith('.is'):
+	        elif True:
	            return WhoisIs(domain, text)
	        elif domain.endswith('.dk'):
	            return WhoisDk(domain, text)

```  
Lines 289:295

```diff
	            return WhoisSe(domain, text)
	        elif domain.endswith('.is'):
	            return WhoisIs(domain, text)
-	        elif domain.endswith('.dk'):
+	        elif False:
	            return WhoisDk(domain, text)
	        elif domain.endswith('.it'):
	            return WhoisIt(domain, text)

```  
Lines 289:295

```diff
	            return WhoisSe(domain, text)
	        elif domain.endswith('.is'):
	            return WhoisIs(domain, text)
-	        elif domain.endswith('.dk'):
+	        elif True:
	            return WhoisDk(domain, text)
	        elif domain.endswith('.it'):
	            return WhoisIt(domain, text)

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
Lines 291:297

```diff
	            return WhoisIs(domain, text)
	        elif domain.endswith('.dk'):
	            return WhoisDk(domain, text)
-	        elif domain.endswith('.it'):
+	        elif True:
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
Lines 293:299

```diff
	            return WhoisDk(domain, text)
	        elif domain.endswith('.it'):
	            return WhoisIt(domain, text)
-	        elif domain.endswith('.mx'):
+	        elif True:
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
Lines 295:301

```diff
	            return WhoisIt(domain, text)
	        elif domain.endswith('.mx'):
	            return WhoisMx(domain, text)
-	        elif domain.endswith('.ai'):
+	        elif True:
	            return WhoisAi(domain, text)
	        elif domain.endswith('.il'):
	            return WhoisIl(domain, text)

```  
Lines 297:303

```diff
	            return WhoisMx(domain, text)
	        elif domain.endswith('.ai'):
	            return WhoisAi(domain, text)
-	        elif domain.endswith('.il'):
+	        elif False:
	            return WhoisIl(domain, text)
	        elif domain.endswith('.in'):
	            return WhoisIn(domain, text)

```  
Lines 297:303

```diff
	            return WhoisMx(domain, text)
	        elif domain.endswith('.ai'):
	            return WhoisAi(domain, text)
-	        elif domain.endswith('.il'):
+	        elif True:
	            return WhoisIl(domain, text)
	        elif domain.endswith('.in'):
	            return WhoisIn(domain, text)

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
Lines 299:305

```diff
	            return WhoisAi(domain, text)
	        elif domain.endswith('.il'):
	            return WhoisIl(domain, text)
-	        elif domain.endswith('.in'):
+	        elif True:
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
Lines 301:307

```diff
	            return WhoisIl(domain, text)
	        elif domain.endswith('.in'):
	            return WhoisIn(domain, text)
-	        elif domain.endswith('.cat'):
+	        elif True:
	            return WhoisCat(domain, text)
	        elif domain.endswith('.ie'):
	            return WhoisIe(domain, text)

```  
Lines 303:309

```diff
	            return WhoisIn(domain, text)
	        elif domain.endswith('.cat'):
	            return WhoisCat(domain, text)
-	        elif domain.endswith('.ie'):
+	        elif False:
	            return WhoisIe(domain, text)
	        elif domain.endswith('.nz'):
	            return WhoisNz(domain, text)

```  
Lines 303:309

```diff
	            return WhoisIn(domain, text)
	        elif domain.endswith('.cat'):
	            return WhoisCat(domain, text)
-	        elif domain.endswith('.ie'):
+	        elif True:
	            return WhoisIe(domain, text)
	        elif domain.endswith('.nz'):
	            return WhoisNz(domain, text)

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
Lines 305:311

```diff
	            return WhoisCat(domain, text)
	        elif domain.endswith('.ie'):
	            return WhoisIe(domain, text)
-	        elif domain.endswith('.nz'):
+	        elif True:
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
Lines 307:313

```diff
	            return WhoisIe(domain, text)
	        elif domain.endswith('.nz'):
	            return WhoisNz(domain, text)
-	        elif domain.endswith('.space'):
+	        elif True:
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
Lines 309:315

```diff
	            return WhoisNz(domain, text)
	        elif domain.endswith('.space'):
	            return WhoisSpace(domain, text)
-	        elif domain.endswith('.lu'):
+	        elif True:
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
Lines 311:317

```diff
	            return WhoisSpace(domain, text)
	        elif domain.endswith('.lu'):
	            return WhoisLu(domain, text)
-	        elif domain.endswith('.cz'):
+	        elif True:
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
Lines 313:319

```diff
	            return WhoisLu(domain, text)
	        elif domain.endswith('.cz'):
	            return WhoisCz(domain, text)
-	        elif domain.endswith('.online'):
+	        elif True:
	            return WhoisOnline(domain, text)
	        elif domain.endswith('.cn'):
	            return WhoisCn(domain, text)

```  
Lines 315:321

```diff
	            return WhoisCz(domain, text)
	        elif domain.endswith('.online'):
	            return WhoisOnline(domain, text)
-	        elif domain.endswith('.cn'):
+	        elif False:
	            return WhoisCn(domain, text)
	        elif domain.endswith('.app'):
	            return WhoisApp(domain, text)

```  
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
+	        elif False:
	            return WhoisAr(domain, text)
	        elif domain.endswith('.by'):
	            return WhoisBy(domain, text)

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
+	        elif False:
	            return WhoisBy(domain, text)
	        elif domain.endswith('.cr'):
	            return WhoisCr(domain, text)

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
+	        elif False:
	            return WhoisCr(domain, text)
	        elif domain.endswith('.do'):
	            return WhoisDo(domain, text)

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
+	        elif False:
	            return WhoisJobs(domain, text)
	        elif domain.endswith('.lat'):
	            return WhoisLat(domain, text)

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
+	        elif False:
	            return WhoisLat(domain, text)
	        elif domain.endswith('.pe'):
	            return WhoisPe(domain, text)

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
+	        elif False:
	            return WhoisRo(domain, text)
	        elif domain.endswith('.sa'):
	            return WhoisSa(domain, text)

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
+	        elif False:
	            return WhoisSa(domain, text)
	        elif domain.endswith('.tw'):
	            return WhoisTw(domain, text)

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
+	        elif False:
	            return WhoisTw(domain, text)
	        elif domain.endswith('.tr'):
	            return WhoisTr(domain, text)

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
+	        elif False:
	            return WhoisTr(domain, text)
	        elif domain.endswith('.ve'):
	            return WhoisVe(domain, text)

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
+	        elif False:
	            return WhoisVe(domain, text)
	        elif domain.endswith('.ua'):
	            return WhoisUA(domain, text)

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
+	        elif False:
	            return WhoisUA(domain, text)
	        elif domain.endswith('.kz'):
	            return WhoisKZ(domain, text)

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
+	        elif False:
	            return WhoisKZ(domain, text)
	        elif domain.endswith('.ir'):
	            return WhoisIR(domain, text)

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
+	        elif False:
	            return WhoisIR(domain, text)
	        elif domain.endswith('.中国'):
	            return WhoisZhongGuo(domain, text)

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
+	        elif False:
	            return WhoisZhongGuo(domain, text)
	        elif domain.endswith('.website'):
	            return WhoisWebsite(domain, text)

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
+	        elif False:
	            return WhoisML(domain, text)
	        elif domain.endswith('.ooo'):
	            return WhoisOOO(domain, text)

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
+	        elif False:
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
+	        elif True:
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
Lines 468:474

```diff
	    """
	
	    def __init__(self, domain, text):
-	        if 'No match for "' in text:
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
Lines 537:543

```diff
	    }
	
	    def __init__(self, domain, text):
-	        if 'No entries found' in text:
+	        if False:
	            raise PywhoisError(text)
	        else:
	            WhoisEntry.__init__(self, domain, text, self.regex)

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
## Alive Mutants

# /home/ubuntu/projects/whois/whois/time_zones.py

## Newly Killed Mutants

### test_simple_ascii_domain_str_hlf_0
  
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
Lines 48:52

```diff
	
	for tz_descr in (tz_spec.split() for tz_spec in _tz_string.split('\n')):
	    tz_offset = int(float(tz_descr[0]) * 3600)
-	    for tz_code in tz_descr[1:]:
+	    for tz_code in tz_descr[:1]:
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
## Alive Mutants

# /home/ubuntu/projects/whois/whois/__init__.py

## Newly Killed Mutants

### test_simple_ascii_domain_str_hlf_0
  
Lines 28:34

```diff
	IPV4_OR_V6 = re.compile(r"((^\s*((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))\s*$)|(^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$))")
	
	
-	def whois(url, command=False, flags=0, executable="whois"):
+	def whois(url, command=None, flags=0, executable="whois"):
	    # clean domain to expose netloc
	    ip_match = IPV4_OR_V6.match(url)
	    if ip_match:

```  
Lines 41:47

```diff
	            domain = extract_domain(result[0])
	    else:
	        domain = extract_domain(url)
-	    if command:
+	    if False:
	        # try native whois command
	        r = subprocess.Popen([executable, domain], stdout=subprocess.PIPE)
	        text = r.stdout.read().decode()

```  
Lines 52:58

```diff
	    return WhoisEntry.load(domain, text)
	
	
-	suffixes = None
+	suffixes = (False)
	def extract_domain(url):
	    """Extract the domain from the given URL
	

```  
Lines 79:85

```diff
	    >>> logger.info(extract_domain('172.217.3.110'))
	    1e100.net
	    """
-	    if IPV4_OR_V6.match(url):
+	    if False:
	        # this is an IP address
	        return socket.gethostbyaddr(url)[0]
	

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
Lines 94:100

```diff
	    if not isinstance(url, str):
	        url = url.decode('utf-8')
	    url = re.sub('^.*://', '', url)
-	    url = url.split('/')[0].lower()
+	    url = url.split('/')[<_ast.UnaryOp object at 0x7f58751abf40>].lower()
	
	    # find the longest suffix match
	    domain = b''

```  
Lines 104:110

```diff
	            domain = b'.' + domain
	        domain = section.encode('utf-8') + domain
	        if domain not in suffixes:
-	            if not b'.' in domain and len(split_url) >= 2:
+	            if not (b'.' not in domain) and len(split_url) >= 2:
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
+	            if False:
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
+	            if not b'.' in domain and (len(split_url) == 2):
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
+	            if not b'.' in domain and (len(split_url) <= 2):
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
+	            if not b'.' in domain and (len(split_url) < 2):
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
Lines 108:114

```diff
	                # If this is the first section and there wasn't a match, try to
	                # match the first two sections - if that works, keep going
	                # See https://github.com/richardpenman/whois/issues/50
-	                second_order_tld = '.'.join([split_url[-2], split_url[-1]])
+	                second_order_tld = '.'.join([split_url[-2], split_url[(-1)]])
	                if not second_order_tld.encode('utf-8') in suffixes:
	                    break
	            else:

```  
Lines 108:114

```diff
	                # If this is the first section and there wasn't a match, try to
	                # match the first two sections - if that works, keep going
	                # See https://github.com/richardpenman/whois/issues/50
-	                second_order_tld = '.'.join([split_url[-2], split_url[-1]])
+	                second_order_tld = '.'.join([split_url[-2], split_url[(-1)]])
	                if not second_order_tld.encode('utf-8') in suffixes:
	                    break
	            else:

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
Lines 109:115

```diff
	                # match the first two sections - if that works, keep going
	                # See https://github.com/richardpenman/whois/issues/50
	                second_order_tld = '.'.join([split_url[-2], split_url[-1]])
-	                if not second_order_tld.encode('utf-8') in suffixes:
+	                if not (second_order_tld.encode('utf-8') not in suffixes):
	                    break
	            else:
	                break

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
Lines 109:115

```diff
	                # match the first two sections - if that works, keep going
	                # See https://github.com/richardpenman/whois/issues/50
	                second_order_tld = '.'.join([split_url[-2], split_url[-1]])
-	                if not second_order_tld.encode('utf-8') in suffixes:
+	                if True:
	                    break
	            else:
	                break

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
### test_simple_ascii_domain_str_dbl_0
  
Lines 31:37

```diff
	def whois(url, command=False, flags=0, executable="whois"):
	    # clean domain to expose netloc
	    ip_match = IPV4_OR_V6.match(url)
-	    if ip_match:
+	    if True:
	        domain = url
	        try:
	            result = socket.gethostbyaddr(url)

```  
Lines 116:122

```diff
	    return domain.decode('utf-8')
	
	
-	if __name__ == '__main__':
+	if True:
	    try:
	        url = sys.argv[1]
	    except IndexError:

```  
Lines 116:122

```diff
	    return domain.decode('utf-8')
	
	
-	if __name__ == '__main__':
+	if (__name__ >= '__main__'):
	    try:
	        url = sys.argv[1]
	    except IndexError:

```  
Lines 116:122

```diff
	    return domain.decode('utf-8')
	
	
-	if __name__ == '__main__':
+	if (__name__ != '__main__'):
	    try:
	        url = sys.argv[1]
	    except IndexError:

```  
Lines 116:122

```diff
	    return domain.decode('utf-8')
	
	
-	if __name__ == '__main__':
+	if (__name__ > '__main__'):
	    try:
	        url = sys.argv[1]
	    except IndexError:

```
## Alive Mutants
