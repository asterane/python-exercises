import random, easygui

money = random.randint(1, 99)
guess = 0
tries = 0
done = False

easygui.msgbox("""Hello!  I'm the Dread Cashier Bob, and I have some money!
It is an amount of money between 1 and 99.  I'll give you 5 tries to guess the amount.
You can have the money if you get the amount right!""")

while guess != money and tries < 5:
    guess = easygui.integerbox("What's your guessed amount of money?")
    if not guess: break
    if guess < money:
        easygui.msgbox(str(guess) + " is too low, have I checked you out before?")
    elif guess > money:
        easygui.msgbox(str(guess) + " is too high, you're getting jipped on the price of your candy bars!")
    

    if guess == money:
        done = True
        easygui.msgbox("Ugh! You guessed the amount of money in the cashier, but I lied! You can't have the money! Bye!")
    tries = tries + 1

else:
    if not done:
        easygui.msgbox("No more guesses! You can't have the money... this time!")           
