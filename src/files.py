"""
Чтение и запись файлов.
Вспомогательный модуль.
"""
from configparser import ConfigParser
import data


# Функции обработки игроков
def read_players(file_path: str = data.players_path) -> data.Players:
    """Функция чтения данных из файла players.ini"""
    players = ConfigParser()
    players.read(file_path)
    players_db = {}
    for player in players.sections():
        players_db[player] = {
            key: int(value) 
            for key, value in players[player].items()
        }
    return players_db 


def write_players(db_players: data.Players) -> None:
    """Функция записи данных в файл players.ini"""
    players = ConfigParser()
    players.read_dict(db_players)
    with open(data.players_path, 'w', encoding='utf-8') as fileout:
        players.write(fileout)


# Функции обработки сохраненных игр
def read_saves(file_path: str = data.saves_path) -> data.Saves:
    """Функция чтения файла saves.ttt"""
    saves = file_path.read_text(encoding='utf-8')
    saves = saves.strip().split('\n')
    db_saves = {}
    for save in saves:
        try:
            players, steps, turns = save.split('!')
        except:
            return db_saves
        players = tuple(players.split(','))
        steps = list(int(s) for s in steps.split(','))
        turns = list(turns.split(','))
        db_saves[players] = (steps, turns)
    return db_saves


def write_saves(db_saves: data.Saves) -> None:
    """Функция записи данных в файл saves.ttt"""
    text_saves = []
    for players, save in db_saves.items():
        players = ','.join(players)
        steps, turns = save
        steps = ','.join(str(s) for s in steps)
        turns = ','.join(str(t) for t in turns)
        text_saves.append(f'{players}!{steps}!{turns}')
    text_saves = '\n'.join(text_saves)
    data.saves_path.write_text(text_saves, encoding='utf-8')


# оптимизировать   
def update_all(players, game_result, saves_db, players_db) -> None:
    """doc"""
    key_save = game_result[1]
    if 'save' in game_result:
        saves_db[key_save] = game_result[2]
        write_saves(saves_db)
        return None 
    player_1 = key_save[0]
    player_2 = key_save[1]
    if 'win' in game_result:
        players_db[player_1]['wins'] += 1
        players_db[player_2]['loses'] += 1
    elif 'draw' in game_result:
        players_db[player_1]['draws'] += 1
        players_db[player_2]['draws'] += 1  
    if players in saves_db:
        saves_db.pop(players)
    write_saves(saves_db)   
    write_players(players_db)
    

