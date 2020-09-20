print("What fact-family would you like?")
j = input("Enter the first number: ")
k = input("Enter the second number: ")
j = int(j)
k = int(k)
print("Here's you fact-family: ")

import time
time.sleep(1)
print(j, "+", k, "=", j + k)
time.sleep(1)
print(k, "+", j, "=", k + j)
time.sleep(1)
print(j + k, "-", j, "=", k)
time.sleep(1)
print(k + j, "-", k, "=", j)
time.sleep(1)
print(j, "*", k, "=", j * k)
time.sleep(1)
print(k, "*", j, "=", k * j)
time.sleep(1)
print(j * k, "/", j, "=", k)
time.sleep(1)
print(k * j, "/", k, "=", j)



