# 🎯 Guess The Number Game (Python Projects)

This repository contains two fun Python projects based on the classic **Guess the Number** game.  
Both versions are interactive and help to understand the basics of Python programming.

## 🕹️ Project 1: User Guesses the Number
In this version, the **computer randomly selects a number**, and the **user has to guess it**.

### 🔑 Features
- Computer picks a random number within a range.
- User guesses until they find the correct number.
- Program gives hints:  
  - "Too high" ⬆️  
  - "Too low" ⬇️  
- Counts the number of attempts.

### 💻 Example Output
Welcome to Guess the Number! 🎮
I'm thinking of a number between 1 and 100...

Welcome! I have Picked a Random Number for you between 1 to 100 🚀
Try to Guess, If you want to quit so press "q"
Enter Your Guess 👀 : 34
📈 Your Guess is too Low.Guess Higher Number
Thanks For Playing😊
Enter Your Guess 👀 : 87
📉 Your Guess is too High. Guess Lower Number
Thanks For Playing😊
Enter Your Guess 👀 : q
✋ Bye! the number was 49

## 🕹️ Project 2: Computer Guesses the Number
In this version, the **user thinks of a number**, and the **computer tries to guess it**.

### 🔑 Features
- User secretly thinks of a number between a range.
- Computer guesses using random numbers within `low` and `high`.
- User provides feedback:
  - `h` → number is higher
  - `l` → number is lower
  - `c` → correct guess
- Computer narrows down the range until it finds the right number.

### 💻 Example Output
Think a Random number between 1 and 100 then I will guess your number.
Let's started ...
My Guess is 52. Am I right or near to high and low? :h
Think a Lower number
My Guess is 3. Am I right or near to high and low? :l
Think a Higher number
My Guess is 87. Am I right or near to high and low? :c
WOW! I Guess it correctly.Your number is 87 number. 
My Guess is 3. Am I right or near to high and low? :q
Bye! the game has ended.
