from comtypes.client import CreateObject
from comtypes.gen import SpeechLib

engine=CreateObject('SAPI.SpVoice')
stream=CreateObject('SAPI.SpFileStream')
infile='demo.txt'
outfile='demo_audio.wav'

stream.open(outfile,SpeechLib.SSFMCreateForWrite)
engine.AudioOutputStream=stream

#读取文本内容
f=open(infile,'r',encoding='utf-8')
theText=f.read()

f.close()
engine.speak(theText)
stream.close()