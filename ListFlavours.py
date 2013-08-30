import os
import pyrax
pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file")
pyrax.set_credential_file(creds_file)

cs = pyrax.cloudservers

flvs = cs.flavors.list()

for flavor in flvs:
    print "Name:", flavor.name
    print " ID:", flavor.id
    print " RAM:", flavor.ram
    print " Disk:", flavor.disk
    print " VCPUs:", flavor.vcpus
    print
