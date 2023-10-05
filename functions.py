#functions

def cse():
    print("hi")
def ece(*x):
    print("hello",x)
ece(1,2)
cse()


    
def cse():
    print("hi")
def ece(x,y=10):
    print("hello",x,y)
ece(1)
cse()


    
def cse():
    print("hi")
def ece(x=20,y):
    print("hello",x,y)
ece(5,6)
cse()


def cse():
    print("hi")
def ece(x,y=50,z=12):
    print("hello",x,y+z)
ece(5+3,5,8)
cse()


def cse():
    print("hi")
def ece(x,y=50,z=12):
    print("hello",x,y+z)
ece(5+3,,8)
cse()

def cse():
    print("hi")
def ece(x,y=50,z=12):
    print("hello",x,y+z)
ece(5+3,5)
cse()





    