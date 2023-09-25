
import utils
import xprint

def play(
        names: tuple[str, str], 
        steps: list[int], turns: tuple[str, str, str]
    ) -> tuple[str, ...]:
    """doc"""
    
    tokens = ('O', 'X')
    size = int(len(turns) ** 0.5)
    wins = utils._wins(size)
    strout = xprint._template(size)
    
    while True:
        # ВЫВОД ИГРОВОГО ПОЛЯ
        print(f'\n{strout.format(*turns)}', end='')
        print(names[0])
        try:
            # ХОД
            step = input(f'Ход {names[len(steps) % 2]}... ')
            
            if step == 'save':
                xprint._message('Игра сохранена!')
                return {'save': (names, steps, turns)}
            else:
                step = int(step)
                utils._addstep(step, steps, size)
                turns[step - 1] = tokens[len(steps)%2]
    
            # НИЧЬЯ
            if utils.isDraw(steps, wins):
                xprint._message(f'The game ended in a draw...')
                return {'draw': (names)}         
            # ПОБЕДА
            if utils.isWin(steps, wins):
                winner = names[len(steps) % 2 - 1]
                loser = names[len(steps) % 2]
                xprint._message(f'Congratulations winner - {winner} !!!')
                return {'win': (winner, loser)}
        except:
            print('Вы ввели не число')
            break
            
# play(('Player_1', 'Player_2'), [], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
# play(('Player_1', 'Player_2'), [1,2,3], ['X', 'O', 'X', ' ', ' ', ' ', ' ', ' ', ' '])