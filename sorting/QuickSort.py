__author__ = 'arunsasidharan'


def quick_sort(input_array):
    sort(input_array, 0, len(input_array) - 1)


def sort(arr, start, end):
    if start >= end:
        return
    else:
        p_index = partition(arr, start, end)
        sort(arr, 0, p_index - 1)
        sort(arr, p_index + 1, end)


def partition(arr, start, end):
    pivot = arr[end]
    p_index = start

    for i in range(start, end):
        if arr[i] > pivot:
            continue
        else:
            swap(arr, i, p_index)
            p_index += 1

    swap(arr, p_index, end)  # swapping so that pivot is on the left of partition index
    return p_index


def swap(arr, i, p_index):
    temp = arr[i]
    arr[i] = arr[p_index]
    arr[p_index] = temp


test_list = [29, 13, 19, 11, 15, 9, 20, 1, 5]
quick_sort(test_list)
print(test_list)