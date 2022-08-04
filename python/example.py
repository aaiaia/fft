# blog: https://kcal2845.tistory.com/35
# github: https://github.com/kcal2845
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim((0,6000))  #ax.set_xlim((0,5000))
ax.set_ylim((0,5000))  #ax.set_ylim((0,10000))
line, = ax.plot([], [],c='k',lw=1)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    data = np.frombuffer(stream.read(CHUNK),dtype=np.int16)
    n = len(data)
    x = np.linspace(0,RATE/2,int(n/2))
    y = np.fft.fft(data)/n
    y = np.absolute(y)
    y = y[range(int(n/2))]
    line.set_data(x, y)
    return line,

CHUNK = 2000
RATE = 8000

p=pyaudio.PyAudio()
#stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
#              frames_per_buffer=CHUNK,input_device_index=2)
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

animation = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=10, blit=True)


plt.show()
