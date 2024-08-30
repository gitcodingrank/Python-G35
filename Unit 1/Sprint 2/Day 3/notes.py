a = 10
b = 10
print(a, id(a))
print(b, id(b))
print(a == b)  #value comparison: True
print(a is b)  #reference comparison: True
a = a + 1
print(a, id(a))

#a is b -> True then a == b -> True
#a == b -> True then a is b may ot may not be true 

print("\n")

c = 1.5
e = 1.5 #same object will be used
d = float(input("Enter 1.5 "))  #new object will created
print(c == d);  #value comparison: True
print(c is d);  #reference comparison: ??

print()

print(c == e);  #value comparison: True
print(c is e);  #reference comparison: ??