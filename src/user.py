"""
Авторизация (регистрация) игрока.
Исполнительный модуль.
"""

import players
import xprint
import litlib

def auth():
    
    db_players = players._read() 
    name_01 = input(litlib.title_name)
    if name_01 not in db_players:
        players._create(name_01)

    # РЕЖИМ ИГРЫ
    xprint.table(litlib.list_mod)
    game_mod = input(litlib.title_mod)
    
    # ОДИН ИГРОК
    if game_mod == '1':
        # УРОВЕНЬ СЛОЖНОСТИ
        xprint.table(litlib.list_diff)
        difficulty = input(litlib.title_diff)
        if difficulty == '1':
            name_02 = litlib.bot_names[0]
        else:
            name_02 = litlib.bot_names[1]

    # ДВА ИГРОКА
    if game_mod == '2':
        name_02 = input(litlib.title_opponent)
    # ДОБАВЛЯЕМ ВТОРОГО ИГРОКА ЕСЛИ НЕТ В БАЗЕ
    if name_02 not in db_players:
        players._create(name_02)
        
    names = (name_01, name_02)
    
    # ВЫБОР ТОКЕНА
    xprint.table(litlib.list_tokens) 
    player_01_token = input(litlib.title_tokens.format(name_01))   
    if player_01_token == '2':
        names = names[::-1]   
    
    return names