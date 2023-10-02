"""
Точка входа.
Модуль верхнего уровня.
"""

import view
import data
import files
import user
import game
import utils





# def start():
    # """"""
view.header(data.MSG_HEAD['title'])
view.print_right(data.MSG_HEAD['version'])
view.table(data.COMMANDS)
players_db = files.read_players()
saves_db = files.read_saves()
players = user.auth(players_db)

# def mainloop():
    # """"""

while True:
    try:
        command = input(data.MSG_HEAD['menu'])
    except:
        print(data.MSG_GAME['error'])
    
    if command in data.COMMANDS[0]:
        data.steps = []
        data.turns = [' ' for _ in range(data.size**2)]
        data.empty = {num: ' ' for num in data.size_range}
        game_result = game.play(players)
        files.update_all(players, game_result, saves_db, players_db)
    # ИСПРАВИТЬ: ну вы чего, Павел — это же проверка одной переменной, в одну итерацию она не может принять несколько разных значений — а вы независимые друг от друга проверки устраиваете, стыдно
    elif command in data.COMMANDS[2]:
        if players in saves_db:
            data.steps = saves_db[players][0]
            data.turns = saves_db[players][1]
           
            game_result = game.play(players)
            files.update_all(players, game_result, saves_db, players_db)
        else:
            view.header(data.MSG_HEAD['not_save'])
    elif command in data.COMMANDS[3]:
        view.table(data.COMMANDS)
    elif command in data.COMMANDS[4]:
        view.header(data.MSG_HEAD['player_change'])
        players = user.auth(players_db)
    elif command in data.COMMANDS[5]:
        view.table(utils.statistics(players_db))
    elif command in data.COMMANDS[6]:
        view.header(data.MSG_HEAD['dim'])
        data.size = utils.dim()
        data.size_range = [i+1 for i in range(data.size**2)]
        data.wins = utils.fill_wins(data.size)
        data.strout = view.template(data.size)
        data.turns = [' ' for _ in range(data.size**2)]
        data.dim_range = range(data.size)

        print(f'{data.size=}')
        print(f'{data.wins=}')
        print(f'{data.turns=}')
        print(f'{data.size_range=}')
        print(f'{data.dim_range=}')
        print(f'{data.empty=}')
    elif command in data.COMMANDS[7]:
        break
    else:
        print(data.MSG_GAME['error'])
    # command = input(data.MSG_HEAD['menu'])    
   
# def end():
    # """"""  
view.header(data.MSG_HEAD['end'])    

def end():
    print('... ... ...')
end()
# if __name__ == '__main__':
    # start()
    # mainloop()
    # end()
