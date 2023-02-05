def main():
    print("Welcome to Rock-Paper-Scissors")
    print("Enter 1 for Rock, 2 for Paper, 3 for Scissors")

    while True:
        player = int(input("Your turn: "))
        while player < 1 or player > 3:
            player = int(input("Enter valid input: "))

        if player == 1:
            player_choice = "Rock"
        elif player == 2:
            player_choice = "Paper"
        else:
            player_choice = "Scissors"

        print(f"Your choice is {player_choice}")
        print("Now it's the computer's turn")

        import random
        computer = random.randint(1, 3)

        if computer == 1:
            computer_choice = "Rock"
        elif computer == 2:
            computer_choice = "Paper"
        else:
            computer_choice = "Scissors"

        print(f"Computer's choice is {computer_choice}")

        print(f"{player_choice} vs {computer_choice}")

        result = (player - computer + 3) % 3

        if result == 0:
            print("Draw")
        elif result == 1:
            print("You Win!")
        else:
            print("Computer Wins!")

        print("Do you want to play again? (Y/N)")
        answer = input()

        if answer == 'n' or answer == 'N':
            break

    print("\nThanks for playing!")


if __name__ == '__main__':
    main()
