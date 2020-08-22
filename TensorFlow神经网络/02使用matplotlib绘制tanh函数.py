import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = np.tanh(x)
plt.plot(x, y)
plt.show()
