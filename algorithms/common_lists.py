from typing import List, Tuple, Optional

def remove_even(lst: List[int])-> List[int]:
    '''
    Remove Even Integers from List 
    in: my_list = [1,2,4,5,10,6,3]
    out: my_list = [1,5,3]
    '''
    #temp = []
    #for i in lst:
    #    if (i%2)==1:
    #        temp.append(i)
    #return temp
    return [i for i in lst if i % 2 != 0]

def merge_lists(lst1: List[int], lst2: List[int])-> List[int]:
    '''
    Merge two sorted Lists
    in: list1 = [1,3,4,5]  
        list2 = [2,6,7,8]
    out: [1,2,3,6,4,7,5,8]
    '''
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
            

def find_sum_native(lst: List[int], k: int) :
    '''
    Native search
    in: lst is a list of intger
        k is a sum
    out: find two values of sum
    '''
    # Write your code here
    for i in range(0, len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i]+lst[j]== k:
                return lst[i], lst[j]

    1, 21, 3, 14, 5, 60, 7, 6

    #return sorted(lst1+lst2)

def find_product(lst: List[int])-> List[int]:
    '''
    Модифицировать лист таким образом чтобы каждый индекс хранил произвеление всех чисел листа кромие числа по данному индлексу
    in: [1,2,3,4]]
    out: [24, 12, 8, 6]
    '''
    temp = []
    for i in range(len(lst)):
        mult = 1
        for j in range(len(lst)):
            if i != j:
                mult = mult*lst[j] 
        temp.append(mult)
    
    return temp 

def find_minimum(lst: List[int])-> int:
    '''
    find smalest value in list
    in: [9,2,3,6]
    out : 2
    '''
    if (len(lst) <= 0):
        return None
    
    min = lst[0]
    for i in range(1,len(lst)):
        if lst[i] < min:
            min = lst[i]
    return min

def find_fisrt_unique(lst: List[int]):
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




#list1 = []  
#list2 = [2,6,7,8]
#print(merge_lists([4, 5, 6], [-2, -1, 0, 7]))

#lst = [1, 2,3,4]
##k = 5
#print(find_sum(lst, k))

#print(find_minimum([9,2,3, 6]))
#print(find_fisrt_unique([4,5,1,2,0,4]))
print(find_second_unique1([5,5,1,2,0,4]))

https://www.educative.io/module/page/8q5JgjuQREjpzD9gq/10370001/4688805018992640/5000095339905024
https://www.educative.io/courses/algorithms-coding-interviews-python/my1vEn9NR3R
