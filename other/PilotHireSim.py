import random

pilotList = ['M','M','M','M','M','M','M','M','M','M','M','M','M','M','M',
             'F','F','F','F','F','F','F','F','F','F']
females=0

for i in range(20):
    females = 0
    for j in range(8):
        person = random.randint(0,24)
        if pilotList[person] == 'F':
            females+=1
    print(females)
        
