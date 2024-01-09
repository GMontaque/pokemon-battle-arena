
def play_game():
    global pl_pokemon
    print("game is running")
    print("please select which pokemon you want to fight with: ")



def game_start():
    print('''welcome to pokemon battle area where trainers are tested''')
    name = input("what is your name player: ")
    # name = "steve"
    print(f"Hello {name}, welcome my names professor oak are you I hope your ready")
    print("*********************start insert rules of game********************")
    print("content")
    print("********************* end insert rules of game********************")
    play = " "

    # play_game()
    while play.lower() not in ['yes', 'no']:
        play = input("Are you ready to fight'yes' or 'no': ")
        if play == "yes":
            play_game()
        else:
            print("ok see you next time")

game_start()