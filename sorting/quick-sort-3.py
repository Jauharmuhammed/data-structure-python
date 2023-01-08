def swap(a, b ,arr):
    arr[a], arr[b] = arr[b], arr[a]


def quick_sort(elements):
    quick_sort_helper(elements, 0, len(elements)-1)

def quick_sort_helper(elements, start, end):
    if start >= end: return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if elements[left] > elements[pivot] and elements[right] < elements[pivot]:
            swap(left, right, elements)
            left += 1
            right -= 1
        
        if  elements[left] <= elements[pivot]:
            left += 1
        
        if elements[right] >= elements[pivot]:
            right -= 1

    swap(pivot, right, elements)

    quick_sort_helper(elements, start, right-1)
    quick_sort_helper(elements, right+1, end)



if __name__ == '__main__':
    test = [
        [10, 4, 3, 1, 7, 5],
        # [2, 3, 1, 4, 5],
        # [9, 5, 1, 3, 2, 4, 5],
        # [1, 2, 3, 4, 5],
        # [4, 56, 3, 10, 0, 19, 99, 37, 43], 
        # [7, 3, 2, 1],
        # [0],
        # [],
    ]

    for arr in test:
        quick_sort(arr)
        print(arr)

