import librosa 
import librosa.display
#%matplotlib inline
import matplotlib.pyplot as plt
path='1.wav'
x,sr=librosa.load(path,sr=44100)
print(x)
n0=0
n1=100
zcr = librosa.feature.zero_crossing_rate(y=x)
print(zcr)
import sklearn
spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0]
spectral_centroids.shape

frames = range(len(spectral_centroids))
t = librosa.frames_to_time(frames)
def normalize(x, axis=0):
    return sklearn.preprocessing.minmax_scale(x, axis=axis)

#librosa.display.waveplot(x, sr=sr, alpha=0.4)
plt.plot(t, normalize(spectral_centroids), color='r')
spectral_rolloff = librosa.feature.spectral_rolloff(x, sr=sr)[0]
librosa.display.waveplot(x, sr=sr, alpha=0.4)
plt.plot(t, normalize(spectral_rolloff), color='r')
mfccs = librosa.feature.mfcc(x, sr=sr)
print(mfccs.shape)

#badwidth
spectral_bandwidth_2 = librosa.feature.spectral_bandwidth(x+0.01, sr=sr)[0]
spectral_bandwidth_3 = librosa.feature.spectral_bandwidth(x+0.01, sr=sr, p=3)[0]
spectral_bandwidth_4 = librosa.feature.spectral_bandwidth(x+0.01, sr=sr, p=4)[0]
#print("bandwith"+spectral_bandwidth_2)
librosa.display.waveplot(x, sr=sr, alpha=0.4)
plt.plot(t, normalize(spectral_bandwidth_2), color='r')
plt.plot(t, normalize(spectral_bandwidth_3), color='g')
plt.plot(t, normalize(spectral_bandwidth_4), color='y')
plt.legend(('p = 2', 'p = 3', 'p = 4'))

#rms
print(librosa.feature.rms(y=x))

#bandwidth

bw=librosa.feature.spectral_bandwidth(y=x, sr=sr)
print(bw)

#tempo

onset_env = librosa.onset.onset_strength(y=x, sr=sr)
tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
print(tempo)

#beats

tempo, beats = librosa.beat.beat_track(y=x, sr=sr)
print(beats[:20])

