""" 
Игровой процесс.
Исполнительный модуль.
"""

import data
import files
import utils
import view


# ИСПРАВИТЬ: над аннотациями надо ещё крепко подумать – сейчас у вас много чего не совпадает
# КОММЕНТАРИЙ: и вынесите их всё-таки в data
def play(names: tuple[str, str], steps: list[int], turns: tuple[str, str, str],) -> tuple[str, ...]:
    """doc"""
    
    tokens = ('O', 'X')
    # УДАЛИТЬ: вы не должны вычислять это число каждый раз, как оно потребуется — объявите необходимую переменную в модулей data и обращайтесь к ней (а менять вы её будете один раз по изменении размера поля)
    size = int(len(turns) ** 0.5)
    # УДАЛИТЬ: аналогично, избыточное вычисление
    wins = utils.fill_wins(size)

    strout = view.template(size)
    
    while True:
        print(f'\n{strout.format(*turns)}', end='')
        # проверка ввода сделать
        # ИСПРАВИТЬ: вычислите индекс-указатель отдельно
        step = input(data.MSG_GAME['step'].format(names[len(steps) % 2]))
        if step == 'save':
            view.header(data.MSG_GAME['save'])
            return 'save', names, (steps, turns)
        else:
            step = int(step)
            utils.add_step(step, steps, size)
            turns[step-1] = tokens[len(steps)%2]
        # НИЧЬЯ
        if utils.is_draw(steps, wins):
            # УДАЛИТЬ: раз уж завели для всех выводов отдельный модуль — что действительно удобно — то и этот вывод тоже туда уберите
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

