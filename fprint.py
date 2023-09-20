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