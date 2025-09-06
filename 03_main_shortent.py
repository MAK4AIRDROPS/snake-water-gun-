import random
'''
1=snake
-1=water
0=gun
'''
computer = random.choice([-1,0,1])
yourstr=input("Enter your choice: ")
yourdict={"s":1 , "w":-1 , "g":0}
reversedict={1:"snake" , -1:"water" , 0:"gun"}
you=yourdict[yourstr]
# Now we have to numbers(variables),you and computer
print(f"You chose {reversedict[you]} \n Computer chose {reversedict[computer]}")
if computer==you:
    print("It's a draw")

else:'''
    if (computer==-1 and you==1): (computer-you)== -2
        print("You win!")

    elif(computer==-1 and you==0):  (computer-you)== -1
        print("You lose!")

    elif(computer==1 and you==-1):  (computer-you)== 2
        print("You lose!")
            
    elif(computer==1 and you==0):  (computer-you)== 1
        print("You lose!")
           
    elif(computer==0 and you==-1):  (computer-you)== 1
        print("You lose!")
         
    elif(computer==0 and you==1):  (computer-you)== -1

        print("You lose!")
    else:
        print("Spomething went wrong")   
     The below value is written on the basis of value  of computer you    
'''
if ((computer-you) == -1 or (computer-you) ==-2):
    print("You lose")
else:
    print("You win")    

        