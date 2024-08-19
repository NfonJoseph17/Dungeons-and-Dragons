def start_adventure():
    print("Welcome to Dungeons & Dragons: The Quest for the Mystic Sword!")
    print("Your adventure begins now...\n")

    # First decision
    print("You find yourself at the entrance of a dark forest. The Mystic Sword is rumored to be hidden deep within.")
    choice1 = input("Do you want to ENTER the forest or RETURN to the village? (Enter/Return): ").lower()

    if choice1 == "enter":
        print("\nYou bravely step into the forest, your senses alert to any danger.\n")
        encounter_wolf()
    elif choice1 == "return":
        print("\nYou decide it's safer to return to the village. Unfortunately, your quest ends before it even begins.")
        print("Game Over. You have lost.")
    else:
        print("\nInvalid choice! The forest consumes you as you hesitate.")
        print("Game Over. You have lost.")


def encounter_wolf():
    print("As you walk deeper into the forest, you hear growling nearby. A wild wolf appears!")
    choice2 = input("Do you want to FIGHT the wolf or RUN away? (Fight/Run): ").lower()

    if choice2 == "fight":
        print("\nYou draw your sword and prepare to fight the wolf.")
        print("The battle is fierce, but you manage to defeat the wolf.")
        find_cave()
    elif choice2 == "run":
        print("\nYou turn and run as fast as you can. The wolf chases you down and you trip on a root.")
        print("Game Over. You have lost.")
    else:
        print("\nInvalid choice! The wolf attacks while you hesitate.")
        print("Game Over. You have lost.")


def find_cave():
    print("\nAfter defeating the wolf, you continue your journey and come across a mysterious cave.")
    choice3 = input("Do you want to EXPLORE the cave or CONTINUE through the forest? (Explore/Continue): ").lower()

    if choice3 == "explore":
        print("\nYou cautiously enter the cave and find a hidden treasure chest.")
        open_chest()
    elif choice3 == "continue":
        print("\nYou decide not to take any risks and continue through the forest.")
        print("Unfortunately, you miss the opportunity to find the Mystic Sword hidden in the cave.")
        print("Game Over. You have lost.")
    else:
        print("\nInvalid choice! The cave entrance collapses as you hesitate.")
        print("Game Over. You have lost.")


def open_chest():
    print("The treasure chest is locked. You notice a strange inscription on the lock.")
    choice4 = input("Do you want to TRY to unlock it or LEAVE the chest? (Try/Leave): ").lower()

    if choice4 == "try":
        print("\nYou carefully decipher the inscription and manage to unlock the chest.")
        print("Inside, you find the legendary Mystic Sword!")
        print("Congratulations! You have won the game!")
    elif choice4 == "leave":
        print("\nYou decide not to risk it and leave the chest untouched.")
        print("As you exit the cave, you feel a sense of regret for leaving the treasure behind.")
        print("Game Over. You have lost.")
    else:
        print("\nInvalid choice! The chest vanishes as you hesitate.")
        print("Game Over. You have lost.")


# Start the game
start_adventure()