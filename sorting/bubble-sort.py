def bubbleSort(list):
    for i in range(len(list) - 1):
        swapped= False
        for j in range(len(list) - 1 - i ):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

                swapped = True
        
        if not swapped:
            break


if __name__ == '__main__':
    lists = [
        [1, 0, 5, 99, 2, 0, 4, 2],
        [9, 9, 9, 0, 0, 99, 999, 9],
        [],
        [1],
     ]
    for a in lists:
        bubbleSort(a)
        print(a)