from pathlib import Path
from sys import path

def parse_to_string(obj):
    """doc"""
    txt_saves = []
    for players, save in obj.items():
        players = ','.join(players)
        steps, turns = save
        steps = ','.join(str(s) for s in steps)
        turns = ','.join(str(t) for t in turns)
        txt_saves.append(f'{players}!{steps}!{turns}')
    return '\n'.join(txt_saves)

def _write_save(obj: str) -> None:
    """doc"""
    save_path = Path(path[0]) / 'saves.ttt'
    with open(save_path, 'w', encoding='utf-8') as fileout:
        fileout.write(obj)
           
def _read_save() -> dict:
    """doc"""
    save_path = Path(path[0]) / 'saves.ttt' 
    text = save_path.read_text(encoding='utf-8')
    saves = text.split('\n')
    
    db_saves = {}
    for save in saves[:-1]:
        players, steps, turns = save.split('!')
        players = tuple(players.split(','))
        steps = list(int(s) for s in steps.split(','))
        turns = list(turns.split(','))
        db_saves[players] = (steps, turns)
    return db_saves