import matplotlib.pyplot as p
import numpy as n
y=0
x=n.linspace(0,20,1000)
for k in range(1,10,1): 
    y+=4*n.sinc((2*k-1)*x)/((2*k-1)*n.pi);
p.plot(x,y,'k',color=(0.7,0,1),label="Fourier",linewidth=1.5)
p.axis([0,22.5,-1.5,4])
p.legend()
p.show()   



