
import math as m
def sum(n):
    s=0
    while n:
        r=n%10
        n=n//10
        s+=r
    return s
def Sumofdigits(n,data):
    for i in range(n):
        data[i]=sum(data[i])
        

n=int(input())
data=list(map(int,input().split()))
Sumofdigits(n,data)
print(*data)
        
        
