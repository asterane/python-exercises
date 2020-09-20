#Written July 2012#
print("This program will help you add up your change.")
print("Enter your name or S to skip.")
SomeName = input()
if SomeName.lower()=="s":
    SomeName = ""
else:
    SomeName = SomeName + ","
print("Enter the number of quarters.")
quarters = input()
print("Enter the number of dimes.")
dimes = input()
print("Enter the number of nickels.")
nickels = input()
print("Enter the number of pennies.")
pennies = input()

a = int(quarters) #****
b = int(dimes)    #Turns strings 
c = int(nickels)  #into intgers.
d = int(pennies)  #****

e = a * 0.25  #****
f = b * 0.10  #Assigns numeric 
g = c * 0.05  #values to coins.
h = d * 0.01  #****

z = e + f + g + h

print("That is $%.2f in quarters, $%.2f in dimes, $%.2f in nickels, and $%.2f in pennies." % (e, f, g, h))
print("Or... $%.2f in all. Goodbye %s and have a nice day."% (z,
                                    SomeName))
