import speech_recognition as sr
import multiprocessing as mp
import os
import time


def func(n):
    print("Task {} convert successfully".format(n))
    speechToText()
    
    time.sleep(2)   #simulate processing or server return time
    print("Task {} has been done now.".format(n))


def speechToText():
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
            print(text)
        
        except:
            print('Could not access API, please run it again.')

if __name__ == '__main__':

    nums_core = mp.cpu_count()
    print("There are {} cores being used now.".format(nums_core))
    pool = mp.Pool(nums_core) #use all available cores
    for i in range(0, 16):
        pool.apply_async(func, args=(i,))
    pool.close()
    pool.join()