from pydub import AudioSegment

original = AudioSegment.from_wav('./beat.wav')
print(type(original))
print(original)

reversed = original.reverse()
reversed.export('./reverse1.wav')

first_two = original[0:2000] #first 2 secs
first_two.export('./2sec.wav')

print(len(original)) #3567 -> 3.5 second

merge = original + reversed
merge.export('merged.wav')

merge1 = original + AudioSegment.silent(1000) +  reversed
merge1.export('merged1.wav')
