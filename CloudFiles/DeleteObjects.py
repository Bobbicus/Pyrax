import os
import time

import pyrax
import pyrax.exceptions as exc

pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file.py")
pyrax.set_credential_file(creds_file)

cf = pyrax.cloudfiles

#Set which conatiner you are going to delete
cont = cf.get_container("cloudservers")
start = time.time()
objects = cont.get_objects()


#Below section has been commented out, you can add this back if you want to list all the objects in a container
for obj in objects:
    if "SMB" in obj.name:
        print obj.name

    
"""

cont.delete_all_objects()

#Check if there are any objects left, if there are provide an update
while objects:
    try:
        objects = cont.get_object(cont)
        print "...still there..."
        time.sleep(0.5)
    except exc.NoSuchObject:
        obj = None
        print "Objects in '%s' have been deleted" % cont
        print "It took %4.2f seconds to appear as deleted." % (time.time() - start)

#Delete the container
cont.delete(True)

"""
