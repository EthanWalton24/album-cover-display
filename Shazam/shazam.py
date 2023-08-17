import asyncio
from shazamio import Shazam
from os.path import exists
from .record import record_audio
import os,time


async def get_song_info():
  shazam = Shazam()
  out = await shazam.recognize_song('recording.wav')
  return(out['track'])

def get_album_cover(songInfo):
	return songInfo['images']['coverart']


def identify_song():
	loop = asyncio.get_event_loop()


	if exists('recording.wav'):
		os.remove('recording.wav')

	record_audio()

	try:
		songInfo = loop.run_until_complete(get_song_info())
		
		return(get_album_cover(songInfo))

		
	except KeyError:
		return("none")
