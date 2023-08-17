import sounddevice as sd
from scipy.io.wavfile import write



def record_audio(duration=5):
	fs = 44100  # Sample rate
	seconds = duration  # Duration of recording
	sd.default.device = 0

	myrecording = sd.rec(seconds * fs, samplerate=fs, channels=1)
	sd.wait()  # Wait until recording is finished
	write('recording.wav', fs, myrecording)  # Save as WAV file


