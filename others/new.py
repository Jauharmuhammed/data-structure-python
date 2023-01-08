def func(A, i):
    l = 2 * i + 1
    r = 2 * i + 2

    if l < len(A) and A[l] < A[i]:
        smallest = l
    else: 
        smallest = i
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        


def build_heap(A):
    n = (len(A)//2) - 1
    for i in range(n, -1, -1):
        func(A, i)