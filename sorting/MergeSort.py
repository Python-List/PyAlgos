__author__ = 'arunsasidharan'


def merge_sort(input_array):
    size = len(input_array)
    if size < 2:
        return

    mid = size / 2
    left = input_array[: mid]
    right = input_array[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(left, right, input_array)


def merge(left, right, input_array):
    left_length = len(left)
    right_length = len(right)

    i = 0
    j = 0
    k = 0
    while i < left_length and j < right_length:
        if left[i] < right[j]:
            input_array[k] = left[i]
            i += 1
        else:
            input_array[k] = right[j]
            j += 1
        k += 1

    while i < left_length:
        input_array[k] = left[i]
        i += 1
        k += 1

    while j < right_length:
        input_array[k] = right[j]
        j += 1
        k += 1


test_list = [29, 13, 19, 11, 15, 9, 20, 1, 5]
merge_sort(test_list)
print(test_list)