#Written July 2012
print("This program will calculate the amount of carpet reqired to cover a rectangular room and the cost of the carpet.")
print("Enter your name or S to skip.")
SomeName = input()
if SomeName.lower()=="s":
    SomeName = ""
else:
    SomeName = SomeName + ","
print("Enter the length of the room in feet.")
SomeLength = input()
print("Enter the width of the room in feet.")
SomeWidth = input()

z = float(SomeLength) #********
x = float(SomeWidth)  #Turns entries from
m = z * x             #strings to integers,
d = m / 9             #multplies and divides integers,
a = float(m)          #and floats the product / quotient. 
c = float(d)          #********

print("The amount of carpet needed is %.1f square feet or %.1f square yards." % (a, c))
print("Enter the cost of the carpet per square foot in American dollars.")
SomeCost = input()

y = float(SomeCost)
o = m * y


print("The total cost of the carpet is $%.2f in American dollars." % o)
print("Goodbye %s and have a nice day." % SomeName)

 

