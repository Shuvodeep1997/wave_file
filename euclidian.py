import librosa 
import librosa.display

from scipy.io import wavfile
import math
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import numpy as np


def calEnergy(wave_data) :
    energy = []
    sum = 0
    for i in range(len(wave_data)) :
        sum = sum + (int(wave_data[i]) * int(wave_data[i]))
        if (i + 1) % 256 == 0 :
            energy.append(sum)
            sum = 0
        elif i == len(wave_data) - 1 :
            energy.append(sum)
    return energy

def square1(arr):
    sqarr=[num**2 for num in arr]
    m1=np.max(sqarr)
    return m1


#%matplotlib inline
#import matplotlib.pyplot as plt
path='male.wav'
c=0
l1=[]
arr=[[]]
x,sr=librosa.load(path,sr=44100)
#r,x= wavfile.read(path,mmap=False)
#print("audio value: ")
print(x[1:100])
l=len(x)
i=8
s=0
flag=0
print("length of audio:"+str(l))
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
    #print("done")    
print(l1)
print("count")
#print(s)
res= np.array(arr[1])
rl=len(res)
print("length of audio: "+str(rl))
i=1
while(i<=s):
    data = np.random.uniform(-1,1,44100) 
    scaled = np.int16(arr[i]/np.max(np.abs(data)) * 32767)
    s1="test"+str(i)+".wav"
    write(s1, 44100, scaled)
    i=i+1
    #print(i)
#i=1
#seg=[[[]]]
#while(i<=s):
#    leng=len(arr[i])
#    ren=int(leng/100)
#    rim=ren*100
#    j=1
#    while(j<=rim):
#        k=1
#        r=1
#        seg[i].append([])
#        while(k<=100):
#            
#            val=arr[i][j]
#            seg[i][r].append(val)
#            j=j+1
#            k=k+1
#            print(i)
#            print(j)
#            print(r)
#        r=r+1
#    i=i+1
seg = []
for i in range(len(arr)):
	seg1 = []
	k1 = math.ceil(len(arr[i])/100) 
	for j in range(k1):
		seg1.append(arr[i][j*100:(j+1)*100])
	seg1.append(arr[i][k1*100:])
	seg.append(seg1)
#print(arr[1][1])
#print(len(seg[5]))
i=0
print("segmentation ")
zcr=[[]]
mfcc=[[]]
while(i<=s):
    o=len(seg[i])
    j=1
    print("segmentation="+str(i))
    #print(o)
    zcr.append([])
    mfcc.append([])
    while(j<o-1):
        zcr1=librosa.feature.zero_crossing_rate(y=np.array(seg[i][j]))
        zcr[i].append(np.mean(zcr1))
        mf1=librosa.feature.mfcc(y=np.array(seg[i][j]))
        mfcc[i].append(np.mean(mf1))
        #print(j)
        j=j+1
    i=i+1 
    #print(i)
print(len(zcr))
print("eucledian")
i=0
ed=[[]]
while(i<=s):
    o=len(zcr[i])
    j=1
    ed.append([])
    while(j<o-1):
        ed1=(((mfcc[i][j+1]-mfcc[i][j])**2)+((zcr[i][j+1]-zcr[i][j])**2))**0.5
        ed[i].append(ed1)
        j=j+1
    i=i+1
    print(i)
print("lenghth"+str(len(ed)))
ed_len=len(ed)
ed_sin=[]
i=0
print("2d to 1d")
while(i<l-1):
    ed_sin+=ed[i]
    i=i+1
    print(i)
plt.title("euclidian  coff values")
plt.plot(ed_sin)  
plt.show()
#win=[]
pts=[[]]
i=0
while(i<=s):
    if(len(ed[i])>0):
        max1=np.max(ed[i])
        m1=max1*0.8
        o=len(ed[i])
        j=1
        k=1
        pts.append([])
        while(j<o):
            if(ed[i][j]>=m1):
                pts[i].append(j)
                j=j+8
            j=j+1
    i=i+1
print(pts[1])        
i=1
q=0
print(" ")
print(" ")
print(" ")
#win=[[[]]]
#while(i<=s):
#    l=len(arr[i])
#    l1=len(pts[i])
#    k=0
#    print("length of audio"+str(l))
#    print("length of points"+str(l1))
#    win.append([])
#    print("i value"+str(i))
#    while(k<l1):
#        tak=pts[i][k]
#        win[i-1].append([])
#        print("point value="+str(tak))
#        while(q<=(tak*100)):
#            print("entering insert zone="+str(q))
#            var=x[i][q]
#            
#            win[i-1][k].append(x[i][q])
#            q=q+1
#            print("q value"+str(q))
#        k=k+1
#        print("k value"+str(k))
#        if(k>l1):
#            print("enter remaing zone !!!!!!")
#            while(q<l1):
#                win[i][k].append(5)
#                q=q+1
#    i=i+1
#    print("i value exit zone"+str(i))
res2=[[var*100 for var in i]for i in pts]
print("slicing starts!!!!!!!!")
print(type(res2))


win =[]
for i in range(0,s+1):
    print(i)
    win1 = []
    pt = [1]
    print(pt)
    pt += res2[i]
    pt.append(len(arr[i]))
    print(pt)
    for j in range(0, len(pt)):
        win1.append(arr[i][pt[j-1]:pt[j]])
    win.append(win1)
#print(win[0])

print(len(win[0]))

i=0
STE=[]
while(i<len(win)):
    lengt=len(win[i])
    j=0
    print(j)
    print(i)
    STE.append([])
    while(j<lengt):
        co=0
        lo=len(win[i][j])
        STE[i].append(square1(win[i][j])) 
        j=j+1
    i=i+1
            
        
        
#    i=i+1
print(STE)
#    
y1=np.abs(librosa.core.stft(np.array(win[0][0])))
plt.title("frequency1")
f1=plt.figure(1)
#plt.subplot(210)
plt.plot(y1)
f1.show()
y3=np.abs(librosa.core.stft(np.array(win[0][1])))
plt.title("frequency2")
g1=plt.figure(2)
#plt.subplot(221)
plt.plot(y3)
g1=plt.show()


y2=librosa.feature.mfcc(np.array(win[0][0]))
print(len(y2))
print(librosa.get_duration(np.array(win[0][0]),sr))
print(len(librosa.feature.spectral_contrast(y=np.array(win[0][0]))))
print(librosa.feature.spectral_flatness(y=np.array(win[0][0])))

RMS=[]
i=0
while(i<len(win)):
    lengt=len(win[i])
    j=0
    print(j)
    print(i)
    RMS.append([])
    while(j<lengt):
        co=0
        lo=len(win[i][j])
        RMS[i].append(np.max(librosa.feature.rms(y=np.array(win[i][j]))))
        j=j+1
    i=i+1
print(RMS)
m1=np.max(np.max(STE))
m2=np.max(np.max(RMS))
i=0
print("max value!!!!")
print(m1)
counter=[]
while(i<len(win)):
    lengt=len(win[i])
    j=0
    while(j<lengt):
        if(STE[i][j]>(m1*0.8)):
            counter.append(i)
        if(RMS[i][j]>m2*0.8):
            counter.append(i)
        j=j+1
    i=i+1
clc=list(set(counter))
print(type(clc))
i=0
fin_list=[]
while(i<len(clc)):
    fin_list+=arr[clc[i]+1]
    i=i+1
print(len(fin_list))
fin_arr=np.array(fin_list)
data = np.random.uniform(-1,1,44100) 
scaled = np.int16(fin_arr/np.max(np.abs(data)) * 32767)
write('final.wav', 44100, scaled)
print("Done!!!!!!")
                 
            
















            
            
            
                        
    

    
    