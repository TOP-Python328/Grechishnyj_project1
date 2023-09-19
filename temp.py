from configparser import ConfigParser
from pathlib import Path
from sys import path

import menu

# Функции для работы с файлом игроков players.ini
def create_player(player_name: str):
    """Функция добавления нового игрока в файл players.ini"""
    player = ConfigParser()
    player.add_section(player_name)
    keys = ('wins', 'draws', 'loses')
    for key in keys:
        player.set(player_name, key, '0')
    file = Path(path[0]) / 'players.ini'
    with open(file, 'a', encoding='utf-8') as fileout:
        player.write(fileout)

def read_players() -> dict:
    """Функция чтения файла players.ini"""
    players = ConfigParser()
    players.read('players.ini')
    return players

def update_player(player_name, key, value):
    """Функция обновления данных в файле players.ini"""
    players = read_players()
    players.set(player_name, key, value)
    file = Path(path[0]) / 'players.ini'
    with open(file, 'w', encoding='utf-8') as fileout:
        players.write(fileout)
        
# Функция шаблона игрового поля
def create_play_field(size: int=3) -> str:
    """Функция генерирует игровое поле для отображения в консоли"""
    field_template = ''
    line = 0
    for _ in range(size):
        field_template += '|'.join(' {} ' for _ in range(size))
        if line == size - 1:
            field_template += '\n'
            break
        line += 1
        field_template += '\n' + '—————'*(size-1) + '————'  + '\n'
    return field_template

# Функция построения выигрышных комбинаций
def create_wins(size: int=3) -> list[set[int]]:
    """Функция возвращает список сетов выигрышных комбинаций в зависимости от размера игрового поля."""
    wins_combinations = []
    all_numbers = [i+1 for i in range(size**2)]

    # Для сбора комбинаций используется двумерный список
    main_list = [all_numbers[i:i+size] for i in range(0, len(all_numbers), size)]
    
    

        
        
   
    # Победная комбинация по главной диагонали
    # Победная комбинация по обратной диагонали    
    diagonal_main = [] 
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
    
# >>> create_wins(4)
# [
    # {1, 2, 3, 4}, {1, 13, 5, 9}, {8, 5, 6, 7}, 
    # {2, 10, 6, 14}, {9, 10, 11, 12}, {11, 3, 15, 7}, 
    # {16, 13, 14, 15}, {8, 16, 4, 12}, {16, 1, 11, 6}, {10, 4, 13, 7}
# ]


    

    
   
 
# ==================================================================
# ПРОЦЕСС ИГРЫ
# ==================================================================

# ==================================================================
# НАЧАЛО - ГЛАВНОЕ МЕНЮ
# ==================================================================

# menu._command()

# # Получаем игоков
# players = read_players() 

# # Получаем имена игроков для игры
# player1_name = input()
# player2_name = input()

# # Проверяем наличие игроков в списке всех игроков
# # Если если кого-то нет, то создаем с новым именем
# if player1_name not in players:
    # create_player(player1_name)

# if player2_name not in players:
    # create_player(player2_name)



