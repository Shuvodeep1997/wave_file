import librosa 
import librosa.display
import numpy as np
import math
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
path='mot.wav'
c=0
l1=[]
arr=[[]]
x,sr=librosa.load(path,sr=44100)
#r,x= wavfile.read(path,mmap=False)
print("audio value in first frame: ")
print(x[1:100])
a=x[1:1000]
l=len(x)
i=8
flag=0
s=0
plt.title("Input Wave")
plt.plot(x)  
plt.show() 
arr=[]
l1=[]
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
ste=[[var**2 for var in i]for i in arr]
#print(ste)
i=0
ste1=[]
ste_max=[]
ste_med=[]
while(i<u):
    if(len(arr[i])>0):
        ste2=[var**2 for var in arr[i]]
        m=np.mean(ste2)
        q=np.median(ste2)
        n=max(ste2)
        ste1.append(m)
        ste_max.append(n)
        ste_med.append(q)
    #print(i)
    i=i+1
new_len=i
print(ste_max)
ul=len(ste1)
print("length of average values:- "+str(ul))
if(len(ste1)>0):
    m1=np.mean(ste1)
    m2=max(ste_max)
    m3=np.median(ste_med)
    print("peek value of avg value:-"+str(m1))
    print("peek value among max value:-"+str(m2))
    print("peek value among median value:-"+str(m2))
plt.title("average values")
plt.plot(ste1)  
plt.show()
plt.title("max values")
plt.plot(ste_max)  
plt.show()    
i=0
pts=[]
while(i<ul):
    if(ste_max[i]<=abs(m2) and ste_max[i]>=abs(m1)):
        pts.append(i)
    #if(ste1[i]<=abs(m1)*0.0000000001):
    #    pts.append(i)
    if(ste_med[i]>=(abs(m3)*0.00000000001) and ste_med[i]<=(abs(m3))*1.1111111111):
        pts.append(i)
    #print(i)
    i=i+1
clc=list(set(pts))
i=0
clc.sort()
print(clc)
fin_list=[]
while(i<len(clc)):
    fin_list+=arr[clc[i]]
    i=i+1
print(len(fin_list))
plt.title("Input Wave")
plt.plot(x)  
plt.show()  
plt.title("Output Wave")
plt.plot(fin_list)  
plt.show()  

y1=np.abs(librosa.core.stft(np.array(x)))
plt.title("Input frequency")
#f1=plt.figure(1)
#plt.subplot(210)
plt.plot(y1)
plt.show()
#y3=np.abs(librosa.core.stft(np.array(fin_list)))
#plt.title("Output frequency")
#g1=plt.figure(2)
#plt.subplot(221)
plt.plot(y3)
g1=plt.show()

fin_arr=np.array(fin_list)
data = np.random.uniform(-1,1,44100) 
scaled = np.int16(fin_arr/np.max(np.abs(data)) * 32767)
write('final.wav', 44100, scaled)
print("Done!!!!!!")
        
    

    
    



