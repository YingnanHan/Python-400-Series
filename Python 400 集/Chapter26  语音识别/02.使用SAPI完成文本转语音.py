from win32com.client import  Dispatch

speaker = Dispatch("SAPI.SpVoice")
speaker.Speak("你好")
del speaker