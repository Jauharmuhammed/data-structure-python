def selectionSort(list):
    for i in range(len(list) - 1):
        min_index = i 
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j

        if i != min_index:
            list[i], list[min_index] = list[min_index], list[i]


if __name__ == '__main__':
    lists = [
        [1, 0, 5, 99, 2, 0, 4, 2],
        [9, 9, 9, 0, 0, 99, 999, 9],
        [],
        [1],
     ]
    for a in lists:
        selectionSort(a)
        print(a)