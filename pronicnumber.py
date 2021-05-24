def disarium(num):
    
    count=0
    res=0
    while num:
        r=num%10
        num=num//10
    count+=1
    res+=pow(r,count)
    if res==num:
        return True
    return False
    
      
num=int(input())


print(disarium(num))
