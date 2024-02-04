import os
import re
import time
from classes.player import Player
from classes.battle import Battle
from colorama import Fore, Back, Style
import pyfiglet

# global styling variables
error_colour = Back.RED + Fore.WHITE
reset_styling = Style.RESET_ALL
proffessor_oak = (Style.RESET_ALL + Fore.GREEN + "Proffessor Oak: "
                  + Style.RESET_ALL)


def game_restart(user1):
    '''
    This function is called when the battle function and battle stage is
    complete player 1 is asked if they wish to play again
    If yes they are asked if they wish to play again a human or PC player
    If a human player is choosen they are asked for user name, if PC
    name auto choosen
    '''
    # player 1 name
    player_1 = user1

    while True:
        # asks player one if they wish to play again
        try:
            play_again = input(proffessor_oak + "Well I hope you had fun "
                               f"{player_1}, will you play again?: "
                               + reset_styling).lower().replace(" ", "")
            # checks value is yes or no
            if play_again.lower() not in ['yes', 'no']:
                raise ValueError(error_colour + "Proffessor Oak: Oop, Sorry I"
                                 " need a Yes or No answer, why not try again"
                                 + reset_styling)
            break
        except ValueError as e:
            # prints error message
            print(f"{e}")
    # player 1 selected to play again
    if play_again == "yes":
        while True:
            # checks if user wants to play against pc or player
            try:
                npc_needed = input(proffessor_oak + "Excellent, do you wish "
                                   "to play against a human player? "
                                   + reset_styling
                                   ).lower().replace(" ", "")
                # checks value is yes or no
                if npc_needed.lower() not in ['yes', 'no']:
                    raise ValueError(error_colour + "Proffessor Oak: Oop, "
                                     "Sorry I need a Yes or No answer, why "
                                     "not try again" + reset_styling)
                break
            except ValueError as e:
                # prints error message
                print(f"{e}")
        # player 1 selected yes to playing with human player
        # asks for player 2 name
        if npc_needed == "yes":
            while True:
                # gets the name for player 2
                try:
                    user_name2 = input(proffessor_oak + "Excellent, what is "
                                       "your friends name: " + reset_styling
                                       ).capitalize().replace(" ", "")
                    # checks their is a value
                    if not user_name2:
                        raise ValueError(error_colour + "Oops seems you forgot"
                                         "to enter your name, why not try"
                                         " again" + reset_styling)
                    # checks the value is in the correct format
                    elif not re.match("^[A-Za-z]+$", user_name2):
                        raise ValueError(error_colour + "Proffessor Oak: Oops"
                                         " seems you entered a number, why not"
                                         " try again" + reset_styling)
                    break
                except ValueError as e:
                    # prints error message
                    print(f"{e}")
            print(proffessor_oak + "Excellent!, now let's pick your pokemon "
                  "to go battle with")
            # player 2 becomes human player
            play_game(player_1, user2=user_name2, human=True)
        else:
            # player 1 inputs no to play with human player
            print(proffessor_oak + "No worries you can fight against John")
            # player 2 becomes the PC
            play_game(player_1, user2="John", human=False)
    else:
        # player 1 select no and game ends, end game message shown
        print(proffessor_oak + "No worries come back any time")
        end_game_text = pyfiglet.figlet_format("Game End",
                                               font="banner3-D",
                                               justify="center")
        print(f"{Fore.CYAN}{Style.BRIGHT}{end_game_text}")


def play_game(user1, user2, human):
    '''
    function is used for the core of the game
    function asks each player to first pick their pokemon to fight with
    function will begin and run the battle phase
    when battle phase is complete function calls game_restart
    '''
    # stores players names
    player_1 = user1
    player_2 = user2

    # subhead pokemon picker
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
    time.sleep(2)
    print(subhead_pick_pokemon)
    print("-----------------------------------------------------")
    print(f"{proffessor_oak} Now, {player_2.capitalize()} choose your pokemon")
    print("-----------------------------------------------------")
    # creates player 2 object
    player2 = Player(name=player_2, is_human=human)
    # method called for player2 to choose the pokemon they wish to battle with
    pokemon_battle_player2 = player2.pick_pokemon()
    print(proffessor_oak + f"That is you sorted {player_2.capitalize()}, "
          "you've choosen your pokemon" + reset_styling)
    # confirmaiton message pokemon picking stage finished
    print(proffessor_oak + "Excellent you've both now choosen your pokemon,\n"
          "lets go to battle arena")
    time.sleep(5)
    os.system("clear")
    # subhead battle arena
    subhead_Battle_Arena = pyfiglet.figlet_format("Battle Arena",
                                                  font="slant",
                                                  justify="center")
    print(subhead_Battle_Arena)
    # creates battle arena from Battle Class
    battle = Battle(player1, player2)
    # lets pplayers choose which pokemon to start the battle with
    battle.fight_setup()
    # starts the battle
    battle.battle_stadium()
    # subhead end game message
    battle_end_message = pyfiglet.figlet_format("Battle Finished",
                                                font="slant",
                                                justify="center")
    print(battle_end_message)
    # end game function called, player 1 name passed
    # asked if they wish to restart and play again
    game_restart(player_1)


def game_start():
    '''
    This is the inital function which is called when the program runs
    In this function player 1 is asked for their name
    Player 1 is asked if player 2 is human or pc
    If palyer 2 is human then player 2 is asked for their name
    If palyer 2 is PC, name is auto selected and variable human set as False
    '''
    # main title
    title_text = pyfiglet.figlet_format("Pokemon Battle Arena",
                                        font="banner3-D",
                                        justify="center")
    print(f"{Fore.CYAN}{Style.BRIGHT}{title_text}")
    time.sleep(5)
    print("-----------------------------------------------------")
    print("Welcome to pokemon battle arena "
          "where trainers are tested" + reset_styling)

    # asks player 1 for their name
    while True:
        try:
            # askes for users name
            user_name = input(proffessor_oak + " What is your name young man? "
                              ).capitalize().replace(" ", "")
            # checks their is a value
            if not user_name:
                raise ValueError(error_colour + "Proffessor Oak: Oops seems "
                                 "you forgot to enter your name, why "
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
    # asks if player 1 brought a human friend to play with
    while True:
        try:
            pc_check = input(proffessor_oak + f" Well hello {user_name}, "
                             "its nice to meet you, did you bring\n a friend "
                             "to fight against?: ").lower().replace(" ", "")
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
        play against a human player or against a pc'''
    if pc_check == "yes":
        while True:
            try:
                # asks for players 2's name
                user_name2 = input(proffessor_oak + " Hello friend, whats"
                                   " your name? "
                                   ).capitalize().replace(" ", "")
                # checks their is a value
                if not user_name2:
                    raise ValueError(error_colour + "Proffessor Oak: Oops "
                                     "seems you forgot to enter your name, "
                                     "why not try again" + reset_styling)
                # checks the value is in the correct format
                elif not re.match("^[A-Za-z]+$", user_name2):
                    raise ValueError(error_colour + "Proffessor Oak: Oops "
                                     "seems you entered a number, why not "
                                     "try again" + reset_styling)
                ''' value from play game and used when picking pokemon
                for battle pack '''
                human_player = True
                print(proffessor_oak + f" Well hello {user_name} and "
                      f"{user_name2} welcome, my name is\n Professor Oak and "
                      "I hope your ready to fight\n")
                break
            except ValueError as e:
                # prints error message
                print(f"{e}")
    # player 1 inputed no and player 2 set as PC player
    else:
        # Player 2 PC name
        user_name2 = "John"
        # passed to play game and used when picking battle pokemon party
        human_player = False
        print(proffessor_oak + f" Well hello {user_name} and welcome, my "
              "name is Professor Oak and I hope your ready to fight we have "
              f"your oppointent {user_name2} ready and waiting\n")
    # game rules subhead
    game_rules = pyfiglet.figlet_format("Game Rules",
                                        font="slant",
                                        justify="center")
    print(Fore.GREEN +
          "**************************************************"
          + reset_styling)
    print(game_rules)
    # game rules text
    print(Fore.GREEN + '''
    Welcome trainers, you are about to enter the battle arena but before
    you do let's go over the rules.\n

    You will each have to pick 3 different Pokémon to battle with from a
    list of 10 Pokémon we have available to use but be careful trainers
    and choose wisely as you will find some Pokémon do double the damage
    to other types of Pokémon. Each Pokemon has a certain type and each
    Pokémon’s attack also has a type, meaning that if the defending
    Pokemonis of type water and your attack is of type electric your
    attack damage is increased by 40 hit points. So make sure that you
    review each Pokémon before selecting them, you can review a Pokemon
    by simply typing its name and the details of that Pokemon will
    appear. You will then be asked if you want to add that Pokemon to
    your battle pack.

    Once you have both chosen your 3 Pokémon you move onto the battle
    phase. You will first be asked to choose which of your 3 Pokémon you
    wish to fight with first, and then each player will take turns
    attacking. You will find that each Pokémon has 4 attacks and it’s up
    to you to choose which attack you wish to do, you select an attack by
    typing in the number next to the attack name.

    If your Pokémon faints and can’t carry on, you can then select a new
    Pokémon but be careful as if all your Pokémon faint you will lose
    the game.

    But not to worry as once the battle phase is over you always have
    the option to play again, maybe against another player or the
    same player.
        ''')
    print(Fore.GREEN +
          "**************************************************")
    print(reset_styling)

    # stores user choice if they wish to play
    play = " "

    # asks user if they are ready to fight
    while True:
        try:
            play = input(proffessor_oak + " Enter 'fight' when your ready to "
                         "contiune or 'exit' to\n exit the "
                         "game after you have read the rules above: "
                         ).lower().replace(" ", "")
            # checks their is a value
            if play.lower() not in ['fight', 'exit']:
                raise ValueError(error_colour + "Proffessor Oak: Oops, close "
                                 "but I need an answer, either fight or "
                                 "exit" + reset_styling)
            # game proceeds and calls play_game
            elif play == "fight":
                print(proffessor_oak + " Great!, now lets pick your pokemon")
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
                print(f"{Fore.CYAN}{Style.BRIGHT}{end_game_text}")
                break
        except ValueError as e:
            # prints error message
            print(f"{e}")


game_start()
