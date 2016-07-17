#!/usr/bin/python
import os
def get_ip():
    ipv4 = os.popen('ip addr show wlx000d81acc768 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()
    print str(ipv4)
get_ip()
