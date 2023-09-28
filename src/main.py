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
view.table(data.COMMANDS)
players_db = files.read_players()
saves_db = files.read_saves()
players = user.auth(players_db)

# def mainloop():
    # """"""
command = input(data.MSG_HEAD['menu'])
while True:
    if command == 'new':
        steps, turns = [], [' ' for _ in range(data.size**2)]
        game_result = game.play(players, steps, turns)
        files.update_all(players, game_result, saves_db, players_db)
    if command == 'load':
        if players in saves_db:
            steps = saves_db[players][0]
            turns = saves_db[players][1]
            game_result = game.play(players, steps, turns)
            files.update_all(players, game_result, saves_db, players_db)
        else:
            view.header(data.MSG_HEAD['not_save'])
    if command == 'help':
        view.table(data.COMMANDS)
    if command == 'player':
        view.header(data.MSG_HEAD['player_change'])
        players = user.auth(players_db)
    if command == 'table':
        view.table(utils.statistics(players_db))
    if command == 'dim':
        view.header(data.MSG_HEAD['dim'])
        data.size = utils.dim()
    if command == 'quit':
        break
    command = input(data.MSG_HEAD['menu'])    
   
# def end():
    # """"""  
view.header(data.MSG_HEAD['end'])    


# if __name__ == '__main__':
    # start()
    # mainloop()
    # end()