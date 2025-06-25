"""
Course: CSE 351 
Lesson: 10 Team
File:   team.py

Purpose: Gain hands on experience with the concepts covered in this lesson, such as cache coherence,
         recursion, and analyzing what is happening at the hardware level of your programs.

Instructions:

- Look for and complete any TODO comments.
- You many attempt to optimize the code we gave you BUT DO NOT change anything we explicitly said
  not to touch.
"""

import time
import random
import threading
import multiprocessing as mp

from cse351 import *

def merge_sort(arr):
    """
    An efficient merge sort algorithm from https://www.geeksforgeeks.org/merge-sort/

    DO NOT MODIFY THIS FUNCTION! You should copy its logic into your own functions and modify there.

    Parameters:
        arr (list): The list to sort.

    Returns:
        void: List are passed by reference so no return is necessary.
    """

    # Base case of the recursion - must have at least 2+ items
    if len(arr) > 1:
 
        # Finding the mid of the array
        mid = len(arr) // 2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        merge_sort(L)
 
        # Sorting the second half
        merge_sort(R)
 
        i = j = k = 0
 
        # Copy data to temporary arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def is_sorted(arr):
    """ Check if a list is truly sorted - DO NOT change. """
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


def merge_normal(arr):
    """ Perform a normal merge sort with no threading or processes. - DO NOT change. """
    merge_sort(arr)


def merge_sort_thread(arr):
    # TODO - Add your code here to use threads.
    #        call, you need to create a thread to handle that call
    pass


def merge_sort_process(arr):
    # TODO - Add your code here to use process.
    #        call, you need to create a process to handle that call
    pass


# TODO - Add any function(s) here if needed.


def main():
    merges = [
        (merge_sort, ' Normal Merge Sort '), 
        (merge_sort_thread, ' Threaded Merge Sort '), 
        (merge_sort_process, ' Processes Merge Sort ')
    ]

    for merge_function, desc in merges:
        # Create list of random values to sort.
        arr = [random.randint(1, 10_000_000) for _ in range(1_000_000)]

        print(f'\n{desc:-^70}')
        print(f'Before: {str(arr[:5])[1:-1]} ... {str(arr[-5:])[1:-1]}')
        start_time = time.perf_counter()

        merge_function(arr)

        end_time = time.perf_counter()
        print(f'Sorted: {str(arr[:5])[1:-1]} ... {str(arr[-5:])[1:-1]}')

        print('Array is sorted' if is_sorted(arr) else 'Array is NOT sorted')
        print(f'Time to sort = {end_time - start_time:.14f}')


if __name__ == '__main__':
    main()