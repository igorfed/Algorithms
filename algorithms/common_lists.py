from typing import List, Tuple, Optional

def remove_even(lst: List[int])-> List[int]:
    '''
    Remove Even Integers from List 
    in: my_list = [1,2,4,5,10,6,3]
    out: my_list = [1,5,3]
    '''
    print('[INFO]: remove even elements')
    #temp = []
    #for i in lst:
    #    if (i%2)==1:
    #        temp.append(i)
    #return temp
    return [i for i in lst if i % 2 != 0]
    
print(remove_even([23, 10, -109, -44, 98, 21]))

def merge_lists(lst1: List[int], lst2: List[int])-> List[int]:
    '''
    Merge two sorted Lists
    in: list1 = [1,3,4,5]  
        list2 = [2,6,7,8]
    out: [1,2,3,6,4,7,5,8]
    '''
    #temp = lst1 + lst2
    
    #return sorted(temp)

    ind1 = 0  # Creating 2 new variable to track the 'current index'
    ind2 = 0
    # While both indeces are less than the length of their lists
    while ind1 < len(lst1) and ind2 < len(lst2):
        # If the current element of list1 is greater
        # than the current element of list2
        if(lst1[ind1] > lst2[ind2]):
            # insert list2's current index to list1
            lst1.insert(ind1, lst2[ind2])

            ind1 += 1  # increment indices
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(lst2):  # Append whatever is left of list2 to list1
        lst1.extend(lst2[ind2:])
    return lst1

def find_sum(lst: List[int], k: int) :
    '''
    Native search
    in: lst is a list of integer
        k is a sum
    out: find two values of sum
    '''
    print('[INFO]: find two number of sum that equal k')         
    # source [0 1 2 3 4 5 6 7]
    # i 
    
    for i in range(len(lst)-1):
        for j in range(1, len(lst)):
            print (lst[i] + lst[j], lst[i], lst[j])
            if (lst[i] + lst[j] == k):
                return (lst[i], lst[j])
            
print(find_sum(lst = [1, 21, 3, 14, 5, 60, 7, 6], k = 81))

def find_product(lst: List[int])-> List[int]:
    '''
    Модифицировать лист таким образом чтобы каждый индекс хранил произведение всех чисел листа кроме числа по данному индексу
    in: [1,2,3,4] -> out: [24=2*3*4, 12=1*3*4, 8=1*2*4, 6=1*2*3]
    '''
    print('[INFO]: find List of Product of all Elements')         
    temp = []
    for i in range(len(lst)):
        mult = 1
        for j in range(len(lst)):
            if i !=j:
                mult = mult* lst[j]
        temp.append(mult)
    return temp

print(find_product(lst = [1, 2, 3, 4]))
print(find_product(lst = [4, 2, 1, 5, 0]))


def find_minimum(lst: List[int])-> int:
    '''
    find smalest value in list
    in: [9,2,3,6]
    out : 2
    '''
    print('[INFO]: smalest value in list')         
    #lst = sorted(lst)
    min = lst[0]
    for i in range(1, len(lst)):
        if min > lst[i]:
            min = lst[i]
    return min


    return lst[0]


print(find_minimum(lst = [4, 2, 1, 5, 0]))
    

def find_first_unique(lst: List[int]):
    '''
    найти первые неповторяющиеся значения
    in: [9,2,3,2,6,6] or [4, 5, 1, 2, 0, 4]
    out : 9 or 5
    '''
    for i in range(len(lst)):
        j = 0
        while (j < len(lst)):
            if (i !=j) and (lst[i]==lst[j]):
                break
            j = j +1
        if (j ==len(lst)):
            return lst[i]
    return None

print(find_first_unique(lst = [4, 2, 1, 5, 0]))





























def find_second_unique1(lst: List[int]):
    '''
    find Second Maximum Value in a list
    in: [9,2,3,6] or [4, 2, 1, 5, 0]
    out : 6 or 4
    '''
    def sort_bubble(lst):
        for i in range(len(lst)):
            for j in range(len(lst)-i-1):
                if lst[j] < lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst
    return sort_bubble(lst)[1]
    
def find_second_unique1(lst: List[int]):
    '''
    find Second Maximum Value in a list without sorting
    in: [9,2,3,6] or [4, 2, 1, 5, 0]
    out : 6 or 4
    '''
    max0 = float('-inf') # setup minimum
    max1 = float('-inf') # setup minimum
    for item in lst:
        if item > max0:
            max0 = item

    for item in lst:
        if (item != max0) and (item > max1):
            max1 = item
    return max1

def right_rotate(lst, k):
    '''
    есть    list [10, 20, 30, 40 50]
            k = 3 
    развернуть лист начиная с позиции k
    '''
    n = len(lst)
    out = lst[n-k:]+lst[:n-k]
    return out


def rearrange(lst):
    '''
    Rearrange Positive & Negative Values
    Rearrange its elements in such a way that the negative elements appear at one end and positive elements appear at the other

    args: lst = [10,-1,20,4,5,-9,-6]
    return [-1,-9,-6, 10, 20, 4, 5]
    '''
    # var 1 with two auxiliary lists, neg and pos
    #lst0, lst1 = [], []
    #for i in lst:
    #    if i<0:
    #        lst0.append(i)
    #    else: 
    #        lst1.append(i)
    #return lst0+lst1
    I , J = [], []
    I = [i for i in lst if i < 0 ]
    J = [i for i in lst if i >= 0 ]
    #return lst0+lst1
    return I + J


def max_min(lst):
    '''
    Rearrange Sorted List in Max/Min Form
    the 0th index will have the largest number, the 1st index will have the smallest, and the 2nd index will have second-largest, and so on.
    '''
    result = []
    print(len(lst)//2)
    for i in range(len(lst)//2):
        result.append(lst[-(i+1)])
        result.append(lst[i])
    if len(lst) % 2:
        result.append(lst[len(lst)//2])
    return result

# Not Fully understand
def find_max_sum_sublist(lst):

    '''
    Задача o максимальной сумме подмассива (алгоритм Кадане)
    Есть несортированный Лист
    '''
    current_max = 0
    global_max = 0
    for i in lst:
        global_max = global_max + i
        # if max sum negative put it as 0
        global_max = max(global_max, 0)
        current_max = max(current_max, global_max)
    return current_max

def f(i, values=[]):
    values.append(i)
    print(values),
    return values
f(1)
f(2)
f(3)

lst = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]

#for i in range(0, 4):
#    print(lst[i].pop()),

#print(find_max_sum_sublist(lst =[-2, 1, -3, 4, -1, 2, 1, -5, 4]))

#print(right_rotate(lst=[13, 'a','Python'], k=3))

#print(rearrange(lst=[10,-1,20,4,5,-9,-6]))
#print(max_min ([1,2,3,4,5]))

#list1 = []  
#list2 = [2,6,7,8]
#print(merge_lists([4, 5, 6], [-2, -1, 0, 7]))

#lst = [1, 2,3,4]
##k = 5
#print(find_sum(lst, k))

#print(find_minimum([9,2,3, 6]))
#print(find_fisrt_unique([4,5,1,2,0,4]))
#print(find_second_unique1([5,5,1,2,0,4]))

#https://www.educative.io/module/page/8q5JgjuQREjpzD9gq/10370001/4688805018992640/5000095339905024
#https://www.educative.io/courses/algorithms-coding-interviews-python/my1vEn9NR3R
