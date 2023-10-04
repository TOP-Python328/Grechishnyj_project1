"""
Глобальные переменные, условные константы.
Вспомогательный модуль.
"""
from collections.abc import Sequence, Callable
from numbers import Real
from pathlib import Path
from sys import path, argv


# Режим разработки 
DEBUG: bool = '-d' in argv
test_path = 'test' if DEBUG else ''


# Файлы хранения данных
FILE_NAME_PLAYERS = 'players.ini'
FILE_NAME_SAVES = 'saves.ttt'
ROOT_DIR = Path(path[0]).parent
DATA_DIR = ROOT_DIR / 'data'
players_path = DATA_DIR / f'{test_path}/{FILE_NAME_PLAYERS}'
saves_path = DATA_DIR / f'{test_path}/{FILE_NAME_SAVES}'


# Переменные для аннотаций
Players = dict[str, dict[str, int]]
Saves = dict[tuple[str, str], tuple[list[int], list[str]]]
UserSave = tuple[list[int], list[str]]
Dim = int
Names = tuple[str, str]
Steps = list[int]
Turns = list[str]
SquareIndex = int
Series = Sequence[Real | str]
Matrix = Sequence[Series]
Statistics = list[tuple[str, str, str, str]]


# Команды управления приложением.
COMMANDS = {
    'начать новую партию': ('new', 'n', 'начать', 'н'),
    'сохранить текущую игру': ('save', 's', 'сохранить', 'с'),
    'загрузить существующую партию': ('load', 'l', 'загрузка', 'з'),
    'отобразить раздел помощи': ('help', 'h', 'помощь', 'п'),
    'создать или переключиться на игрока': ('player', 'p', 'игрок', 'и'),
    'отобразить таблицу результатов': ('table', 't', 'таблица', 'т'), 
    'изменить размер поля': ('dim', 'd', 'размер', 'р'),
    'выйти': ('quit', 'q', 'выход', 'в'),
}


# Сообщения пользователю во время игры.
MSG_GAME = {
    'step': 'Ход {}... ',
    'save': 'Игра сохранена!',
    'draw': 'НИЧЬЯ...',
    'win': 'ПОЗДРАВЛЯЕМ ПОБЕДИТЕЛЯ - {} !!!',
    'busy': 'Клетка занята, повторите...',
    'error': 'Не корректный ввод, повторите...',
}


# Заголовки приложения.
MSG_HEAD = {
    'title': 'TIC TAC TOE',
    'version': 'version 0.0.4',
    'menu': '\nМЕНЮ: > ',
    'user_save': 'Введите номер партии: > ',
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

# авторизованный пользователь (главный игрок)
user_auth: str = None
# второй игрок соперник
opponent: str = None
# база игроков
players_db: Players = {}
# база сохранений
saves_db: Saves = {} 
# игровая пара: имена
players: Names = None
# сохраненные игры авторизованного игрока
user_save: UserSave = None
# размер игрового поля
size = 3
# числовая последовательность от 1 до количества ячеек поля
size_range = [i+1 for i in range(size**2)]
# числовая последовательность от 0 до размера поля
dim_range = range(size)
# игровые символы
tokens = ('X','O')
# список победных комбинаций
wins: list[set[int, int, int]] = None
# шаблон игрового поля
strout: str = None
# упорядоченный список сделанных ходов
steps = []
# упорядоченный список символов (X, O) сделанных ходов
turns = [' ' for _ in range(size**2)]
# словарь ячеек игрового поля со значением сделанного хода  --> номер: символ (X, O)
steps_turns: dict[int, str] = {}
# словарь всех ячеек игрового поля --> номер: ' '
empty: dict[int, str] = None
# стратегические матрицы
start_matrices: tuple[Matrix, Matrix] = tuple()
# веса токенов
WEIGHT_OWN: float = 1.5
WEIGHT_FOE: float = 1.0
WEIGHTS: set[float] = {WEIGHT_OWN, WEIGHT_FOE}