import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea
import os
sea.set()

def predict (X, w, b):
    """
        X is an input variable
        w is a weight
        b is a bias
    """
    return X*w+b

def loss(X, Y, w, b):
    """
        why is it in ^2 -> becouse error always should be positive
    """
    return np.average((predict(X, w, b)-Y)**2)

def train(X, Y, iterations, lr):
    w = b = 0
    for i in range(iterations):
        current_loss = loss(X, Y, w, b)
        if i % 300 == 0:
            print("Iteration %4d => Loss: %.6f" % (i, current_loss))

        if loss(X, Y, w + lr, b) < current_loss: # Updating weight
            w += lr
        elif loss(X, Y, w - lr, b) < current_loss: # Updating weight
            w -= lr
        elif loss(X, Y, w, b + lr) < current_loss: # Updating bias
            b += lr
        elif loss(X, Y, w, b - lr) < current_loss: # Updating bias
            b -= lr
        else:
            return w, b, np.round(current_loss,3)

    raise Exception("Couldn't converge within %d iterations" % iterations)

filename = f"../datasets/pizzas.txt"
print(os.path.isfile(filename))

X, Y = np.loadtxt(filename, skiprows=1, unpack=True)

# Train the system
w, b, current_loss = train(X, Y, iterations=10000, lr=0.01)
print("\nw=%.3f, b=%.3f" % (w, b))

# Predict the number of pizzas
print("Prediction: x=%d => y=%.2f" % (20, predict(20, w, b)))

plt.figure('Linear Regression Training')

plt.plot(X, predict(X, w, b), "r-", label=f'w={w}, b={b}, loss={current_loss}')  
plt.plot(X, 
         Y, "bo", label='Ground Thruth')         
plt.legend()
plt.show()    