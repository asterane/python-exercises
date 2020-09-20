#Written March 2013
from random import randint

right = 0
no = 1

ques=int(input("How many questions do you want?"))
print("")

for index in range(ques):   #This tells it how many times to loop based on what you enter above#
    
    y=randint(0,10)    #Generates random integers between set amounts#
    x=randint(0,10)
    

    print(no,". " ,y,"x",x,"=")          #Prints problem number and problem#
    ans = input("Enter something: ")  
    print("You entered ", ans)
    no=no+1
    if int(ans)==y*x:    #Double equals sign tests for equality#
        print("Correct! \n")
        right=right+1
       
    
    if int(ans)!=y*x:      #Exclamation point is symbol for incorrect#
        print("Incorrect,")
        print("The correct answer is",y*x,". \n")
        
        

print("You got",right,"out of",ques,"questions correct.")


percent= float((float(right)/float(ques))*100)   #Calculates percent correct#



print("That is",float(percent),"% correct.")    
