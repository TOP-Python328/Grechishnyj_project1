""" 
Точка входа.
Модуль верхнего уровня.
"""
import players
import saves
import user
import game

import menu

import xprint
import xstat
import litlib

# Проверка на то импортирован модуль или передан интерпритатору.
# Условие выполняется когда модуль передан интерпритатору.
if __name__ == '__main__':
    ...

# ПЕРВЫЙ ЗАПУСК
helper = menu.options
xprint._message(litlib.title_game)
xprint.right(litlib.version)
xprint.table(helper)

# АВТОРИЗАЦИЯ ИГРОКА
players_names = user.auth()
db_players = players._read()
db_saves = saves._read_save()

size = 3
command = input(litlib.title_menu)

while True:
    # НОВАЯ ИГРА
    if command == 'new':
        turns = [' ' for _ in range(size**2)]
        steps = []
        db_saves[players_names] = (steps, turns)
        result_game = game.play(players_names, steps, turns)
        # ВЫНЕСТИ В ФУНКЦИЮ 1 1-2
        if 'save_game' in result_game:
            db_saves[players_names] = (result_game[1][0], result_game[1][1])
            saves._write_save(f'{saves.parse_to_string(db_saves)}\n')
        if 'win_game' in result_game:
            winner = result_game[1][0]
            loser = result_game[1][1]
            win = str(int(db_players[winner]['wins']) + 1)
            los = str(int(db_players[loser]['loses']) + 1)
            players._update(winner, 'wins', win)
            players._update(loser, 'loses', los)
        if not result_game:
            player_1 = result_game[1][0]
            player_2 = result_game[1][1]
            draw_1 = str(int(db_players[player_1]['draws']) + 1)
            draw_2 = str(int(db_players[player_2]['draws']) + 1)
            players._update(player_1, 'draws', draw_1)
            players._update(player_2, 'draws', draw_2)
         
    # ЗАГРУКА ИГРЫ
    if command == 'load':
        if players_names in db_saves:
            steps = db_saves[players_names][0]
            turns = db_saves[players_names][1]
            result_game = game.play(players_names, steps, turns)
            # ВЫНЕСТИ В ФУНКЦИЮ 1 2-2
            if 'save_game' in result_game:
                db_saves[players_names] = (result_game[1][0], result_game[1][1])
                saves._write_save(f'{saves.parse_to_string(db_saves)}\n')
            if 'win_game' in result_game:
                winner = result_game[1][0]
                loser = result_game[1][1]
                win = str(int(db_players[winner]['wins']) + 1)
                los = str(int(db_players[loser]['loses']) + 1)
                players._update(winner, 'wins', win)
                players._update(loser, 'loses', los)
                db_saves.pop(players_names)
                saves._write_save(f'{saves.parse_to_string(db_saves)}\n')
            if not result_game:
                player_1 = result_game[1][0]
                player_2 = result_game[1][1]
                draw_1 = str(int(db_players[player_1]['draws']) + 1)
                draw_2 = str(int(db_players[player_2]['draws']) + 1)
                players._update(player_1, 'draws', draw_1)
                players._update(player_2, 'draws', draw_2) 
                db_saves.pop(players_names)
                saves._write_save(f'{saves.parse_to_string(db_saves)}\n')                
        else:
            xprint._message(litlib.not_save)
    # ПОКАЗАТЬ ПОМОЩЬ    
    if command == 'help':
        xprint.table(helper)
    # СМЕНИТЬ ИГРОКА
    if command == 'player':
        xprint._message(litlib.player_change)
        players_names = user.auth()
        db_players = players._read()
    # ПОКАЗАТЬ СТАТИСТИКУ
    if command == 'table':
        xprint._message(litlib.result_table)
        xprint.table(xstat.show_games()) 
    # ИЗМЕНИТЬ РАЗМЕР ПОЛЯ
    if command == 'dim':
        size = menu._dim()
    if command == 'quit':
        break
    
    command = input(litlib.title_menu)
xprint._message(litlib.end_game)