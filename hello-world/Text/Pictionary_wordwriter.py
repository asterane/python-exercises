import random
lines = []
words = []

z = open("shortwords.txt", 'w')

x = open("pictionary words.txt", 'r')
lines = x.readlines()
x.close()


for i in range(1, 16): 
    a = random.choice(lines)
    words.append(a)
    lines.remove(a)
    
for i in range(1, 16):
    b = words.pop()
    z.write(b)

z.close()
