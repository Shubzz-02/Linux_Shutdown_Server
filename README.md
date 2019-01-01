# Linux Shutdown Server
Batch shutdown Linux Computers connected to LAN.

Intro
Shutdown all slave linux system connected to same network.

### Prerequisites
* Python 

###Setup:-

* Server:-
1) Copy ShutdownServer.py to a master computer.
2) Move ShutdownServer.py to /usr/local/bin/.
3) Open terminal and type "chmod 744 ShutdownServer.py".
4) Now navigate to directory "/etc/systemd/system".
5) create a file shutdown_server.service  and paste the following content:-
    ```
        Description=Shutdown Server Service
        After=dbus.service
        [Service]
        ExecStart=/usr/local/bin/node.py
        [Install]
        WantedBy=default.target
     ```
6) Open terminal and type "chmod 744 shutdown_server.service".
7) In terminal type systemctl daemon-reload
8) then systemctl enable shutdown_server.service

* Client:-
1) Copy Setup.py and node.py  to a Client computer.
2) Open node.py and replace Ip with your server Ip.
3) Open terminal and run setup.py

Done

### How to Use 
When you have to shutdown all slave system, just run MasterClient.py on Master system and type shutdown -R now commmand.


``` 
If you want to add more command just add command to acc array on both ShutdownServer.py and node.py.
```
