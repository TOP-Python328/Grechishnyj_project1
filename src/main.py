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


def start() -> None:
    """Функция авторизации пользователя и выбора режима игры."""
    view.header(data.MSG_HEAD['title'])
    view.print_right(data.MSG_HEAD['version'])
    view.table(data.COMMANDS)
    data.players_db = files.read_players()
    data.saves_db = files.read_saves()
    data.players = user.auth(data.players_db)


def mainloop() -> None:
    """Функция - суперцикл. Игровой процесс и обработка файлов данных."""
    while True:
        try:
            command = input(data.MSG_HEAD['menu'])
        except:
            print(data.MSG_GAME['error'])
        if command in data.COMMANDS[0]:
            data.steps = []
            data.turns = [' ' for _ in range(data.size**2)]
            data.empty = {num: ' ' for num in data.size_range}
            data.wins = utils.fill_wins(data.size)
            data.strout = view.template(data.size)
            game_result = game.play(data.players)
            files.update_all(data.players, game_result, data.saves_db, data.players_db)
        # ИСПРАВИТЬ: ну вы чего, Павел — это же проверка одной переменной, 
        # в одну итерацию она не может принять несколько разных значений — 
        # а вы независимые друг от друга проверки устраиваете, стыдно
        elif command in data.COMMANDS[2]:
            if data.players in data.saves_db:
                data.steps = data.saves_db[data.players][0]
                data.turns = data.saves_db[data.players][1]
                game_result = game.play(data.players)
                files.update_all(data.players, game_result, data.saves_db, data.players_db)
            else:
                view.header(data.MSG_HEAD['not_save'])
        elif command in data.COMMANDS[3]:
            view.table(data.COMMANDS)
        elif command in data.COMMANDS[4]:
            view.header(data.MSG_HEAD['player_change'])
            data.players = user.auth(data.players_db)
        elif command in data.COMMANDS[5]:
            view.table(utils.statistics(data.players_db))
        elif command in data.COMMANDS[6]:
            view.header(data.MSG_HEAD['dim'])
            utils.configure()
        elif command in data.COMMANDS[7]:
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
