import win32com.client 
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
l=['light','camera','fashion']
nl=list(map(lambda x:x,l))
for s in nl:
  speaker.Speak(s) 