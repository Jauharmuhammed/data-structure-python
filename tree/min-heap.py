class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.bubble_up()


    def remove(self):
        if not self.heap:
            return None

        value = self.heap[0]
        last_value = self.heap.pop()
        if self.heap:
            self.heap[0] = last_value
            self.bubble_down()
            
        return value


    def bubble_up(self):
        index = len(self.heap) - 1
        while index > 0:
            if (self.heap[index] >= self.heap[self.parent(index)] ):
                return
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]

            index = self.parent(index)

    def bubble_down(self):
        index = 0
        while index < len(self.heap):
            if (self.left(index) > len(self.heap)):
                return
            if (self.right(index) > len(self.heap)):
                min_index = self.left(index)
            else:
                min_index = self.left(index) if self.heap[self.left(index)] < self.heap[self.right(index)] else self.right(index)

            if self.heap[index] <= self.heap[min_index]:
                return
            self.heap[index], self.heap[min_index] =   self.heap[min_index], self.heap[index]

            index = min_index               

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2


    def min_heapify(self, A,i):
        l = self.left(i)
        r = self.right(i)
        if l < len(A) and A[l] < A[i]:
            smallest = l
        else:
            smallest = i
        if r < len(A) and A[r] < A[smallest]:
            smallest = r
        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            self.min_heapify(A, smallest)

    
    def build_min_heap(self, A):
        n = int((len(A)//2)-1)
        for i in range(n, -1, -1):
            self.min_heapify(A,i)

if __name__ == '__main__':
    # h = MinHeap()
    # h.insert(5)
    # h.insert(10)
    # h.insert(1)
    # h.insert(9)
    # h.insert(0)
    # h.insert(7)
    
    # print(h.heap)

    # h.remove()

    # print(h.heap)

    a = [5, 10, 1, 9, 0, 7]
    h2 = MinHeap()
    h2.build_min_heap(a)
    print(a)