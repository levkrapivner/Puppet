#!/usr/bin/python
from datetime import *
from functions import *
#get the time
current_time =  datetime.now().strftime('%H:%M:%S %Y-%m-%d')

print """

################################################################################

Python 102 name: Lev [%s]

################################################################################

""" % current_time
print """
Segment: %s

Your dns:

Your gateway:

##############################
""" % get_ip()
