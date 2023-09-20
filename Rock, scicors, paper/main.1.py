import random

while True:
    try:
        count = int(input("How many times do you want to play?: "))
    except ValueError:
        print("Enter the number!")
    else:
        count_start = 1
        win = 0
        lose = 0
        while count_start <= count:
            print("Round", count_start)
            user_action_1 = input("\nYour chose — rock, paper, scissors, spock или lizard:\n")
            user_action = user_action_1.lower()
            possible_actions = ["rock", "paper", "scissors", "spock", "lizard"]
            computer_action = random.choice(possible_actions)
            print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

            if user_action == computer_action:
                count_start += 1
                print(f"Two users chose {user_action}. Draw!!")

            elif user_action == "rock":
                count_start += 1
                if computer_action == "scissors":
                    print("Rock kick scissors! You win!")
                    win += 1
                elif computer_action == "lizard":
                    print("Rock kick lizard! You win!")
                    win += 1
                elif computer_action == "spock":
                    print("Spock brock rock! You lose!")
                    lose += 1
                else:
                    print("Paper wrap rock! You lose!")
                    lose += 1

            elif user_action == "paper":
                count_start += 1
                if computer_action == "rock":
                    print("Paper wrap rock! You win!")
                    win += 1
                elif computer_action == "спок":
                    print("Paper wrap spock! You win")
                    win += 1
                elif computer_action == "lizard":
                    print("Lizard bite spock! You lose!")
                    lose += 1
                else:
                    print("Scissors cut paper! You lose!")
                    lose += 1

            elif user_action == "scissors":
                count_start += 1
                if computer_action == "paper":
                    print("Scissors cut paper! You win!")
                    win += 1
                elif computer_action == "lizard":
                    print("Scissors cut lizard! You win!")
                    win += 1
                elif computer_action == "spock":
                    print("Spock brock scissors! You lose!")
                    lose += 1
                else:
                    print("Rock kick scissors! =You lose!")
                    lose += 1

            elif user_action == "lizard":
                count_start += 1
                if computer_action == "paper":
                    print("Lizard bite paper! You win!")
                    win += 1
                elif computer_action == "spock":
                    print("Lizard bite spock! You win!")
                    win += 1
                elif computer_action == "rock":
                    print("Rock kick lizard! You lose!")
                    lose += 1
                else:
                    print("Scissors cut lizard! You lose!")
                    lose += 1

            elif user_action == "spock":
                count_start += 1
                if computer_action == "rock":
                    print("Spock brock rock! You win!")
                    win += 1
                elif computer_action == "scissors":
                    print("Spock bock scissors! You win!")
                    win += 1
                elif computer_action == "lizard":
                    print("Lizard bite spock! You lose!")
                    lose += 1
                else:
                    print("Paper wrap spock! You lose!")
                    lose += 1

            else:
                print("Your choise does not match with game gestures!\n")

        print("Check -", "Player:", win, "Computer:", lose)
        over = input("\nDo you want to play again? Yes/No:\n")
        over = over.lower()
        if over == "No":
            break
