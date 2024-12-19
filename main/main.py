from worlds.garden import Garden
from main.game.player import Player

def intro():
    get_player_name = input("What is your name?: ")
    player = Player(get_player_name)

    # Inputs for how long they want to play here

    # Pick world
    print("\nChoose a world to explore: ")
    print("1. Garden")
    # print("2. Dinosaurs")
    # print("3. Forest")
    # print("4. Plains")
    # print("5. Dungeon")

    choice = input("Enter the number of your choice or quit to exit: ")

    match choice:
        case 1:
            world = Garden()
        case 'quit':
            player.active = False
            print('Thanks fo visiting, please come again!')

    return player, world

def main():
    player, world = intro()

    while player.active:
        command = input()

        match command:
            case 1:
                print(world)
            case 'quit':
                player.active = False
                print('Thanks fo visiting, please come again!')


main()