import os
import subprocess
import sys
import time
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0


loop = 0

# instantiate
config = ConfigParser()

# parse existing file
config.read('config.ini')

# read values from a section
EcoServer = config.get('Dir', 'EcoServer')
WorkingDir = config.get('Dir', 'WorkingDir')

def start():
    subprocess.Popen(EcoServer, cwd=WorkingDir)

def stop():
    os.system("TASKKILL /F /IM EcoServer.exe")

def getTasks(name):
    r = os.popen('tasklist /v').read().strip().split('\n')
    #print ('# of tasks is %s' % (len(r)))
    for i in range(len(r)):
        s = r[i]
        if name in r[i]:
            #print ('%s in r[i]' %(name))
            return r[i]
    return []

while True:
    imgName = 'EcoServer.exe'
    notResponding = 'Not Responding'
    r = getTasks(imgName)

    if not r:
        start()
        time.sleep(1)
         

    elif 'Not Responding' in r:
        stop()
        time.sleep(15)
        start()
        time.sleep(1)
        
