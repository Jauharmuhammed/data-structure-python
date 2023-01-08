def linearSearch(list, value):
    for index, element in enumerate(list):
        if element == value:
            return index

    return -1


def binarySearch(list, value):
    left = 0
    right = len(list) -1
    mid = 0

    while left <= right:
        mid = (left + right ) // 2
        mid_element = list[mid]

        if mid_element == value:
            return mid
            
        if mid_element < value:
            left = mid + 1
        else:
            right = mid - 1

    return -1

list = [1,4,5,6,8,9,10,15]

print(linearSearch(list, 8))
print(binarySearch(list, 8))