def game_start():
    '''
    inital game function
    called when game starts
    Gets the users name and provides them with the rules of the game
    '''
    print('''welcome to pokemon battle area where trainers are tested''')
    name = input("what is your name player: ")
    print(f"Hello {name}, welcome my names professor oak are you I hope your ready")
    print("*********************start insert rules of game********************")
    print("content")
    print("********************* end insert rules of game********************")
    play = " "

    # play_game()
    while play.lower() not in ['yes', 'no']:
        play = input("Are you ready to fight'yes' or 'no': ")
        if play == "yes":
            print("play Game")
        else:
            print("ok see you next time")

game_start()