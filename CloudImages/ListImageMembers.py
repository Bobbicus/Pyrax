from __future__ import print_function

import os
import pyrax

pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file.py")
pyrax.set_credential_file(creds_file)


imgs = pyrax.images

print("This will loop through all your private images and list the members for "
        "each.")
images = imgs.list(visibility="private")
if not images:
    print("No images exist.")
    exit()
for image in images:
    members = imgs.list_image_members(image)
    if not members:
        print("Image %s: no members" % image.id)
    else:
        print("Image %s:" % image.id)
        for member in members:
            print(" %s (%s)" % (member.id, member.status)) 
