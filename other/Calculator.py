done = False
while not done:
    equation = eval(input('Enter an equation: '))
    ans = eval(equation)
    print(('Your answer is %s.' % ans))
    d = eval(input('Done (Y/N)?'))
    if d.lower().startswith('y'):
        done = True
    else:
        done = False
