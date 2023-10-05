#ip : h 3 op  k jumping 3 times

#if sm is less than 122
'''a=input()
b=int(input())
print(chr(ord(a)+b))'''
  
  
  
a=input()
b=int(input())
if(ord(a)+b>122):
    print(chr((ord(a)+b)-26))
else:
    print(chr(ord(a)+b))