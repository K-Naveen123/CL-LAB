import numpy as np
import matplotlib.pyplot as plt
frequency_1=3
amplitude_1=1.5
frequency_2=7
amplitude_2=0.8
num_samples=1000
t=np.arange(0,1,num_samples)
sinwave1=amplitude_1*np.sin(2*np.pi*frequency_1*t)
sinwave2=amplitude_2*np.sin(2*np.pi*frequency_2*t)
sinwave=sinwave1+sinwave2
plot(t,sinwave)
