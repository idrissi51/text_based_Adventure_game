
# The Game

def start():
    print("start")
    print("There is a door to your left and right, which one do you take? (l or r)")
    opt = input("=> ").lower().strip()
    if opt == "r":

        monster_room()

    elif opt == "l":

        bear_room()

    else:
        print("wrong choice")
        game_over()


def bear_room():
    text = """
    There is a bear here
    Here two doors 1 and 2
    choose one 
    """
    print(text)
    choose = int(input("=> "))
    if choose == 1:
        game_over()
    elif choose == 2:
        diamond_room()
    else:
        print("wrong choice")
        game_over()


def monster_room():
    text = """
    Now you entered the room of a monster!
    Here two doors 1 and 2
    choose one 
    """
    print(text)
    choose = int(input("=> "))
    if choose == 1:
        diamond_room()
    elif choose == 2:
        game_over()
    else:
        print("wrong choice")
        game_over()


def diamond_room():
    text = """
    You are now in a room filled with diamonds!
    Here two doors 1 and 2
    choose one 
    """
    print(text)
    choose = int(input("=> "))
    if choose == 1:
        game_over()
    elif choose == 2:
        win()
    else:
        print("wrong choice")


def game_over():
    print("Game over")
    print("Do You want to play again? (y or n)")
    choose = input("=> ").lower().strip()
    if choose == "y":
        start()
    elif choose == "n":
        print("Good bye")
        exit()
    else:
        print("wrong choice")
        game_over()


def win():
    print("WOW!! You win")
    game_over()


start()
