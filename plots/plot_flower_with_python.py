import matplotlib.pyplot as plt
import math
import numpy as np

# set things
t = np.linspace(0, 75.4, 5000, endpoint = False)
x = []
y = []
for k in t:
    x_i = (3*np.cos(k)+2)*np.cos(k/12) - np.sin(k)*np.sin(k/12)
    y_i = (3*np.cos(k)+2)*np.sin(k/12) + np.sin(k)*np.cos(k/12)
    x.append(x_i)
    y.append(y_i)

# plot the graph
plt.plot(x,y)
plt.title('Nice plot')
Text(0.5, 1.0, 'Nice plot')

plt.show()
