import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

proto = 'https://'
error = 'API Call Error'

def buildApiCallDict(call, ip):
    apicalldict = {
        'license_info':'/sdwan/nitro/v1/config/license_info',
        'virtual_paths':'/sdwan/nitro/v1/monitor/virtual_paths',
        'paths':'/sdwan/nitro/v1/monitor/paths',
        'service':'/sdwan/nitro/v1/config/service',
        'wanlinkstat':'/sdwan/nitro/v1/monitor/wanlinkstat'
    }
    if call in apicalldict:
        url = proto + ip + apicalldict.get(call,'none')
        return url
    else:
        print('API Call not found')


class monitoring(object):
    def __init__(self, ip, cookie):
        self.ip = ip
        self.cookie = cookie

    def getLicense(self):
        try:
            r = requests.get(buildApiCallDict('license_info', self.ip),cookies=self.cookie,verify=False)
            return r.text
        except:
            print(error)

    def getVpath(self):
        try:
            r = requests.get(buildApiCallDict('virtual_paths', self.ip), cookies=self.cookie, verify=False)
            return r.text
        except:
            print(error)
    def getService(self):
        try:
            r = requests.get(buildApiCallDict('service', self.ip), cookies=self.cookie, verify=False)
            return r.text
        except:
            print(error)

    def getPath(self):
        try:
            r = requests.get(buildApiCallDict('paths', self.ip), cookies=self.cookie, verify=False)
            return r.text
        except:
            print(error)

    def getWanLinkStat(self):
        try:
            r = requests.get(buildApiCallDict('wanlinkstat', self.ip), cookies=self.cookie, verify=False)
            return r.text
        except:
            print(error)