'''Merge sorting an array of dictionary using keys
optionally you can sort in descending order also'''


def merge_sort(arr, key='', descending=False):
    if len(arr) <= 1: return
    if key == '' or key not in arr[0]: return

    mid = len(arr)//2
    left = arr[mid:]
    right = arr[:mid]

    merge_sort(left, key=key, descending=descending)
    merge_sort(right, key=key, descending=descending)

    merge(arr, left, right, key, descending)


def merge(arr, a, b, key, descending):
    i = j= k = 0

    while i < len(a) and j < len(b):

        if ( a[i][key] >= b[j][key] if descending else a[i][key] <= b[j][key]):
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
        

    while i < len(a):
        arr[k] = a[i]
        k+=1
        i+=1

    while j < len(b):
        arr[k] = b[j]
        k+=1
        j+=1


if __name__ == '__main__':
    elements = [
        {'name': 'Alfas', 'age': 21, 'LPA': 8},
        {'name': 'Naji', 'age': 22, 'LPA': 6},
        {'name': 'Javad', 'age': 24, 'LPA': 5.5},
        {'name': 'Parol', 'age': 23, 'LPA': 5},
        {'name': 'Jaseem', 'age': 24, 'LPA': 10},
        {'name': 'Ashwin', 'age': 25, 'LPA': 6.5},
        {'name': 'Althaf', 'age': 20, 'LPA': 6},
    ]

    merge_sort(elements, key='age', descending=False)

    for i in elements:
        print(i)
