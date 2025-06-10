import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="sample.wav", duration=5, fs=44100):
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    write(filename, fs, recording)
    print(f"Saved recording to {filename}")
