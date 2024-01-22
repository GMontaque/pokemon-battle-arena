import os
import re
import time
from classes.player import Player
from classes.battle import Battle

def game_restart(user1,user2):
    # player 1 and 2 names
    player_1 = user1
    player_2 = user2
    
    while True:
        # gets the name for player 2
        try:
            play_again = input(f"Proffessor Oak: Well I hope you had fun {player_1}, do you want to try again: ")
            # checks their is a value
            if play_again.lower() not in ['yes', 'no']:
                raise ValueError("Proffessor Oak: Oop, Sorry I need a Yes or No answer, why not try again")
            break
        except ValueError as e:
            # prints error message
            print(f"{e}")

    if play_again == "yes":
        while True:
            # gets the name for player 2
            try:
                npc_needed = input(f"Proffessor Oak: Excellent, do you wish to play against a human player? ")
                # checks their is a value
                if npc_needed.lower() not in ['yes', 'no']:
                    raise ValueError("Proffessor Oak: Oop, Sorry I need a Yes or No answer, why not try again")
                break
            except ValueError as e:
                # prints error message
                print(f"{e}")
        if npc_needed == "no":
            print("Proffessor Oak: No worries you can fight against John")
            # player 2 becomes the PC
            play_game(player_1, user2= "John", human= False)
        else:
            play_game(player_1, player_2, human= True)       
    else:
        print("Proffessor Oak: No worries come back any time")
  

def play_game(user1, user2, human):
    # stores players names
    player_1 = user1
    player_2 = user2

    # creates player1 object
    player1 = Player(name=player_1, is_human=True)
    # method called for player1 to choose the pokemon they wish to battle with
    pokemon_battle_player1 = player1.pick_pokemon()
    print(f"{player_1} picked {pokemon_battle_player1}")
    print("------------------------------------------------")
    print(f"Proffessor Oak: Now, {player_2} choose your pokemon")
    print("------------------------------------------------")
    # creates players object
    player2 = Player(name=player_2, is_human=human)
    # method called for player2 to choose the pokemon they wish to battle with
    pokemon_battle_player2 = player2.pick_pokemon()
    print(f"{player_2} picked {pokemon_battle_player2}")

    print("Proffessor Oak: Excellent you've both now choosen your pokemon, lets"
          " go to to battle arena")
    # creates battle area from Battle Class
    battle = Battle(player1, player2)
    # lets palyers choose which pokemon to start the battle with
    battle.fight_setup()
    # starts the actually battle
    battle.battle_stadium()
    print("battle finished")
    # asks user if they wish to restart and play again
    # pass player 1 and 2 name
    game_restart(player_1,player_2)


def game_start():
    print("Proffessor Oak: welcome to pokemon battle area "
          "where trainers are tested")
    while True:
        try:
            # askes for users name
            user_name = input("Proffessor Oak: what is your name young man? ").capitalize()
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
                                 "write Yes or No, why not try again")
            # checks the value is in the correct format
            elif pc_check.lower() not in ['yes', 'no']:
                raise ValueError("Proffessor Oak: Oops sorry i didn't "
                                 "understand, was that a 'yes' or 'no' ")
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
                user_name2 = input("Hello friend, whats your name be? ").capitalize()
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
                print(f"Proffessor Oak: Well hello {user_name} and "
                      f"{user_name2}, welcome my names professor oak and "
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

    # asks user if they are ready to fight
    while True:
        try:
            play = input("Proffessor Oak: Enter 'fight' when your ready to "
                         "contiune or 'exit' to exit the game: ")
            # checks their is a value
            if play.lower() not in ['fight', 'exit']:
                raise ValueError("Proffessor Oak: Oops, close but I need an "
                                 "answer, either fight or exit")
            elif play == "fight":
                print("Proffessor Oak: Great!, now lets pick your pokemon: ")
                time.sleep(2.5)
                os.system("clear")
                play_game(user1=user_name,
                          user2=user_name2,
                          human=human_player)
                break
            else:
                # prints if user states no
                print("Proffessor Oak: Ok see you next time")
                break
        except ValueError as e:
            # prints error message
            print(f"{e}")


game_start()
