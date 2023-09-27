import players

def show_games():
    """doc"""
    db_players = players._read()
    table_line = tuple('—' * 10 for _ in range(4))
    table_stat = [('PLAYER', 'WINS', 'DRAWS', 'LOSES'), table_line]
    for name, stat in db_players.items():
        if name in ('DEFAULT', 'HARDBOT','EASYBOT'):
            continue
        table_stat.append((name, *(value for value in stat.values()))) 
    return table_stat
    


