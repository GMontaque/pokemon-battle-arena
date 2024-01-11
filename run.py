import re
from classes.player import Player

def play_game(user1,user2):
    # stores players names
    player_1 = user1
    player_2 = user2

    # creates a player object for each player
    player1 = Player(name=player_1,is_human=True)
    player2 = Player(name=player_2,is_human=True)
    
    # player choose the pokemon they will battle with
    print("Proffessor Oak: Great!, now lets pick your pokemon: ")
    pokemon_battle_player1 = player1.pick_pokemon()
    print("------------------------------------------------")
    print("Proffessor Oak: Now, player 2 choose your pokemon")
    print("------------------------------------------------")
    pokemon_battle_player2 = player1.pick_pokemon()
    print(f"{player_1} picked {pokemon_battle_player1}, and {player_2} picked {pokemon_battle_player2}")
    
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

    print(f"Proffessor Oak: Well hello {user_name}, its nice to meet you, I see you also brought a friend")

    while True:
        try:
            user_name2 = input("Hello friend and what might your name be? ")
            if not user_name2:
                raise ValueError("Proffessor Oak: Oops seems you forgot to enter your name, why not try again")
            elif not re.match("^[A-Za-z]+$", user_name2):
                raise ValueError("Proffessor Oak: Oops seems you entered a number, why not try again")
           
            break
        except ValueError as e:
            print(f"{e}")

    print(f"Proffessor Oak: Well hello {user_name2} and {user_name}, welcome my names professor oak and I hope your ready to fight")
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
                play_game(user1= user_name,user2= "John")
            else:
                print("Proffessor Oak: Ok see you next time")
        except ValueError as e:
            print(f"{e}")

game_start()
