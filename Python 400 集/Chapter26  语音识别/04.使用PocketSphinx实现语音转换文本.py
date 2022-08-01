import speech_recognition as sr

#预备待识别文件
audio_file = "demo_audio.wav"
#生成一个语音识别对象
r = sr.Recognizer()
#打开语音文件
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)

#将语音转化为文本
print("本文内容为\n")
print(r.recognize_sphinx(audio,language="zh-CN"))#指定语言