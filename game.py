def intro():
    print("Welcome to the Dungeon Adventure!")
    print("You are standing at the entrance of a dark and mysterious dungeon.")
    print("Your goal is to escape, but the path is filled with choices.")
    print("Make the right decisions to find your way out!")
    print("--------------------------------------------------")

def room_1():
    print("You are in a dimly lit hallway. There are two doors in front of you.")
    print("One door is to your left and the other is to your right.")
    choice = input("Do you choose to go left or right? ").lower()

    if choice == "left":
        print("You entered a room filled with treasure! Congratulations, you've won the game!")
        return False
    elif choice == "right":
        print("You walk into a dark room, and the door locks behind you. It's a dead end!")
        return True
    else:
        print("Invalid choice. Try again!")
        return True

def room_2():
    print("You are in a room with a strange glowing stone in the center.")
    print("There's a door to the north and a ladder leading down.")
    choice = input("Do you go through the door to the north or climb down the ladder? ").lower()

    if choice == "north":
        print("The door opens, but you find yourself surrounded by enemies. Game over!")
        return False
    elif choice == "down":
        print("You descend into a cave and find a hidden exit. You've escaped the dungeon!")
        return False
    else:
        print("Invalid choice. Try again!")
        return True

def game():
    intro()
    game_over = False
    while not game_over:
        print("You are in the first room of the dungeon.")
        game_over = room_1()
        
        if not game_over:
            break  # End the game if the player won in room_1
        
        print("You are now in the second room of the dungeon.")
        game_over = room_2()

        if not game_over:
            break  # End the game if the player escaped in room_2
        
    print("Thanks for playing!")

game()