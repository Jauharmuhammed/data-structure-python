def left(i):
    return 2*i +1

def right(i):
    return 2*i +2

def parent(i):
    return (i -1) // 2


def max_heapify(arr, i, n):
    l = left(i)
    r = right(i)

    if l < n and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    
    if r < n and arr[r] > arr[largest]:
        largest = r

    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, n)

def heap_sort(arr):
    n= len(arr)

    # build a max heap
    last_parent = parent(n-1)
    for i in range(last_parent, -1, -1):
        max_heapify(arr, i, n)


    # extract elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, 0, i)


if __name__ == '__main__':

    test = [
        [9, 5, 1, 3, 2, 4, 5],
        [1, 2, 3, 4, 5],
        [4, 56, 3, 10, 0, 19, 99, 37, 43], 
        [7, 3, 2, 1],
        [0],
        [],
    ]

    for arr in test:
        heap_sort(arr)
        print(arr)