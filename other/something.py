import time,random
def sleep():
    time.sleep(1)
    print("")

print("I am the Dread Pirate Roberts! Guess me secret! Blah blah blah...")
sleep()
print("To high, ye landlubber!")
sleep()
print("To low, ye scurvy dog!")
sleep()
print("I spray ye with squid ink if ye get it wrong!")
sleep()
print("It's a number between 1 and Infiniti(almost)!")
sleep()
print("Good luck!")
sleep()
print("Ye get a but 1 guess!")
secret = random.randint(1,10000000000000000000000)
guess = input()
if secret == guess:
    print("Found my secret, ye have! Impossible!!!!!!")
    
if guess != secret:
    print("Ye didn't find my secret and ye never shall!!! Go find me some squid ink instead!")
    print("The secret was...")
    sleep()
    print("Wait a wee moment... it was")
    sleep()
    print("Drumroll please!")
    sleep()
    sleep()
    sleep()
    print("It was %s!!! Ha!"%secret)
    time.sleep(3)