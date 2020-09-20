print("This program will figure out how many miles you walk in a certain amount of minutes.")
strideLength == float(input('What is the approx. length of your strides in feet?'))
stepNum == float(input('Approx. how many steps do you take in a minute?'))
minutes == float(input('Approx. how many minutes did you walk?'))

footNum == strideLength * stepNum
footNum2 == footNum * minutes
mileNum == int(footNum2 / 5280)

print("You walked", mileNum, "miles.")
