"""n=int(input())
data=[None for i in range(n)]
for i in range(n):
    val=int(input())
    data[i]=val
print(data)'"""



"indexbased"
"""n=int(input())
data=list(map(int,input().split()))
for i in range(n):
    print(i,data[i])"""



"Total marks of a student"
"""def total_marks(n,data):
    res=0
    for i in data:
        res+=i
    return res
n=int(input())
data=list(map(int,input().split()))
total=total_marks(n,data)
print(total)"""



"Even and Odd count of data"
"""def ec_data(n,data):
    count=0
    for i in data:
        if i%2==0:
            count+=1
    return (count,n-count) 
n=int(input())
data=list(map(int,input().split()))
ec=ec_data(n,data)
print(*ec)"""
























