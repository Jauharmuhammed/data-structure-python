def merge_two_sorted_list(a, b):
    sorted_list = []
    i = j = 0
    len_a = len(a)
    len_b = len(b)

    while i < len_a and j< len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < len_a:
        sorted_list.append(a[i])
        i += 1

    while j < len_b:
        sorted_list.append(b[i])
        j += 1

    return sorted_list
    


if __name__ == '__main__':
    a = [4, 6, 7, 10, 56]
    b = [1, 4, 5, 7, 34, 67]

    print(merge_two_sorted_list(a, b))