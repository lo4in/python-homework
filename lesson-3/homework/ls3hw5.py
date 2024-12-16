#Check Element: Given a list and an element, check if the element is present in the list.

list = [2, 3, 5, 1, 4, 13, 13, 15, 56, 2, 3, 4]
num = int(input())

a = list.count(num)

print(a)
if a != 0:
    print("presented")
else:
    print("not presented")