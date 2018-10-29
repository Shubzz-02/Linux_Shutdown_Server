#!/usr/bin/env python
import os


def start():
    if os.geteuid() is not 0:
        print "[-] Root permission required"
        print "[+] Run command chmod +x ./Setup"
        print "[+] sudo ./Setup "


def write_file():
    os.chdir("/etc/systemd/system")
    fo = open("shutdown_client.service","w")
    fo.write("[Unit]\nDescription=Shutdown Client Service\nAfter=dbus.service\n"
             "\n[Service]\nExecStart=/usr/local/bin/node.py\n"
             "\n[Install]\nWantedBy=default.target")


start()



https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/sect-managing_services_with_systemd-unit_files
https://linuxconfig.org/how-to-automatically-execute-shell-script-at-startup-boot-on-systemd-linux