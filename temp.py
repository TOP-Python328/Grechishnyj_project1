import user
import menu
import players
import utils
import xprint
import saves
import game
import xstat
import litlib

# ПЕРВЫЙ ЗАПУСК
helper = menu.options
xprint._message(litlib.title_game)
xprint.right(litlib.version)
xprint.table(helper)

# АВТОРИЗАЦИЯ ИГРОКА
names = user.auth()
db_players = players._read()
db_saves = saves._read_save()

size = 3
command = input(litlib.title_menu)

#ВКЛ/ВЫКЛ
while True:
    # НОВАЯ ИГРА
    if command == 'new':
        turns = [' ' for _ in range(size**2)]
        steps = []
        db_saves[names] = (steps, turns)
        result_game = game.play(names, steps, turns)
        game.update_players(result_game, db_players)
        game.update_save(result_game, db_saves)  
    # ЗАГРУКА ИГРЫ
    if command == 'load':
        if names in db_saves:
            steps = db_saves[names][0]
            turns = db_saves[names][1]
            result_game = game.play(names, steps, turns)
            game.update_players(result_game, db_players)
            game.update_save(result_game, db_saves)
        else:
            xprint._message(litlib.not_save)
    # ПОКАЗАТЬ ПОМОЩЬ    
    if command == 'help':
        xprint.table(helper)
    # СМЕНИТЬ ИГРОКА
    if command == 'player':
        xprint._message(litlib.player_change)
        names = user.auth()
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