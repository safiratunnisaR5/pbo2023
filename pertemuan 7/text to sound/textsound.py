from gtts import gTTS 
from playsound import playsound

mytext = 'Selamat Hari Natal dan Tahun Baru!'
language = 'id'
myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("selamat.mp3") 
playsound("selamat.mp3", True)