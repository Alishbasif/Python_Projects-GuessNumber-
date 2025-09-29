import random

def main():
    high = 100
    low = 1
    feedback = ""
     
    print("Think a Random number between 1 and 100 then I will guess your number.")
    print("Let's started ...")

    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low 

        comp_int = input(f"My Guess is {guess}. Am I right or near to high and low? :").lower()    
        
        if comp_int == 'h':
           guess -= 1 
           print("Think a Lower number")

        elif comp_int == 'l':
            guess += 1
            print("Think a Higher number")

        elif comp_int == 'c':
            print(f"WOW! I Guess correct {guess} number.")
     
        elif comp_int == 'q':
            print("Bye! the game has ended.")
            break

        else:
            print("Wrong Input! Please enter a number of (high,low,correct)")

if __name__ == "__main__":
    main()
