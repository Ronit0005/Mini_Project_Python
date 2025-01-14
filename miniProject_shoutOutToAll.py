import win32com.client 
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
l=['Ronit','Rishi','Rahul','Ritik','Abhishek','Sakshi','tanisha']
nl=list(map(lambda x:'shout out to '+x,l))
for s in nl:
  speaker.Speak(s) 