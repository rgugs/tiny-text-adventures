def get_name():
    player_name = input('What is your name?: ')
    sure = input(f'Is {player_name} correct? Y/N:')
    if sure.strip().lower() == 'y':
        return player_name   
    else:
        get_name()

def get_race():
    player_race_choice = input('What race are you?\n1. Human\n2. Elf\n3. Troll\n')
    player_race = ''
    match int(player_race_choice):
        case 1:
            player_race = 'Human'
        case 2:
            player_race = 'Elf'
        case 3:
            player_race = 'Troll'
        case _:
            print('Please try again')
            get_race()
    sure = input(f'Is {player_race} correct? Y/N:')
    if sure.strip().lower() == 'y':
        return player_race
    else:
        get_race()

def intro():
    print('Welcome to Tiny Text Adventures!')
    print('Choose your name and race to enter the adventure')
    player_name = get_name()
    player_race = get_race()
    print(f'Welcome to Tiny Text Adventures, {player_name} the {player_race}!')
    print('To leave the world, type q or quit at any time. Good Adventuring!')
    return player_name, player_race
    
def game_loop(name, race):
    while True:
        user_input = input("Type something ").strip().lower()
        
        if user_input in ('q', 'quit'):
            print("Goodbye!")
            break
        print(f'{name} the {race} typed: {user_input}')

def main():
    name, race = intro()
    game_loop(name, race)

main()