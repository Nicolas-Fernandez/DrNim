"""Textual python game based on the classical game Dr.Nim,
      with goal to discover youtube webpage : StanDuMaths"""

#init var
COINS = 12
PLAYER = 1
CHOICE = 0

#fonct def
def print_coins(coins):
    """take a number of coins and print this in ASCI draw table"""

    print('')
    print('-------------------------')
    print(' O' * coins)
    print('-------------------------')
    print('')

def player_turn(player):
    """take who player turn is and ask him how many coins he want"""

    global COINS
    global PLAYER
    global CHOICE

    if player == 1:
        answer = 1
        print_coins(COINS)
        while answer:
            print('')
            CHOICE = raw_input('How many coins you take?  ')
            if CHOICE == '3' or CHOICE == '2' or CHOICE == '1':
                CHOICE = int(CHOICE)
                COINS = COINS - CHOICE
                answer = 0
                PLAYER = 2
                string = ('You take ' + str(CHOICE) + ' coins and now we have '
                          + str(COINS) + ' remaing coins.')
                print(string)
                print('')
            else:
                print('You can take 1, 2 or 3 coins.')
                print('')

    if player == 2:
        answer = 1
        print_coins(COINS)
        while answer:
            print('')
            print('Mmm, hard to choose...')
            COINS = COINS - (4 - CHOICE)
            answer = 0
            PLAYER = 1
            string = ('I take ' + str(4 - CHOICE) + ' coins and now we have '
                      + str(COINS) + ' remaing coins.')
            print(string)
            print('')

#intro Dr. Nim
print('')
print('WELCOME! My name is Nim, Dr. Nim.')
print('Would you play a game with me ?')
print('')
print('Look the table, we share 12 coins. Each of us, turn by turn, we can take 1, 2 or 3 coins.')
print('Who take the last coin, win the game, and the 12 coins.')
print('')
print('Be my guest, I let you start.')
print('')

#start game
while COINS >= 1:
    player_turn(PLAYER)

#end game
print_coins(COINS)
print('')
print('Oh, wait a seconde, look at that! I win!')
print('What a beautifull game, thank for the coins!')
print('')
print('Know more about Dr. Nim?')
print('Visit StanDupMaths youtube webpage')
print('')
print('|------------------------------|')
print('| https://youtu.be/9KABcmczPdg |')
print('|------------------------------|')
print('')
print('Press enter key to escape the game')
CLOSE = raw_input()
