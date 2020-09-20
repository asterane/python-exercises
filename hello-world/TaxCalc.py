def calculateTax(price, tax_rate):
    total = price = (price * tax_rate)
    return total

my_price = float(input ("Enter a price: "))
my_rate = float(input ("Enter a tax rate: "))

totalPrice = calculateTax(my_price, my_rate)
print("price = ", my_price, " Total price = ", totalPrice)
