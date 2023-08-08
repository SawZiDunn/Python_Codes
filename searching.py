import math


def jump_search(my_arr, find, start, end):
    while start <= end:
        median = (start + end) // 2
        if my_arr[median] == find:
            return median
        elif my_arr[median] > find:
            end = median - 1
        else:
            start = median + 1
    return -1


if __name__ == '__main__':
    arr = [1, 3, 5, 6, 7, 9, 11, 15, 58]
    to_find = 58
    result = jump_search(arr, to_find, 0, len(arr) - 1)

    if result == -1:
        print("We haven't found ", to_find, ".")
    else:
        print(f"We found {to_find} at index {result}.")

