import os 
import sys 

def getvenvloc(serverFile):
    List = serverFile.split('/')
    del List[len(list)-1]
    List.append('venv/')
    return '/'.join(List)

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
            'ExecStart=/bin/sh -c python3 ', getserverloc() , '>', getlogloc(getserverloc()) ,'\n',
            '\n',
            '[Install]', '\n',
            'WantedBy=multi-user.target'
        ])
    with open("Flask_Service_Script", "w+") as script:
        script.writelines([
            '. ' + getvenvloc + 'bin/activate', '\\n',
            'python3 ' + getserverloc()
        ])

servgen(sys.argv[1])