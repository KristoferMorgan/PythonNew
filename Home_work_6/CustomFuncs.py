def enterStrForm(a,n,d,):
    result = list()
    for i in range(n ):
        result.append(a + i * d)
    return result
def indexRange(arr,min,max):
    result = list()
    for i in range((len(arr)) + 1 ):
        if min < int(arr[i-1]) < max:
           result.append(i ) 
    return result