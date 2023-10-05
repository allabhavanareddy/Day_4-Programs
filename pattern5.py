n=int(input())
for i in range(1,n+1):
    print((10**(i-1))*i)
    
n=int(input())
b=1
for i in range(1,n+1):
    print(b*i)
    b=(b*10)+1
    
n=int(input())
for i in range(1,n+1):
    print(i*((10**i)//9))
    