import math as m
def fac_num(num):
    n=int(m.sqrt(num))
    fc=2
    for i in range(2,n+1):
        if num%i==0:
            if i!=num//i:
                fc+=2
            else:
                fc+=1
    print(fc)
num=int(input())
fac_num(num)
