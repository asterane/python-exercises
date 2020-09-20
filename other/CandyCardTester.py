import random

for i in range(100):
    fullset=False
    candy_count=0
    card_count=0
    Conway=False
    Descartes=False
    Euler=False
    Fermat=False
    Gauss=False
    while not fullset:
        card=random.randint(0,9)
        candy_count+=1
        
        if card==0:
            if Conway==False:
                Conway=True
                card_count+=1
            else:
                pass
        elif card==1:
            if Descartes==False:
                Descartes=True
                card_count+=1
            else:
                pass
        elif card==2 or card==3:
            if Euler==False:
                Euler=True
                card_count+=1
            else:
                pass
        elif card==4 or card==5 or card==6:
            if Fermat==False:
                Fermat=True
                card_count+=1
            else:
                pass
        elif card==7 or card==8 or card==9:
            if Gauss==False:
                Gauss=True
                card_count+=1
            else:
                pass

        if card_count==5:
            print(candy_count)
            fullset=True
        
