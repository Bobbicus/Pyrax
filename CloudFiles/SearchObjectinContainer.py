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

"""
#list all the objects in a container that conatin a certain sting
for obj in objects:
    if "beforeafter_btn_f2" in obj.name:
        print obj.name"""

objID =[obj1 for obj1 in cont.get_objects() if "beforeafter_btn_f2" in obj1.name]
