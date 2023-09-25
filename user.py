import players
import xprint


def _auth():
    # ИГРОК
    # ==========================
    # читаем проверяем добавляем
    db_players = players._read() 
    name_01 = input('Введите имя игрока 1: > ')
    print()
    # ДОБАВЛЯЕМ ИГРОКА ЕСЛИ НЕТ В БАЗЕ
    if name_01 not in db_players:
        players._create(name_01)
        
    # читаем проверяем добавляем
    # ==========================


    # РЕЖИМ ИГРЫ
    xprint._table([('ОДИНОЧНАЯ ИГРА', 1), ('ИГРА С СОПЕРНИКОМ', 2)])
    game_mod = input('Выберете режим игры: > ')
    print()
    # ОДИН ИГРОК
    if game_mod == '1':
        # УРОВЕНЬ СЛОЖНОСТИ
        xprint._table([('ПРОСТО', 1), ('СЛОЖНО', 2)])
        difficulty = input('Выберете уровень сложности: > ')
        print()
        if difficulty == '1':
            name_02 = 'EASYBOT'
        else:
            name_02 = 'HARDBOT'


    # ДВА ИГРОКА
    # ==========================
    # читаем проверяем добавляем
    if game_mod == '2':
        name_02 = input('Введите имя игрока 2: > ')
        print()
    # ДОБАВЛЯЕМ ВТОРОГО ИГРОКА ЕСЛИ НЕТ В БАЗЕ
    if name_02 not in db_players:
        players._create(name_02)
        
    names = (name_01, name_02)
    # читаем проверяем добавляем
    # ==========================

    # ВЫБОР ТОКЕНА
    xprint._table([('Играть X', 1), ('Играть O', 2)]) 
    player_01_token = input(f'{name_01} выберете чем будете играть: > ')   
    if player_01_token == '2':
        names = names[::-1]
        
    
    return names