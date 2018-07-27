from random import randint
numb = randint(1, 100)
print(numb)

loop = True
solan = 0
while loop:
    guess = int(input("Guess my number (1-100)?"))
    solan +=1
    if solan == 7:
        print("You lose!")
        loop = False
    else:
        if guess > numb:
            print("A little too large!")
        elif guess < numb:
            print ("Too small")
        else:
            print("Bingo")
            loop = False
            

    
        
