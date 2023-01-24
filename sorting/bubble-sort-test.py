def bubble_sort(arr):
    if len(arr) < 2:
        return arr

    for i in range(len(arr)-1):
        swapped =False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] =  arr[j+1], arr[j]
                swapped = True

        if not swapped:
            return arr



if __name__ == '__main__':
    lists = [
        [1, 0, 5, 99, 2, 0, 4, 2],
        [9, 9, 9, 0, 0, 99, 999, 9],
        [],
        [1],
     ]
    for a in lists:
        bubble_sort(a)
        print(a)