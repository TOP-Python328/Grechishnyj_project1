import players
import saves
import utils
import xprint

def play(
        names: tuple[str, str], 
        steps: list[int], 
        turns: tuple[str, str, str]
    ) -> tuple[str, ...]:
    """doc"""
    
    tokens = ('O', 'X')
    size = int(len(turns) ** 0.5)
    wins = utils.fill_wins(size)
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
                utils.add_step(step, steps, size)
                turns[step - 1] = tokens[len(steps)%2]
    
            # НИЧЬЯ
            if utils.is_draw(steps, wins):
                xprint._message(f'The game ended in a draw...')
                return {'draw': (names)}         
            # ПОБЕДА
            if utils.is_win(steps, wins):
                winner = names[len(steps) % 2 - 1]
                loser = names[len(steps) % 2]
                xprint._message(f'Congratulations winner - {winner} !!!')
                return {'win': (winner, loser)}
        except:
            print('Вы ввели не число')
            break

def update_save(item: dict[str: tuple], db_file) -> None:
    """doc"""
    values = list(value for value in item.values())[0]
    if 'save' in item:
        db_file[values[0]] = values[1:]
        saves._write_save(f'{saves.parse_to_string(db_file)}\n')
    if 'win' in item or 'draw' in item:
        db_file.pop(values)
        saves._write_save(f'{saves.parse_to_string(db_file)}\n')     

def update_players(item: dict[str: tuple], db_file):
    """doc"""
    values = list(value for value in item.values())[0]
    if 'win' in item:
        winner = values[0]
        loser = values[1]
        players._update(winner, 'wins', str(int(db_file[winner]['wins']) + 1))
        players._update(loser, 'loses', str(int(db_file[loser]['loses']) + 1))
    if 'draw' in item:
        draw_01 = values[0]
        draw_02 = values[1]
        players._update(draw_01, 'draws', str(int(db_file[draw_01]['draws']) + 1))
        players._update(draw_02, 'draws', str(int(db_file[draw_02]['draws']) + 1))
    

