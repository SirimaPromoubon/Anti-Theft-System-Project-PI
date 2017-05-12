import RPi.GPIO as GPIO
import time 
import MySQLdb
import subprocess
import re
import sys
import datetime
import picamera
import os
import paramiko 
import requests

#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#ssh.connect('localhost',username = "pi",password="raspberry",port=22)
#sftp = ssh.open_sftp()

#conn = MySQLdb.connect(user='root',passwd="root",host='localhost',db='antytheft')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)  #Motion sensor
GPIO.setup(3, GPIO.OUT)  #LED sensor
GPIO.setup(10, GPIO.IN) # switch
GPIO.setup(13,GPIO.OUT)	 #Buzzer sensor
GPIO.setup(7,GPIO.IN)  #Magnatic sensor
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
count = 0
sw = GPIO.input(10)
while True:
	j=GPIO.input(11)
	i=GPIO.input(7)
	if (j or i)==0: 
        	print "No intruders",i,j
		GPIO.output(3,0)
		GPIO.output(13,0)
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S');
		print st

	elif (j or i)==1:
		print "Intruder detected",i,j
		#GPIO.output(3,1)
		#GPIO.output(7,1)
		url = 'https://maker.ifttt.com/trigger/notification/with/key/jMaI0vcKp127VT81vdJrT50JeQ2omUTaysNyBrTCTDH'
		with picamera.PiCamera() as camera:
			if(os.path.isfile('/home/pi/Desktop/node-v0.10.33/public/video'+str(count)+'.mp4')):
				os.remove('/home/pi/Desktop/node-v0.10.33/public/video'+str(count)+'.mp4')
				os.remove('/home/pi/Desktop/node-v0.10.33/public/video'+str(count)+'.h264')			
                        filename = '/home/pi/Desktop/node-v0.10.33/public/video'+str(count)+'.h264'
			#filename = 'http://172.26.240.61/public/photo/p'+ st +'.h264'
			#camera.start_recording('/home/pi/Desktop/p'+ st+'.h264')
			camera.start_recording(filename)
			res = requests.post(url, data = {"value1" : "warnning!!!"})
			#print "after starting"
			camera.wait_recording(5)
			#print "after wait"
			GPIO.output(3,1)
                        GPIO.output(13,1)

			camera.start_preview()
                        camera.capture('/home/pi/Desktop/node-v0.10.33/public/picturebefor'+ str(count)+'.jpg')
                        camera.stop_preview()

			camera.wait_recording(5)

			camera.start_preview()
			camera.capture('/home/pi/Desktop/node-v0.10.33/public/pictureafter'+ str(count)+'.jpg')
			camera.stop_preview()

			camera.stop_recording()
			#print "after stop"
#			output = '/home/pi/Desktop/node-v0.10.33/public/video'+str(count)+'.mp4'
			#ffmpeg -i filename -vcodec copy -an output
			os.chdir('/home/pi/Desktop/node-v0.10.33/public/')				
			os.system('MP4Box'+' -fps 30 -add'+' video'+str(count)+'.h264' +' video'+str(count)+'.mp4')

			#ssh = paramiko.SSHClient()
			#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			#ssh.connect('31.170.165.141', username="u192824589", password="gee27111!")
			#sftp = ssh.open_sftp()
			#localpath = '/public_html'
			#remotepath = output
			#sftp.put(localpath, remotepath)
			#sftp.close()
			#ssh.close()
			#os.rename(filename,'/home/pi/Desktop/node-v0.10.33/public/video'+str(count)+'.mp4')
			#os.rename(filename,'http://172.26.240.61/public/photo/p'+ st +'.mp4')
			#camera.start_recording('/home/pi/Desktop/picture'+ st+'.h264')
			#camera.start_preview()
			count = (count + 1)
			time.sleep(0.1)
			#camera.omxplayer('/home/pi/Desktop/picture'+ st+'.h264')
			#camera.capture('/home/pi/Desktop/picture'+ st+'.jpg')
			#camera.stop_recording()
			#camera.stop_preview()

#		GPIO.output(7,0)
#		url = 'node-v0.10.33/public/video.mp4'
#		c = conn.cursor()
 #               c.execute("INSERT INTO video (name,time) VALUES (%s,%s)",(url,st))
#		conn.commit()
		#localpath = '/home/pi/Desktop/video.mp4'
		#remotepath = '/home/pi/Desktop/video/video.mp4'
		#sftp.put(localpath, remotepath)
	time.sleep(0.3)
        
