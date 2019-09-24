from scipy.io import wavfile
import math
import statistics
import numpy
import matplotlib.pyplot as plt

fName = './Desktop/wave_file/4.wav'
 
fs, signal = wavfile.read(fName)
signal = signal / max(abs(signal))                        
assert min(signal) >= -1 and max(signal) <= 1
print ('sampling freq= ', fs)                     
print ('total samples= ', len(signal))

assert fs % 1000 == 0
 
sampsPerMilli = int(fs / 1000)
millisPerFrame = 20
sampsPerFrame = sampsPerMilli * millisPerFrame
nFrames = int(len(signal) / sampsPerFrame)       
 
print ('samples/ms= ', sampsPerMilli)
print ('samples/[%dms]frame= ' % millisPerFrame, sampsPerFrame)
print ('number of frames= ', nFrames)


DC = statistics.mean(signal)
newSignal = signal - DC
ZCCs = []                                     
for i in range(nFrames):
    startIdx = i * sampsPerFrame
    stopIdx = startIdx + sampsPerFrame
    s = newSignal[startIdx:stopIdx]            
    ZCC = 0
    for k in range(1, len(s)):
        ZCC += 0.5 * abs(numpy.sign(s[k]) - numpy.sign(s[k - 1]))
    ZCCs.append(ZCC)
    
plt.plot(ZCCs)
plt.title('Short-Time Zero Crossing Counts')
plt.ylabel('ZCC')
plt.xlabel('FRAME')