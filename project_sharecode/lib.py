def try_me():

    import random


    def game(choice):
        options = ["rock", "paper", "scissors"]
        bot = random.choice(options)
        if choice == "rock" and bot == "scissors":
            print("You chose rock and I played scissors, YOU WIN! Press c to continue [c]")
        elif choice == "rock" and bot == "paper":
            print(" You chose rock and I played paper, YOU LOSE!")
        elif choice == "rock" and bot == "rock":
            print("we chose the same thing...")
        elif choice == "paper" and bot == "paper":
            print("we chose the same thing.")
        elif choice == "paper" and bot == "scissors":
            print("You chose paper and i chose scissors, YOU LOSE!")
        elif choice == "paper" and bot == "rock":
            print("You chose paper and i chose rock, YOU WIN! Press c to continue [c]")
        elif choice == "scissors" and bot == "scissors":
            print("We chose the same thing")
        elif choice == "scissors" and bot == "paper":
            print("You chose scissors and i chose paper, YOU WIN!")
        elif choice == "scissors" and bot == "rock":
            print("You chose scissors and i chose rock, YOU LOSE!")


    def again(x):
        if x == "y":
            game(input("rock, paper or scissors? "))
            again(input("play again? y / n. "))
        elif x == "c":
            print("You can open the door")
        else:
            print("goodbye")


    snow = str("You end up in a snowy storm, you walk and walk for hours until you reach a forest")
    sun = str("You end up in a vast desert, as you walk for hours you see an oasis. You have a drink and notice a door" +
            " with warning signs. ")
    name = input("Hello adventurer what is you name ? ")
    print(name + " you are about to go on an adventure, are you ready ?\nToo late it has already started.")
    print("You wake up dizzy in an empty white room, while looking around you find 2 doors.")
    beginning = input("One has a sun on it the other a moon, which door would you like to open ?[sun/moon]")
    if beginning == "sun":
        print(sun)
        sun1 = input("What do you want to do ? [enter/wait]")
        if sun1 == "wait":
            print("You waited for ages and nothing happened. GAME OVER !!!")
        elif sun1 == "enter":
            print("You enter a dark tunnel lit only by torches. You keep on walking and find 2 doors." +
                "The first door is filled with lions that haven't eaten in months.\nThe second one is filled with traps.")
            sun2 = input("Which door do you choose? [lions/traps]")
            if sun2 == "traps":
                print("You walk into a trap. GAME OVER !!!")
            elif sun2 == "lions":
                print("The lions have been dead for months you walk across the room safely.")
                print("You reach an enormous golden door with diamonds ornaments, an old man sits in front of" +
                    " it and tells you:" + "\n*I am the guardian of the door to continue you have to beat me...*")

            game(input("rock, paper or scissors? "))

            again(input("play again? [y / n] "))

            print("You enter the room and it's filled with gold and precious stones,\n in the middle of the room " +
                "you can see a beautiful chest and you know you've reached the end of your adventure...")
            sun3 = input("What do you want to do? Open the chest or leave? [open/leave]")
            if sun3 == "leave":
                print("You stopped right before fining the most incredible treasure, what a shame ...")
            elif sun3 == "open":
                print("You open the chest and find a golden inscription: The biggest treasure is :\n...")
                print("SEND NUDES!!!")

    elif beginning == "moon":
        print(snow)
        snow1 = input("What do you want to do ? Light a fire and rest or keep walking in the forest ?[fire/walk]")
        if snow1 == "fire":
            print("You fall asleep by the warmth of the fire and wild beasts attack you.\nGAME OVER!!!")
        elif snow1 == "walk":
            print("You arrive before a research station you get in and the room is warm and cozy." + "\nYou fell asleep and"
                + " when you wake up you explore the room to find a passage behind a shelf.")
            print("You walk in the tunnel and stumble before 2 doors with inscriptions on them:")
            snow2 = input("One room is warmed by the sun and if you get in you'll burn, the second one" +
                        " is filled with venomous snakes.\nWhich room do you choose? [snake/sun]")
            if snow2 == "snake":
                print("You walk into the room and a snake bites you. You're dead.\nGAME OVER!!!")
            elif snow2 == "sun":
                print("The sun is setting and as you walk into the sun room you find a big computer.")
                print("You can read on the screen: toss this dice if you get above 4,\nI'll tell you the secret of the" +
                    " universe.")


    def game2(toss):
        options = ["1", "2", "3", "4", "5", "6"]
        bot = random.choice(options)
        print(bot)
        if toss == "t" and bot == "4":
            print("You can access the computer press c [c]")
        elif toss == "t" and bot == "5":
            print("You can access the computer press c [c]")
        elif toss == "t" and bot == "6":
            print("You can access the computer press c [c]")


    def again2(a):

        if a == "y":
            game2(input("Toss dice [t] "))
            again2(input("play again? y / n. "))
        elif a == "c":
            print("The secret of the universe is :\n...\n42")
        else:
            print("goodbye")


    game2(input("Toss dice [t] "))


    again2(input("play again? [y / n] "))
