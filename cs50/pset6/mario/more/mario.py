# get a valid height from the user
while True:
    try:
        height = int(input("Enter pyramid height (1-8, inclusive): "))
        if height >= 1 and height <= 8:
            break
    except ValueError:
        pass

# print out a pyramid of the correct size
for i in range(height):
    print(" " * (height - (i + 1)), end="")
    print("#" * (i + 1), end="")
    print("  ", end="")
    print("#" * (i + 1))
