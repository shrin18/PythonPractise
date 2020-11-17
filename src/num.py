import numpy as np
import matplotlib.pyplot as plt

'''x = np.linspace(0, 40, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.tan(x))       # Plot the sine of each x point
plt.show()
'''
x=np.arange(1,11)
y=2*x^2 + 5 + x^3

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(2,1,1)
plt.plot(x,y_sin)
plt.title('Sine')

plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('Cosine')

plt.title("Matplotlib")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y)
plt.show()

z = np.arange(0,3*np.pi, 0.1)
w = np.sin(x)
plt.title("Sine wave form")
plt.plot(z,w)
plt.show()

x1 = [5,8,10]
y1 = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.bar(x,y,align = 'center')
plt.bar(x2,y2, color = 'g', align= 'center')
plt.title('Bar graph')
plt.ylabel('y axis !')
plt.xlabel('x axis !')

plt.show()

