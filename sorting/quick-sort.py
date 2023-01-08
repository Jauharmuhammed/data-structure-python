def swap(a, b ,arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

def partition(elements, start, end):
    
    pivot = elements[start]

    while start < end:
        while start < len(elements) and elements[start] <= pivot :
            start += 1
        
        while end > 0 and elements[end] >= pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    return end


def quick_sort(elements, start, end):
    if start < end:
        partition_index = partition(elements, start, end)

        # left partition
        quick_sort(elements, start, partition_index -1)

        # right partition
        quick_sort(elements, partition_index +1 , end)


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
        quick_sort(arr, 0, len(arr)-1)
        print(arr)
