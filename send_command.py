import speech_recognition as sr
import subprocess
import os
import signal
import Virtual_asistent as asistant
import time
import multiprocessing
from multiprocessing import Queue
import threading
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
from wikipedia_window import Wikipedia_show
#import weather
from weather import weather_GUI
#from youtube_search_GUI import yt_search
import youtube_search_GUI as yt_search_GUI
from youtube_search_GUI import yt_search
#from .other_GUIs import weather
#command:str
open_processes=[]
class Do_for_command:
	def __call__(args):
			try: 
				print('test:     '+args)
			except:
				print('')
	def __init__(self, command):

		print('WE HAVE IT')
		numbers_int=["1","2","3","4","5","6","7","8","9","10"]
		numbers_string=["one","two","three","four","five","six","seven","eight","nine","ten"]
		position=["first", "second","thirth","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]
		show_news=5
		if (" for " in command):
			command_search=command.split(" for ")[1]
		if (command!=""):
			if("forecast" in command or "weather" in command):
				if (command_search==""):
					'''for p in open_processes:
						if ("Open_forecast" in p):
							Open_forecast.terminate()'''
					Open_forecast=subprocess.Popen(["python3","weather.py"])
					open_processes.append("Open_forecast:"+str(Open_forecast.pid))
					print(Open_forecast.pid)
				else:
					'''for p in open_processes:
						if ("Open_forecast" in p):
							Open_forecast.terminate()'''
					#Open_forecast.terminate()
					print(command_search)
					#Open_forecast=threading.Thread(target=weather_GUI(command_search))
					#Open_forecast=multiprocessing.Process(target=weather_GUI(command_search))
					#Open_forecast.start()
					Open_forecast=subprocess.Popen(["python3","weather.py",command_search])
					open_processes.append("Open_forecast:"+str(Open_forecast.pid))
					print(Open_forecast.pid)
			elif ("who" in command or "was" in command or "what" in command):
				#subprocess.Popen(["python3","wikipedia_window.py", command])	
				wiki_command=command.split("who was ")[1]
				Open_wiki=threading.Thread(target=Wikipedia_show(wiki_command.replace(" ","_")))
				Open_wiki.start()
			elif ("youtube" in command):
				#if ("open" in command):
				#Openyt=multiprocessing.Process(target=youtube.yt())
				#Openyt.start()
				if ("search" in command):
					#Open_yt_search=subprocess.Popen(["python3","youtube.py", command_search])
					#open_processes.append("Open_yt_search")
					print('SEARCH YOUTUBE')
					try:
						yt_search_query=command_search
						Open_yt_search=threading.Thread(target=yt_search(yt_search_query))
						Open_yt_search.start()
					except Exception as e:
						print(e)
					#self.Frame.delete('1.0', END)
					#AskMirror=multiprocessing.Process(target=yt_search(self.Frame))
					#AskMirror.start()
				elif ("play" in command):
					Open_yt=subprocess.Popen(["python3","youtube_stream.py", command])
					open_processes.append("Open_yt")

			elif ("calibration" in command):
				Open_calibrate=subprocess.Popen(["python3", "calibrate.py", "test"], stdin=subprocess.PIPE)
				open_processes.append("Open_calibrate:"+str(Open_calibrate.pid))
			elif ("news" in command):
				#Open_news=threading.Thread(target=yt_search(yt_search_query))
				#Open_news.start()
				Open_news=subprocess.Popen(["python3", "news.py", str(show_news)])
				open_processes.append("Open_news:"+str(Open_news.pid))
			elif("picture" in command):
				if ("take" in command):
						take_pic=subprocess.Popen(["python3","tale_picture.py"])
						open_processes.append("take_pic:"+str(take_pic.pid))
			elif ("home" in command):
				for i in open_processes:
					if("Open_news" in i):
						Open_news.terminate()
						open_processes.remove(i)
					elif("Open_yt_search" in i):
						Open_yt_search.terminate()
						open_processes.remove(i)
					elif("Open_yt" in i):
						Open_yt.terminate()
						open_processes.remove(i)							
					elif("Open_calibrate" in i):
						Open_calibrate.terminate()
						open_processes.remove(i)
					else:
						continue
			'''elif(command in numbers_int or command in numbers_string or command in position):
				if (command in numbers_int):
					ni = numbers_int.index(command)
					print(yt_search_query)
					print(str(show_news-(5-int(ni))))
					if("Open_news" in open_processes[len(open_processes)-1]):
						Open_news=subprocess.Popen(["python3", "show_news.py", str(show_news-(5-int(ni)))])
					elif("Open_yt" in open_processes[len(open_processes)-1]):
						Open_yt=subprocess.Popen(["python3","youtube_stream.py", yt_search_query, str(ni)])
						
				elif (command in numbers_string):
					ns = numbers_string.index(command)
					print(str(show_news-(5-int(ns))))
					print(yt_search_query)
					if("Open_news" in open_processes[len(open_processes)-1]):
						Open_news=subprocess.Popen(["python3", "show_news.py", str(show_news-(5-int(ns)))])
					elif("Open_yt" in open_processes[len(open_processes)-1]):
						Open_yt=subprocess.Popen(["python3","youtube_stream.py", yt_search_query, str(ns)])
					
				elif (command in position):
					po = position.index(command)  	
					print(yt_search_query)
					print(str(show_news-(5-int(po))))
					if("Open_news" in open_processes[len(open_processes)-1]):
						Open_news=subprocess.Popen(["python3", "show_news.py", str(show_news-(5-int(po)))])
					elif("Open_yt" in open_processes[len(open_processes)-1]):
						Open_yt=subprocess.Popen(["python3","youtube_stream.py", yt_search_query, str(po)])
					
			elif ("close" in command):
				if("Open_news" in open_processes[len(open_processes)-1]):
					Open_news.terminate()
					open_processes.remove([len(open_processes)-1])
				elif("Open_yt_search" in open_processes[len(open_processes)-1]):
					Open_yt_search.terminate()
					#open_processes.remove([len(open_processes)-1])
					open_processes.remove("Open_yt_search")
				elif("Open_yt" in open_processes[len(open_processes)-1]):
					Open_yt.terminate()
					open_processes.remove("Open_yt")    								
				elif("Open_calibrate" in open_processes[len(open_processes)-1]):
					Open_calibrate.terminate()
					open_processes.remove([len(open_processes)-1])
				elif("take_pic" in open_processes[len(open_processes)-1]):
						take_pic.terminate()
						open_processes.remove([len(open_processes)-1])
			elif ("next" in command):
				if("Open_news" in open_processes[len(open_processes)-1]):
					Open_news.terminate()
					Open_news=subprocess.Popen(["python3", "news.py", show_news+5])
					show_news=show_news+5			
			else:
				AskMirror=multiprocessing.Process(target=asistant.jarvis(command))
				AskMirror.start()'''
				#AskMirror.join()
				#subprocess.Popen(["python3","Virtual_asistent.py", command])