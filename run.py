import re
from classes.player import Player

player1 = Player(name="steve",is_human=True)
player2 = Player(name="steve",is_human=True)

def play_game():
    print("game is running")
    print("please select which pokemon you want to fight with: ")
    player1.pick_pokemon()
    player2.pick_pokemon()



def game_start():
    print('''Proffessor Oak: welcome to pokemon battle area where trainers are tested''')
    while True:
        try:
            user_name = input("Proffessor Oak: what is your name player? ")
            if not user_name:
                raise ValueError("Proffessor Oak: Oops seems you forgot to enter your name, why not try again")
            elif not re.match("^[A-Za-z]+$", user_name):
                raise ValueError("Proffessor Oak: Oops seems you entered a number, why not try again")
            print(f"Proffessor Oak: Hello {user_name}, welcome my names professor oak, I hope your ready to fight")
            print("*********************start insert rules of game********************")
            print("content")
            print("********************* end insert rules of game********************")
            break
        except ValueError as e:
            print(f"Error: {e}")

    play = " "

    # play_game()
    while play.lower() not in ['fight', 'exit']:
        try:
            play = input("Enter fight when your ready to contiune or 'exit' to exit the game: ")
            if play.lower() not in ['fight', 'exit']:
                    raise ValueError("Proffessor Oak: Oops, close but I need an answer, either fight or exit")
            elif play == "fight":
                play_game()
            else:
                print("Proffessor Oak: Ok see you next time")
        except ValueError as e:
            print(f"Error: {e}")

game_start()
