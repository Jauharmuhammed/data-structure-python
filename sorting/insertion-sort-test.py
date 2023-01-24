def insertion_sort(arr):
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i-1
        while j>= 0 and anchor < arr[j]:
            arr[j+1]= arr[j]
            j -= 1

        arr[j+1] = anchor


if __name__ == '__main__':
    lists = [
        [1, 0, 5, 99, 2, 0, 4, 2],
        [9, 9, 9, 0, 0, 99, 999, 9],
        [],
        [1],
     ]
    for a in lists:
        insertion_sort(a)
        print(a)