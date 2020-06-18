import librosa 
import librosa.display

from scipy.io import wavfile
import math
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import numpy as np
#%matplotlib inline
#import matplotlib.pyplot as plt
path='long.wav'
c=0
l1=[]
arr=[[]]
x,sr=librosa.load(path,sr=44100)
#r,x= wavfile.read(path,mmap=False)
print("audio value: ")
print(x.ndim)
l=len(x)
i=8
flag=0
s=0
print(l)
while(i<l):
    arr.append([])
    if abs(x[i-7])<0.00001 and abs(x[i-6])<0.00001 and abs(x[i])<0.00001 and abs(x[i-5])<0.00001 and abs(x[i-4])<0.00001 and abs(x[i-3])<0.00001 and abs(x[i-2])<0.00001 and abs(x[i-1])<0.00001 and flag==0:
       c=c+1
       s=s+1
       flag=1
       l1.append(i)
    elif abs(x[i-7])>0.00001 or abs(x[i-6])>0.00001 or abs(x[i])>0.00001 or abs(x[i-5])>0.00001 or abs(x[i-4])>0.00001 or abs(x[i-3])>0.00001 or abs(x[i-2])>0.00001 or abs(x[i-1])>0.00001:
        #print("s value"+str(s))
        arr[s].append(x[i-7])
        arr[s].append(x[i-6])
        arr[s].append(x[i-5])
        arr[s].append(x[i-4])
        arr[s].append(x[i-3])
        arr[s].append(x[i-2])
        arr[s].append(x[i-1])
        arr[s].append(x[i])
        flag=0
    i+=8
print("points are: ")
print(l1)
print("values are:" )
print(arr[1])
u=len(arr)
print("length of array"+str(u))
i=1
while(i<=s):
    data = np.random.uniform(-1,1,44100) 
    scaled = np.int16(arr[i]/np.max(np.abs(data)) * 32767)
    s1="long"+str(i)+".wav"
    write(s1, 44100, scaled)
    i=i+1
#i=1
seg = []
for i in range(len(arr)):
	seg1 = []
	k1 = math.ceil(len(arr[i])/100) - 1
	for j in range(k1):
		seg1.append(arr[i][j*100:(j+1)*100])
	seg1.append(arr[i][k1*100:])
	seg.append(seg1)
#zcr = librosa.feature.zero_crossing_rate(y=res)
#print("ZCR values")
#print(zcr[0][633])
#print("length of ZCR: "+str(len(zcr[0])))
#ns=ns*100
#print(ns)
#res1=[[]]
#k=1
#i=1
##print(x[1])
#while(i<=ns):
#    #print(i)
#    res1.append([])
#    j=1
#    while(j<=100):
#        #print(j)
#        #print(i)
#        #print(k)
#        res1[k].append(x[i])
#        j=j+1
#        i=i+1
#    k=k+1
    #i=i+1
    #print(k)
zcr_seg=[[]]
shr_seg=[[]]
shr_adj=[[]]
shr_plus=[[]]
#res2=[[]*k]*101
i=0
#print("k value"+str(k))
#print("i value:")
#while(i<k):
#    res2[i]=np.array(res1[i])
while(i<=s):
    o=len(seg[i])
    j=0
    zcr_seg.append([])
    shr_seg.append([])
    shr_adj.append([])
    shr_plus.append([])
    while(j<o-1):
        z1=np.mean(librosa.feature.zero_crossing_rate(y=np.array(seg[i][j])))
        zcr_seg[i].append(z1)
        s1=(np.mean(np.square(np.array(seg[i][j]))))
        shr_seg[i].append(s1)
        s2=(np.mean(np.square(np.array(seg[i][j+1]))))
        shr_adj[i].append(s2)
        s3=(np.mean(np.square(np.array(seg[i][j]+seg[i][j+1]))))
        shr_plus[i].append(s3)
        j=j+1
    i=i+1
    #print(i)
print("energy")
print(shr_seg)    
print(len(shr_seg))

#i=1
#while(i<k):
#    shr_seg.append(np.mean(np.square(np.array(res1[i]))))
#    i=i+1
#i=1
#zcr_adj=[]
#while(i<k-1):
#    zcr2=librosa.feature.zero_crossing_rate(y=np.array(res1[i]+res1[i+1]))
#    zcr_adj.append(np.mean(zcr2))
#    i=i+1
#print(zcr_adj)
##print("bic value")
##bic cofficient
bic_coff=[]
i=0
while(i<=s):
    #print(i)
    o=len(seg[i])
    #print("length:-"+str(o))
    j=0
    while(j<o-1):
        #print("i-value"+str(i))
        #print("j value"+str(j))
        s1=200*np.log(np.absolute(shr_plus[i][j]))
        s2=100*np.log(np.absolute(shr_seg[i][j]))
        s3=100*np.log(np.absolute(shr_adj[i][j]))
        bic1=(100*np.log(np.absolute(shr_plus[i][j])))-(50*np.log(np.absolute(shr_seg[i][j])))-(50*np.log(np.absolute(shr_adj[i][j])))
        bic_coff.append(bic1)
        j=j+1
    i=i+1
    
print("bic values")
print(bic_coff)
plt.title("bic coff values")
plt.plot(np.absolute(bic_coff))  
plt.show()
i=0
bic_len=len(bic_coff)
maxy=0

        
    
    
    


    
 
    
    


