Nested For Loops

Concept: A nested for loop is essentially a for loop within another for loop. This allows you to iterate through multiple levels of data or perform operations that require repeated iterations.
Implementation:
Outer Loop: The first for loop acts as the outer loop. It iterates over a sequence (like a list or range) and executes the code within its block.
Inner Loop: For each iteration of the outer loop, the inner for loop executes completely. This means the inner loop runs multiple times for every single iteration of the outer loop.

matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

for row in matrix:  # Outer loop iterates through each row
    for element in row:  # Inner loop iterates through each element in the current row
        print(element, end=" ") 
    print()  # Move to the next line after printing each row