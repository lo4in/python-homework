import random

num = random.randint(1, 100)
val = 1
print(num)

for i in range(0, 10):
    user = int(input())
    if user < num:
        print("Too low!")
    elif user > num:
        print("Too high!")
    elif num == user:
        print("You guessed it right!")
        break
    
print("End of the game")
while 2 > 1:
    ans_list="Yes"    
    ans = input("Want to play again?\n")
    if ans == ans_list:
        val = 1
        while val == 1:
            for i in range(0, 10):
                user = int(input())
                if user < num:
                    print("Too low!")
                elif user > num:
                    print("Too high!")
                elif num == user:
                    print("You guessed it right!")
                    break
            break
    else:
        val = 0
        break
