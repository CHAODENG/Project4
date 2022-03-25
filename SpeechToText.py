#import Library
import speech_recognition as sr

# Initialize recognizer class
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable
# The path should be correct

with sr.AudioFile('Sample.wav') as source:
    
    audio = r.listen(source)
    
# Using exception handling in case the api could not be acceessed successfully.
    try:
        # using google speech recognition
        text = r.recognize_google(audio)
        print('Convertint Speech into text successfully!')
        print(text)
     
    except:
         print('Could not access API, please run it again.')