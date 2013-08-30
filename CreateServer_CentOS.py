
import os
import pyrax
pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")
#request user input for Server name
server_name =  raw_input ("Server Name:")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file.py")
pyrax.set_credential_file(creds_file)

cs = pyrax.cloudservers

imgage3 = cs.images.list()
flvs = cs.flavors.list()
#check for image type sent OS
images2 = [imgs for imgs in cs.images.list()
        if "CentOS 6.3" in imgs.name][0]
print "Cent OS server", images2
#check for flavor type with disk size 20GB
flvs20 = [flavor for flavor in cs.flavors.list()
        if flavor.disk == 20][0]
print "20GB RAM", flvs20

#Create the server using the images/flavor from above
server = cs.servers.create(server_name, images2.id, flvs20.id)
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

