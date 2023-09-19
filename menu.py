# Главное меню программы
# Проработать структуру данных ???
options = {
    'начать новую партию': {
        'en_long': 'new',
        'en_short': 'n',
        'ru_long': 'начать',
        'ru_short': 'н'},
    'загрузить существующую партию': {
        'en_long': 'load', 
        'en_short': 'l', 
        'ru_long': 'загрузка', 
        'ru_short': 'з'},
    'отобразить раздел помощи': {
        'en_long': 'help', 
        'en_short': 'h', 
        'ru_long': 'помощь', 
        'ru_short': 'п'},
    'создать или переключиться на игрока': {
        'en_long': 'player', 
        'en_short': 'p', 
        'ru_long': 'игрок', 
        'ru_short': 'и'},
    'отобразить таблицу результатов': {
        'en_long': 'table', 
        'en_short': 't', 
        'ru_long': 'таблица', 
        'ru_short': 'т'}, 
    'изменить размер поля': {
        'en_long': 'dim', 
        'en_short': 'd', 
        'ru_long': 'размер', 
        'ru_short': 'р'},
    'выйти': {
        'en_long': 'quit', 
        'en_short': 'q', 
        'ru_long': 'выход', 
        'ru_short': 'в'}}   

# Функция(и) для команд главного меню 
def _command():
    
    def _help():
            help_string = ''
            for keys, values in options.items():
                help_string += keys
                for key, value in values.items():
                    help_string += f' | {value}'
                help_string += '\n'  
            print(help_string)
            
    command = input('Введите команду: ')
    
    while command:
        for option in options.values():
            for value in option.values():
                if command in ('help', 'h', 'помощь', 'п'):
                    return _help()
        else:
            command = input('Введите команду: ')
            
    