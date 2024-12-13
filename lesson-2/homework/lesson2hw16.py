txt = input()

a = txt.count("0")
b = txt.count("1")
c = txt.count("2")
d = txt.count("3")
f = txt.count("4")
g = txt.count("5")
l = txt.count("6")
r = txt.count("7")
m = txt.count("8")
q = txt.count("9")

if a and b and c and d and f and g and l and r and m and q == 0:
    print("no digit")
else:
    print("digit est'")