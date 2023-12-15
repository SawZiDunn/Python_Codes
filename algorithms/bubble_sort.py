def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp

    return arr


if __name__ == '__main__':

    arr = [8, 9, 6, 2, 1, 4, 5, 7, 8, 9, 6, 2, 1, 1, 5, 4, 7, 8, 9, 6]
    print(arr)

    new_arr = bubble_sort(arr)
    print(new_arr)

    arr.sort()
    print(arr)
