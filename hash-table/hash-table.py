class HashTable:
    def __init__(self) :
        self.MAX = 100
        self.arr = [ None for i in range(self.MAX) ]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % 100

    def add(self, key, val):
        hash = self.get_hash(key)
        self.arr[hash] = val

    def __setitem__(self, key, val):
        hash = self.get_hash(key)
        self.arr[hash] = val

    def get(self, key):
        hash = self.get_hash(key)
        return self.arr[hash] 

    def __getitem__(self, key):
        hash = self.get_hash(key)
        return self.arr[hash] 

    def delete(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None

    def __delitem__(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None

    

if __name__ == '__main__':
    h = HashTable()
    h.add('Cristano', 37)
    h.add('Messi', 35)
    h.add('Benzema', 34)
    h.add('Haaland', 21)
    h.add('Mbappe', 23)
    h.add('Lewandowski', 34)

    h['Modric'] = 37
    h['Ozil'] = 34

    print('Cristano :', h.get('Cristano'))
    print("Neymar :",h.get('Neymar'))

    print('Ozil', h['Ozil'])
    print('Haaland', h['Haaland'])

    h.delete('Cristano')
    print('Cristano after deletion :',h.get('Cristano'))

    del h['Messi']
    print('Messi after deletion :',h.get('Messi'))

