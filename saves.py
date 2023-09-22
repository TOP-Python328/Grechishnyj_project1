from pathlib import Path
from sys import path


db_saves = {
    ('player_01', 'player_02'): ([1, 2, 4, 3, 9], ['X', '0', '0', 'X', '', '', '', '', 'X']),
    ('player_01', 'player_03'): ([1, 2, 4, 3, 9], ['X', '0', '0', 'X', '', '', '', '', 'X']),
    ('player_01', 'player_04'): ([1, 2, 4, 3, 9], ['X', '0', '0', 'X', '', '', '', '', 'X']),
    ('player_01', 'player_05'): ([1, 2, 4, 3, 9], ['X', '0', '0', 'X', '', '', '', '', 'X']),
    ('player_01', 'player_08'): ([1, 2, 4, 3, 9], ['X', '0', '0', 'X', '', '', '', '', 'X']),
    ('player_01', 'player_06'): ([1, 2, 4, 3, 9], ['X', '0', '0', 'X', '', '', '', '', 'X']),
    ('player_01', 'player_07'): ([1, 2, 4, 3, 9], ['X', '0', '0', 'X', '', '', '', '', 'X']),
}
def _parse_ts(obj):
    """doc"""
    txt_saves = []
    for players, save in obj.items():
        players = ','.join(players)
        steps, turns = save
        steps = ','.join(str(s) for s in steps)
        turns = ','.join(str(t) for t in turns)
        txt_saves.append(f'{players}!{steps}!{turns}')
    return '\n'.join(txt_saves)
 

save = 'player_01,player_02!1,2,4,3,9!X,0,0,X,,,,,X' 
# def _parse_fs(obj):
    # """doc"""
    # db_saves = {}
    # players, steps, turns = obj.split('!')
    # players = tuple(players.split(','))
    # steps = list(int(s) for s in steps.split(','))
    # turns = list(turns.split(','))
    # db_saves[players] = (steps, turns)
    # return db_saves

def _write_save(obj: str) -> None:
    """doc"""
    save_path = Path(path[0]) / 'saves.ttt'
    with open(save_path, 'a', encoding='utf-8') as fileout:
        fileout.write(obj)
           
    
def _read_save() -> dict:
    """doc"""
    save_path = Path(path[0]) / 'saves.ttt' 
    text = save_path.read_text(encoding='utf-8')
    saves = text.split('\n')
    db_saves = {}
    for save in saves:
        players, steps, turns = save.split('!')
        players = tuple(players.split(','))
        steps = list(int(s) for s in steps.split(','))
        turns = list(turns.split(','))
        db_saves[players] = (steps, turns)
    return db_saves