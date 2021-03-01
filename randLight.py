#!/root/scripts/plant/plant_env/bin/python
# 2021 - Enigaticdevices.com

import subprocess
import json
import urllib.request
import time
from time import strftime 
from time import sleep

def setPlugState(a1,c1):
	 exec = subprocess.run(["kasa","--plug","--alias",a1,c1])

def getRandom(l,h):
	#print(l)
	#print(h)
	#update IP address below
	restEndpoint = "http://xxx.xxx.xxx.xxx:5000/rangeInt/"+l+"/"+h
	getnum = json.load(urllib.request.urlopen(restEndpoint))
	output = getnum[0]["value"]
	return output

def setAllPlugsOff():
	setPlugState('P1','off')
	setPlugState('P2','off')
	setPlugState('P3','off')
	setPlugState('P4','off')

def setPlug(x,sleep_factor):
	global plug
	global cmd
	if(x == 1):
		plug = 'P1'
		cmd = 'on' 
		setPlugState(plug,cmd)
		logWrite(plug,cmd)
	if(x == 2):
		plug = 'P2'
		cmd = 'on'
		setPlugState(plug,cmd)
		logWrite(plug,cmd)
	if(x == 3):
		plug = 'P3'
		cmd = 'on'
		setPlugState(plug,cmd)
		logWrite(plug,cmd)
	if(x == 4):
		plug = 'P4'
		cmd = 'on'
		setPlugState(plug,cmd)
		logWrite(plug,cmd)


def logWrite(plug,cmd):
	dtime = strftime("%m-%d-%Y %H:%M:%S")
	logfile.write(dtime+" rand_select="+str(x)+" plug="+plug+" state="+cmd+"+plant_position="+str(plant_position)+" plant_num="+str(plant_num)+" light_time="+str(light_time)+" exper_num="+str(exper_num)+"\n")
	
## of positions
low_range = '1'
high_range = '4'

## plant location
plant_position='2'

## number of plants
plant_num = 1 

## slow script speed
sleep_factor = 1 

## how long to keep light on
light_time = 2 

## experiment #
exper_num = 9 

## open log

loghandle = '/some/file/some.file' 

logfile = open(loghandle, "a")


count = 0
#init
setAllPlugsOff()
while count < 1:

	x=int(getRandom(low_range,high_range))
	print(x)
	if (x == 1):
		plug_set = 'P1'
	if (x == 2):
		plug_set = 'P2'
	if (x == 3):
		plug_set = 'P3'
	if (x == 4):
		plug_set = 'P4'

	setPlug(x,sleep_factor)

	sleep(light_time)
	setPlugState(plug_set,'off')
	logWrite(plug_set,'off')
