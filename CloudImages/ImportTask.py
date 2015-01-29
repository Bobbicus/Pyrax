from __future__ import print_function

import os
import pyrax

pyrax.set_default_region("ORD")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file_Bob.py")
pyrax.set_credential_file(creds_file)

imgs = pyrax.images
cf = pyrax.cloudfiles

print("You will need an image file stored in a Cloud Files container.")
conts = cf.list()
print()
print("Select the container containing the image to import:")
for pos, cont in enumerate(conts):
    print("[%s] %s" % (pos, cont.name))
snum = raw_input("Enter the number of the container: ")
if not snum:
    exit()
try:
    num = int(snum)
except ValueError:
    print("'%s' is not a valid number." % snum)
    exit()
if not 0 <= num < len(conts):
    print("'%s' is not a valid container number." % snum)
    exit()
cont = conts[num]

print()
print("Select the image object:")
objs = cont.get_objects()
for pos, obj in enumerate(objs):
    print("[%s] %s" % (pos, obj.name))
snum = raw_input("Enter the number of the image object: ")
if not snum:
    exit()
try:
    num = int(snum)
except ValueError:
    print("'%s' is not a valid number." % snum)
    exit()
if not 0 <= num < len(conts):
    print("'%s' is not a valid object number." % snum)
    exit()
obj = objs[num]

fmt = raw_input("Enter the format of the image [VHD]: ")
fmt = fmt or "VHD"
base_name = os.path.splitext(os.path.basename(obj.name))[0]
obj_name = raw_input("Enter a name for the imported image ['%s']: " % base_name)
obj_name = obj_name or base_name

task = imgs.import_task(obj, cont, img_format=fmt, img_name=obj_name)
print("Task ID=%s" % task.id)
print()
answer = raw_input("Do you want to track the task until completion? This may "
        "take several minutes. [y/N]: ")
if answer and answer[0].lower() == "y":
    pyrax.utils.wait_until(task, "status", ["success", "failure"],
            verbose=True, interval=30)
    print()
    if task.status == "success":
        print("Success!")
        print("Your new image:")
        new_img = imgs.find(name=obj_name)
        print(" ID: %s" % new_img.id)
        print(" Name: %s" % new_img.name)
        print(" Status: %s" % new_img.status)
        print(" Size: %s" % new_img.size)
        print(" Tags: %s" % new_img.tags)
    else:
        print("Image import failed!")
        print("Reason: %s" % task.message)
