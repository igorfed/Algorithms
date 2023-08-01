import numpy as np
filename = f"../datasets/pizzas.txt"
X, Y = np.loadtxt(filename, skiprows=1, unpack=True)
print('done')