from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy
x = read('./Desktop/wave_file/4.wav')
time=numpy.array(x[1],dtype=float)/44100
print(x)