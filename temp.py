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
    return dict(players)

     

# def update_player(player_name):
    # """docstring"""
    
    # player = ConfigParser()

    # player.set(player_name, 'wins', '1')
    # player.set(player_name, 'draws', '2')
    # player.set(player_name, 'loses', '3')
    
    # file = Path(path[0]) / 'settings.ini'
    # with open(file, 'w', encoding='utf-8') as fileout:
        # player.write(fileout)     