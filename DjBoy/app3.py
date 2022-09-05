from pydub import AudioSegment

beat = AudioSegment.from_wav('./beat.wav')

lo_beat = beat.low_pass_filter(2000)
lo_beat.export('lo.wav')

beat_left = lo_beat.pan(-0.5)
# beat_left.export('beatlf.wav') #only left sided stereo
beat_right = lo_beat.pan(0.5)
beat_final = beat_left + beat_right
beat_final.export("finalbeat.wav")