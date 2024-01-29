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

## Flowchart

- This flow chart shows the user journey from start to finish
  ![picture of initial game screem](assets/img/)

- This flow chart specifically shows the battle sections of the game
  ![picture of initial game screem](assets/img/)

- This flow chart specifically shows the Pokémon selection section
  ![picture of initial game screem](assets/img/)

## Data Model

When planning out the project I had decided that not all my code would be written within my run.py file. This is because I was looking to create and to simplify the layout of the game by grouping together related code. This led to the creation of two extra files each of which contains a class to be used in the game.
The game begins in the run.py file. Here, I created a function called “play game” which introduces the player to the game and asks the player for some information, including their name and their opponent’s name - or a PC player is selected. Once they have read the rules, they are taken to a second function called ’play game’
The majority of the game is run within this function. Firstly, a player variable is created for each player and this variable stores as a value an instance of the player class that is created in the player.py file.

When planning the game there were certain actions that related purely to the player, so I grouped all these together inside the player class, as it made it easier to plan and run the game. The other benefit of this approach is that the entire player object can then be passed to different functions and different parts of the object can be extracted and used. For example, each player is made to choose 3 Pokémon they wish to battle with. The selection process to do this is done within the player class as a method called ‘pick Pokémon’. This is stored in a battle pack which is unique to each player.

Once the selection process is complete the next stage of the game is the battle stage, I created another file for this and within that, created the battle class. This class contains a number of different methods. The battle class was created to group together all the methods relating to the battle section of the game. Within the battle class, you will find fight set up, choose new Pokémon, battle stadium and flip.

Once the battle stage is finished, the final section of the game is a function called game Restart which was included in the run.py file. Here the player is given the option to play again or end the game. This, together with the other 2 functions were included in the main run.py as they are the core 3 functions, one starts the game, one runs the game and one restarts the game.

## Colour and Font Scheme

- Colour for user input and name
- Colour for Pokémon NPC text
- Colour for loading text
- Colour for wrong answers
- Colour for game notifications
- Colour for end game

## Features

- Welcome page

  - This screen will be the first thing that the player sees when they load up the game, it contains the name of the game to clearly indicate to the player the type of game that they have loaded up. It also contains a message from an in-game character called Professor Oak who welcomes them to the game.

- Player 1 User input name and validation

  - The user is asked to enter their name which will be used throughout the game
  - When asking for their name, validation has been added to make sure they enter a string value
  - Error feedback is provided to the user if they raise an error

- Player 2 selection - human or computer

  - Player 1 is asked if they have a friend to play with
  - if the user states ‘no’ in response, then a PC player will be automatically selected as player 2
  - If they respond ‘yes’, they are prompted to input player 2’s name
  - A variable called human is also created and is used later on in the function to automate computer choices

- Game Rules

  - Once both players have been chosen, they are shown the rules of the game
  - The rules contain information about the Pokémon selection progress.
  - The rules also contain information about the battle arena.
  - The rules go through the importance of selecting your Pokémon and depending on your Pokémon type, the attacks can be amplified.
  - Finally, it contains information about how to restart the game or exit the game.

- Each player reviewing and picking Pokémon for their battle pack.

  - This is the Pokémon selection phase.
  - A player can input any 1 of the 10 Pokémon and get back a detailed information sheet about that Pokémon. The information sheet will contain their name, description, type of Pokémon and attack moves. There is also important information about weakness to other Pokémon types.
  - A player can review as many Pokémon as they wish, after each Pokémon’s information sheet, they will be given a choice to add the Pokémon to the battle pack

- Players adding Pokémon to battle pack

  - Adding a Pokémon to a players battle pack is linked with reviewing the Pokémon
  - After a player inputs a Pokémon’s name and receives the detailed information sheet, they are asked if they wish to add the Pokémon to their battle pack
  - If they say ‘yes’, the Pokémon is added and this is confirmed by a on screen message
  - If they type ‘no’, they are taken back to the reviewing stage
  - An error catch has also been included so that the user is unable to select the same Pokémon twice to add to their battle pack. Each Pokémon must be unique

- PC adding Pokémon to battle pack

  - If the player has chosen not to play against a human player, then the PC will automatically choose their own battle pack Pokémon
  - This is confirmed on screen for the user to see that their opponent has selected their Pokémon
  - The variable “human” is used here to check that player 2 is not human

- Entering the battle arena

  - When entering the battle arena there is an on-screen message that first appears from the in-game character Professor Oak informing them they have entered the battle arena.
  - Each player is then asked which Pokémon they wish to start the battle arena with
  - Once both players have chosen their starting Pokémon the battle will start
  - If the user is playing against the computer this selection will be done automatically due to the “human” variable

- Pokémon fight in battle arena display

  - The image attached show the screen that will appear to the user when the battle has started
  - Included in the image is the attack Pokémon and player at the top along with the attacking Pokémon’s health bar
  - Below the attacking Pokémon and player is the same information for the defending Pokémon and player

- Health reduction

  - Under the on-screen battle arena, the attacking player will be asked what attack they wish to execute
  - They have the option to choose 1 of 4 attacks
  - The player selects the attack by inputting the attack number. The attack hit point value will be the amount of damage that will be taken off the defending Pokémon’s health
  - This attack can be increased by 40 if the defending Pokémon is weak to the attack move type, i.e fire type is weak to water
  - Then the attack and defender will switch and the new attacker will then be given the same options and can then attack
  - This process of flipping will continue until one of the players’ Pokémon has fainted (health is 0)

- Selection of a new Pokémon

  - When a player’s Pokémon has fainted, it triggers a method called ‘Choose new Pokémon’
  - In the method there is first a check to see if the player with the fainted Pokémon has any Pokémon left in their battle pack as after each Pokémon faints it is removed from the battle pack so it can’t be used again
  - If there are no Pokémon left for the player to use, the game ends
  - If the player has a Pokémon left which they can use, they are asked which Pokémon they wish to fight with next
  - Then the battle restarts with the player whose Pokémon did not faint having the first attack

- Restart and end game

  - When all Pokémon in a players battle pack have fainted (health 0) it will trigger the restart game function
  - Here player 1 is asked if they want to play another game
  - If player 1 inputs ‘no’ then the game ends and the in-game character Professor Oak confirm this in a goodbye message, asking them to come back soon
  - If player 1 inputs ‘yes’, they are asked if they want to play against a human player
  - If player 1 states ‘no’ a PC player is inputted as player 2
  - If player 1 has stated yes to a human player, player 2 is prompted for their name and then both player 1 and 2 are taken to the review Pokémon stage to add new Pokémon to their battle pack.
  - This is the same if player 2 is the computer, but they will select their own Pokémon for their battle pack

## Future Implementations

- Add in accuracy as a factor to if the attacking Pokémon lands their attack
- Attacks cannot be used infinitely
- A Pokémon’s accuracy can be reduced or increased
- A user can swap out Pokémon mid battle
- Health potions can be used on the players fighting Pokémon
