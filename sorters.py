# Parameters in the following functions:
#   data: a list of tuples
#   index: the tuple index to sort by
#
# Consider the following example data:
#   data = [
#       ( 'homer', 'simpson', 50 ),
#       ( 'luke', 'skywalker', 87 ),
#       ( 'bilbo', 'baggins', 111 ),
#   ]
#
#   bubble_sort(data, 0) sorts on first name (a..z)
#   bubble_sort(data, 0, True) sorts on first name (z..a)
#   bubble_sort(data, 2) sorts on age (1..infinity)
#
# The data list is sorted in place (anew list is not created).
# You do NOT need to perform validation on input data
# (null data list, index out of bounds, etc.)
#


def bubble_sort(data, index, descending=False):
    '''Sorts using the bubble sort algorithm'''
    for end_cursor in range(len(data) - 1, 0, -1):
        for idx in range(end_cursor):
            if descending and (data[idx][index] < data[idx + 1][index]):
                data[idx], data[idx + 1] = data[idx + 1], data[idx]
            elif not descending and (data[idx][index] > data[idx + 1][index]):
                data[idx], data[idx + 1] = data[idx + 1], data[idx]
    return data


def insertion_sort(data, index, descending=False):
    '''Sorts using the insertion sort algorithm'''
    for cursor in range(1, len(data)):
        current = data[cursor]
        position = cursor

        if descending:
            while position > 0 and data[position - 1][index] < current[index]:
                data[position] = data[position - 1]
                position -= 1
        else:
            while position > 0 and data[position - 1][index] > current[index]:
                data[position] = data[position - 1]
                position -= 1

        data[position] = current
    return data


def selection_sort(data, index, descending=False):
    '''Sorts using the selection sort algorithm'''
    for cursor in range(len(data) - 1, 0, -1):
        target_index = 0

        if descending:
            for position in range(1, cursor + 1):
                if data[position][index] < data[target_index][index]:
                    target_index = position

        else:
            for position in range(1, cursor + 1):
                if data[position][index] > data[target_index][index]:
                    target_index = position

        data[cursor], data[target_index] = data[target_index], data[cursor]
    return data
