#Basic script to create Load Balancer
from __future__ import print_function
import os
import pyrax

import sys

pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credfile.py")
pyrax.set_credential_file(creds_file)

clb = pyrax.cloud_loadbalancers
try:
    lb = clb.list()[0]
except IndexError:
    print("You do not have any load balancers yet.")
    print("Please create one and then re-run this script.")
    sys.exit()

print("Load Balancer:", lb)
print("Name:", lb.name)
print("ID:", lb.id)
print("Status:", lb.status)
print("Nodes:", lb.nodes)
print("Virtual IPs:", lb.virtual_ips)
print("Algorithm:", lb.algorithm)
print("Protocol:", lb.protocol)
