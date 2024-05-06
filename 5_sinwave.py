import numpy as np
import matplotlib.pyplot as plt
frequency=5
amplitude=1
num_sample=1000
t=np.linspace(0,1,num_sample)
sinwave=amplitude*np.sin(2*np.pi*frequency*t)
plt.plot(t,sinwave)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("sinwave")
plt.show()
