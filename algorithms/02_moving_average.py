
import random 
from typing import List

list = [random.randint(0, 9) for _ in range(16)]

def foo(x: List, k: int):
    y = []
    for i in range(len(x)-(k-1)):### index
    #for i in range(len(x)-1):### index
        temp = 0
        for j in range(i,i+k):
            temp = temp + x[j]
        temp = temp/k
        y.append(round(temp, 2))
    return y

if __name__ == '__main__':
    y = foo(list, 3)
    print(list, len(list))
    print(y, len(y))