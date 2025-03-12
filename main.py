
print()
print('Welcome to tic tac toe')

print()
print('Player 1 is "X"')
print('Player 2 is "0"')

def get_current_player(player):
    return 'PLAYER 1 (X)' if player[0]==1 else "PLAYER 2 (O)"

def switch_turns(player):
    return [2,'O'] if player[0]==1 else [1, 'X']

def padder(text):
    return text.center(len(text) + 4)     
    

positions = {
    '1':'-',
    '2':'-',
    '3':'-',
    '4':'-',
    '5':'-',
    '6':'-',
    '7':'-',
    '8':'-',
    '9':'-',
}

def print_board(positions):
    print(f"{padder(positions['1'])}|{padder(positions['2'])}|{padder(positions['3'])}")
    print("----------------")
    print(f"{padder(positions['4'])}|{padder(positions['5'])}|{padder(positions['6'])}")
    print("----------------")
    print(f"{padder(positions['7'])}|{padder(positions['8'])}|{padder(positions['9'])}")

winning_lines = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [7,5,3]    
]

def check_full_line(line):
    for position in line:
        if positions[f'{position}'].strip()=='-':
            return True
        
        if positions [f'{line[0]}'] == positions [f'{line[1]}'] == positions [f'{line[2]}']:
            # print(f'victory for {positions [f'{line[0]}']}')
            return False #, positions [f'{line[0]}']
    
    return True


game_on  = True
player = [1, "X"]

available_options = ['1','2','3','4','5','6','7','8','9']

while game_on:
    
    if len(available_options) == 0:
        print("its a tie")
        break
    
    CURRENT_PLAYER = get_current_player(player)

    print()
    print('below is the number map, pick a spot to fill!')
    print()
    print ([1,2,3])
    print ([4,5,6])
    print ([7,8,9])
    
    print()
    print('Actual Board')
    
    print()
    
    
    # print ([positions['1'],positions['2'],positions['3']])
    # print ([positions['4'],positions['5'],positions['6']])
    # print ([positions['7'],positions['8'],positions['9']])
    
    # print_board(positions)




    
    print()
    
    print('Available spots are ', available_options)
    choice = input(f"{CURRENT_PLAYER}: ")
    
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
    
    print(positions)
    
    for line in winning_lines:
        game_on = check_full_line(line)
        if not game_on:
            print_board(positions)
            print(f"player {player[0]} ({player[1]}) Wins")
            break
    
    
    
    
    player = switch_turns(player)
    
    
    



