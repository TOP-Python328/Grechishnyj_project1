import xprint

# Главное меню программы
# Проработать структуру данных ???
# Использование 
    # 1 - вывод инструкции
    # 2 - управление игрой


   
options = [
    ('начать новую партию', 'new', 'n', 'начать', 'н'),
    ('загрузить существующую партию', 'load', 'l', 'загрузка', 'з'),
    ('отобразить раздел помощи', 'help', 'h', 'помощь', 'п'),
    ('создать или переключиться на игрока', 'player', 'p', 'игрок', 'и'),
    ('отобразить таблицу результатов', 'table', 't', 'таблица', 'т'), 
    ('изменить размер поля', 'dim', 'd', 'размер', 'р'),
    ('выйти', 'quit', 'q', 'выход', 'в')
] 


    
def _help(list_options: list[tuple]) -> list[tuple]:
    """doc"""
    return list_options
    
def _dim() -> int:
    """Функция запрашивает и возвращает размер поля"""
    while True:
        size = input('Введите размер поля: ') 
        if size.isdigit(): 
            size = int(size)
            if 2 < size <= 20:
                return size
            else:
                print('Введен не допустимый размер.')
        else:
            print('Введено не число.')
 
    
def _menu():  

    while True:
        try:
            command = input('Введите команду: ') 
        except:
            print('Ошибка ввода:')
            command = input('Введите команду: ') 
        
        for key, value in options.items():
            if command in value:
                if command in ('new', 'n', 'начать', 'н'):
                    print(key)
                if command in ('load', 'l', 'загрузка', 'з'):
                    print(key)
                if command in ('help', 'h', 'помощь', 'п'):
                    _help(options)
                if command in ('player', 'p', 'игрок', 'и'):
                    print(key)
                if command in ('table', 't', 'таблица', 'т'):
                    print(key)
                if command in ('dim', 'd', 'размер', 'р'):
                    print(_dim())
                if command in ('quit', 'q', 'выход', 'в'):
                    print(key)

    