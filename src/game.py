""" 
Игровой процесс.
Исполнительный модуль.
"""

import data
import files
import utils
import view
import bot


# ИСПРАВИТЬ: над аннотациями надо ещё крепко подумать – сейчас у вас много чего не совпадает
# КОММЕНТАРИЙ: и вынесите их всё-таки в data
def play(names: data.Names) -> tuple[str, ...]:
    """Функция игрового процесса"""
    
    # УДАЛИТЬ: вы не должны вычислять это число каждый раз, как оно потребуется 
    #    — объявите необходимую переменную в модулей data и обращайтесь к ней 
    #    (а менять вы её будете один раз по изменении размера поля)
    # size = int(len(turns) ** 0.5)
    
    # УДАЛИТЬ: аналогично, избыточное вычисление
    # wins = utils.fill_wins(data.size)

    # strout = view.template(data.size)
    
    while True:
        # последние 2 хода, если steps не пустой

        # ИСПРАВИТЬ: вычислите индекс-указатель отдельно
        pointer = len(data.steps) % 2
        view.print_play(data.strout, data.turns, pointer)
        if pointer:
            view.print_right(data.MSG_GAME['step'].format(names[pointer]))
        else:
            print(data.MSG_GAME['step'].format(names[pointer]))
        
        if names[pointer] == data.MSG_USER['bots'][0]:
            step = bot.easy_mode()
        elif names[pointer] == data.MSG_USER['bots'][1]:
            step = bot.hard_mode(pointer)
        else:
            step = input(' > ')
                
        if step in data.COMMANDS[1]:
            view.header(data.MSG_GAME['save'])
            return 'save', names, (data.steps, data.turns)
        else:
            try:
                step = int(step)
                if step in data.steps:
                    print(data.MSG_GAME['busy'])
                    continue
            except ValueError:
                print(data.MSG_GAME['error'])
                continue
            utils.add_step(step, data.steps, data.size)
            data.turns[step-1] = data.tokens[pointer]
            data.empty[step] = data.tokens[pointer]
        # НИЧЬЯ
        if utils.is_draw(data.steps, data.wins):
            # УДАЛИТЬ: раз уж завели для всех выводов отдельный модуль — что действительно удобно — то и этот вывод тоже туда уберите
            # print(f'\n{template.format(*chars)}', end='')
            data.empty = {num: ' ' for num in data.size_range}
            view.print_play(data.strout, data.turns, pointer)
            view.header(data.MSG_GAME['draw'])
            return ['draw', names]
        # ПОБЕДА
        if utils.is_win(data.steps, data.wins):
            winner = names[pointer]
            loser = names[pointer - 1]
            data.empty = {num: ' ' for num in data.size_range}
            view.print_play(data.strout, data.turns, pointer)
            view.header(data.MSG_GAME['win'].format(winner))
            return ['win', (winner, loser)]

