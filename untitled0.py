from scipy.io import wavfile
import math
import matplotlib.pyplot as plt

fName = './Desktop/wave_file/4.wav'
 
fs, signal = wavfile.read(fName)
signal = signal / max(abs(signal))                        
assert min(signal) >= -1 and max(signal) <= 1
print ('fs           ==> ', fs, 'Hz')                     
print ('len(signal)  ==> ', len(signal), 'samples')

assert fs % 1000 == 0
 
sampsPerMilli = int(fs / 1000)
millisPerFrame = 20
sampsPerFrame = sampsPerMilli * millisPerFrame
nFrames = int(len(signal) / sampsPerFrame)       
 
print ('samples/millisecond  ==> ', sampsPerMilli)
print ('samples/[%dms]frame  ==> ' % millisPerFrame, sampsPerFrame)
print ('number of frames     ==> ', nFrames)

fc = 20
a = math.exp(-fc * 2 * math.pi / fs)
STEs = []
for n in range(len(signal)):
    if n == 0:
         STEs.append(a * 0 + signal[n] ** 2)          
    else:
         STEs.append(a * STEs[n - 1] + signal[n] ** 2)
print(STEs)
 
plt.plot(STEs)
plt.title('Short-Time Energy')
plt.ylabel('ENERGY')
plt.xlabel('SAMPLE')
pyplot.autoscale(tight='both');