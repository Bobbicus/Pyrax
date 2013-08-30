
import os
import pyrax
pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file.py")
pyrax.set_credential_file(creds_file)

cs = pyrax.cloudservers
servers = cs.servers.list()
flvs = cs.flavors.list()

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

image12 = cs.images.get(img_id)
image = pyrax.utils.wait_until(image12, "status", ["ACTIVE", "ERROR"], attempts=0)


images = cs.images.list()
#between these taqgs is test code
srv_clone = {}
print "Select a image to create server from"
for pos, img in enumerate(images):
    print "%s: %s" % (pos, img.name)
    srv_clone[str(pos)] = img.name
selection = None
while selection not in srv_clone:
    if selection is not None:
        print " -- Invalid choice"
    selection = raw_input("Enter the number for your choice: ")

clone_id = srv_clone[selection]
print

images2 = [imgs for imgs in cs.images.list()
        if imgs.name == clone_id][0]
print images2.id

flv_clone = {}
print "Select a Flavor"
for pos, flv in enumerate(flvs):
    print "%s: %s" % (pos, flv.name)
    flv_clone[str(pos)] = flv.name
selection = None
while selection not in flv_clone:
    if selection is not None:
        print " -- Invalid choice"
    selection = raw_input("Enter the number for your choice: ")

server_flav = flv_clone[selection]
print

flvs30 =[flavor for flavor in cs.flavors.list() if flavor.name == server_flav][0]
print flvs30
#between these taqgs is test code

server = cs.servers.create("TESTCLone", images2.id, flvs30.id)
print "Name:", server.name
print "ID:", server.id
print "Status:", server.status
print "Admin Password:", server.adminPass
print "Networks:", server.networks

#wait for server to build before doing anything else
new_srv = pyrax.utils.wait_until(server, "status", 
        ["ACTIVE", "ERROR"], attempts=0)

status = server.status

if status == "ACTIVE" :
    print "Server build complete"
else:
    print "Server Build error please investigate"

#print network details, these are not available when you first build the server
server = cs.servers.get(server.id)
print server.networks

