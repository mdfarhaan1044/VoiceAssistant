import pyttsx3 as p
import speech_recognition as sr
import selenium_web 
from yt_video import *
from news import *
import randfacts
from weather import *
import datetime



engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',180)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
  engine.say(text)
  engine.runAndWait()

def wishme():
     hour=int(datetime.datetime.now().hour)
     if hour>0 and hour <12:
        return("morning")
     elif hour>12 and hour<16:
        return("evening")
     else:
        return("evening")

today_date=datetime.datetime.now()
r = sr.Recognizer()
 
speak("Hello sir, good "+ wishme() +", I'm your voice assistant.")
speak("today is "+today_date.strftime('%d')+"of"+today_date.strftime('%B')+today_date.strftime('%Y')+"and its currently"+today_date.strftime('%I')+today_date.strftime('%M')+today_date.strftime('%p'))
# speak("Temperature in Hyderabad is" + str(temp()) +"degree celsius and with" + str(des()))
speak("What can i do for you?")

# with sr.Microphone() as source:
#     r.energy_threshold=10000
#     r.adjust_for_ambient_noise(source,1.2)

#     print('Listening...')
#     audio = r.listen(source)
#     text=r.recognize_google(audio)
#     print(text)
# if "what" and "about" and "you" in text:
#    speak("i'm having a good day sir")
# speak("what can i do for you")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print('Listening...')
    audio = r.listen(source)
    text2=r.recognize_google(audio)

if "information" in text2:
   speak('sure sir, you need information related to which topic?')

   with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print('Listening...')
    audio = r.listen(source)
    infor = r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))
    print("searching {} in wikipedia".format(infor))

    x = selenium_web.information
    x().get_info(infor)


elif "play" and "video" in text2:
   speak("Which video should i play?")
   with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print('Listening...')
    audio = r.listen(source)
    vid = r.recognize_google(audio)
    print("Playing {} on YouTube".format(vid))
    speak("Playing {} on YouTube".format(vid))

    assist = video()
    assist.play(vid)

elif "news" in text2:
   print("sure sir, I will read news for you")
   speak("sure sir, I will read news for you")
   arr=news()
   for i in range(len(arr)):
      print(arr[i])
      speak(arr[i])
      
elif "fact" in text2:
   y=randfacts.get_fact()
   print(y)
   speak("Did you know that,"+y)




      



