""" 
Игровой процесс.
Исполнительный модуль.
"""

import xprint
import litlib
from itertools import compress

def fill_wins(size: int) -> list[set[int, ...]]:
    """Функция возвращает список победных комбинаций в зависимости от размера игрового поля.
    
    Параметры: size - размер игрового поля.
    Возвращает: список победных множеств, которые содержат в себе номера клеток 
    """
    
    # Целевой список победных комбинаций
    wins_combinations = []
    # Список всех номеров игрового поля
    all_numbers = [i+1 for i in range(size**2)]
    # Для сбора комбинаций используется двумерный список
    main_list = [all_numbers[i:i+size] for i in range(0, len(all_numbers), size)]
    # Победная комбинация по главной диагонали 
    diagonal_main = [] 
    # Победная комбинация по обратной диагонали
    diagonal_back = []    
    
    for i in range(size):
        # Победные комбинации по рядам
        rows = []
        # Победные комбинации по колонкам
        columns = []    
        for j in range(size):
            rows.append(main_list[i][j])
            columns.append(main_list[j][i])
            if i == j:
                diagonal_main.append(main_list[i][j])
            if i + j == size - 1: 
                diagonal_back.append(main_list[i][j])
        wins_combinations.append(set(rows))
        wins_combinations.append(set(columns))   
    wins_combinations.append(set(diagonal_main))
    wins_combinations.append(set(diagonal_back))
    return wins_combinations 


def add_step(step, steps, size) -> list[int]:
    """Функция проверяет корректность ввода и добавляет значение хода если проверка пройдена"""
    if step not in steps and 0 < step <= size**2: 
        steps.append(step)
        return steps
        

def is_win(steps: list[int], wins: list[set[int, ...]]) -> bool:
    """Функция проверки наличия выигрышной комбинации в списке шагов.
    
    Параметры: steps - список всех ходов, wins - список победных комбинаций.
    Возвращает: True | False проверяя на подмножество победные комбинации в списке ходов.
    """
    crosses = set(steps[::2])
    zeros = set(steps[1::2])
    for comb in wins:
        if comb <= crosses or comb <= zeros:
            return True
    else:
        return False
        
def is_draw(steps: list[int], wins: list[set[int]]) -> bool:
    """Функция исключает победную комбинацию из списка победную комбинаций.

    Параметры: steps - список всех ходов, wins - список победных комбинаций.
    Возвращает: True | False проверяя на истину список победных комбинаций.
    """
    crosses = set(steps[::2])
    zeros = set(steps[1::2])
    selectors = []
    for comb in wins:
        if comb & crosses and comb & zeros:
            selectors.append(0)
        else:
            selectors.append(1)
    wins = list(compress(wins, selectors))
    return not bool(wins)

def play(
        names: tuple[str, str], 
        steps: list[int], 
        turns: tuple[str, str, str],
    ) -> tuple[str, ...]:
    """doc"""
    
    tokens = ('O', 'X')
    size = int(len(turns) ** 0.5)
    wins = fill_wins(size)
    strout = xprint._template(size)
    
    while True:
        # ВЫВОД ИГРОВОГО ПОЛЯ
        print(f'\n{strout.format(*turns)}', end='')
        try:
            # ХОД
            step = input(litlib.title_step.format(names[len(steps) % 2]))
            if step == 'save':
                xprint._message(litlib.game_saved)
                return ['save_game', (steps, turns)]
            else:
                step = int(step)
                add_step(step, steps, size)
                turns[step - 1] = tokens[len(steps)%2]
            # НИЧЬЯ
            if is_draw(steps, wins):
                print(f'\n{strout.format(*turns)}', end='')
                print(f'Ничья\n')
                xprint._message(litlib.end_draw)
                return False        
            # ПОБЕДА
            if is_win(steps, wins):
                winner = names[len(steps) % 2 - 1]
                loser = names[len(steps) % 2]
                print(f'\n{strout.format(*turns)}', end='')
                print(f'Победитель - {winner}\n')
                xprint._message(litlib.end_win.format(winner))
                return ['win_game', (winner, loser)]
        except:
            print(litlib.error_digit)
            break


    

