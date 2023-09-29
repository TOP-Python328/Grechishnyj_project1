"""
Дополнительные функции.
Вспомогательный модуль.
"""

from itertools import compress


# ИСПОЛЬЗОВАТЬ: во время аннотаций множеств, как и для списков, мы указываем типы сразу для всех элементов
# КОММЕНТАРИЙ: я бы перенёс всё же эту развёрнутую аннотацию в data, объявив там отдельную переменную, и использовав её здесь
def fill_wins(size: int) -> list[set[int]]:
    # ИСПОЛЬЗОВАТЬ: разметку reStructuredText для документации функций — пригодится дальше, при работе в IDE
    """Функция возвращает список победных комбинаций в зависимости от размера игрового поля.
    
    :param size: размер игрового поля.
    :returns: список победных множеств, которые содержат в себе номера клеток
    """
    # Целевой список победных комбинаций
    wins_combinations = []
    # УДАЛИТЬ: вы не должны вычислять эту последовательность каждый раз, как она потребуется — объявите необходимую переменную в модулей data и обращайтесь к ней (а менять вы её будете один раз по изменении размера поля)
    # Список всех номеров игрового поля
    all_numbers = [i+1 for i in range(size**2)]
    # Для сбора комбинаций используется двумерный список
    main_list = [all_numbers[i:i+size] for i in range(0, len(all_numbers), size)]
    # Победная комбинация по главной диагонали 
    diagonal_main = []
    # Победная комбинация по обратной диагонали
    diagonal_back = []
    
    for i in range(size):
        # ИСПРАВИТЬ: работайте сразу с множествами, лишние преобразования не нужны
        # Победные комбинации по рядам
        rows = []
        # Победные комбинации по колонкам
        columns = []    
        for j in range(size):
            rows.append(main_list[i][j])
            columns.append(main_list[j][i])
            if i == j:
                diagonal_main.append(main_list[i][j])
            if i + j == size - 1: 
                diagonal_back.append(main_list[i][j])
        wins_combinations.append(set(rows))
        wins_combinations.append(set(columns))   
    wins_combinations.append(set(diagonal_main))
    wins_combinations.append(set(diagonal_back))
    return wins_combinations 


# ДОБАВИТЬ: аннотацию параметров
def add_step(step, steps, size) -> list[int]:
    """Функция проверяет корректность ввода и добавляет значение хода если проверка пройдена"""
    if step not in steps and 0 < step <= size**2: 
        steps.append(step)
        return steps


def is_win(steps: list[int], wins: list[set[int, ...]]) -> bool:
    """Функция проверки наличия выигрышной комбинации в списке шагов.
    
    Параметры: steps - список всех ходов, wins - список победных комбинаций.
    Возвращает: True | False проверяя на подмножество победные комбинации в списке ходов.
    """
    crosses = set(steps[::2])
    zeros = set(steps[1::2])
    for comb in wins:
        if comb <= crosses or comb <= zeros:
            return True
    else:
        return False


def is_draw(steps: list[int], wins: list[set[int]]) -> bool:
    """Функция исключает победную комбинацию из списка победную комбинаций.

    Параметры: steps - список всех ходов, wins - список победных комбинаций.
    Возвращает: True | False проверяя на истину список победных комбинаций.
    """
    crosses = set(steps[::2])
    zeros = set(steps[1::2])
    selectors = []
    for comb in wins:
        if comb & crosses and comb & zeros:
            selectors.append(0)
        else:
            selectors.append(1)
    wins = list(compress(wins, selectors))
    return not bool(wins)


def statistics(players):
    """doc"""
    table_line = tuple('—' * 10 for _ in range(4))
    table_stat = [('PLAYER', 'WINS', 'DRAWS', 'LOSES'), table_line]
    for name, state in players.items():
        if name in ('HARDBOT','EASYBOT'):
            continue
        table_stat.append((name, *(value for value in state.values()))) 
    return table_stat


# ИСПРАВИТЬ: перепишите эту функцию так, чтобы она в модуле data переопределяла все находящиеся там и связанные с размером поля переменные — и не вычисляйте эти переменные в каждой функции
def dim() -> int:
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

