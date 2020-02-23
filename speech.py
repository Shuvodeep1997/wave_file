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
print(len(res))
data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1
scaled = np.int16(arr[1]/np.max(np.abs(data)) * 32767)
write('test.wav', 44100, scaled)

#p=np.ndarray(shape=(324208,),dtype=float)
#segmentation
print("segmentation")
cent = librosa.feature.spectral_centroid(y=res, sr=sr)
#print(cent)
print("contrast value")
S = np.abs(librosa.stft(res))
contrast = librosa.feature.spectral_contrast(S=S, sr=sr)
l=len(contrast[0])
print("no of segents: ")
print(int(len(res)/l))


plt.title("Signal Wave")
plt.plot(res)
plt.show()
print("Segmentation by STE")
#print(x[:1000])
seg=[[]]
c=1
n=1
k=1
while n<len(res)-5:
    if ((res[n]**2+res[n+1]**2+res[n+2]**2+res[n+3]**2+res[n+4]**2+res[n+5]**2)<0.0000001):
        d=n
        c=c+1
        print(n)
        n=n+6
        k=1
    else:
        #seg[c][k]=res[n]
        
        k=k+1;
        
    n=n+1;
print("no. of segments")
print(c)
print(3**2)

#plt.figure()
#plt.subplot(2, 1, 1)
#librosa.display.specshow(librosa.amplitude_to_db(S,ref=np.max),y_axis='log')
#plt.colorbar(format='%+2.0f dB')
#plt.title('Power spectrogram')
#plt.subplot(2, 1, 2)
#librosa.display.specshow(contrast, x_axis='time')
#plt.colorbar()
#plt.ylabel('Frequency bands')
#plt.title('Spectral contrast')
#plt.tight_layout()
#plt.show()
