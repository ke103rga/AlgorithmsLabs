import operator


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


def sort_not_prime_elements(arr, key=None, asc=True):
    source_arr_len = len(arr)
    prime_elements = []
    not_prime_elements  =[]


    sorted_not_prime_elements = selection_sort(not_prime_elements, key, asc)


# selection_sort([2, 3, 4, 6, 10, -1, -100, 3, 3, 2, 1, -40], key=lambda x: int(str(x)[-1]), asc=True)
sort_not_prime_elements([0, 1, 2, 3, 4, 5, 6, 7])
