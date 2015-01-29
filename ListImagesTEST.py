import os
import pyrax
pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file.py")
pyrax.set_credential_file(creds_file)

cs = pyrax.cloudservers

image3 = cs.images.list()

for imgs in image3:
    print "Name:", image3.name
    print "ID:", image3.id
