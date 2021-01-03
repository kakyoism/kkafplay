"""PyAudio Example: Play a wave file (callback version)"""

import pyaudio
import wave
import time
import sys


def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return data, pyaudio.paContinue


def play(wavefile):
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wavefile.getsampwidth()),
                    channels=wavefile.getnchannels(),
                    rate=wavefile.getframerate(),
                    output=True,
                    stream_callback=callback)

    stream.start_stream()

    while stream.is_active():
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    wavefile.close()

    p.terminate()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
        sys.exit(-1)

    wf = wave.open(sys.argv[1], 'rb')
    play(wf)
