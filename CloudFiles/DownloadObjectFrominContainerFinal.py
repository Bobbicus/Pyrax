import os
import time

import pyrax
import pyrax.exceptions as exc

pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file.py")
pyrax.set_credential_file(creds_file)


cf = pyrax.cloudfiles

#Set which container to search
cont = cf.get_container("CFLab")
start = time.time()
objects = cont.get_objects()

#user prompt for what file to download
download_file = raw_input("What file would you like to download: ")


#Lists the images and asks for user input
obj_dict = {}
print "Objects"
for pos, obj in enumerate(objects):
    if download_file in obj.name:
        print "%s: %s" % (pos, obj.name)
    obj_dict[str(pos)] = obj.name
selection = None
while selection not in obj_dict:
    if selection is not None:
        print " -- Invalid choice"
    selection = raw_input("Enter the object you would like to download: ")

obj.name= obj_dict[selection]
print

obj_to_download = obj.name
cf.download_object("CFLab",obj_to_download,"/Cloud Brown Bag/",structure=False)


