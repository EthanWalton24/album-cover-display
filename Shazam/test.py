import record, shazam, os
from pydub import AudioSegment




'''record a 5 second sample from microphone and play it back'''
record.record_audio(duration=5)
sound = AudioSegment.from_wav('recording.wav')

#convert wav to mp3 and remove wav file
sound.export('recording.mp3', format='mp3')
os.remove("recording.wav")

#play the mp3 file
os.startfile("recording.mp3")


'''identify song, returning a link to the album cover of the song currently playing'''
print(identify_song())