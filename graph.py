import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile as wav
rate, data = wav.read('./Desktop/wave_file/4.wav')
#%matplotlib inline
#%matplotlib inline
#plt.plot(data)
#plt.show()
print(data)
time=np.arange(0,len(data))/44100
print(time)

fig,ax=plt.subplots()
ax.plot(time,data)
plt.show()
