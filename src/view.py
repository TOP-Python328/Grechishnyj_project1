"""
Форматирование и вывод данных в консоль.
Вспомогательный модуль.
""" 

from shutil import get_terminal_size


def template(size: int) -> str:
    """Функция генерирует игровое поле для отображения в консоли"""
    field_template = ''
    line = 0
    for _ in range(size):
        field_template += '|'.join(' {} ' for _ in range(size))
        if line == size - 1:
            field_template += '\n'
            break
        line += 1
        field_template += '\n' + '————' * (size - 1) + '———' + '\n'
    return field_template
    

def table(table_dt: list[tuple]) -> None:
    """Функция печатает в консоли таблицу в рамке"""
    w_terminal = get_terminal_size().columns
    width = [
        max(len(str(obj)) for obj in column)
        for column in zip(*table_dt)
    ]
    rows = list(tuple(zip(width, tr)) for tr in table_dt)
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
        table += start_str + f'{tr[:-1]} '
        table += f'{" " * (w_terminal - len(tr) - len(start_str) - len(end_str))}{end_str}'
    table += line + border  
    print(table)
    return None


def header(text: str) -> None:
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


def print_right(text: str) -> None:
    """Функция выводит в stdout текст выравнивая его справа"""
    w_terminal = get_terminal_size().columns
    text = text.split('\n')
    text_right = ''
    for line in text:
        text_right += ' ' * (w_terminal - len(line)) + line
    print(text_right)
    
def print_center(text: str) -> None:
    """Функция выводит в stdout текст выравнивая его по центу"""
    w_terminal = get_terminal_size().columns
    text = text.split('\n')
    text_center = ''
    for line in text:
        len_line = len(line)
        width_out_line = w_terminal - len_line
        margin_left = width_out_line // 2
        if len_line % 2:
            margin_right = margin_left + 1
        else:
            margin_right = margin_left
        text_center += ' ' * margin_left + line + ' ' * margin_right
    return text_center


def print_play(template: str, chars: tuple, right: bool=False) -> None:
    """Функция выводит в stdout игровое поле"""
    if right:
        print_right(f'\n{template.format(*chars)}')
    else:
        print(f'\n{template.format(*chars)}')

def header2(text: str, char_top: str = '-', char_bottom: str = '-') -> None:
    """Функция выводит в stdout форматированную строку сообщения в рамке по ширине CLI"""
    width = get_terminal_size().columns
    inside = width - 6

    char_line = '='
    char_spot = '#'
    char_empt = ' ' 
    border_top = char_spot + char_top * (width - 2) + char_spot
    border_bottom = char_spot + char_bottom * (width - 2) + char_spot
    empt_line = char_spot + char_empt * (width - 2) + char_spot
    
    
    text_main = border_top + empt_line if char_top == '=' else border_top
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
    text_main += (empt_line + border_bottom) if border_bottom == '=' else border_bottom
    print(text_main, end="")
    return None