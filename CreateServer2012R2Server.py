
import os
import pyrax
pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")
#request user input for Server name
server_name =  raw_input ("Server Name:")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file.py")
pyrax.set_credential_file(creds_file)

cs = pyrax.cloudservers


#Create the server using the images/flavor from above
server = cs.servers.create(server_name, "02f046e8-7380-42fa-a2e6-fc3d3c0ecacc", "performance1-2")
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

