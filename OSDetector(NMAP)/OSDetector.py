#!/usr/bin/python3
#coding: utf-8

import re, sys, subprocess


if len(sys.argv) != 2:
        print("\n Usage: [#] getOS.py <ip-adress> \n ")
        sys.exit(1)

def get_ttl(ip_adress):

    ping_proc = subprocess.Popen(["ping -c 1 {}".format(ip_adress), ""], stdout=subprocess.PIPE, shell=True)

    (out,err) = ping_proc.communicate()

    out = out.split()

    out = out[12].decode('utf-8')

    ttl = re.findall("\d{1,3}", out)[0]

    return ttl

def os(ttl):

    ttl = int(ttl)
    if ttl >= 0 and ttl <= 64:
        return "Linux"
    elif ttl >= 65 and ttl <= 128:
        return "Windows"

    else:
        return "Not found"

if __name__=='__main__':
    try:

        ip_adress = sys.argv[1]

        print("\n Machine {} With TTL -> {} \n OS -> {} \n".format(ip_adress, get_ttl(ip_adress), os(get_ttl(ip_adress))))

    except:
       print("\n Usage: [#] getOS.py <ip-adress> \n")
