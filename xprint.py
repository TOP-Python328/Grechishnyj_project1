from shutil import get_terminal_size

def _message(text: str) -> str:
    """Функция выводит в stdout форматированную строку сообщения в рамке по ширине CLI"""
    
    width = get_terminal_size().columns
    inside = width - 6
    
    char_line = '='
    char_spot = '#'
    char_empt = ' '
    
    bord_line = char_spot + char_line * (width - 2) + char_spot
    empt_line = char_spot + char_empt * (width - 2) + char_spot
    
    text_main = bord_line + empt_line
    
    start = 0
    batch = inside
    text_split = []
    
    while batch < len(text):
        text_split.append(text[start:batch])
        start, batch = batch,  batch + inside
    text_split.append(text[start:])
    
    for text_part in text_split:
        if len(text_part) < inside:
            start_remains = int((inside - len(text_part)) / 2) + 2
            end_remains = inside - start_remains - len(text_part) + 4
        else:
            start_remains = end_remains = 2
        
        text_main += (
            char_spot + 
            char_empt * start_remains +
            text_part +
            char_empt * end_remains +
            char_spot
        )
            
    text_main += (empt_line + bord_line)
    print(text_main)

# переработать
def _table(dt_table: list[tuple]) -> str:
    """doc"""
    w_terminal = get_terminal_size().columns
    width = [
        max(len(str(obj)) for obj in column)
        for column in zip(*dt_table)
    ]
    width_line = sum(width)

    str_table = ''
    str_table += f'#{"=" * width_line}#\n'
    str_table += f'#{" " * width_line}#\n'     
    for i in range(len(dt_table)):
        str_table += ''.join(f'#    {i+1}. {dt_table[i][0]:<{width[0]}}'
            f' | {dt_table[i][1]:<{width[1]}}' 
            f' | {dt_table[i][2]:^{width[2]}}'
            f' | {dt_table[i][3]:<{width[3]}}'
            f' | {dt_table[i][4]:^{width[4]}}'
            f' #\n')
    str_table += f'#{" " * width_line}#\n' 
    str_table += f'#{"=" * width_line}#'
    
    table = str_table.split('\n')
    for li in table:
        char = li[-2]
        lilen = w_terminal - len(li)
        li = li[:-1] + char * lilen + '#'
        print(li, end='')