import copy

a = 1
b = [1,2,3]
c = a
d = copy.copy(b)
b.append(5)

print(a, b, c, d, sep='\n')

