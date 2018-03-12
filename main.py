import os
import subprocess
import sys
import time


loop = 0

def start():
    subprocess.Popen(r'C:\\Users\\Administrator\\Desktop\\Server\\ECO_v0.7.2.3\\EcoServer.exe', cwd=r'C:\\Users\\Administrator\\Desktop\\Server\\ECO_v0.7.2.3')

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
        
