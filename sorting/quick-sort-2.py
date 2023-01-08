def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr)-1)

def quick_sort_helper(arr, start, end):
    if start >= end : return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
            swap(arr, left, right)
            left += 1
            right -= 1

        if arr[left] <= arr[pivot]:
            left += 1

        if arr[right] >= arr[pivot]:
            right -= 1

    swap(arr, pivot, right)

    quick_sort_helper(arr, start, right-1)
    quick_sort_helper(arr, right+1, end)


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
        quick_sort(arr)
        print(arr)
