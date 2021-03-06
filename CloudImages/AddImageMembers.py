from __future__ import print_function

import os
import pyrax

pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file.py")
pyrax.set_credential_file(creds_file)

imgs = pyrax.images

print("You will need a valid project_id for the member you wish to add.")
images = imgs.list(visibility="private")

if len(images) == 1:
    image = images[0]
    print("Only one image available; using '%s'." % image.name)
else:
    print("Images:")
    for pos, image in enumerate(images):
        print("[%s] - %s" % (pos, image.name))
    snum = raw_input("Enter the number of the image you want to share: ")
    if not snum:
        exit()
    try:
        num = int(snum)
    except ValueError:
        print("'%s' is not a valid number." % snum)
        exit()
    if not 0 <= num < len(images):
        print("'%s' is not a valid image number." % snum)
        exit()
    image = images[num]

project_id = raw_input("Enter the project ID of the member you wish to share "
        "this image with: ")
if not project_id:
    print("No project ID entered; exiting.")
    exit()
imgs.http_log_debug = True
member = imgs.add_image_member(image, project_id)
print("The following member was added:")
print(" ID: %s" % member.id)
print(" Status: %s" % member.status)
print(" Created at: %s" % member.created_at)
