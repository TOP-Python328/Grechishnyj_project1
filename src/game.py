import players
import saves
import utils
import xprint
import litlib

def play(
        names: tuple[str, str], 
        steps: list[int], 
        turns: tuple[str, str, str],
    ) -> tuple[str, ...]:
    """doc"""
    
    tokens = ('O', 'X')
    size = int(len(turns) ** 0.5)
    wins = utils.fill_wins(size)
    strout = xprint._template(size)
    
    while True:
        # ВЫВОД ИГРОВОГО ПОЛЯ
        print(f'\n{strout.format(*turns)}', end='')
        try:
            # ХОД
            step = input(litlib.title_step.format(names[len(steps) % 2]))
            if step == 'save':
                xprint._message(litlib.game_saved)
                return ['save_game', (steps, turns)]
            else:
                step = int(step)
                utils.add_step(step, steps, size)
                turns[step - 1] = tokens[len(steps)%2]
            # НИЧЬЯ
            if utils.is_draw(steps, wins):
                print(f'\n{strout.format(*turns)}', end='')
                print(f'Ничья\n')
                xprint._message(litlib.end_draw)
                return False        
            # ПОБЕДА
            if utils.is_win(steps, wins):
                winner = names[len(steps) % 2 - 1]
                loser = names[len(steps) % 2]
                print(f'\n{strout.format(*turns)}', end='')
                print(f'Победитель - {winner}\n')
                xprint._message(litlib.end_win.format(winner))
                return ['win_game', (winner, loser)]
        except:
            print(litlib.error_digit)
            break


    

