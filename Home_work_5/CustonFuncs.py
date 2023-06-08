def LastFibo(n):
    if n in [0,1]:
        return n
    return LastFibo(n - 1) + LastFibo(n - 2)

def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

def check(n, div = None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print("Число не является простым")
            return False
        else:
            return check(n, div-1)
    else:
        print("Число является простым")
        return True

def reverse_range(num):
    print(num,end =' ')
    if num > 0:
        reverse_range(num - 1)
        
def powerOfNumber(a,b):
    if b == 1:
        return a
    return a * powerOfNumber(a,b-1)
        
def recursionSum(a,b):
    if a ==0:
        return b
    return recursionSum(a-1,b+1)