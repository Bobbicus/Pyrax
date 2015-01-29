from __future__ import print_function

import os
import pyrax

pyrax.set_default_region("ORD")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file_Bob.py")
pyrax.set_credential_file(creds_file)

imgs = pyrax.images
imgs.http_log_debug = True

print("Listing images with pending status...")
images = imgs.list(visibility="shared", member_status="pending")

if not images:
    print("No pending images found")
    exit()

for pos, image in enumerate(images):
    new_status = None
    print("[%s] - %s" % (pos, image.name))
    choice = raw_input("Would you like to accept, reject or skip? "
            "('a', 'r', or 's'): ")
    if choice == 'a':
        new_status = 'accepted'
    elif choice == 'r':
        new_status = 'rejected'

    if new_status is not None:
        print("[%s] - %s : Updating status to %s" % (pos, image.name, new_status))
        imgs.update_image_member(image.id, new_status)
        print("[%s] - %s : has been updated" % (pos, image.name))
    else:
        print("[%s] - %s : Skipping update" % (pos, image.name))
