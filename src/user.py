"""
Исполнительный модуль - авторизация (регистрация) игрока.
"""

import data
import files
import view


def create() -> dict[str, int]:
    """Функция генерации статистических полей для нового игрока.
    
    :returns: список статистических показателей с начальными значениями.
    """
    return {key: 0 for key in ('wins', 'draws', 'loses')}


def auth(players_db: data.Players) -> str:
    """Функция авторизации (регистрации) игрока.
    
    :param players_db: база данных всех игроков.
    :returns: имя игрока.
    """
    user_name = input(data.MSG_USER['name'])
    if user_name not in players_db:
        players_db[user_name] = create()
        files.write_players(players_db)
    return user_name
        

def get_opponent(players_db: data.Players) -> str:
    """Функция выбора второго игрока и сложности игры.
    
    :param players_db: база данных всех игроков.
    :returns: имя игрока.
    """
    view.table(data.MSG_USER['modes'])
    user_input = input(data.MSG_USER['mode'])
    if user_input == '1':
        view.table(data.MSG_USER['diffs'])
        user_input = input(data.MSG_USER['diff'])
        if user_input == '1':
            opponent = data.MSG_USER['bots'][0]
        else:
            opponent = data.MSG_USER['bots'][1]
    elif user_input == '2':
        opponent = input(data.MSG_USER['opponent'])
    if opponent not in players_db:
        players_db[opponent] = create()
        files.write_players(players_db)
    return opponent

    
def get_token(players: data.Names) -> data.Names:
    """Функция выбора игрового токена для главного игрока.
    
    :param players: кортеж с именами игроков.
    :returns: кортеж с именами игроков. 
    """
    view.table(data.MSG_USER['tokens']) 
    token = input(data.MSG_USER['token'].format(players[0]))   
    if token == '2':
        players = players[::-1] 
    return players

    
def get_save(user: str, saves: data.Saves) -> data.UserSave | None:
    """Функция взаимодействия с пользователем, для получения одной из сохраненных игр.
    
    :param user: имя авторизованного пользователя.
    :param saves: список всех игровых сейвов.
    :returns: кортеж сохраненной партии для авторизованного пользователя.    
    """
    table_header = [
        ('Игрок 1', 'Игрок 2', 'Нажмите'),
        ('———————', '———————', '———————',),
    ]
    user_saves = []
    num = 1
    for key in saves.keys():
        if user in key:
            key += (num, )
            user_saves.append(key)
            num += 1

    save = None
    if user_saves:
        view.table(table_header + user_saves)
        while True:
            try:
                number_save = int(input(data.MSG_HEAD['user_save']))
                key = number_save - 1
                players = user_saves[key][:-1]
                save = players, saves[players]
                break
            except:
                print(data.MSG_GAME['error'])
    return save
