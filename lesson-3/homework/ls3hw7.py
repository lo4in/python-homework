#Last Element: Access the last element of a list, considering what to return if the list is empty.

list = [2, 3, 5, 1, 4, 13, 13, 15, 56, 2, 3, 4]
emp = []
print(list[-1])
if list == emp:
    print("list is empty")