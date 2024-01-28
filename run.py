import os
import re
import time
from classes.player import Player
from classes.battle import Battle
from colorama import Fore, Back, Style
import pyfiglet

error_colour = Back.RED + Fore.WHITE
reset_styling = Style.RESET_ALL
game_notification = Back.BLUE + Fore.GREEN
proffessor_oak = (Style.RESET_ALL + Fore.GREEN + "Proffessor Oak: "
                  + Style.RESET_ALL)


def game_restart(user1, user2):
    # player 1 and 2 names
    player_1 = user1
    player_2 = user2

    while True:
        # gets the name for player 2
        try:
            play_again = input(proffessor_oak + "Well I hope you had fun "
                               f"{player_1}, do you want to try again: " 
                               + reset_styling).lower().replace(" ", "")
            # checks their is a value
            if play_again.lower() not in ['yes', 'no']:
                raise ValueError(error_colour + "Proffessor Oak: Oop, Sorry I need a Yes "
                                 "or No answer, why not try again" + reset_styling)
            break
        except ValueError as e:
            # prints error message
            print(f"{e}")

    if play_again == "yes":
        while True:
            # gets the name for player 2
            try:
                npc_needed = input(proffessor_oak + "Excellent, do you wish "
                                   "to play against a human player? " + reset_styling
                                   ).lower().replace(" ", "")
                # checks their is a value
                if npc_needed.lower() not in ['yes', 'no']:
                    raise ValueError(error_colour + "Proffessor Oak: Oop, Sorry I need a Yes "
                                     "or No answer, why not try again" + reset_styling)
                break
            except ValueError as e:
                # prints error message
                print(f"{e}")
        if npc_needed == "yes":
            while True:
                # gets the name for player 2
                try:
                    user_name2 = input(proffessor_oak + "Excellent, what is "
                                       "your friends name: " + reset_styling
                                       ).capitalize().replace(" ", "")
                    # checks their is a value
                    if not user_name2:
                        raise ValueError(error_colour + "Oops seems you forgot to"
                                         " enter your name, why not try again" + reset_styling)
                    # checks the value is in the correct format
                    elif not re.match("^[A-Za-z]+$", user_name2):
                        raise ValueError(error_colour + "Proffessor Oak: Oops seems you "
                                         "entered a number, why not try again" + reset_styling)
                    break
                except ValueError as e:
                    # prints error message
                    print(f"{e}")
            # player 2 becomes the PC
            play_game(player_1, user2=user_name2, human=True)
        else:
            print(proffessor_oak + "No worries you can fight against John")
            # player 2 becomes the PC
            play_game(player_1, user2="John", human=False)
    else:
        print(proffessor_oak + "No worries come back any time")
        end_game_text = pyfiglet.figlet_format("Game End",
                                               font="banner3-D",
                                               justify="center")
        print(end_game_text)


def play_game(user1, user2, human):
    # stores players names
    player_1 = user1
    player_2 = user2

    subhead_pick_pokemon = pyfiglet.figlet_format("Pokemon Picker",
                                                  font="slant",
                                                  justify="center")
    print(subhead_pick_pokemon)
    print("-----------------------------------------------------")
    print(f"{proffessor_oak} Now, {player_1.capitalize()} choose your pokemon")
    print("-----------------------------------------------------")
    # creates player1 object
    player1 = Player(name=player_1, is_human=True)
    # method called for player1 to choose the pokemon they wish to battle with
    pokemon_battle_player1 = player1.pick_pokemon()
    print(proffessor_oak + f"That is you sorted {player_1.capitalize()}, "
          "you've choosen your pokemon" + reset_styling)
    print(subhead_pick_pokemon)
    print("-----------------------------------------------------")
    print(f"{proffessor_oak} Now, {player_2.capitalize()} choose your pokemon")
    print("-----------------------------------------------------")
    # creates players object
    player2 = Player(name=player_2, is_human=human)
    # method called for player2 to choose the pokemon they wish to battle with
    pokemon_battle_player2 = player2.pick_pokemon()
    print(proffessor_oak + f"That is you sorted {player_2.capitalize()}, "
          "you've choosen your pokemon" + reset_styling)
    time.sleep(3)
    os.system("clear")
    print(proffessor_oak + "Excellent you've both now choosen your pokemon, "
          "lets go to to battle arena")
    # creates battle area from Battle Class
    battle = Battle(player1, player2)
    # lets palyers choose which pokemon to start the battle with
    battle.fight_setup()
    # starts the actually battle
    battle.battle_stadium()
    battle_end_message = pyfiglet.figlet_format("Battle Finished",
                                                  font="slant",
                                                  justify="center")
    print(battle_end_message)
    # print(game_notification + "battle finished" + reset_styling)
    # asks user if they wish to restart and play again
    # pass player 1 and 2 name
    game_restart(player_1, player_2)


def game_start():
    title_text = pyfiglet.figlet_format("Pokemon Battle Arena",
                                        font="banner3-D",
                                        justify="center")
    print(f"{Fore.GREEN}{title_text}\n")
    print("Proffessor Oak: welcome to pokemon battle area "
          "where trainers are tested")
    print("-----------------------------------------------------")
    while True:
        try:
            # askes for users name
            user_name = input(proffessor_oak + " What is your name young man? "
                              ).capitalize().replace(" ", "")
            # checks their is a value
            if not user_name:
                raise ValueError(error_colour + "Proffessor Oak: Oops seems "
                                 " you forgot to enter your name, why "
                                 "not try again" + reset_styling)
            # checks the value is just letters
            elif not re.match("^[A-Za-z]+$", user_name):
                raise ValueError(error_colour + "Proffessor Oak: Oops seems "
                                 "you entered a number, why not try again"
                                 + reset_styling)
            break
        except ValueError as e:
            # prints error message
            print(f"{e}")

    while True:
        # gets the name for player 2
        try:
            pc_check = input(proffessor_oak + f" Well hello {user_name}, "
                             "its nice to meet you, did you bring a friend "
                             "to fight agaisnt?: ").lower().replace(" ", "")
            # checks their is a value
            if not pc_check:
                raise ValueError(error_colour + "Proffessor Oak: Oops seems "
                                 "you forgot to write Yes or No, why not"
                                 " try again" + reset_styling)
            # checks the value is in the correct format
            elif pc_check.lower() not in ['yes', 'no']:
                raise ValueError(error_colour + "Proffessor Oak: Oops sorry i"
                                 " didn't understand, was that a"
                                 " 'yes' or 'no' " + reset_styling)
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
                user_name2 = input(proffessor_oak + " Hello friend, whats "
                                   " your name be? "
                                   ).capitalize().replace(" ", "")
                # checks their is a value
                if not user_name2:
                    raise ValueError(error_colour + "Proffessor Oak: Oops "
                                     "seems you forgot to enter your name, "
                                     "why not try again" + reset_styling)
                # checks the value is in the correct format
                elif not re.match("^[A-Za-z]+$", user_name2):
                    raise ValueError(error_colour + "Proffessor Oak: Oops "
                                     " seems you entered a number, why not "
                                     "try again" + reset_styling)
                # passed to play game as used when picking battle pokemon party
                human_player = True
                print(proffessor_oak + f" Well Hello {user_name} and "
                      f"{user_name2}, welcome my names professor oak and "
                      "I hope your ready to fight")
                break
            except ValueError as e:
                # prints error message
                print(f"{e}")
    else:
        user_name2 = "John"
        human_player = False
        print(proffessor_oak + f" Well hello {user_name}, welcome my names "
              "professor oak and I hope your ready to fight we have your "
              f"oppointent {user_name2} ready and waiting")

    print(Fore.GREEN +
          "*********************start insert rules of game*******************")
    print("content")
    print(Fore.GREEN +
          "********************* end insert rules of game********************")
    print(reset_styling)

    play = " "

    # asks user if they are ready to fight
    while True:
        try:
            play = input(proffessor_oak + " Enter 'fight' when your ready to "
                         "contiune or 'exit' to exit the "
                         "game: ").lower().replace(" ", "")
            # checks their is a value
            if play.lower() not in ['fight', 'exit']:
                raise ValueError(error_colour + "Proffessor Oak: Oops, close "
                                 "but I need an answer, either fight or "
                                 "exit" + reset_styling)
            elif play == "fight":
                print(proffessor_oak + " Great!, now lets pick your pokemon: ")
                time.sleep(2.5)
                os.system("clear")
                play_game(user1=user_name,
                          user2=user_name2,
                          human=human_player)
                break
            else:
                # prints if user states no
                print(proffessor_oak + " Ok see you next time")
                end_game_text = pyfiglet.figlet_format("Game End",
                                                       font="banner3-D",
                                                       justify="center")
                print(end_game_text)
                break
        except ValueError as e:
            # prints error message
            print(f"{e}")


game_start()
