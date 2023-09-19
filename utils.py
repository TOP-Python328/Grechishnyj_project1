# Функция шаблона игрового поля
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

# Функция построения выигрышных комбинаций
def _wins(size: int) -> list[set[int]]:
    """Функция возвращает список сетов выигрышных комбинаций в зависимости от размера игрового поля."""
    
    # Целевой список победных комбинаций
    wins_combinations = []
    # Список всех номеров игрового поля
    all_numbers = [i+1 for i in range(size**2)]
    # Для сбора комбинаций используется двумерный список
    main_list = [all_numbers[i:i+size] for i in range(0, len(all_numbers), size)]
    # Победная комбинация по главной диагонали 
    diagonal_main = [] 
    # Победная комбинация по обратной диагонали
    diagonal_back = []    
    
    for i in range(size):
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

# Функция проверяет корректность ввода и добавляет значение хода если проверка пройдена
def _addstep(step, steps, size) -> list[int]:
    """Функция проверяет корректность ввода и добавляет значение хода если проверка пройдена"""
    if step not in steps and 0 < step <= size**2: 
        steps.append(step)
        return steps
        
# Функция проверки наличия выигрышной комбинации в списке шагов
def _wincheck(steps: list[int], wins: list[tuple]) -> bool:
    """Функция проверки наличия выигрышной комбинации в списке шагов"""
    steps1 = set(steps[::2])
    steps2 = set(steps[1::2])
    for win in wins:
        if win == steps1:
            print('Победил игрок 1')
            return True
        if win == steps2:
            print('Победил игрок 2')
            return True
        else:
            print('Игра продолжается...')
            return False

    