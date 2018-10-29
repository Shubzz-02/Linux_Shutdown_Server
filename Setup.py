#!/usr/bin/env python
import os
from os import path
import shutil
import subprocess


def start():
    if os.geteuid() is not 0:
        print "[-] Root permission required"
        print "[+] Run command chmod +x ./Setup.py"
        print "[+] sudo ./Setup.py "
        return False
    else:
    	return True


def write_file():
	try:
		os.chdir("/etc/systemd/system")
		fo = open("shutdown_client.service","w")
		fo.write("[Unit]\nDescription=Shutdown Client Service\nAfter=dbus.service\n"
				 "\n[Service]\nExecStart=/usr/local/bin/node.py\n"
				 "\n[Install]\nWantedBy=default.target")
		fo.close()
		os.chmod("shutdown_client.service",0644)
		return True
	except Exception as error:
		print error
		return False
		



def copy_file():
	if path.exists("node.py"):
		shutil.copy("node.py","/usr/local/bin/node.py")
		os.chmod("/usr/local/bin/node.py",0744)
		return True
	else:
		print "[-] File node.py no found"
		print "[-] Check if same location contains 'node.py'"
		return False

def initialize():
	subprocess.check_output(["systemctl","daemon-reload"],stderr=subprocess.STDOUT)
	subprocess.check_output(["systemctl","enable","shutdown_client.service"],stderr=subprocess.STDOUT)
	

if start():
	if copy_file():
		if write_file():
			initialize()
			



'https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/sect-managing_services_with_systemd-unit_files'
'https://linuxconfig.org/how-to-automatically-execute-shell-script-at-startup-boot-on-systemd-linux'
