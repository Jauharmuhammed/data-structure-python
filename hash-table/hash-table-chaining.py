class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % 10

    def __setitem__(self, key, val):
        hash = self.get_hash(key)
        for idx, element in enumerate(self.arr[hash]):
            if element[0] == key:
                self.arr[hash][idx] = (key,val)
                return

        self.arr[hash].append((key, val))

    def __getitem__ (self, key):
        hash = self.get_hash(key)
        for idx, element in enumerate(self.arr[hash]):
            if element[0] == key:
                return self.arr[hash][idx]

    def __delitem__ (self, key):
        hash = self.get_hash(key)
        for idx, element in enumerate(self.arr[hash]):
            if element[0] == key:
                return self.arr[hash].pop(idx)

if __name__ == '__main__':
    h = HashTable()
    h['Cristano Ronaldo']= 37
    h['Lionel Messi']= 35
    h['Erling Haaland']= 21
    h['Kylian Mbappe']= 23
    h['Robert Lewandowski']= 34
    h['Zlatan Ibrahimovich']= 41
    h['Toni Kroos']= 33
    h['Muhammed Salah']= 32
    h['Sadio Mane']= 31
    h['Mesut Ozil']= 34
    h['Neymar Jr']= 30
    h['Kevin De Bruyne']= 32

    h['Muhammed Salah']= 34

    del h['Robert Lewandowski']

    for i in h.arr:
        print(i)

    print(h['Sadio Mane'])
    print(h['Muhammed Salah'])