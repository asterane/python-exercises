import time
StarPrint = False
secs = int(input("Countdown timer: how many seconds? "))
starry = input("Print stars (Y/N)? ")
if starry.lower().startswith('y'):
    StarPrint = True
else:
    StarPrint = False
for i in range (secs, 0, -1):
    if not StarPrint:
        print(i)
    if StarPrint:
        print(i, "* " * i)
    time.sleep(1)
    
print("BLAST OFF!")
