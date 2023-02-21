import random


def generate_int_arr(n_numbers, sort=True):
    rand_arr = [random.randint(0, 10) for _ in range(n_numbers)]
    if sort:
        return sorted(rand_arr)
    return rand_arr


def binary_search(arr, elem_to_find):
    indices = []
    arr_len = len(arr) - 1
    first = 0
    last = arr_len
    mid = (first + last) // 2
    middle_elem = arr[mid]

    # Searching an entry which we will meet first
    while middle_elem != elem_to_find:
        if middle_elem > elem_to_find:
            last = mid - 1
        else:
            first = mid + 1
        mid = (first + last) // 2
        middle_elem = arr[mid]
    indices.append(mid)

    # searching entries nex to fist met element
    prev = mid - 1
    while prev >= 0:
        if arr[prev] == elem_to_find:
            indices.append(prev)
            prev -= 1
        else:
            break

    next = mid + 1
    while next <= arr_len:
        if arr[next] == elem_to_find:
            indices.append(next)
            next += 1
        else:
            break

    return sorted(indices)


def linear_structures_search():
    n_numbers = int(input("Please enter the number of elements-> "))
    random_arr = generate_int_arr(n_numbers)
    element_to_find = int(input("Please enter the element which you want to find-> "))
    indices = binary_search(random_arr, element_to_find)
    print(f"The amount of entries is {len(indices)}, indices of entries are{indices}")


# print(binary_search([1, 1, 1, 2, 2, 3, 4, 5, 7, 7, 7, 8, 8, 8], 8))