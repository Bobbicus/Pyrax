
import os
import pyrax
pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file.py")
pyrax.set_credential_file(creds_file)

cs = pyrax.cloudservers
servers = cs.servers.list()

srv_dict = {}
print "Select a server from which an image will be created."
for pos, srv in enumerate(servers):
    print "%s: %s" % (pos, srv.name)
    srv_dict[str(pos)] = srv.id
selection = None
while selection not in srv_dict:
    if selection is not None:
        print " -- Invalid choice"
    selection = raw_input("Enter the number for your choice: ")

server_id = srv_dict[selection]
print
nm = raw_input("Enter a name for the image: ")

img_id = cs.servers.create_image(server_id, nm)

print "Image '%s' is being created. Its ID is: %s" % (nm, img_id)
