import random

def game(barrels, player_cards, computer_cards):
    print('Player')
    print(player_cards)
    print('Computer')
    print(computer_cards)
    rand_barrel = random.choice(barrels)
    barrels.remove(rand_barrel)
    print('Вытянутый бочонок ' + str(rand_barrel))
    print('Зачеркнуть ? y - да n - нет q - выход')
    str_input = input()
    if str_input == 'y':
        if rand_barrel in player_cards:
            player_cards[player_cards.index(rand_barrel)] = '-'
        else:
            return print('Проигрыш')
    elif str_input == 'n':
        if rand_barrel in player_cards:
            return print('Проигрыш')
    elif str_input == 'q':
        return print('Пока')
    else:
        print('Некорректный ввод')
    if rand_barrel in computer_cards:
        computer_cards[computer_cards.index(rand_barrel)] = '-'
    if (player_cards.count('-') != 15) and (computer_cards.count('-') != 15):
        game(barrels, player_cards, computer_cards)
    else:
        print('Игра окончена')


def main():
    barrels = [x for x in range(1, 91)]
    player_cards = random.sample(range(1, 90), 15)
    computer_cards = random.sample(range(1, 90), 15)
    game(barrels, player_cards, computer_cards)
if __name__ == '__main__':
    main()