from pydub import AudioSegment

beat = AudioSegment.from_wav('./beat.wav')
sax = AudioSegment.from_wav('./sax.wav')
bea2 = beat* 2 


mixed = bea2.overlay(sax)
mixed.export('awesome.wav')

final = bea2 + mixed *2 + sax * 4 + bea2 + sax 
final.export("dontknow.wav")
