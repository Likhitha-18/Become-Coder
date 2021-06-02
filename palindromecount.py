def palcount(n,data):
    pc=0
    for i in range(n):
        c=0
        temp=data[i]
        while data[i]>0:
            r=data[i]%10
            data[i]=data[i]//10
            c=c*10+r
        if temp==c:
            pc+=1
    return pc
n=int(input())
data=list(map(int,input().split()))
print(palcount(n,data))
