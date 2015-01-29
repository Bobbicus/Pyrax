#This script will ask you which Cloud Files Container you want to delete.  It will delete all the objects in the containter
#and then it will delete the container

import os
import time

import pyrax
import pyrax.exceptions as exc

pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file.py")
pyrax.set_credential_file(creds_file)

cf = pyrax.cloudfiles

currentcont = cf.list_containers()


#Set which conatiner you are going to delete
#contname = raw_input("Enter the container you wish to delete: ")
#cont = cf.get_container(cont_dict)
#objects = cont.get_objects()
start = time.time()

cont_dict = {}
print "Select a server from which an image will be created."
for pos, con in enumerate(currentcont):
    print "%s: %s" % (pos, con)
    cont_dict[str(pos)] = con
selection = None
while selection not in cont_dict:
    if selection is not None:
        print " -- Invalid choice"
    selection = raw_input("Enter the number for your choice: ")

contname = srv_dict[selection]


cont.delete_all_objects()

#Check if there are any objects left, if there are provide an update
while objects:
    try:
        objects = cont.get_object(cont)
        print "...still there..."
        time.sleep(0.5)
    except exc.NoSuchObject:
        objects = None
        print "Objects in '%s' have been deleted" % cont
        print "It took %4.2f seconds to appear as deleted." % (time.time() - start)

#Delete the container
cont.delete(True)


