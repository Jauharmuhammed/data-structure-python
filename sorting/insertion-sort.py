def insertionSort(list):
    for i in range(1, len(list)):
        anchor = list[i]
        j = i - 1
        while j >= 0 and anchor < list[j]:
            list[j+1] = list[j]
            j -= 1

        list[j+1] = anchor


if __name__ == '__main__':
    lists = [
        [1, 0, 5, 99, 2, 0, 4, 2],
        [9, 9, 9, 0, 0, 99, 999, 9],
        [],
        [1],
     ]
    for a in lists:
        insertionSort(a)
        print(a)