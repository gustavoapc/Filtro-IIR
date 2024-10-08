import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt 

def iir_filter(x, a):
    y = np.zeros_like(x)
    for n in range(1, len(x)):
        y[n] = a * x[n] + (1 - a) * y[n-1]
    return y

filename = 'Welcome to the Jungle.wav' 
audio_data, sample_rate = sf.read(filename) 

if audio_data.ndim > 1:
    audio_data = audio_data[:, 0] 

a = 0.1 
filtered_audio = iir_filter(audio_data, a)


sf.write('Welcome to the Jungle 0.1.wav', filtered_audio, sample_rate)

time = np.arange(0, len(audio_data)) / sample_rate

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, audio_data, label='Áudio Original')
plt.title('Áudio Original')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(time, filtered_audio, label='Áudio Filtrado', color='orange')
plt.title('Áudio Filtrado (Com Filtro IIR)')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
