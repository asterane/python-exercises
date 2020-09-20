import time, random
print("Now opening Cryptography v1.0...")
time.sleep(3)
enl = 1
nice = False
alph1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encode(message, key):
    encMsg = []
    for char in message:
        good = False
        for letter in alph1:
            if char == letter:
                good = True
            else:
                good = False
        if good == True:
            encMsg.append(ord(char) - 96)
        elif good == False:
            if char == ' ':
                encMsg.append(27)
            if char == '.':
                encMsg.append(28)
            if char == ',':
                encMsg.append(29)
            else:
                encMsg.append(30)
                
    encMsg.append(int(key) + 2)
    
    for num in encMsg:
        num += (10 + int(key))
        num = str(num)
        
    
    encMsg = ''.join(encMsg)
    
    return encMsg
    
prepvar = input("To encode, type e. To decode, type d.")

if prepvar.lower().startswith('e'):
    message = input('Type your message: ')
    while nice == False:
        key = input('Type a key between 0 and 9, inclusive:')
        try:
            if int(key) < 0 or int(key) > 9:
                nice = False
                print("Try again.")
            else:
                nice = True
        except:
            nice = False
            print("Try again.")
            
    print(("Your encoded message is: %s" % encode(message, key)))
    
stop = input('Type OK to end')