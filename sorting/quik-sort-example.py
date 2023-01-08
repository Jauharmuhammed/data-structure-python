def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr)-1)

def quick_sort_helper(arr, start, end):
    if start >= end: return

    pivot = start
    left = start+1
    right = end
    
    while left < right:
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


