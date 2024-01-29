# Pokemon Battle Arena

## About the Project

![picture of initial game screem](assets/img/)

- I have taken inspiration for creating this game from the very popular Pokémon franchise – the aim of which is to build up your skills, catch new Pokémon and battle other trainers with the Pokémon you catch.

- The specific game that I have created is just the battle part, where a player is given the option to fight against another player, or they can play against the PC. I have included an additional feature, in that each player or PC is given the option to choose their battle Pokémon from a pre-defined list which also contains details of the Pokémon. This is important as the attacks executed depend on the Pokémon type that the player has chosen, and the Pokémon type they are fighting. This means the player will need to choose strategically.

- A player is given the option to review a number of different Pokémon. When reviewing the Pokémon, the information provided displays the Pokémon type, includes a description which explains the Pokémon along with their name and the attack moves that they can do. This then allows the user to make an informed decision as to the Pokémon they want to use in their battle party. Once the user has chosen their Pokémon, they are taken to the battle area which is where the actual battle takes place between the selected Pokémon. The battle arena first starts by each player picking an initial Pokémon to fight with, then each player will take turns to complete an attack until one of the players’ Pokémon has a health of 0 (fainted). When the players’ Pokémon faints, they are then asked to select another Pokémon from their battle party to continue the fight. When a player has no more Pokémon in their party, the game finishes and the user can either play again or exit the game. If they wish to play again, they will be asked if this is against a human player or the PC.

[Live Website Link](https://pokemon-battle-arena-52c50ec4c2a7.herokuapp.com/)

## Target Audience

**What was the idea behind building the product?**

- To allow users to play a fun enjoyable game.
- To allow users to regain some nostalgia and engage people.
- Create a simple game that can be picked up and played.
- Create a game that the users will want to keep returning to play.
- Create a game which allows the user to make different choices which will affect the outcome of the game, l add a level of difficulty and require greater skill to play successfully
- To create a game that does not get boring or repetitive.
- Make new memories and to allow them to play the game with others.

**Who is the user?**

- The user will be somebody of any age but most likely an older person who has played Pokémon before
- The person may have grown up with Pokémon as a child.
- The person will be an avid gamer and enjoy the nostalgia of old games.
- The person maybe be used to and aware of emulator games.

**What are the needs/wants of the users?**

- The game must be easy to navigate.
- The game must clearly state the rules and how to play.
- The game should guide the member.
- The game must have simple controls.
- The game must be replayable.
- The user is able to pick up the game with little experience.
- The game is fun to play and has varying levels of difficulty
- The game challenges the user

**What are the needs/wants of the business?**

- To create a game that users enjoy
- A game that informs the player of errors and what to do.
- A game that users want to come back to and play again and again.
- A game that keeps the users interested
- A game that taps into a person’s nostalgia
- A game that they will recommend to their friends.
- A game with a level of immersion
- A game users can either play single player or with others.

**How does the site meet the needs of the user and business?**

- The game will contain content which will link directly to content from the previous Pokémon games.
- The names used in the game will be from the original list of Pokémon’s.
- The game has been created so that it can be played again and again helping to keep the user engaged.
- A description/game rules have been included so that the business can easily and effectively describe the site and explain how to use it
- A person with an interest in classic games will find the program both interesting and familiar.
- The game is easy to play.
- Included in the program is error handling and feedback for the user.
- The program has been created to guide users to improve the play ability.

## How to play/ Game Flow

**Walk through of the game**

- When the game starts the user (player 1) will be asked for their name, player 1 will be asked if they are going to be playing against a friend (human player). If they say yes to this, they will be directed to enter the users name (player 2), if they say no, a pre-defined username will be used by the game which will be the PC player.

- After the names have been selected, the user will be shown the rules of the game, and what to expect. Once they have read through this, they will be given the option to move to the Pokémon selection stage or they can exit the game here.

- Assuming they have typed in the word “fight”, they are taken to the Pokémon selection stage. Here, players will take turns in reviewing Pokémon before being asked if the Pokémon is to be added to their battle pack. Once player 1 has chosen all their Pokémon, player 2 will be asked to choose their Pokémon. If player 2 is the PC this will be automated.

- When the Pokémon selection is completed, players are taken to the battle arena. In the battle arena each player is asked to choose which Pokémon from their battle pack they wish to start the battle with. If player 2 is a PC this is automated. After Pokémon selection, the turn-based attacks begin. Each player can choose from 1 of 4 attacks they can execute against the other player. Multipliers have also been included in the game that will add 40 hit points to the attacking Pokémon’s attack depending on the type of the defending Pokémon’s - as this is taken into account. If the attacker is super effective against the defender, then the attack will be increased by the 40 hit points mentioned. But if they are not super effective the normal value of the attack is applied and the defender’s health is deducted by that amount.

- When a players Pokémon faint (0 health) they are given the option to bring out another Pokémon, and the battle will continue again. This loop will repeat until one player has no Pokémon left to fight with and the game will be over.

- The player will then be taken to the next stage where they will be asked if they wish to play another game. If they say yes, they will then be asked if they wish to play against a human player. If they say no then player 2 will become a non-human player (PC) and they will then both be taken to the Pokémon selection stage to pick a new set of 3 Pokémon to add to their battle pack before going into the battle arena.

- The player also has the option to completely exit the game during the game restart stage if they do not wish to play another game

## Design choice

The design choice of the game was heavily influenced by the Pokémon games. The Pokémon games has character called Professor Oak. His role in the game is to provide the user with information, details about the game and about Pokémon as well as explaining different aspects of the game. He will guide the user through the game and provides new and important information as required.

I have used this theme in my game tool and created the game as a story. It has a conversational style, meaning that most inputs of information that the user has to provide are answers to questions presented to them by Professor Oak. I have continued this theme with the error handling. For example: if the user enters an incorrect value, they will receive a message from Professor Pak informing them of the error they have made. Another example of this conversational style is Or, when the game first loads. A function called ‘game start’ is called from the run.py file, and the player is greeted with a message from Professor Oak and asked for information regarding players and names.

Once that is completed the function ‘play game’ is called. This function is the core of the game and controls most of the game. In this function the player objects are created and each player picks their Pokémon. Then, the battle phase is entered and finally the game restart function is called once the battle phase is completed.

The creation of the player object is done in a separate file called player.py. The reason for this is that there are a certain number of methods and data which solely relate to the player. It also means that once created, the player object can be passed around and then important information pulled and used from that.

The battle phase was also created in a separate file called battle.py and a class was used in order to group related methods together – as explained with the ‘player object’. In order to run the battle and the different methods which relate to it such as health reduction, it is cleaner and simpler to have that all in one file. It means each player object need only to be passed to the battle class and the game will run.

Finally, when the Battle phase is completed, we return to the run.py file. The restart’ function is called which asks the user if they wish to play again or exit the game. If they wish to play again some details are taken and then ’play game’ is called again and the game restarts.

When designing the game, I have used information from the actual Pokémon game such as names descriptions of Pokémon, Pokémon attack moves and the Pokémon types so that a person with previous knowledge of the games can pick up the game I have created easily as they will be able to tap into the same areas of knowledge. I have done the same with the Pokémon attacks and how damage is inflicted against another Pokémon by taking the Pokémon’s type into account.
