import numpy as np
import matplotlib.pyplot as plt

f_max = 100000
f_c = 2E3
omega_0 = 2*np.pi*f_c
L = 40E-3 # H
C = 1/(L*omega_0)**2
Q = 10**(0.5/20) # valeur minimale de Q
R = 1/Q*np.sqrt(L/C) # valeur maximale de R

def gain(omega) :
    return 1/np.sqrt((1-(omega/omega_0)**2)**2+Q**2*(omega/omega_0)**2)

def gain_dB(omega) :
    return 20*np.log10(gain(omega))

f = np.linspace(0,f_max,10000)

G = gain(2*np.pi*f)
G_dB = gain_dB(2*np.pi*f)

plt.semilogx(f,G_dB, color='red')
plt.xlabel('fréquence (en Hz)')
plt.ylabel('Gain (en dB)')
plt.hlines(-0.5,0,100000,ls='dashed',color='C1') # -0.5 dB
plt.hlines(-10,0,100000,ls='dashed',color='C1') # -10 dB
plt.vlines(f_c,min(G_dB),max(G_dB),ls='dashed',color='C1') # f_c
plt.vlines(2*f_c,min(G_dB),max(G_dB),ls='dashed',color='C1') # 2 f_c
plt.fill((2*f_c,f_max,f_max,2*f_c),(max(G_dB),max(G_dB),-10,-10),color='C1', alpha=0.3)
plt.fill((0,f_c,f_c,0),(min(G_dB),min(G_dB),-0.5,-0.5),color='C1', alpha=0.3)
plt.show()
