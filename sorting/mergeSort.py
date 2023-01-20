def merge_sort(arr):
    if len(arr) <= 1: return

    mid = len(arr) // 2
    left = arr[mid:]
    right = arr[:mid]

    merge_sort(left)
    merge_sort(right)

    merge(arr, left, right)


def merge(arr, a, b):
    i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else: 
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len(a):
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len(b):
        arr[k] = b[j]
        j+=1
        k+=1


a = [4, 1, 6, 7,3, 8, 0]
merge_sort(a)
print(a)