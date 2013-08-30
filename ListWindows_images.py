import os
import pyrax
pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file")
pyrax.set_credential_file(creds_file)

cs = pyrax.cloudservers

imgage3 = cs.images.list()

images2 = [imgs for imgs in cs.images.list()
        if "Windows Server 2008 R2 SP1" in imgs.name][0]

print "Name:", images2.name
print "ID:", images2.id
