import numpy as np
import matplotlib.pyplot as plt
def unit_impulse(a, n):
    delta =[]
    for sample in n:
        if sample == a:
            delta.append(1)
        else:
            delta.append(0)
              
    return delta
  
a = 0 # Enter delay or advance
UL = 10
LL = -10
n = np.arange(LL, UL, 1)
d = unit_impulse(a, n)

plt.figure(1)
plt.stem(n, d)
plt.xlabel('n')
plt.xticks(np.arange(LL, UL, 1))
plt.yticks([0, 1])
plt.ylabel('\u03B4[n]')
plt.grid(True,which='both')
plt.title('Unit Impulse: \u03B4[n]')
plt.savefig("Unit Impulse1.png")

plt.figure(2)
plt.plot(n, d)
plt.xlabel('t')
plt.xticks(np.arange(LL, UL, 1))
plt.yticks([0, 1])
plt.ylabel('\u03B4[t]')
plt.grid(True,which='both')
plt.title('Unit Impulse: \u03B4[t]')
plt.savefig("Unit Impulse2.png")