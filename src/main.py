"""
Точка входа.
Модуль верхнего уровня.
"""

import data
import files
import user
import game
import utils
import view
import help



def start() -> None:
    """Функция авторизации пользователя и выбора режима игры."""
    view.header(data.MSG_HEAD['title'])
    view.print_right(data.MSG_HEAD['version'])
    help.info_game('ПРАВИЛА ИГРЫ')
    help.rules_game('ИНТЕРФЕЙС')
    help.main_menu(data.COMMANDS)
    data.players_db = files.read_players()
    data.saves_db = files.read_saves()
    data.user_autn = user.auth(data.players_db)
    data.players = data.user_autn 


def mainloop() -> None:
    """Функция - суперцикл. Игровой процесс и обработка файлов данных."""
    while True:
        try:
            command = input(data.MSG_HEAD['menu'])
        except:
            print(data.MSG_GAME['error'])
        if command in data.COMMANDS['начать новую партию']:
            data.opponent = user.get_opponent(data.players_db)
            data.players = data.user_autn, data.opponent
            data.players = user.get_token(data.players)
            data.steps = []
            data.turns = [' ' for _ in range(data.size**2)]
            data.empty = {num: ' ' for num in data.size_range}
            utils.config_game(data.size)
            game_result = game.play(data.players)
            files.update_all(data.players, game_result, data.saves_db, data.players_db)
        # ИСПРАВИТЬ: ну вы чего, Павел — это же проверка одной переменной, 
        # в одну итерацию она не может принять несколько разных значений — 
        # а вы независимые друг от друга проверки устраиваете, стыдно
        elif command in data.COMMANDS['загрузить существующую партию']:
            data.user_save = user.get_save(data.user_autn, data.saves_db)
            if data.user_save:
                data.players = data.user_save[0]
                data.size = int(len(data.user_save[1][1]) ** 0.5)
                utils.config_game(data.size)
                data.steps = data.user_save[1][0]
                data.turns = data.user_save[1][1]
                data.empty = dict(zip(data.size_range, data.turns))
                game_result = game.play(data.players)
                files.update_all(data.players, game_result, data.saves_db, data.players_db)
            else:
                view.header(data.MSG_HEAD['not_save'])
        elif command in data.COMMANDS['отобразить раздел помощи']:
            help.main_menu(data.COMMANDS)
        elif command in data.COMMANDS['создать или переключиться на игрока']:
            data.players = None
            view.header(data.MSG_HEAD['player_change'])
            data.user_autn = user.auth(data.players_db)
            data.players = data.user_autn
        elif command in data.COMMANDS['отобразить таблицу результатов']:
            view.table(utils.statistics(data.players_db))
        elif command in data.COMMANDS['изменить размер поля']:
            view.header(data.MSG_HEAD['dim'])
            data.size = utils.dim()
            utils.config_game(data.size)
        elif command in data.COMMANDS['выйти']:
            break
        else:
            print(data.MSG_GAME['error'])
   

def end() -> None:
    """Функция печатает заголовок окончания игры"""  
    view.header(data.MSG_HEAD['end'])    


if __name__ == '__main__':
    start()
    mainloop()
    end()
