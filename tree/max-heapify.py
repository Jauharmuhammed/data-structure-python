class MaxHeap:
    def __init__(self):
        self.heap = []            

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def max_heapify(self, A,i):
        l = self.left(i)
        r = self.right(i)
        if l < len(A) and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < len(A) and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(A, largest)


    def build_max_heap(self, A):
        n = int((len(A)//2)-1)
        for i in range(n, -1, -1):
            self.max_heapify(A,i)

if __name__ == '__main__':

    a = [5, 10, 1, 9, 0, 7]
    h2 = MaxHeap()
    h2.build_max_heap(a)
    print(a)