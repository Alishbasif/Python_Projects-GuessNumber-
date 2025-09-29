import random

def main():
    random_num = random.randint(1,100)
    
    print("Welcome! I have Picked a Random Number for you between 1 to 100 🚀")
    print("""Try to Guess, If you want to quit so press "q" """)

    while True :
        user_guess = input("Enter Your Guess 👀 : ").strip()
        attempt = 0
        # error handling
        if user_guess == "q":
            print(f"✋ Bye! the number was {random_num}")
            break

        try:
            guess = int(user_guess)

        except Exception as e :
            print(f"😥 OOPS! The Game is Abondan due to {e}")
            continue
         
        attempt += 1 
        if guess == random_num:
            print(f"Correct! Your Guess is in {attempt} attempts 👏✨") 

        elif guess < random_num:
            print(f"📈 Your Guess is too Low.Guess Higher Number")

        else:    
            print(f"📉 Your Guess is too High. Guess Lower Number")

        print("Thanks For Playing😊")    

if __name__ == "__main__":
    main()