import re
from classes.player import Player

def play_game(user1,user2,npc):
    # stores players names
    player_1 = user1
    player_2 = user2

    # creates a player object for each player
    player1 = Player(name=player_1,is_human=True)
    player2 = Player(name=player_2,is_human=npc)
    
    # player choose the pokemon they will battle with
    print("Proffessor Oak: Great!, now lets pick your pokemon: ")
    pokemon_battle_player1 = player1.pick_pokemon()
    print(f"{player_1} picked {pokemon_battle_player1}")
    print("------------------------------------------------")
    print("Proffessor Oak: Now, player 2 choose your pokemon")
    print("------------------------------------------------")
    pokemon_battle_player2 = player2.pick_pokemon()
    print(f"{player_2} picked {pokemon_battle_player2}")
    
    print(player1.name)
    print(player2.name)

def game_start():
    print("Proffessor Oak: welcome to pokemon battle area where trainers are tested")
    while True:
        try:
            user_name = input("Proffessor Oak: what is your name young man? ")
            if not user_name:
                raise ValueError("Proffessor Oak: Oops seems you forgot to enter your name, why not try again")
            elif not re.match("^[A-Za-z]+$", user_name):
                raise ValueError("Proffessor Oak: Oops seems you entered a number, why not try again")
            break
        except ValueError as e:
            print(f"{e}")

    while True:
        try:
            pc_check = input(f"Proffessor Oak: Well hello {user_name}, its nice to meet you, did you bring a friend to fight agaisnt?: ")
            if not pc_check:
                raise ValueError("Proffessor Oak: Oops seems you forgot to enter your name, why not try again")
            elif pc_check.lower() not in ['yes', 'no']:
                raise ValueError("Proffessor Oak: Oops sorry i didn't understnad, was that a 'yes' or 'no' ")
            break
        except ValueError as e:
            print(f"{e}")        

    

    if pc_check == "yes":
        while True:
            try:
                user_name2 = input("Hello friend and what might your name be? ")
                if not user_name2:
                    raise ValueError("Proffessor Oak: Oops seems you forgot to enter your name, why not try again")
                elif not re.match("^[A-Za-z]+$", user_name2):
                    raise ValueError("Proffessor Oak: Oops seems you entered a number, why not try again")
                human_player = True
                print(f"Proffessor Oak: Well hello {user_name2} and {user_name}, welcome my names professor oak and I hope your ready to fight")
                break
            except ValueError as e:
                print(f"{e}")
    else:
        user_name2 = "John"
        human_player = False
        print(f"Proffessor Oak: Well hello {user_name}, welcome my names professor oak and I hope your ready to fight we have your oppointent {user_name2} ready and waiting")
    
    print("*********************start insert rules of game********************")
    print("content")
    print("********************* end insert rules of game********************")

    play = " "

    # play_game()
    while play.lower() not in ['fight', 'exit']:
        try:
            play = input("Proffessor Oak: Enter 'fight' when your ready to contiune or 'exit' to exit the game: ")
            if play.lower() not in ['fight', 'exit']:
                    raise ValueError("Proffessor Oak: Oops, close but I need an answer, either fight or exit")
            elif play == "fight":
                play_game(user1= user_name,user2= user_name2,npc=human_player)
            else:
                print("Proffessor Oak: Ok see you next time")
        except ValueError as e:
            print(f"{e}")

game_start()
