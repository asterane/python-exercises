from random import randint, choice
import time

def addition(x, y):
    us = '+'
    cs = (x + y)
    x = x
    y = y

def subtraction(x, y):
    us = '-'
    cs = (x - y)
    x = x 
    y = y

def multiplication(x, y):
    us = 'x'
    cs = (x * y)
    x = x
    y = y

def division(x, y):
    us = '/'
    cs = (x / y)
    x = x
    y = y

def all_4():
    ptyp = choice('a', 's', 'm', 'd')
    if ptyp == 'a':
        addition(rand(ptyp))
    if ptyp == 'm':
        multiplication(rand(ptyp))
    if ptyp == 's':
        subtraction(rand(ptyp))
    if ptyp == 'd':
        division(rand(ptyp))

def rand(ptyp):
    if ptyp == 'm' or ptyp == 'a':
        x = randint(1, 11)
        y = randint(1, 11)
    if ptyp == 's':
        x = randint(1, 11)
        y = randint(1, x)
    if ptyp == 'd':
        y = randint(1, 11)
        z = randint(1, 11)
        x = (y * z)
    randnums = [x, y]
    return randnums

no = 1
right = 0

typ = input('Would you like 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, or 5. All four?' )
ques = int(input('How many questions would you like? '))
print('Starting in...')
for i in range(3,0,-1):
    print(i)
    time.sleep(1)
print('Now! \n')

for index in range(ques):
    ans = int(input('Enter your answer: '))
    print('You answered: %i' % ans)
    no += 1
    if ans == cs:
        print('Correct! \n')
        right += 1
    if ans != cs:
        print('Incorrect.\nThe correct answer is: %i \n' % cs)


print('You got %i out of %i problems correct' % (right, ques))
percent = float(float(float(right) / float(ques)) * float(100))
print('Or... %.2f percent correct.' % percent)


