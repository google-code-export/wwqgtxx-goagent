#!/usr/bin/env python
# coding:utf-8
# by:wwqgtxx

import sys
import os
import re

try:
    import gevent
    import gevent.monkey
    import gevent.timeout
    gevent.monkey.patch_all()
except ImportError:
    if os.name == 'nt':
        sys.stderr.write('WARNING: python-gevent not installed. `https://github.com/SiteSupport/gevent/downloads`\n')
    else:
        sys.stderr.write('WARNING: python-gevent not installed. `curl -k -L http://git.io/I9B7RQ|sh`\n')
    sys.exit(-1)

import ssl
import socket

ips = []

def check_ip(ip):
    try:
        with gevent.timeout.Timeout(5):
            sock = socket.create_connection((ip, 443))
            ssl_sock = ssl.wrap_socket(sock)
            peer_cert = ssl_sock.getpeercert(True)
            if '.google.com' in peer_cert:
                print ip
                ips.append(ip)
                #print ips
    except gevent.timeout.Timeout as e:
        pass
    except Exception as e:
        pass

def getfile(filename):
    global __file__
    __file__ = os.path.abspath(__file__)
    if os.path.islink(__file__):
        __file__ = getattr(os, 'readlink', lambda x:x)(__file__)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(os.path.dirname(__file__), filename)

def ifhasfile(filename):
    if os.path.isfile(getfile(filename)):
        os.remove(getfile(filename)) 
		
def write(filename,str_ips):
    f = open(getfile(filename),'a+') 
    print str_ips
    f.write(str_ips)
    f.close()

def getln():
    if os.name == 'nt':
        return '\r\n'
    else:
        return '\n'

def writeln(filename):
    write(filename,getln())
	
def writeline(filename):
    writeln(filename)
    write(filename,'----------------------------------------------------')
    writeln(filename)

def run(filename,ip_head,ip_start,ip_end):
    for a in xrange(ip_start,(ip_end+1)):
        global ips
        str_a = '%d' % a
        greenlets = [gevent.spawn(check_ip, ip_head+str_a+'.%d' % i)for i in xrange(1, 256)]
        gevent.joinall(greenlets)
        str_ips = ''
        print getln()
        if ips!=[]:
            for item in ips:
                str_ips = str_ips+item+'|'
            write(filename,str_ips)
            ips = []
        else:
            print ip_head+str_a+'.* is no useable ip.'
        print getln()

def main():
    filename = 'ip.txt'
    ifhasfile(filename)
    writeline(filename)
    write(filename,'Google Cn Ip:')
    writeline(filename)
    run(filename,'203.208.',36,37)
    writeline(filename)
    write(filename,'Google Hk Ip:')
    writeline(filename)
    run(filename,'74.125.',0,255)

if __name__ == '__main__':
    main()