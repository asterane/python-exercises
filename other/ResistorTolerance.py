while True:
    txtval=eval(input("Value: "))
    if txtval=="stop":
        print("\n")
        break
    try:
        val=int(txtval)
    except:
        print("\n")
        continue
    tol=0.05*(val)
    upper=val+tol
    lower=val-tol
    print(("Tolerance: %s \nUpper: %s \nLower: %s \n" %(tol, upper, lower)))
