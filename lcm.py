a,b=map(int,input().split())
res1=1
res2=1
t=2
for t in range(1,a+b):
    
    if a%t==0 and b%t==0:
        a=a//t
        b=b//t
        res1=1*t
        
    else:
        t+=1
        a=a//t
        b=b//t
        res2=1*t
    
    if t>a or t>b:
        res=res1*res2*a*b
        print(res)
        break
        
        
