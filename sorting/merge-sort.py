def merge_sort(arr):
    if len(arr) <= 1 : return

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_list(arr, left, right)

def merge_two_sorted_list(arr, a, b):
    i = j = k = 0
    len_a = len(a)
    len_b = len(b)

    while i < len_a and j< len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

    


if __name__ == '__main__':
    test = [
        [6, 0, 1, 4, 3, 9, 6, 1],
        [9, 8, 7, 6, 4, 3, 1],
        [1, 4, 5, 6, 9],
        [4, 6, 7, 10, 56, 1, 4, 5, 7, 34, 67],
        [1, 1, 1],
        [4],
        [],
    ]
    for arr in test:
        merge_sort(arr) 
        print(arr)