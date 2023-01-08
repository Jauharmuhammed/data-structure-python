class MaxHeap:
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
            if (self.heap[index] <= self.heap[self.parent(index)] ):
                return
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]

            index = self.parent(index)

    def bubble_down(self):
        index = 0
        while index < len(self.heap):
            if (self.left(index) > len(self.heap)):
                return
            if (self.right(index) > len(self.heap)):
                max_index = self.left(index)
            else:
                max_index = self.left(index) if self.heap[self.left(index)] > self.heap[self.right(index)] else self.right(index)

            if self.heap[index] >= self.heap[max_index]:
                return
            self.heap[index], self.heap[max_index] =   self.heap[max_index], self.heap[index]

            index = max_index               

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2


if __name__ == '__main__':
    h = MaxHeap()
    h.insert(5)
    h.insert(10)
    h.insert(1)
    h.insert(9)
    h.insert(0)
    h.insert(7)
    
    print(h.heap)

    h.remove()

    print(h.heap)