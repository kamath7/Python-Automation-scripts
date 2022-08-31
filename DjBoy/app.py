from pydub import AudioSegment

original = AudioSegment.from_wav('./beat.wav')
print(type(original))
print(original)

reversed = original.reverse()
reversed.export('./reverse1.wav')