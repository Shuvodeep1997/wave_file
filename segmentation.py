import librosa 
import librosa.display

from scipy.io import wavfile
#import math
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import numpy as np
#%matplotlib inline
#import matplotlib.pyplot as plt
path='male.wav'
c=0
l1=[]
arr=[[]]
x,sr=librosa.load(path,sr=44100)
#r,x= wavfile.read(path,mmap=False)
print("audio value: ")
print(x.ndim)
l=len(x)
i=8
s=1
print(l)
while i<=l:
    arr.append([])
    if abs(x[i-7])<0.0001 and abs(x[i-6])<0.0001 and abs(x[i])<0.0001 and abs(x[i-5])<0.0001 and abs(x[i-4])<0.0001 and abs(x[i-3])<0.0001 and abs(x[i-2])<0.0001 and abs(x[i-1])<0.0001:
       c=c+1
       s=s+1
       l1.append(i)
    else:
        arr[s].append(x[i-7])
        arr[s].append(x[i-6])
        arr[s].append(x[i-5])
        arr[s].append(x[i-4])
        arr[s].append(x[i-3])
        arr[s].append(x[i-2])
        arr[s].append(x[i-1])
        arr[s].append(x[i])
    i+=8    
print(l1)
print("count")
res= np.array(arr[1])
rl=len(res)
print("length of audio: "+str(rl))
data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1
scaled = np.int16(arr[1]/np.max(np.abs(data)) * 32767)
write('test.wav', 44100, scaled)

zcr = librosa.feature.zero_crossing_rate(y=res)
print("ZCR values")
#print(zcr[0][634])
print("length of ZCR: "+str(len(zcr[0])))
ed=[0]*632
#eucledean distance
i=1
while(i<632):
    ed[i]=(((zcr[0][i+1]-zcr[0][i])**2)+(((res[i+1]**2)-(res[i]**2))**2))**0.5
    i=i+1
print(ed)  
fed=np.array(ed)
plt.title("Eucledean distance")
plt.plot(ed)  
plt.show()
i=1
c=0
while(i<631):
    if(ed[i+1]<ed[i]):
        c=c+1
    i=i+1
print("no of segments")
print(c)      

    
    


