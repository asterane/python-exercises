#Written April 2013#
def z():
    print("")
print("Please enter the date in mm/dd/yyyy format.")
date = input()
z()

print("Please enter all information capitalized. Enter your age as a number.")
z()

print("What is your first name? ")
name = input()
z()

print("What is your last name? ")
lastName = input()
name2 = name+""+lastName
z()

print("How old are you? ")
age = input()
age2 = int(age)
z()

print("What is your favorite color? ")
fcol = input()
col2 = fcol.lower()
z()

print("What is your favorite food?")
faveFood = input()
food2 = faveFood.lower()
z()

a=open("%s.txt"%str(name2), 'a')

def writ(item):
    a.write(item)
    a.write("\n")

print("Your name is", name, ", you are", age2, "years old, your favorite food is", food2, ", and your favorite color is", col2, ".")

a.write("\n")
writ(str(date))
writ(name)
a.write("Age: ")
a.write(age)
writ(" years")
a.write("Favorite color: ")
writ(fcol)
a.write("Favorite food: ")
writ(faveFood)
a.close()
