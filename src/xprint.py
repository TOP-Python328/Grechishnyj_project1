"""
Форматированне и вывод данных в консоль
Вспомогательный модуль
""" 

from shutil import get_terminal_size

def _template(size: int) -> str:
    """Функция генерирует игровое поле для отображения в консоли"""
    field_template = ''
    line = 0
    for _ in range(size):
        field_template += '|'.join(' {} ' for _ in range(size))
        if line == size - 1:
            field_template += '\n'
            break
        line += 1
        field_template += '\n' + '————'*(size) + '\n'
    return field_template


def _message(text: str) -> None:
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
    print(text_main, end="")
    return None

      
def table(dt_table: list[tuple]) -> None:
    """Функция печатает в консоли таблицу в рамке"""
    
    w_terminal = get_terminal_size().columns
    width = [
        max(len(str(obj)) for obj in column)
        for column in zip(*dt_table)
    ]
    rows = list(tuple(zip(width, tr)) for tr in dt_table)
    
    border = f'#{"=" * (w_terminal - 2)}#'
    line = f'#{" " * (w_terminal - 2)}#'
    table = ''
    table += border + line
    for row in rows:
        start_str = f'#    '
        tr = ''
        end_str = f'#'
        for cell in row:
            tr += ''.join(f' {cell[1]:<{cell[0]}}  ')
        table += start_str +  f'{tr[:-1]} '
        table += f'{" " * (w_terminal - len(tr) - len(start_str) - len(end_str))}{end_str}'
    table += line + border  
    print(table)
    return None
    
def right(string) -> None:
    """doc"""
    w_terminal = get_terminal_size().columns
    str_left = '\n' + ' ' * (w_terminal - len(string)) + string
    print(str_left)
    return None
    
    

