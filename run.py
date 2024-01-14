import re
from classes.player import Player
from classes.battle import Battle


def play_game(user1, user2, npc):
    # stores players names
    player_1 = user1
    player_2 = user2

    # creates a player object for each player
    player1 = Player(name=player_1, is_human=True)
    player2 = Player(name=player_2, is_human=npc)
    # player choose the pokemon they will battle with
    print("Proffessor Oak: Great!, now lets pick your pokemon: ")
    pokemon_battle_player1 = player1.pick_pokemon()
    print(f"{player_1} picked {pokemon_battle_player1}")
    print("------------------------------------------------")
    print(f"Proffessor Oak: Now, {player_2} choose your pokemon")
    print("------------------------------------------------")
    pokemon_battle_player2 = player2.pick_pokemon()
    print(f"{player_2} picked {pokemon_battle_player2}")
    print(player1.name)
    print(player2.name)

    print("Proffessor Oak: Excellent you've both choosen now they"
          " go to to battle arena")
    battle = Battle(player1, player2)
    battle.fight_setup()
    battle.battle_stadium()


def game_start():
    print("Proffessor Oak: welcome to pokemon battle area "
          "where trainers are tested")
    while True:
        try:
            # askes for users name
            user_name = input("Proffessor Oak: what is your name young man? ")
            # checks their is a value
            if not user_name:
                raise ValueError("Proffessor Oak: Oops seems you forgot to"
                                 " enter your name, why not try again")
            # checks the value is just letters
            elif not re.match("^[A-Za-z]+$", user_name):
                raise ValueError("Proffessor Oak: Oops seems you entered a"
                                 " number, why not try again")
            break
        except ValueError as e:
            # prints error message
            print(f"{e}")

    while True:
        # gets the name for player 2
        try:
            pc_check = input(f"Proffessor Oak: Well hello {user_name}, "
                             "its nice to meet you, did you bring a friend "
                             "to fight agaisnt?: ")
            # checks their is a value
            if not pc_check:
                raise ValueError("Proffessor Oak: Oops seems you forgot to "
                                 "enter your name, why not try again")
            # checks the value is in the correct format
            elif pc_check.lower() not in ['yes', 'no']:
                raise ValueError("Proffessor Oak: Oops sorry i didn't "
                                 "understnad, was that a 'yes' or 'no' ")
            break
        except ValueError as e:
            # prints error message
            print(f"{e}")

    ''' checks if answer to pc_check is true and user wants to
        play 2 palyer or against a pc'''
    if pc_check == "yes":
        while True:
            try:
                # asks for players 2's name
                user_name2 = input("Hello friend, whats your name be? ")
                # checks their is a value
                if not user_name2:
                    raise ValueError("Proffessor Oak: Oops seems you forgot "
                                     "to enter your name, why not try again")
                # checks the value is in the correct format
                elif not re.match("^[A-Za-z]+$", user_name2):
                    raise ValueError("Proffessor Oak: Oops seems you entered "
                                     "a number, why not try again")
                # passed to play game as used when picking battle pokemon party
                human_player = True
                print(f"Proffessor Oak: Well hello {user_name2} and "
                      f"{user_name}, welcome my names professor oak and "
                      "I hope your ready to fight")
                break
            except ValueError as e:
                # prints error message
                print(f"{e}")
    else:
        user_name2 = "John"
        human_player = False
        print(f"Proffessor Oak: Well hello {user_name}, welcome my names "
              "professor oak and I hope your ready to fight we have your "
              f"oppointent {user_name2} ready and waiting")

    print("*********************start insert rules of game*******************")
    print("content")
    print("********************* end insert rules of game********************")

    play = " "

    # play_game()
    # asks user if they are ready to fight
    while play.lower() not in ['fight', 'exit']:
        try:
            play = input("Proffessor Oak: Enter 'fight' when your ready to "
                         "contiune or 'exit' to exit the game: ")
            # checks their is a value
            if play.lower() not in ['fight', 'exit']:
                raise ValueError("Proffessor Oak: Oops, close but I need an "
                                 "answer, either fight or exit")
            elif play == "fight":
                play_game(user1=user_name, user2=user_name2, npc=human_player)
            else:
                # prints if user states no
                print("Proffessor Oak: Ok see you next time")
        except ValueError as e:
            # prints error message
            print(f"{e}")


game_start()
