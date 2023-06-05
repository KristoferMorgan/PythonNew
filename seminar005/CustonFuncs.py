# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1 , ..., an , ..., где a0  = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

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
    

