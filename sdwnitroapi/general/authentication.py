import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import sys

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Auth(object):

    def __init__(self, ip):
        self.ip = ip
        self.apiUrl = 'https://' + ip + '/sdwan/nitro/v1/config/login'

    def login(self, username, password):
        r = requests.post(self.apiUrl, json={"login": {"password": password, "username": username}}, verify=False)
        if r.cookies:
            return r.cookies
        else:
            sys.exit('Login error')

    def logoff(self, cookie):
        try:
            r = requests.delete(self.apiUrl, cookies=cookie, verify=False)
            return r
        except:
            print("Logoff error")
