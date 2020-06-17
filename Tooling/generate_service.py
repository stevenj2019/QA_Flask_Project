import os 
import sys 

def getserverloc():
    os.chdir('../')
    return os.path.abspath('server.py')

def servgen(Description):
    with open("Flask.service", "w+") as service:
        service.writelines([
            '[Unit]', '\n',
            'Description=', Description , '\n',
            '\n',
            '[Service]', '\n',
            'ExecStart=/bin/sh -c python3 ', getserverloc() ,'\n',
            '\n',
            '[Install]', '\n',
            'WantedBy=multi-user.target'
        ])

servgen(sys.argv[1])