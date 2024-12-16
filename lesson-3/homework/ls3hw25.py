list = [2, 3, 5, 1, 4, 13, 13, 15, 56, 2, 3, 4]

a = len(list)

if a %2 == 0:
    b = a//2 - 1
    c = a//2 
    print(list[b], list[c])
if a%2 != 0:
    d = a//2
    print(list[d])