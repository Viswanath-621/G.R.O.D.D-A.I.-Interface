import os
import cv2
import sys
from requests import get 
import requests as re 
import datetime as dt 
import wikipedia 
import webbrowser
import smtplib
import pywhatkit as kit
import speech_recognition as sr 
import pyttsx3 as ptx3 

## G.R.O.D.D's Commands 

'''
open opera
open terminal
start camera
play music
ip address
wikipedia
open youtube
open facebook
open my linkedin profile
open my github profile
open google
send message
play song on youtube
send email

'''
import pyttsx3 as ptx3 


grodd_eng = ptx3.init('sapi5')
voices = grodd_eng.getProperty('voices')

grodd_eng.setProperty('voices',voices[0].id)


class Engine:
	def speak(self,audio):
		
		grodd_eng.say(audio)
		print(audio)
		grodd_eng.runAndWait()

	def hear(self):
		cmd = sr.Recognizer()
		with sr.Microphone() as mic:
			print("Hanging on your every word...")
			cmd.pause_threshold = 1
			vocal = cmd.listen(mic,phrase_time_limit = 10,timeout = 5)

		try:
			print("Recognizing the words...")
			qry = cmd.recognize_google(vocal,language = 'en-in')
			print(f"The words: {qry}")
	
		except Exception as e:
			print(e)
			self.speak("Sorry sir, repeat it again.")
			return 'none'
		return qry 

	def wish(self):
		hr = int(dt.datetime.now().hour)
		if hr>=0 and hr<12:
			self.speak("Good Morning Sir.")
		elif hr>=12 and hr<18:
			self.speak("Good Afternoon Sir.")
		elif hr>=18 and hr<24:
			self.speak("Good Evening Sir.")
		
		self.speak("How can i help you ?")
	
	def sendemail(self,id,content):
		server = smptlib.SMTP('smtp.gmail.com',587)
		server.ehlo()
		server.starttls()
		server.login('opticremo@gmail.com','viswanath_123')
		server.sendmail('opticremo@gmail.com',to,content)
		server.close()

model = Engine()

if __name__ == '__main__':
	model.wish()

	while True:
		
		qry = model.hear().lower()

		if 'you' in qry:
			model.speak('Allow me to introduce myself, my name is Grodd. A Virtual Artificial Intelligence. I am here to assist you with a variety of tasks as best i can, 24 hours a day, 7 days a week.')
			model.speak('Importing all preferences from home Interface. Systems are now fully operationable. How can i Help You.')
		
		elif 'open opera' in qry:
			npath = "C:\\Users\\Viswanath Bodapati\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
			os.startfile(npath)

		elif 'open terminal' in qry:
			os.system('start cmd')

		elif 'start camera' in qry:
			cam = cv2.VideoCapture(0)
			for i in range(100000):
				ret,img = cam.read()
				cv2.imshow('webcam',img)
				k = cv2.waitKey(50)
				if k==27:
					break
			cam.release()
			cv2.destroyAllWindows()

		elif 'play music' in qry:
			m_dir = 'C:\\Users\\Viswanath Bodapati\\Music'
			songs = os.listdir(m_dir)
			for song in songs:
				if song.endswith('.mp3'):
					os.startfile(os.path.join(m_dir,song))

		elif 'ip address' in qry:
			ip = re.get('https://api.ipify.org').text
			model.speak(f'My Ip address is {ip}.')


		elif 'wikipedia' in qry:
			model.speak("According to wikipedia... ")
			query = qry.replace("wikipedia","")
			results = wikipedia.summary(query,sentences =2)
			model.speak(results)

		elif 'open youtube' in qry:
			webbrowser.open("www.youtube.com")

		elif 'open facebook' in qry:
			webbrowser.open("www.facebook.com")

		elif 'open my linkedin profile' in qry:
			webbrowser.open("https://www.linkedin.com/in/viswanath-bodapati-56944714a/")
		
		elif 'open my github profile' in qry:
			webbrowser.open("https://github.com/Viswanath-621")

		elif 'open google' in qry:
			model.speak('Sir, what should i search on google')
			cm = model.hear().lower()
			webbrowser.open(f'{cm}')

		elif 'send message' in qry:
			model.speak('To whom should i send the message sir.')
			num ='+91'+ str(model.hear())
			model.speak("please say me the message to be conveyed.")
			msg = model.hear()
			kit.sendwhatmsg(num,msg,2,25)

		elif 'play song on youtube' in qry:
			model.speak("which song should i play Sir")
			sn = model.hear()
			kit.playonyt(sn)
 
		elif 'send email' in qry:
			try:
				model.speak("To whom should i send the mail sir.")
				mail = model.hear().lower() + '@gmail.com'
				model.speak("What should be the body of the mail sir.")
				body = model.hear()
				sendemail(mail,body)
				model.speak("Mail has been sent .!!")
			
			except Exception as e:
				print(e)
				model.speak('Sorry sir, i am unable to send the email.')
		
		elif 'vishwanath' in qry:
			txt = "Viswanath Bodapati, known mononymously as Viswa, an Indian programmer, dancer, playback singer and philanthropist who works predominantly in solving the coding questions and also appeared in other college coding events. Referred to by fans and media as 'Master'."
			model.speak(txt)
		elif 'skanda' in qry:
			model.speak("he is a person who you value above other friends in your life, someone you have fun with, someone you trust and someone in whom you confide.")
		elif 'shutdown' in qry:
			model.speak("Good night sir, Shutting down.")
			sys.exit()

