def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(min_index+1, len(arr)):
            if arr[j]< arr[min_index]:
                min_index = j
        
        if i != min_index:
            arr[i], arr[min_index] =  arr[min_index], arr[i]

        

if __name__ == '__main__':
    lists = [
        [1, 0, 5, 99, 2, 0, 4, 2],
        [9, 9, 9, 0, 0, 99, 999, 9],
        [],
        [1],
        ]
    for a in lists:
        selection_sort(a)
        print(a)