import operator
import random
import time
from datetime import timedelta

import pandas as pd


def selection_sort(array, key=None, asc=True):
    if key is None:
        key = lambda x: x
    comp = operator.lt if asc is True else operator.gt
    size = len(array)
    for ind in range(size):
        new_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if comp(key(array[j]), key(array[new_index])):
                new_index = j
        # swapping the elements to sort the array
        (array[ind], array[new_index]) = (array[new_index], array[ind])
    return array


def shaker_sort(array, key=None, asc=True):
    if key is None:
        key = lambda x: x
    comp = operator.gt if asc is True else operator.lt
    length = len(array)
    swapped = True
    start_index = 0
    end_index = length - 1

    while swapped:
        swapped = False

        for i in range(start_index, end_index):
            if comp(key(array[i]), key(array[i + 1])):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end_index = end_index - 1

        for i in range(end_index - 1, start_index - 1, -1):
            if comp(key(array[i]), key(array[i + 1])):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        start_index = start_index + 1
    return array


def sort_not_prime_elements(arr, method, key=None, asc=True):
    start_time = time.monotonic()
    result = []
    prime_elements = []
    not_prime_elements  =[]
    for ind, elem in enumerate(arr):
        if ind % 2 == 0:
            prime_elements.append(elem)
        else:
            not_prime_elements.append(elem)

    sorted_not_prime_elements = method(not_prime_elements, key, asc)
    for i in range(len(sorted_not_prime_elements)):
        result.append(prime_elements[i])
        result.append(sorted_not_prime_elements[i])
    if len(prime_elements) > len(sorted_not_prime_elements):
        result.append(prime_elements[-1])

    end_time = time.monotonic()
    return result, timedelta(seconds=end_time - start_time).total_seconds()


def generate_int_arr(n_numbers):
    return [random.randint(10, 1000) for _ in range(n_numbers)]


def partly_sort(arr, part=0.5):
    new_arr = arr.copy()
    split_index = int(part*len(new_arr))
    to_sort = new_arr[split_index:]
    sorted_arr = sorted(to_sort)
    new_arr[split_index:] = sorted_arr
    return new_arr


def sort_method_comparison():
    print("First of all let's demonstrate that the both of methods work")
    # We need ro sort by the second digit from end
    key = lambda x: int(str(x)[-2])
    # We need do to descending array
    asc = False
    # create a small array
    dem_arr = [20, 17, 40, -32, 60, 50, 80, -171, 100, 11]
    print("The unsorted array:")
    print(dem_arr)

    print("The result of selection sorting:")
    print(sort_not_prime_elements(dem_arr, selection_sort, key, asc)[0])

    print("The result of shaker sorting:")
    print(sort_not_prime_elements(dem_arr, selection_sort, key, asc)[0])
    print("As we can see the both of method works, so let's compare them on different arrays")

    # Creating an array with random numbers
    arr = generate_int_arr(500)
    sorted_arr = sorted(arr)
    partly_sorted_arr = partly_sort(arr)
    types_of_arrays = {"unsorted": arr, "partly_sorted": partly_sorted_arr, "sorted_arr": sorted_arr}
    results = []
    # print(arr, partly_sorted_arr, sorted_arr, sep="\n\n")
    for arr_type, ar in types_of_arrays.items():
        results.append({"type of array": arr_type, "method": "selection sort",
                        "time": sort_not_prime_elements(ar, selection_sort, key, asc)[1]})

        results.append({"type of array": arr_type, "method": "shaker sort",
                        "time": sort_not_prime_elements(ar, shaker_sort, key, asc)[1]})

    print(pd.DataFrame(results))


# selection_sort([2, 3, 4, 6, 10, -1, -100, 3, 3, 2, 1, -40], key=lambda x: int(str(x)[-1]), asc=True)
# print(sort_not_prime_elements([6, 11, 4, 3, 2, 5, 0]))
# shaker_sort([6, 11, 4, 3, 2, 5, 0], asc=True)

sort_method_comparison()
# print(partly_sort(generate_int_arr(10)))

