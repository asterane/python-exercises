print("Hello!")
print("My", end=' ')
print("name", end=' ')
print("is", end=' ')
print("Victor the computer!")
somebody = input("Please enter your name: ")
print("Hi ", somebody, " how are you today? Answer good or bad.")

answer = input()
if answer == 'good':
    print("Oh good! Tell me about your day.")
    response = input()
    print("I'm glad you had a good day! Is there anything I could do for you?")
    command = input()
    print("Sure! Check back in ten years, I'll have done it by then. Is that ok? Answer yes or no.")
    answer2 = input()

    if answer2 == 'yes':
        print("Ok! Have a good day! Remember to check in in ten years, ok? Bye!")

    if answer2 == 'no':
        print("Ok, have a good day. Bye!")
        





if answer == 'bad':
    print("BUMMER! Tell me what happened today.")
    response = input()
    print("That's sad. Is there anything I can do for you?")
    command = input()
    print("Sorry, I am not able to do that... Seeing as I don't have legs. Anything else I can do?")
    command2 = input()
    print("Sorry, I can't do that either. Have a good day!")
