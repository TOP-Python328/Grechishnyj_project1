"""
Авторизация (регистрация) игрока.
Исполнительный модуль.

Выполняется со старта программы.
Выполняется при смене игрока.
"""

import data
import files
import view


def create() -> dict[str, int]:
    """Функция генерации статистических полей для нового игрока"""
    return {key: 0 for key in ('wins', 'draws', 'loses')}

def auth(players_db: data.Players) -> tuple[str, str]:
    """Функция авторизации (регистрации) игрока и настройка режима игры"""
    user_name = input(data.MSG_USER['name'])
    if user_name not in players_db:
        players_db[user_name] = create()
        files.write_players(players_db)
    view.table(data.MSG_USER['modes'])
    user_input = input(data.MSG_USER['mode'])
    # Один или два игрока
    if user_input == '1':
        view.table(data.MSG_USER['diffs'])
        user_input = input(data.MSG_USER['diff'])
        if user_input == '1':
            opponent = data.MSG_USER['bots'][0]
        else:
            opponent = data.MSG_USER['bots'][0]
    elif user_input == '2':
        opponent = input(data.MSG_USER['opponent'])
        
    if opponent not in players_db:
        players_db[opponent] = create()
        files.write_players(players_db)
    players = (user_name, opponent)
    # Выбор токена
    view.table(data.MSG_USER['tokens']) 
    token = input(data.MSG_USER['token'].format(user_name))   
    if token == '2':
        players = players[::-1] 
    return players