from configparser import ConfigParser
from pathlib import Path
from sys import path

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
        
        
# ==================================================================
# ПРОЦЕСС ИГРЫ
# ==================================================================

# получаем игоков

players = read_players() 

# Имя игрока 1
player1_name = input()
player2_name = input()

if player1_name not in players:
    create_player(player1_name)

if player2_name not in players:
    create_player(player2_name)

print(*read_players())

