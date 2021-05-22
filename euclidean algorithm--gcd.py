def egcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a==b:
        return a
    while b>0:
        if a<b:
            a,b=b,a
        t=b
        b=a%b
        a=t
    return a
a,b=map(int,input().split())
print(egcd(a,b))
    
   
