import random


def create_stock_dominos_and_deal() -> []:
    dominos = []
    for i in range(0, 7):
        for j in range(1, 7):
            if j < i:
                continue
            else:
                dominos.append([i, j])
    dominos.insert(0, [0, 0])
    stock_dominos = random.sample(dominos, 14)
    for domino in stock_dominos:
        dominos.pop(dominos.index(domino))
    random.shuffle(dominos)
    p_dominos = dominos[:7]
    c_dominos = dominos[7:]
    return stock_dominos, p_dominos, c_dominos


def deal_pieces(player: [], computer: [], stock: []):
    random.shuffle(stock)
    for i in range(len(stock)):
        if i % 2 == 0:
            computer.append(stock[i])
        else:
            player.append(stock[i])


def check_doubles(stock: []) -> bool:
    for i in stock:
        if i[0] == i[1]:
            return True
    return False


def determine_turn(p_pieces: [], comp_pieces: []):
    highest_player_double = [0, 0]
    highest_comp_double = [0, 0]
    for i in p_pieces:
        if i[0] == i[1]:
            if i > highest_player_double:
                highest_player_double = i
    for j in comp_pieces:
        if j[0] == j[1]:
            if j > highest_comp_double:
                highest_comp_double = j
    if highest_player_double[0] > highest_comp_double[0]:
        turn_status = "computer"
        snake = highest_player_double
        return [turn_status, [snake]]
    else:
        turn_status = "player"
        snake = highest_comp_double
        return [turn_status, [snake]]


def play_piece(snake: [], player_pieces: [], player_input):
    if player_input == 0:
        return

    piece_choice = abs(player_input) - 1
    if player_input > 0:
        snake.append(player_pieces[piece_choice])
    else:
        snake.insert(0, player_pieces[piece_choice])
    player_pieces.pop(piece_choice)


def validate_input(playerinput) -> bool:
    try:
        int(playerinput)
        if -6 <= int(playerinput) <= 6:
            return True
        else:
            print("Invalid input. Please try again.")
            return False
    except:
        print("Invalid input. Please try again.")
        return False


if __name__ == '__main__':
    player_pieces = []
    computer_pieces = []
    stock_pieces = []
    domino_snake = []
    status = ""
    while not check_doubles(stock=stock_pieces):
        stock_pieces, player_pieces, computer_pieces = create_stock_dominos_and_deal()
    status, domino_snake = determine_turn(player_pieces, computer_pieces)
    if status == "computer":
        player_pieces.pop(player_pieces.index(domino_snake[0]))
    else:
        computer_pieces.pop(computer_pieces.index(domino_snake[0]))
    game_over = False
    while not game_over:
        print("======================================================================")
        print("Stock size:", len(stock_pieces))
        print("Computer pieces: ", len(computer_pieces))
        print("")
        if len(domino_snake) < 6:
            print(''.join(str(i) for i in domino_snake))
        else:
            string_one = ''.join(str(i) for i in domino_snake[:3])
            string_two = ''.join(str(i) for i in domino_snake[-3:])
            print("...".join([string_one, string_two]))
        print("")
        print("Your pieces:")
        for i in player_pieces:
            print(f"{player_pieces.index(i) + 1}:{i}")
        print("")
        if len(player_pieces) == 0:
            print("Status: The game is over. You won!")
        else:
            if status == "player":
                print("Status: It's your turn to make a move. Enter your command.")
            else:
                print("Status: Computer is about to make a move. Press Enter to continue...")
        player_input = input()
        if player_input == "":
            status = "player"
            computer_input = random.randint((len(computer_pieces)) * -1, len(computer_pieces))
            play_piece(domino_snake, computer_pieces, computer_input)
            continue
        while not validate_input(player_input):
            player_input = input()
        player_input = int(player_input)
        play_piece(domino_snake, player_pieces, player_input)
        status = "computer"
        if player_input == "done":
            game_over = True
