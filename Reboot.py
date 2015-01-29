from __future__ import print_function

import os
import pyrax

pyrax.set_default_region("LON")
pyrax.set_setting("identity_type", "rackspace")

creds_file = os.path.expanduser("C:\Python27\Scripts\credentials_file.py")
pyrax.set_credential_file(creds_file)

import sys

cs = pyrax.cloudservers

servers = cs.servers.list()
# Find the first 'ACTIVE' server
try:
    active = [server for server in servers
            if server.name =="BobPython"]
except IndexError:
    print("There are no active servers in your account.")
    print("Please create one before running this script.")
    sys.exit()
# Display server info
print("Server Name:", active.name)
print("Server ID:", active.id)
print("Server Status:", active.status)
print()
answer = raw_input("Do you wish to reboot this server? [y/n] ")
if answer.strip().lower()[0] == "y":
    print()
    print("A 'soft' reboot attempts a graceful shutdown and restart of your "
        "server.")
    print("A 'hard' reboot power cycles your server.")
    answer = raw_input("Which type of reboot do you want to do? [s/h] ")
    answer = answer.strip().lower()[0]
    reboot_type = {"s": "soft", "h": "hard"}[answer]
    active.reboot(reboot_type)
    # Reload the server
    after_reboot = cs.servers.get(active.id)
    print()
    print("After reboot command")
    print("Server Status =", after_reboot.status)
