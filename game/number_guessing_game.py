import random 

#intializing the variables 
number = 0
tries = 0 
upper_limit = 0
is_win = False 

# Getting the difficulty level from the user 

difficulty = input('''Enter the difficulty level ("E" for Easy "M" for Medium "H" for Hard ) : ''')
difficulty = difficulty.lower()

# Assigning the bounds of the random number based on the difficulty level

if difficulty == 'e' :
    upper_limit = 10
    tries = 5
    print("You have select the EASY level you have ",tries," tries to get the number ")
elif difficulty == 'm' :
    upper_limit = 50 
    tries = 10
    print("You have select the MEDIUM level you have ",tries," tries to get the number ")
elif difficulty == 'h' :
    upper_limit = 100
    tries = 15
    print("You have select the HARD level you have ",tries," tries to get the number ")
else :
    print("Sorry! You have entered the invalid data ")
    print("Game Exited")
    exit()

# Assigning the random value to the number based on the difficulty level they have chosen

number = random.randint(0,upper_limit)

    # Defining the function to guess the number 

def guessing(input_number) :
    global is_win #Fixing the scoping
    if(input_number < 0 or input_number > upper_limit) :
        print("Sorry the number you have entered is out of bounds ")
    elif(input_number < number) :
        print("It's too low ")
    elif(input_number > number) :
        print("It's too high ")
    else :
        print("Congratulations ! You Guessed it correctly ")
        is_win = True

for i in range(tries) :
    print("Attempt ",i+1," out of ",tries,"to guess the number between 0 and ",upper_limit)
    input_number = (input("Enter the number : "))
    if input_number.isdigit() : 
        input_number = int(input_number)
        guessing(input_number)
        if is_win :
            break
    else : print("Enter the valid number ")
        

if not is_win :
    print("You are unable to guess the number better luck next time ")
    print("The number is ",number)
