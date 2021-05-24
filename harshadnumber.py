def harshad(n):
    res=0
    while n:
        r=n%10
        n=n//10
        res=res+r
    print(res)
    if n%res==0:
        return True
    return False
n=int(input())
print(harshad(n))
