__author__ = 'arunsasidharan'


def binary_search(input_array, value):  # iterative

    lower = 0
    upper = len(input_array) - 1

    while lower <= upper:
        mid = (upper + lower) / 2
        target = input_array[mid]
        if target == value:
            return mid
        elif value < target:
            upper = mid - 1
        else:
            lower = mid + 1

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))