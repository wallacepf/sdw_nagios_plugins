#!/usr/bin/python3

from sdwnitroapi.general.authentication import Auth
from sdwnitroapi.general.monitoring import monitoring
from optparse import OptionParser
import json
import sys

parser = OptionParser()
parser.add_option('-H', dest='ip')
parser.add_option('-U', dest='username')
parser.add_option('-P', dest='password')

(options, args) = parser.parse_args()

ip = options.ip
username = options.username
password = options.password

def apiAuth():
    try:
        authcookie = Auth(ip).login(username,password)
        return authcookie
    except:
        print('CRITICAL | Login Error')
        sys.exit(2)

def getHealthStatus():
    data = monitoring(ip, apiAuth()).getService()
    health = json.loads(data)
    health = health['service']['service_state']
    if health == "enabled":
        print('OK | service_status=%s' % (health))
        sys.exit(0)
    else:
        print('CRITICAL | service_status=%s' % (health))
        sys.exit(2)

getHealthStatus()