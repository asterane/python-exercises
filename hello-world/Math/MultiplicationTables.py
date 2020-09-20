#Written July 2012
print("Which multiplication table would you like to view?")
multiplier = input()
print("How high would you like the table to go?")
size = input()

m = int(multiplier)  #Turns strings#
s = int(size)        #into numbers.#

for i in range (s):
    print(i, "x", m, "=", i * m)
