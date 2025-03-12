
print('\nWelcome to tic tac toe\n')

print('Player 1 is X  ---  Player 2 is  O ')

def get_current_player(player):
    return 'PLAYER 1 (X)' if player[0]==1 else "PLAYER 2 (O)"

def switch_turns(player):
    return [2,'O'] if player[0]==1 else [1, 'X']

def padder(text):
    return text.center(len(text) + 4)     

positions = { '1':'-', '2':'-', '3':'-', '4':'-', '5':'-', '6':'-', '7':'-', '8':'-', '9':'-' }


def print_actual_board(positions):
    print(f"{padder(positions['1'])}|{padder(positions['2'])}|{padder(positions['3'])}")
    print("----------------")
    print(f"{padder(positions['4'])}|{padder(positions['5'])}|{padder(positions['6'])}")
    print("----------------")
    print(f"{padder(positions['7'])}|{padder(positions['8'])}|{padder(positions['9'])}")
    
def print_sample_board():
    print(f"{padder('1')}|{padder('2')}|{padder('3')}")
    print("----------------")
    print(f"{padder('4')}|{padder('5')}|{padder('6')}")
    print("----------------")
    print(f"{padder('7')}|{padder('8')}|{padder('9')}")

winning_lines = [ [1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [7,5,3] ]

def check_full_line(line):
    for position in line:
        
        if positions [f'{line[0]}'] == positions [f'{line[1]}'] == positions [f'{line[2]}'] and positions[f'{position}'].strip()!='-':
            return False
        
    return True


game_on  = True
player = [1, "X"]

available_options = ['1','2','3','4','5','6','7','8','9']

while game_on:
    
    if len(available_options) == 0:
        print("It is a DRAW")
        break
    
    CURRENT_PLAYER = get_current_player(player)

    print('\nbelow is the number map, pick a spot to fill!\n')
    print_sample_board()
    
    print('\nActual Board\n')
    print_actual_board(positions)

    choice = input(f"{CURRENT_PLAYER} ( Q to quit ): ")
    
    if choice.upper() == 'Q':
        break
    elif choice in positions.keys():
        if choice in available_options:
            positions[choice] = player[1]
            available_options.remove(choice)
        else:
            print('position filled, not available!, try again')
            continue
    else:
        print('invalid choice')
        continue
        
    for line in winning_lines:
        game_on = check_full_line(line)
        if not game_on:
            print()
            print_actual_board(positions)
            print(f"player {player[0]} ({player[1]}) Wins")
            break
    
    player = switch_turns(player)
    
    
    



