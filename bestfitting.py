import matplotlib.pyplot as plt
import numpy as np

points = [(1, 2), (2, 2.8), (3, 3.6), (4, 4.5), (5, 5.1)]  #points defined
#points=eval(input("Enter a list of coordinates"))         #user input of points
x=[i[0] for i in points]
y=[i[1] for i in points]
n=len(points)

m=(n*sum(x[i]*y[i] for i in range(n)) - (sum(x)*sum(y)))/(n*sum(x[i]**2 for i in range(n)) - sum(x)**2) #slope

c=(sum(y)-m*sum(x))/n   #intercept

print("y =",m,"x+",c)
xp=np.linspace(min(x),max(x),100)
yp=m*xp+c

plt.scatter(x,y)
plt.plot(xp,yp)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("BEst fitting line")
plt.show()

