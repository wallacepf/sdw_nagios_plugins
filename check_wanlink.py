#!/usr/bin/python3
from easysnmp import snmp_get
from optparse import OptionParser
import sys

parser = OptionParser()
parser.add_option('-H', dest='ip')
parser.add_option('-C', dest='community')
parser.add_option('-O', dest='object')
(options, args) = parser.parse_args()

ip = options.ip
community = options.community
object_number = options.object

linkstatus = {}

def getStatus():
    checkprev = 0
    i = 1
    while True:
        try:
            linkname = snmp_get('1.3.6.1.4.1.3845.31.4.2.2.15.2.1.3.' + str(i), hostname=ip, community=community, version=2)
            state = snmp_get('1.3.6.1.4.1.3845.31.4.2.2.15.2.1.4.' + str(i), hostname=ip, community=community, version=2)
        except:
            print('CRITICAL | Connection Error')
            sys.exit(2)
        if state.value != str(0):
            if state.value == str(1):
                state.value = 'DISABLED'
            elif state.value == str(2):
                state.value = 'DEAD'
            elif state.value == str(3):
                state.value = 'BAD'
            elif state.value == str(4):
                state.value = 'GOOD'
            linkstatus.update({linkname.value:state.value})
            if checkprev == len(linkstatus):
                break
            else:
                checkprev += 1
        else:
            break
        i += 1
    return linkstatus

def monitor():
    if not object_number:
        print(list(sorted(getStatus().items())))
    else:
        try:
            r = list(sorted(getStatus().items()))[int(object_number)-1]
            if r[1] == "GOOD":
                print('OK | name=%s, status=%s' % (r[0], r[1]))
                sys.exit(0)
            elif r[1] == "BAD":
                print('WARNING | name=%s, status=%s' % (r[0], r[1]))
                sys.exit(1)
            elif r[1] == "DEAD":
                print('CRITICAL | name=%s, status=%s' % (r[0], r[1]))
                sys.exit(2)
            else:
                print('UNKNOWN | Unknown Status')
                sys.exit(3)
        except IndexError:
            print('UNKNOWN | Número do link inexistente')
            sys.exit(3)

monitor()
