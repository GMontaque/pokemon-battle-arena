class Player:
    def __init__(self,**kwargs):
        self.name = kwargs["name"]
        self.is_human = kwargs["is_human"]


    def pick_pokemon(self):
        print('''
        please choose a pokemon numer 0 to 2

        [0]: squirtle

        [1]: charmander

        [2]: bulbasaur
        
        ''')
        seleceted = -1
        while seleceted == -1:
            seleceted = int(input("choose a pokemon: "))
        
