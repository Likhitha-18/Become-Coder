import math as m
def rev(n):
    r=0
    while n:
        a=n%10
        r=r*10+a
        n=n//10
    return r
def Reverseofdigits(n,data):
    for i in range(n):
        data[i]=rev(data[i])
n=int(input())
data=list(map(int,input().split()))
Reverseofdigits(n,data)
print(*data)
