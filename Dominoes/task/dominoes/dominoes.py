import random


def create_stock_dominos() -> []:
    dominos = []
    for i in range(1, 7):
        for j in range(2, 7):
            if j == i - 1:
                continue
            else:
                dominos.append([i, j])
    dominos.insert(0, [1, 1])
    stock_dominos = random.sample(dominos, 14)
    return stock_dominos


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


if __name__ == '__main__':
    player_pieces = []
    computer_pieces = []
    stock_pieces = []
    domino_snake = []
    status = ""
    while not check_doubles(stock=stock_pieces):
        stock_pieces = create_stock_dominos()
        deal_pieces(player_pieces, computer_pieces, stock_pieces)

    status, domino_snake = determine_turn(player_pieces, computer_pieces)
    if status == "computer":
        player_pieces.pop(player_pieces.index(domino_snake[0]))
    else:
        computer_pieces.pop(computer_pieces.index(domino_snake[0]))
    print("Stock pieces:", stock_pieces)
    print("Computer pieces:", computer_pieces)
    print("Player pieces:", player_pieces)
    print("Domino snake:", domino_snake)
    print("Status:", status)
