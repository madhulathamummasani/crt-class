#Functions programs in python
#1
def sree(a,b):#with argument without return type
    print(a+b)
sree(15,20)
sree(5,20)
#2
def sree(a,b):#with argument without return type
    return a+b
print(sree(15,20))
print(sree(5,20))
#3
a=lambda x,y:x+y
print(a(1,9))
#4 generator func
def fun(n):
    i=0
    while i<n:
        yield i
        i+=1
print(list(fun(5)))
#5 Decorator func:that modify (or) extend behavior of other function.
def my_dec(func):
    def wrapper():
        print("a")
        func()
        print("ab")
    return wrapper
@my_dec
def say_hello():
    print("Hi")
say_hello()  
#6
def my_dec(a):
    def b():
        a()
        print("ab")
        print("abd")
    return b
@my_dec
def say_hello():
    print("Hi")
say_hello()   
#7 closure: that captures and remember the values in the enclosing scope even if they are not present in memory.
def outer_function(x):
    def inner_function(y):
        return x+y
    return inner_function
closure=outer_function(10)
print(closure(5))
#Built-in functions: python standard library
#8
a="7skjdbf"
print(a[0].isalpha())
#9
a="79984375"
print(a.count("9"))
#10
a="HGFHGJ"
print(a.lower())
#11
a="HGFHGJ"
print(a.replace("H","k"))
#12
a="HGFHGJ"
for i, e in enumerate(a):
    print(i,e)
#Recursive functions: Functions that call themselves, either directly or indirectly.
#13
def a():
    print("sd")
    a()
a()
#14
def a(n):
    if n==1:
        return
    print(n)
    a(n-1)
a(5)
#15
def a(n):
    print(n)
    if n==1:
        return
    a(n-1)
a(5)
#16
def a(n):
    if n==1:
        return
    a(n-1)
    print(n)
a(5)
#17
def a(n):
    if n==1:
        return
    print(n)
    a(n-1)
    print(n)
a(5)
#18
def a(n):
    if n==1:
        return
    a(n-1)
    print(n)
    a(n-1)
a(3)
#19
def sree(a,b):#parameters
    print(a,b)
sree(10,20)#arguments
#20
def sree(a,b=0):
    print(a,b)
sree(10)
#21
def sree(a,b=0):
    print(a,b)
sree(10,8)
#23
def sree(b=3):
    print(b)
sree()
#24
def sree(a,b=3,c=0,d=0,e=0):
    print(a,b,c)
sree(2,4)
#25
def sree(*a):
    print(a)
sree(2,6.7,"hi")
def sree(*a):
    a=list(a)
    print(a)
sree(2,6.7,"hi")
#26 Arbitrary keyword:
def sree(**a):
    print(a)
sree(rank=1,age=20,roll=21,name="lakshmi")
#27
def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
print(sum(5))
#28 fibonnaci
def sum(n):
    if n==1:
        return 1
    return n*sum(n-1)
print(sum(5))
#29 sum of given integer
def sum(n):
    if n<10:
        return n
    return n%10+sum(n//10)
print(sum(123))
#30 finding min in given list
def sum(n,i=0):
    if i==len(n)-1:
        return n[i]
    return min(n[i],sum(n,i+1))    
l=[2,3,6,1,5]
print(sum(l))
#method-2                                                                                      
def sum(n,i=0):
    if i==len(n)-1:
        return n[i]
    min=sum(n,i+1)
    return n[i] if n[i]<min else min  
l=[2,3,6,5]
print(sum(l))
#OOPS
#31. class & object:
class com_lab:
    bench=2
    dustbin=1
vin=com_lab() #vin is member of class
print(vin.bench)
#32
class com_lab:
    bench=2
    dustbin=1
vin=com_lab()
sid=com_lab()
gin=com_lab()
print(vin.bench, sid.bench)
#33
class com_lab:
    bench=2
    dustbin=1
    def projector():
        print("on")
vin=com_lab()
sid=com_lab()
gin=com_lab()
com_lab.projector() #only com_lab has access but not vin, sid, gin.
#34 Instance Method:
class com_lab:
    bench=2
    dustbin=1
    def system(self):
        print("System")
    def projector():
        print("on")
vin=com_lab()
sid=com_lab()
gin=com_lab()
gin.system() #this is not accessed by class.
#35 (or)
class com_lab:
    bench=2
    dustbin=1
    def system(self):
        print("System")
    def projector():
        print("on")
vin=com_lab()
sid=com_lab()
gin=com_lab()
com_lab.system(gin)
#36 constructor
class com_lab:
    bench=2
    dustbin=1
    def __init__(self): #constructor
        print("Welcome")
    def system(self):
        print("System")
    def projector():
        print("on")
gin=com_lab()
gin.system()
#37 Instance attribute:
class com_lab:
    def __init__(self,amt):
        self.amt=amt
    def return_back(self):
        return self.amt
gin=com_lab(10)
vin=com_lab(20)
sin=com_lab(30)
print(sin.return_back())
#Inheritance:Inheriting the properties and behavior from the parent class.
#38
class com_lab_a:
    gin=56
class com_lab_b(com_lab_a):
    sin_amt=80
sin=com_lab_b()
print(sin.sin_amt+sin.gin)
#39
class com_lab_a:
    gin=56
class com_lab_b(com_lab_a):
    sid=20
s=com_lab_b()
print(s.gin)
#40 
class a:
    def bike(self):
        print("hi")
class b:
    def car(self):
        print("helloo")
class c(a,b):
    def car(self):
        print("how r u")
obj=c()
obj.car()
#41
class a:
    def car(self):
        print("hi")
class b:
    def car(self):
        print("helloo")
class c(a,b):
    def bike(self):
        print("how r u")
obj=c()
obj.car()
#42 Multiple Inheritance: two or more parents and one child.
class a:
    def __init__(self):
        print("hi")
class b:
    def __init__(self):
        print("helloo")
class c(b,a):
    def bike(self):
        print("how r u")
obj=c()
obj.bike()    
#43
class a:
    def __init__(self):
        print("hi")
class b:
    def car(self):
        print("helloo")
class c(a,b):
    def __init__(self):
        super().__init__()
    def aero(self):
        print("how r u")
obj=c()
obj.aero()
#44 multi-level Inheritance:grand parent and parent and child.
class a:
    gin=30
class b(a):
    gin=10
class c(b):
    gin=40
obj=c()
print(obj.gin)
#45    
class a:
    gin=30
class b(a):
    pass
class c(b):
    pass
obj=c()
print(obj.gin)
#46
class a:
    def __init__(self):
        print("a")
class b(a):
    def __init__(self):
        print("b")
class c(b):
    pass
obj=c()
#47
class a:
    def __init__(self):
        print("a")
class b(a):
    def __init__(self):
        print("b")
class c(b):
    pass
c()
#48
class a:
    def __init__(self):
        print("a")
class b(a):
    def __init__(self):
        print("b")
    def bike(self):
        print("bike")
class c(b):
    pass
c().bike()
c().bike()
#49 hierarchial Inheritance: One parent class and two child classes.
class a:
    def __init__(self):
        print("a")
class b(a):
    def bike(self):
        print("bike")
class c(b):
    pass
b()
#50 Hybrid Inheritance: combination of two or more inheritances.
class a:
    def __init__(self):
        print("a")
class b(a):
    def bike(self):
        print("bike")
class c(b):
    pass
class m(b):
    pass
b()
#51
class a:
    def __init__(self):
        print("a")
class b(a):
    def bike(self):
        print("bike")
class c(a):
    pass
class m(b,c):
    pass
m()
#52 Encapsulation
class gin:
    _a=10
class sin(gin):
    def __init__(self):
        print(super()._a)
    pass
sin()
#53
class com_lab:
    def __init__(self):
        self.__locker()
    def __locker(self):
        print(1000000)
com_lab()
#54 method overriding
class a:
    def sin(self,amt):
        print(amt)
class b(a):
    def sin(self,amt):
        print("1",amt)
a().sin(45)
#55 Duck typing:different class having same method name but without inheritance
class a:
    def sin(self,amt):
        print(amt)
class b:
    def sin(self,amt):
        print("1",amt)
b().sin(45)
#56 
class dog:
    def sound(self):
        print("bow")
class cat:
    def sound(self):
        print("meow")
class duck:
    def sound(self):
        print("quack")
def makee_sound(obj):
    obj.sound()
d=dog()
c=cat()
du=duck()
makee_sound(du)
#57
class cse:
    def __init__(self,t,e,m,s,so,h):
        self.t=t 
        self.e=e 
        self.m=m
        self.s=s
        self.so=so
        self.h=h
    def total(self):
        return (self.t+self.e+self.m+self.s+self.so+self.h)
    def avg(self):
        return (self.total()/6)
gin=cse(45,34,34,56,67,34)
sid=cse(34,65,46,67,23,74)
kin=cse(45,56,67,94,35,75)
print(kin.total())
print(kin.avg())
#58
class cse:
    def __init__(self,name):
        print(f"Details of {name}")
        self.t= int(input("TELUGU : "))
        self.e=int(input("ENGLISH : "))
        self.m =int(input("MATHS : "))
        self.s = int(input("SCIENCE : "))
        self.so =int(input("SOCIAL : "))
    def total(self):
        return (self.t+ self.e+self.m+self.s+self.so)
    def avg(self):
        return self.total() / 5
narasimha = cse("NARASHIMA")
yuvaraj = cse("yuvaraj")
pavan  = cse("pavan")

