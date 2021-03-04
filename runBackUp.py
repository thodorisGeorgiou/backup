#!/usr/bin/python3
import time
import os
import sys
from datetime import datetime

pathToBackupLogs = "/home/userName/.backup/"
# Open file with timestamp of last backup, if it does not exist, or has too many entries exit
try:
	f = open(pathToBackupLogs+"lastUpdated.dat", "r")
	lastUpdateTime = f.readlines()
	f.close()
except IOError:
	sys.exit("BACKUP: No recorded back up date")

if len(lastUpdateTime)>1:
	sys.exit("BACKUP: Too many entries in \"lastUpdated.dat\" file")


#If last update is more recent than threshold exit
# lastUpdated = datetime.fromtimestamp(int(lastUpdateTime[0].split(".")[0]))
# delta = datetime.now() - lastUpdated
# if delta.days < 1:
# 	f = open(pathToBackupLogs+"skippedBecauseOfThreshold.dat", "a")
# 	f.write(str(time.time())+"\n")
# 	f.close()	
# 	sys.exit("BACKUP: Updated in the last 24 hours")

#list of directories to back up
listOfPaths=["/home/userName/Downloads","/home/userName/Desktop","/home/userName/Documents","/home/userName/Pictures",\
"/home/userName/Videos","/home/userName/.backup","/home/userName/.ssh","/home/userName/.i3","/home/userName/.i3status.conf"]

#create bash command and execute
comm = " ".join(listOfPaths)
res = os.system("rsync -a "+comm+" serverUserName@serverIP:/backup/path")

#If backup is succesfull update timestamp else write timestamp in the "failed backups" file
if res==0:
	f = open(pathToBackupLogs+"lastUpdated.dat", "w")
else:
	f = open(pathToBackupLogs+"notUpdating.dat", "w")

f.write(str(time.time()))
f.close()
