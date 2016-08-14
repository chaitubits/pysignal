# from __future__ import division
# 
# This is my first program in trying to learn how to use python for Signal Processing.
# A discrete time representation of a sinewave of freuency 'f' sampled at frequency 'fs' 
# is represented as sin(2*pi*f*1/fs*n) where 'n' is the sample number.
# So, in order to generate a sine wave of frequency 100Hz and sampled at 400Hz, for a time of 
# 1 sec. we set n = 1:400.
# 
# One important lesson I learnt when writing this script is about the __future__ module.
# The division by default in python 2.7 depends on the value of the variable, 
# meaning that, the result is a float iff either one of the variables is a float.
# I made a mistake by defining the frequency 'f' below as 100 an 'int' and not 100.0 
# hence the timeperiod and correspondingly the time variables all ended up being zeros.
# I have implemented the sinewave generation in two different ways.
  
import numpy as np
import matplotlib.pyplot as plt



n = np.linspace(0, 20, 21)
f = 100.0
fs = 1000
y = np.sin(2* np.pi * f * 1/fs * n)

figure01 = plt.subplot(211) 
plt.plot(n, y)
plt.xlabel('number of samples(n)')
plt.ylabel('amplitude')

fs = 1000
f = 100.0
time_period = 1/f
time = time_period*2

t = np.linspace(0, time, 500, endpoint=True)
#print t[1:10]
y1 = np.sin(2* np.pi * f * t )
#print y1[1:10]
axes1 = plt.subplot(212)
#figure01 = plt.figure(figsize=(10,4))
#axes1 = figure01.add_axes([0.1, 0.1, 0.8, 0.8])
axes1.set_ylim([-1, 1])
axes1.set_xlim([0, np.max(t)])
print np.max(t)
axes1.set_xticks(np.linspace(0, np.max(t), 7, endpoint=True))
axes1.plot(t,y1)
print 2*np.pi*f*np.arange(0, np.max(t), 0.005)
axes1.set_xticklabels(np.linspace(0, 20, 7), fontsize=14)
axes1.set_yticks([-1, -0.5, 0, 0.5, 1])
axes1.set_yticklabels([-1, -0.5, 0, 0.5, 1], fontsize=14)

axes1.set_xlabel("time (ms)", fontsize=18)
axes1.set_ylabel("amplitude", fontsize=18)

plt.show()



