import numpy as np
import matplotlib.pyplot as plt

def f(x,E,I):
    return (1/(12*E*I))*(-x**4+10*x**3-125*x)

L=5
E=5e4
a=0.5              
b=1-a            
I=(1/12)*b*a**3
x0=0
xN=L
N=10
h=(xN-x0)/N
x = np.linspace(x0,xN,N+1)
xx = np.linspace(x0+h,xN-h,N-1)
y1 = f(x,E,I)
M=5*xx-xx**2
f=(h**2)*(M/(E*I))
A=np.zeros((N-1,N-1))

for i in range(N):
    if i==0:
        A[i][i]=-2
        A[i][i+1]=1
    elif i==N-2:
        A[i][i]=-2
        A[i][i-1]=1
    elif i==N-1:
        None
    else:
        A[i][i]=-2
        A[i][i-1]=1
        A[i][i+1]=1
        
y = np.linalg.solve(A,f)
y = np.append(y,0)
y = y.tolist()
y[:0] = [0.0]
plt.plot(x,y,label='Diferencias finitas')
plt.plot(x,y1,label='Solución analítica')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()