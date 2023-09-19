from configparser import ConfigParser
from pathlib import Path
from sys import path

# Функции для работы с файлом игроков players.ini
def _create(player_name: str):
    """Функция записи нового игрока в файл players.ini"""
    player = ConfigParser()
    player.add_section(player_name)
    keys = ('wins', 'draws', 'loses')
    for key in keys:
        player.set(player_name, key, '0')
    file = Path(path[0]) / 'players.ini'
    with open(file, 'a', encoding='utf-8') as fileout:
        player.write(fileout)
    

def _read() -> ConfigParser:
    """Функция чтения файла players.ini"""
    players = ConfigParser()
    players.read('players.ini')
    return players
    
# >>> players = read_players()
# >>> players
# <configparser.ConfigParser object at 0x000001705E61F450>
# >>> type(players)
# <class 'configparser.ConfigParser'>
# >>> print(dict(players))
# {'DEFAULT': <Section: DEFAULT>, 'Olga': <Section: Olga>, 'Pavel': <Section: Pavel>, 'Ivan': <Section: Ivan>}

def _update(player_name: str, key: str, value: str):
    """Функция обновления данных в файле players.ini"""
    players = _read()
    players.set(player_name, key, value)
    file = Path(path[0]) / 'players.ini'
    with open(file, 'w', encoding='utf-8') as fileout:
        players.write(fileout)