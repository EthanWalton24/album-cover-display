import os,time,json
from threading import Thread
from Shazam.shazam import identify_song
from assistant import run_assistant
from matrix import displayCover

from rgbmatrix import RGBMatrix,RGBMatrixOptions


#create matrix object and configure settings for matrix setup
options = RGBMatrixOptions()
options.rows=64
options.cols=64
options.scan_mode=1
options.gpio_slowdown=5
options.brightness=100
options.hardware_mapping='adafruit-hat-pwm'
options.drop_privileges=False
#options.limit_refresh_rate_hz=100
#options.disable_hardware_pulsing=True
#options.show_refresh_rate=True
options.pwm_dither_bits=2
#options.pwm_lsb_nanoseconds=50
matrix = RGBMatrix(options=options)

#open the json file, displaying the image if there is one, otherwise display the default image
with open('cover.json','r') as file:
	info = json.load(file)
if info['cover'] == 'none':
	displayCover(matrix)
else:
	displayCover(matrix,info['cover'])



def album_cover_display():

	#record audio and get album cover of song playing
	albumCover = identify_song()

	#get the previous album cover
	with open('cover.json','r') as file:
		info = json.load(file) 
		previousCover = info['cover']


	#check if a new album is being played, if so then replace the old cover and display the new one
	if albumCover != previousCover:
		with open('cover.json','w') as file:
			info['cover'] = albumCover if albumCover != 'none' else info['cover']
			json.dump(info,file,indent=4)

		#change the display if a new,different album is being played
		if albumCover != 'none':
			displayCover(matrix,albumCover)




#set status of album display
on = True

#setup and run alexa in another thread
alexa = Thread(target=run_assistant)
alexa.start()


while True:
	if on:
		album_cover_display()

