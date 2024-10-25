import random

rock=""" 
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""
scicccor=""" 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
thing=[rock,paper,scicccor]

while(True):
    computer_choice=random.choice(thing)
    user=  user = int(input("""Choose the object:
1. Rock
2. Paper
3. Scissors
Enter the number of your choice: """))
    
    if user <1 and user >3:
         print("enter a positive number less than or equal to 3")
         continue
    
    if user==1  :
        user_choice=rock
    elif user==2:
        user_choice=paper
    else:
        user_choice=scicccor

    print("\nYour choice:")
    print(user_choice)
    
    print("Computer's choice:")
    print(computer_choice)

    if user_choice==computer_choice:
        print("It's a Tie")
    elif (user_choice == rock and computer_choice == scicccor) or (user_choice == paper and computer_choice == rock) or (user_choice == scicccor and computer_choice == paper):
        print("You Win!")
    else:
        print("You Lose!")
    
    play_again=input("Do you want to play again?(yes/no):").strip().lower()
    if play_again != "yes":
        break