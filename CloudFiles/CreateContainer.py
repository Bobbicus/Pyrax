import os
import pyrax
pyrax.set_default_region("SYD")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file.py")
pyrax.set_credential_file(creds_file)

cf = pyrax.cloudfiles

print "list_containers:", cf.list_containers()

