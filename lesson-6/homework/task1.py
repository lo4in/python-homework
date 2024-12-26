

def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Error"
        return func(a, b)
    return wrapper
@check
def div(a,b):
    return a / b

a = int(input())
b = int(input())


print(div(a,b))