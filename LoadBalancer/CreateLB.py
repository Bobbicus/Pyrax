#Basic script to create Load Balancer

import os
import pyrax
pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file.py")
pyrax.set_credential_file(creds_file)

clb = pyrax.cloud_loadbalancers
lb_name = "LBTest1"

# You may have to adjust the address of the node to something on
# the same internal network as your load balancer.  The internal IP of one of your nodes.
node = clb. Node(address="10.179.200.58", port=80, condition="ENABLED")
vip = clb.VirtualIP(type="PUBLIC")
lb = clb.create(lb_name, port=80, protocol="HTTP", nodes=[node], virtual_ips=[vip])

print "Node:", node.to_dict()
print "Virtual IP:", vip.to_dict()
print
print "Load Balancer:", lb
