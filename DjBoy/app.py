from pydub import AudioSegment

original = AudioSegment.from_wav('./beat.wav')
print(type(original))
print(original)

reversed = original.reverse()
reversed.export('./reverse1.wav')

first_two = original[0:2000] #first 2 secs
first_two.export('./2sec.wav')