import speech_recognition as sr
from floor_code import *

def VoiceInput():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Give the command")
        audio_text = r.listen(source,10,5)
        
        print("Time over, thanks")
        
        try:
            result = r.recognize_google(audio_text)
            
        except:
            print('No command detected')
            return []
            
    result = result.lower()
    result = result.replace(" ","")
    
    floors = result.split('floor')[:-1]
    res = []
    for each in floors:
        res.append(floorCode(each))

    return res
    

    

"""
    res = [i for i in range(len(result)) if result.startswith('floor', i)]
    res2 = []
    for i in res:
        try:
            
            res2.append(int(result[i-4]))
        except:
            continue
    return res2
"""
