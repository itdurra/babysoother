import pyaudio
import numpy as np
from pydub import AudioSegment
from pydub.playback import play

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
THRESHOLD = 1000

# Load the lullabies
folderlocation = "[[ABSOLUTE PATH]]"
lullaby1 = AudioSegment.from_file(folderlocation + "lullaby1.mp3")
lullaby2 = AudioSegment.from_file(folderlocation + "lullaby2.mp3")

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Listening...")

while True:
    data = stream.read(CHUNK)
    audio_data = np.frombuffer(data, dtype=np.int16)
    if np.max(audio_data) > THRESHOLD:
        print("Loud sound detected!")
        # Play a lullaby
        play(lullaby2)  # You can choose which lullaby to play here
        # Add a delay before resuming listening
        # This prevents repeated detections of the same loud sound
        time.sleep(10)  # Wait for 10 seconds

stream.stop_stream()
stream.close()
p.terminate()
