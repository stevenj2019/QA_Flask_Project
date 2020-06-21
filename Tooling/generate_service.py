import os 
import sys 

def getlogloc(serverFile):
    List = serverFile.split('/')
    del List[len(List)-1]
    List.append('FlaskLog.txt')
    return '/'.join(List)

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
            'EXECStart=/bin/sh -c gunicorn --workers 4 ', getserverloc(), ' > ', getlogloc(getserverloc()),'\n'
            '\n',
            '[Install]', '\n',
            'WantedBy=multi-user.target'
        ])

servgen(sys.argv[1])