from configparser import ConfigParser
from pathlib import Path
from sys import path

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
 
# ==================================================================
# ПРОЦЕСС ИГРЫ
# ==================================================================

# Получаем игоков
players = read_players() 

# Получаем имена игроков для игры
player1_name = input()
player2_name = input()

# Проверяем наличие игроков в списке всех игроков
# Если если кого-то нет, то создаем с новым именем
if player1_name not in players:
    create_player(player1_name)

if player2_name not in players:
    create_player(player2_name)



