# import the necessary packages
import speech_recognition as sr 
from pydub import AudioSegment

# preconversion of daudio sample from .m4a to .wav
def preConvert():
    initialSound = 'Your_audio_sample_path.m4a'
    track = AudioSegment.from_file(initialSound, format='mp4')
    track.export('Your_audio_sample_path.wav',format='wav')
    newSound = 'Your_audio_sample_path.wav'
    return newSound
    

sound = preConvert()


# getting the speech recognizer function
r = sr.Recognizer()

# this indicates the length of quietness
# this is used when the speaker is slow 
# and there are lot of pauses in the audio sample
# the value is in seconds and it means that 
# if the audio sample is quiet for more than 3 seconds
# it will stop recognizing 

r.pause_threshold = 3

# for the sound 
with sr.AudioFile(sound) as source:
    r.adjust_for_ambient_noise(source)
    print('Converting audio to text....')
    audio = r.listen(source)
    
    try:
        # printing the words spoken
        print(r.recognize_google(audio))
    except Exception as e:
        print("Error {} : ".format(e) )