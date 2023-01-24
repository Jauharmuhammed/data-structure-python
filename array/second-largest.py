def second_largest(arr):
    if len(arr) < 2: return

    if arr[0] >=  arr[1]:
        l1, l2 = arr[0], arr[1] 
    else:
        l1, l2 = arr[1], arr[0] 

    for i in range(2, len(arr)):
        if arr[i] > l1:
            l2 = l1
            l1 = arr[i]

        elif arr[i] <= l1 and arr[i] > l2:
            l2 = arr[i]

    return l2

if __name__ == '__main__':
    a = [3,5,1,5,6, 9,10, 10]
    print(second_largest(a))