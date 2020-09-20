dist = input("How far away is the next gas station in kilometers? ")
print("")

print("How big is your fuel tank, in liters? ")
size = input()
print("What percentage full is your tank? ")
percent = input()
print("How many km per liter does your car get? ")
milage = input()

size2 = int(size)
pct2 = int(percent)
pct3 = float(pct2 / 100)

amount = float(pct2 * float(size2)) - 5

miles = float(amount * pct3)

print("Your car can go", miles, "more kilometers.")
print("The next gas station is", dist, "km away.")

if float(miles) > float(dist):
    print("You can wait for the next station.")
    
else:
    print("You can't wait for the next station!!! Get gas now!")
