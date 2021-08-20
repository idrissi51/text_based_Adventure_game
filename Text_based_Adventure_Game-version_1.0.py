# Text-based Adventure Game


print("Game is Started")

text_one = """
Do you want to go to the right or to the left?
Type r to right
     l to left
"""


def opt_r():
    z = 10
    while z > 0:
        print("monster_room\nchoose number(1 or 2)")
        x = int(input("=> "))

        if x == 1:
            z = 10
            while z > 0:
                print("diamond_room\nchoose number(1 or 2)")
                y = int(input("=> "))
                if y == 2:
                    print("WOOOOW!! You Win")
                    z = 0
                elif y == 1:
                    print("Game_over")
                    z = 0
                else:
                    print("please choose the appropriate number" if z >
                          1 else "Game over")
                    z -= 1
        elif x == 2:
            print("Game_Over")
            break
        else:
            print("please choose the appropriate number" if z > 1 else "Game over")
            z -= 1


def opt_l():
    z = 10
    while z > 0:
        print("bear_room\nchoose number(1 or 2)")
        x = int(input("=> "))

        if x == 2:
            z = 10
            while z > 0:
                print("diamond_room\nchoose number(1 or 2)")
                y = int(input("=> "))
                if y == 2:
                    print("WOOOOW!! You Win")
                    z = 0
                elif y == 1:
                    print("Game_over")
                    z = 0
                else:
                    print("please choose the appropriate number" if z >
                          1 else "Game over")
                    z -= 1
        elif x == 1:
            print("Game_Over")
            break
        else:
            print("please choose the appropriate number" if z > 1 else "Game over")
            z -= 1


z = 10
while z > 0:
    print(text_one)
    option1 = input("=> ").lower().strip()
    if option1 == "r":
        opt_r()
        z = 0
    elif option1 == "l":
        opt_l()
        z = 0
    else:
        print("please choose the appropriate option" if z > 1 else "Game over")
        z -= 1
