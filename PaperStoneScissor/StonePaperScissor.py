from random import randrange

options = ["Scissor", "Stone", "Paper"]
random_number = randrange(3)
user_option = input("Choose between Paper, Scissor and Stone:")
computer_option = options[random_number]

def play():
    if computer_option == user_option:
        user_optionNew = input("Choose again:")
    elif computer_option == "Scissor" and user_option == "Stone" or computer_option == "Stone" and user_option == "Paper" \
            or computer_option == "Paper" and user_option == "Scissor":
        print("You won")
        print("Computer: " + computer_option)
    elif computer_option == "Scissor" and user_option == "Paper" or computer_option == "Stone" and user_option == "Scissor" \
            or computer_option == "Paper" and user_option == "Stone":
        print("You lost")
        print("Computer: " + computer_option)


play()
