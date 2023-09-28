"""
Глобальные переменные, условные константы.
Вспомогательный модуль.
"""

from pathlib import Path
from sys import path, argv

# Режим разработки 
DEBUG: bool = '-d' in argv
test_path = 'test/' if DEBUG else ''

# Файлы хранения данных
FILE_NAME_PLAYERS = 'players.ini'
FILE_NAME_SAVES = 'saves.ttt'
ROOT_DIR = Path(path[0]).parent
DATA_DIR = ROOT_DIR / 'data'
players_path = DATA_DIR / f'{test_path}{FILE_NAME_PLAYERS}'
saves_path = DATA_DIR / f'{test_path}{FILE_NAME_SAVES}'

# Переменные для аннотаций
Players = dict[str, dict[str, int]]
Saves = dict[tuple[str, str], tuple[list[int], list[str]]]

# Комманды управления приложением.
COMMANDS = [
    ('начать новую партию', 'new', 'n', 'начать', 'н'),
    ('сохранить текущую игру', 'save', 's', 'сохранить', 'с'),
    ('загрузить существующую партию', 'load', 'l', 'загрузка', 'з'),
    ('отобразить раздел помощи', 'help', 'h', 'помощь', 'п'),
    ('создать или переключиться на игрока', 'player', 'p', 'игрок', 'и'),
    ('отобразить таблицу результатов', 'table', 't', 'таблица', 'т'), 
    ('изменить размер поля', 'dim', 'd', 'размер', 'р'),
    ('выйти', 'quit', 'q', 'выход', 'в'),
]

# Сообщения пользователю во время игры.
MSG_GAME = {
    'step': 'Ход {}... ',
    'save': 'Игра сохранена!',
    'draw': 'The game ended in a draw...',
    'win': 'Congratulations winner - {} !!!',
    'error': 'Не корректный ввод, повторите...',
}

# Заголовки приложения.
MSG_HEAD = {
    'title': 'TIC TAC TOE',
    'version': 'version 0.0.3',
    'menu': '\nМЕНЮ: > ',
    'not_save': 'СОХРАНЕННЫХ ПАРТИЙ НЕ НАЙДЕНО!',
    'player_change': 'СМЕНИТЬ ИГРОКА.',
    'table': 'ТАБЛИЦА РЕЗУЛЬТАТОВ.',
    'dim': 'ИЗМЕНЕНИТЕ РАЗМЕР ИГРОВОГО ПОЛЯ!',
    'end': 'ИГРА ЗАКОНЧЕНА!',
    
}

# Сообщения при авторизации пользователя и выборе режима.
MSG_USER = {
    'name': 'Введите имя игрока: > ',
    'modes': [('ОДИНОЧНАЯ ИГРА', 1), ('ИГРА С СОПЕРНИКОМ', 2)],
    'mode': 'Выберете режим игры: > ',
    'diffs': [('ПРОСТО', 1), ('СЛОЖНО', 2)],
    'diff': 'Выберете уровень сложности: > ',
    'bots': ('EASYBOT', 'HARDBOT'),
    'opponent': 'Введите имя игрока 2: > ',
    'tokens': [('Играть X', 1), ('Играть O', 2)],
    'token': '{} выберете чем будете играть: > ', 
}

size = 3



