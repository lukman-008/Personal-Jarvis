  
from mimetypes import init
import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import os

import datetime
import pywhatkit
from bs4 import BeautifulSoup
import requests
import urllib
from PyQt5 import QtCore , QtWidgets ,QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from jarvisui import Ui_MainWindow
import sys
import cv2
import numpy







def speak(audio):
    
    engine.say(audio)
    print("  ") 
    engine.runAndWait()

def wish():
        
      hour = int(datetime.datetime.now().hour)
      strTime = datetime.datetime.now().strftime("%I:%M %p")
                

      if hour >= 0 and hour <=12:
             speak(f"good morning boss")
             
             speak(f"it is{strTime}")
             print(f"it is {strTime} now")

      elif hour >=12 and hour <= 18:
             speak(f"good afternoon boss")
             speak(f"it is{strTime} now ")
             print(f"it is {strTime} now")

      elif hour >=18 and hour <= 23:
                 speak(f"good evening boss")
                 speak(f"it is {strTime} now")
                 print(f"it is {strTime} now")

      else:
        speak("good night boss")
        speak(f"it is {strTime} now")
        print(f"it is {strTime} now")
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)

class MainThread(QThread):

          def __init__(self) :
                 super(MainThread,self).__init__()

          def run(self):
                  self.TaskExecution()

          def takecommand(self):    
                        r = sr.Recognizer() 
                        with sr.Microphone() as source: 
                         print("Listning....")
                         r.pause_threshold = 1
                         r.energy_threshold = 500
                         audio = r.listen(source)

                        try:
                          print("Recognizing...")
                          query = r.recognize_google(audio,language= 'en-in')
                          print(f"you said :{query}")


                        except Exception as e:

                           return "none"
                        query = query.lower()
                        return query
                
                
          def TaskExecution(self):
                 speak( " hello sir  i am  jarvis an artificial intelligence made by  Prabhash  Ranjan how can i help you") 
                 print( " hello sir  i am jarvis an artificial intelligence  made by  Prabhash Ranjan how can i help you") 
                 wish()
                 while True:

                  self.query = self.takecommand()

                  if 'what is your name' in self.query:

                                print(" My name is jarvis I am Prabhash Artificial Intelligence")
                                speak(" my name is  jarvis i am prabhash artificial intelligence")
                                
                  elif 'search' in self.query and 'youtube' in self.query:
                        speak("this is what i found for you sir")
                        self.query = self.query.replace("search","")

                        self.query = self.query.replace("on youtube","")
                        self.query = self.query.replace("youtube","")
                        
                        web = "https://www.youtube.com/results?search_query="+ self.query
                        webbrowser.open(web)
                        pywhatkit.playonyt(self.query)
                        speak("here you go ,sir")



                  elif 'open youtube' in self.query:
                        speak(" youtube is now opening")
                        webbrowser.open("youtube.com")

                

                  elif 'open google' in self.query:  
                                speak(" google is now opening")
                                webbrowser.open("google.com")


                  elif 'open visual studio' in self.query:
                        speak(" visual studio code is now opening")
                        codePath = "C:\\Users\\Prabhash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        os.startfile(codePath)

                  elif 'open powershell' in self.query:
                        speak( " Microsoft  powershell  is now opening")
                        codePath = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
                        os.startfile(codePath)
                  elif "google" in self.query:
                                import wikipedia as googleScrap
                                self.query = self.query.replace("lucifer", "")
                                self.query = self.query.replace("google search", "")
                                self.query = self.query.replace("google", "")
                                speak("This is what I found")
                                try:
                                    pywhatkit.search(self.query)
                                    result = googleScrap.summary(self.query, 1)
                                    speak(result)

                                except:
                                    speak("Did not find anything about that, sorry")
                                self.query = self.query.replace("youtube", "")
                                self.query = self.query.replace("google search", "")
                                self.query = self.query.replace("google", "")
                                speak("This is what I found on google")

                  elif 'open chrome' in self.query:
                                speak(" chrome is now opening")
                                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                                os.startfile(chromePath)

                  elif 'remember that' in self.query:
                        rememberMsg = self.query.replace("remember that","")
                        rememberMsg = rememberMsg.replace("jarvis","")
                        speak("You tell me to Remind You That:" +rememberMsg)
                        remember = open('data.txt','w')
                        remember.write(rememberMsg)
                        remember.close()
                        
                  elif 'what do you remember' in self.query:
                        remember = open('data.txt','r')
                        speak("You Tell Me That"+remember.read())

                  elif 'open instagram' in self.query:
                        speak("instagram is now opening")
                        webbrowser.open("instagram.com")

                  elif 'the time' in self.query:
                                strTime = datetime.datetime.now().strftime("%I:%M %p")
                                print(strTime)
                                speak(f"sir ,the time is{strTime}")
                                
                  elif 'how are you Monica' in self.query:
                                
                        print(" I am fine sir how are you sir")
                        speak(" i am fine sir how are you sir")

                  elif 'temperature' in self.query:

                        search = "temperature in bhopal"
                        url = f"http://www.google.com/search?q={search}"
                        r = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div",class_="BNeawe").text
                        print(f"current {search} is {temp}")
                        speak(f"current {search} is {temp}")

                  elif 'the time' in self.query:
                                strTime = datetime.datetime.now().strftime("%I:%M %p")
                                print(strTime)
                                speak(f"sir ,the time is{strTime}")

                  elif 'play music' in self.query:   
                        music = 'D:\\music'
                        songs = os.listdir(music)   
                        speak(" music is now playing")
                        os.startfile(os.path.join(music, songs[2]))

                  elif 'change music' in self.query:   
                        num = random.randint(0,5)
                        music = 'D:\\music'
                        songs = os.listdir(music)   
                        speak(" next  music is playing")
                        os.startfile(os.path.join(music, songs[num]))

                  elif 'thank you' in self.query:
                                
                        print(" you are welcome sir")
                        speak(" you are welcome sir")

startExecution = MainThread()
class Main(QMainWindow):
        def  __init__(self):
               super().__init__()    
               self.ui = Ui_MainWindow()
               self.ui.setupUi(self)
               self.ui.pushButton.clicked.connect(self.startTask)
               self.ui.pushButton_2.clicked.connect(self.close)
               
        def startTask(self):
                self.ui.movie = QtGui.QMovie("C:\\Users\\Prabhash\\OneDrive\\Desktop\\jarvis.gif")
                self.ui.jarvisui.setMovie(self.ui.movie)
                self.ui.movie.start()
                self.ui.movie = QtGui.QMovie("C:\\Users\\Prabhash\\OneDrive\\Desktop\\initial.gif")
                self.ui.label_2.setMovie(self.ui.movie)
                self.ui.movie.start()
                self.ui.movie = QtGui.QMovie("C:\\Users\\Prabhash\\OneDrive\\Desktop\\q2.gif")
                self.ui.label_3.setMovie(self.ui.movie)
                self.ui.movie.start()
                startExecution.start()    

app = QApplication(sys.argv)
jarvis =  Main()
jarvis.show()
exit(app.exec_())                 