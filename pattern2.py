'''n=int(input())
for i in range(n):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(i+1):
        print("*",end=' ')
    print()'''
    
a=int(input())
for i in range(a):
    print(" "*(i+1)+"* " *(a-i))
    
a=int(input())
for i in range(a):
    print(" "*(a-i)+"* " *(i+1))