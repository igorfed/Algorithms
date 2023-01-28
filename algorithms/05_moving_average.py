from typing import List, Tuple

def moving_average(arr: List[int], window_size: int) -> List[float]:
    y = []
    for i in range(len(arr)-(window_size-1)):
        sum = 0
        for j in range(i,i+window_size):
            sum = sum + arr[j]
        
        y.append(sum/window_size)
    return y


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size

arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))