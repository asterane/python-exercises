print("This program will figure out how many miles you walk in a certain amount of minutes.")
print("")
strideLength = float(input('What is the approx. length of your strides in feet? '))
print("")
stepNum = float(input('Approx. how many steps do you take in a minute? '))
print("")
minutes = float(input('Approx. how many minutes did you walk? '))
print("")
	
footNum = strideLength * stepNum
footNum2 = footNum * minutes
mileNum = float(footNum2 / 5280)

print("You walked %.2f miles."%float(mileNum))
