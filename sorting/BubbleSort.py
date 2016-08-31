__author__ = 'arunsasidharan'


def bubble_sort(input_array):
    count = 1
    size = len(input_array)
    for i in range(0, size - 1):
        for j in range(count, size):
            if input_array[i] > input_array[j]:
                swap(i, j, input_array)
        count += 1


def swap(i, j, input_array):
    temp = input_array[i]
    input_array[i] = input_array[j]
    input_array[j] = temp


test_list = [29, 13, 19, 11, 15, 9, 20, 1]
bubble_sort(test_list)
print(test_list)