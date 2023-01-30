from typing import List

def selection_sort(lst : List [int])-> List [int]:
    """ O(n^2)
    Selection sort function
    arg: list of integers
    out: sorted list of integer
    """

    # Traverse through all lst elements
    for i in range(len(lst)):
        # Find the minimum element in unsorted lst
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

def bubble_sort(lst : List [int])-> List [int]:
    """ O(n^2)
    Selection sort function
    arg: list of integers
    out: sorted list of integer
    """
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j]> lst[j+1]:
                # swip elements
                lst[j], lst[j+1] = lst[j+1], lst[j]


def insert_sort(lst : List [int])-> List [int]:
    """ O(n^2)
    Сортировка вставкой 
    arg: list of integers
    out: sorted list of integer
    """

print(selection_sort([8, 5, 2, -1, 6, 3, 0, 9]))
print(bubble_sort([8, 5, 2, -1, 6, 3, 0, 9]))
print(insert_sort([8, 5, 2, -1, 6, 3, 0, 9]))