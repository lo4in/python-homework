#Insert Element: Given a list and an element, insert the element at a specified index.
list = [2, 3, 5, 1, 4, 13, 13, 15, 56, 2, 3, 4]
element = int(input())
index = int(input()) - 1

list.insert(index, element)

print(list)