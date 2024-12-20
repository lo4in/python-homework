def prime(n):
    factors=[]
    for i in range(1, n+1):
        if n%i == 0:
            factors.append(i)
    #print(factors)
    a= factors.count(1)
    b= factors.count(n)
    len1 = len(factors)
    if a and b == 1 and len1 == 2:
        return True
    else:
        return False

n= int(input())
print(prime(n))