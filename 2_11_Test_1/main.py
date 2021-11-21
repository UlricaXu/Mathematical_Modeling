import matplotlib.pyplot as plt
import numpy as np
ax = plt.axes(projection='3d')
s = np.linspace(-1, 1, 1000)
t = np.linspace(0, 2 * np.pi, 1000)
x = (2 + s / 2 * np.cos(t / 2) * np.cos(t))
y = (2 + s / 2 * np.cos(t / 2) * np.sin(t))
z = s / 2 * np.sin(t / 2)
ax.plot3D(x, y, z,  'gray')
plt.title("Figure Of Möbius strip")
plt.show()
