import pyttsx3 as pyttsx

engine = pyttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)# 设置系统语音 0 汉语 1日语
engine.say("この番組はご覧のスポンサーの提供でお送りします")
engine.runAndWait()