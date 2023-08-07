import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea
import os
sea.set()

def predict (X, w):
    """
        X is an input variable
        w is a weight
    """
    return X*w

def loss(X, Y, w):
    """
        why is it in ^2 -> becouse error always should be positive
    """
    return np.average((predict(X, w)-Y)**2)

def train(X, Y, iterations, lr, bias=False): 
  w = 0
  for i in range(iterations):
    current_loss = loss(X, Y, w)
    print("Iteration %4d => Loss: %.6f" % (i, current_loss))
    
    if loss(X, Y, w + lr) < current_loss: 
      w += lr
    elif loss(X, Y, w - lr) < current_loss: 
      w -= lr
    else:
      return w, np.round(current_loss,3)
      
  raise Exception("Couldn't converge within %d iterations" % iterations)


#training process. 
# we want to find the best approximation of the examples. 
# we want to find w from known X and Y

filename = f"../datasets/pizzas.txt"
print(os.path.isfile(filename))

X, Y = np.loadtxt(filename, skiprows=1, unpack=True)


plt.figure('Linear Regression')
plt.axis([0, 30, 0, 50])                                 # scale axes (0 to 50)
plt.xticks(fontsize=14)                                  # set x axis ticks
plt.yticks(fontsize=14)                                  # set y axis ticks
plt.xlabel("Reservations", fontsize=14)                  # set x axis label
plt.ylabel("Pizzas", fontsize=14)                        # set y axis label
plt.plot(X, Y, "bo", label='Ground Thruth')         

w = 0.8      
for i in range (16):                      # plot data
    w = w +0.2
    y = predict(X, w)
    error = np.average((y-Y)**2)
    plt.plot(X, predict(X, w), label = f"w={np.round(w,2)}, loss = {np.round(error,2)}")                                     # plot data

plt.legend()
print('Train')
w, current_loss = train(X, Y, iterations=10000, lr=0.01)
plt.figure('Linear Regression Training')

plt.plot(X, predict(X, w), "r-", label=f'train w={w}, loss={current_loss}')  
plt.plot(X, 
         Y, "bo", label='Ground Thruth')         
plt.legend()
plt.show()    
                                       # display chart
print('done')