#Count Even Numbers: Given a list of integers, count how many of them are even.

list = [2, 3, 5, 1, 4, 13, 13, 15, 56, 2, 3, 4]

odd = 0

for num in list:
  
    
    if num % 2 != 0:  
        odd += 1

print(odd)