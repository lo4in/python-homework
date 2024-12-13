a = input()
b = input()

c = a.count(b)
d = b.count(a)

if c and d != 0:
    print("contain")
else:
    print("not contain")