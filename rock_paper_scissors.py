
import random
print("-----------welcome to: rock, paper, scissors play----------------")
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action :
        print(f"Both players selected {user_action}. It's a tie!")
        
    elif user_action== "rock" :
        if computer_action ==  "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("paper cover rock  you lose!!!")

    elif user_action== "scissors" :   
        if computer_action=="rock":
            print("Rock smashes scissors! You lose!!! ")     
        else:
            print("Scissors cuts paper! You win.")
        
        
    elif user_action== "paper" :   
        if computer_action=="rock":
            print("paper cover rock ! You win!!! ")     
        else:
            print("Scissors cuts paper! You lose.")  
    
    play_again = input("Play again? (y/n): ") # new
    if play_again.lower() != "y": # new
        break            
