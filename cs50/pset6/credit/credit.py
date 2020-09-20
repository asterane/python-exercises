from sys import exit

# get a credit card number from the user
number = input("Number: ")
digits = []
code = "INVALID"

# place all digits into a list in reverse order
for c in number:
    try:
        digits.insert(0, int(c))
    except ValueError:
        print(code)
        exit(1)

# check for characteristic features of different card types
l = len(digits)
if l in [13, 15, 16]:
    if digits[l - 1] == 4:
        code = "VISA"
    elif digits[l - 1] == 3 and digits[l - 2] in [4, 7]:
        code = "AMEX"
    elif digits[l - 1] == 5 and digits[l - 2] in range(1, 6):
        code = "MASTERCARD"
    else:
        print(code)
        exit(1)
else:
    print(code)
    exit(1)

# run Luhn's algorithm over the digits
sum = 0
for i in range(len(digits)):
    if i % 2 == 0:
        sum += digits[i]
    elif digits[i] < 5:
        sum += 2 * digits[i]
    else:
        sum += 1 + (2 * digits[i]) % 10

if sum % 10 != 0:
    code = "INVALID"

# report on the validity and origin of the card
print(code)

exit(0)
