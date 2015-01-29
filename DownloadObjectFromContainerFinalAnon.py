# Change where you see "ContainerName" change this to your cloud files container name
# Where you see "/Directory/" change this to direcoty on your machine that you want to downlaod the file to
#

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
cont = cf.get_container("ContainerName")
start = time.time()
objects = cont.get_objects()

#user prompt for what file name to search for
download_file = raw_input("Search for file to download: ")


#Lists the matching object and asks for user input
obj_dict = {}
print "List of object matching your search"
for pos, obj in enumerate(objects):
    if download_file in obj.name:
        print "%s: %s" % (pos, obj.name)
    obj_dict[str(pos)] = obj.name
selection = None
while selection not in obj_dict:
    if selection is not None:
        print " -- Invalid choice"
    selection = raw_input("Enter the number of the object you would like to download: ")

obj.name= obj_dict[selection]
print
#Downloads the chosen object to a local directory
obj_to_download = obj.name
cf.download_object("ContainerName",obj_to_download,"/Directory/",structure=False)



