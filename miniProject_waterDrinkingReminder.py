from win10toast import ToastNotifier
import win32com.client
import time
toast = ToastNotifier()
speaker=win32com.client.Dispatch("SAPI.SpVoice")
while True:

 toast.show_toast(
    "Water Reminder",
    "hey Ronit drink water !!!!!",
    duration = 10,
    icon_path = "icon.ico",
    threaded = True,
 )
 speaker.speak("Hey Ronit drink water")
 time.sleep(10)