def reverse_array(arr, start, end):
    if start >= end:
        return
    
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start+1, end-1)


if __name__ == '__main__':
    a = [3, 5, 2, 54, 1, 2]
    reverse_array(a, 0, len(a)-1)
    print(a)