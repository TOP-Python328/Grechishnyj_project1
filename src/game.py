""" 
Игровой процесс.
Исполнительный модуль.
"""

import data
import files
import utils
import view

def play(names: tuple[str, str], steps: list[int], turns: tuple[str, str, str],) -> tuple[str, ...]:
    """doc"""
    
    tokens = ('O', 'X')
    size = int(len(turns) ** 0.5)
    wins = utils.fill_wins(size)
    strout = view.template(size)
    
    while True:
        print(f'\n{strout.format(*turns)}', end='')
        # проверка ввода сделать
        step = input(data.MSG_GAME['step'].format(names[len(steps) % 2]))
        if step == 'save':
            view.header(data.MSG_GAME['save'])
            return ('save', names, (steps, turns))
        else:
            step = int(step)
            utils.add_step(step, steps, size)
            turns[step - 1] = tokens[len(steps)%2]
        # НИЧЬЯ
        if utils.is_draw(steps, wins):
            print(f'\n{strout.format(*turns)}', end='')
            view.header(data.MSG_GAME['draw'])
            return ['draw', names]       
        # ПОБЕДА
        if utils.is_win(steps, wins):
            winner = names[len(steps) % 2 - 1]
            loser = names[len(steps) % 2]
            print(f'\n{strout.format(*turns)}', end='')
            view.header(data.MSG_GAME['win'].format(winner))
            return ['win', (winner, loser)]