import soundcard as sc



usbsp=sc.get_speaker('USB Audio Device')
usbmic=sc.get_microphone('USB Audio Device')

with usbmic.recorder(samplerate=48000) as mic, \
      usbsp.player(samplerate=48000) as sp:
    for _ in range(100):
        data = mic.record(numframes=1024)
        sp.play(data)
   
print(type(data)) 
for i in range(50):
    print(i) #print ลำดับ
    print(data[i][0])
