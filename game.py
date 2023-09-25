import utils
import xprint

def play(names, steps, turns):
    """doc"""
    TOKENS = ('O', 'X')
    size = int(len(turns) ** 0.5)
    wins = utils._wins(size)
    strout = xprint._template(size)
    
    while True:
        print(f'\n{strout.format(*turns)}', end='')
        try:
            # ХОД
            step = input(f'Ход {names[len(steps) % 2]}... ')
            
            # if not STEP:
            if step == 'save':
                #SAVE[names] = (STEPS, TURNS)
                # print(SAVE)
                # STR_SAVE = f'{saves._parse_ts(SAVE)}\n'
                # saves._write_save(STR_SAVE)
                xprint._message('Игра сохранена!')
                break
            else:
                print(f'{len(steps)=}')
                step = int(step)
                utils._addstep(step, steps, size)
                turns[step - 1] = TOKENS[len(steps)%2]
            # ВЫВОД ПОЛЯ
             
            # НИЧЬЯ
            if utils.isDraw(steps, wins):
                # ОБНОВЛЕНИЕ ДАННЫХ
                # players._update(name_01, 'draws', str(int(db_players[name_01]['draws']) + 1))
                # players._update(name_02, 'draws', str(int(db_players[name_02]['draws']) + 1))
                xprint._message(f'The game ended in a draw...')
                print(f'{names=}')
                break            
            # ПОБЕДА
            if utils.isWin(steps, wins):
                winner = names[len(steps) % 2 - 1]
                loser = names[len(steps) % 2]
                # players._update(winner, 'wins', str(int(db_players[winner]['wins']) + 1))
                # players._update(loser, 'loses', str(int(db_players[loser]['loses']) + 1))
                xprint._message(f'Congratulations winner - {winner} !!!')
                print(f'{winner=}, {loser=}') 
                break
        except:
            print('Вы ввели не число')
            continue
            
play(('Player_1', 'Player_2'), [], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
play(('Player_1', 'Player_2'), [1,2,3], ['X', 'O', 'X', ' ', ' ', ' ', ' ', ' ', ' '])