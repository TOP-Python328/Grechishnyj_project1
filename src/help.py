"""
Исполнительный модуль — раздел помощи.
"""

import data
import view


def info_game(key) -> None:
    """Функция выводит сообщение с правилами игры"""
    view.print_box(key, data.TITLES[key], 'X')

    
def rules_game(key) -> None:
    """Функция выводит сообщение с пояснением интерфейса"""
    view.print_box(key, data.TITLES[key])
    
    
def main_menu(dict_command) -> None:
    """Функция выводит команды меню"""
    menu = []
    for key, values in dict_command.items():
        menu.append((key, *values))
    view.table(menu)
    return None


"""
ПРАВИЛА ИГРЫ

Вы играете одним из двух символов: крестиком 'X' или ноликом 'O'. Чтобы победить, первым составьте последовательность
из 3 своих символов в одной строке, в обном столбце, либо диагонали.

ИНТЕРФЕЙС

Игра предлагает вам интерфейс командной строки. Это означает, что для выполнения определенного действия в игре необходимо ввести команду и нажать Enter.
В последнем разделе данной справки приведен список действий и соответсвующих им команд, которые можно использовать в славном меню между партиями.

Во время выполнения различных действий игра может запрашивать у Вас дополнительные данные или задавать уточняющие вопросы.
В таких случаях возможные варианты ввода перечисляются в скобках в конце строки с приглашением для ввода.
Отсутствие перечисления вариантов ввода означает, что можно вводить любые данные: например, когда запрашивает имя игрока.

Во время партии игра ожидает от игрока(-ов) ввода номера клетки для текущего хода.
Нумерация клеток показана в примере ниже. Ввод одной из следующих команд: save, s, сохранить, с - позволит Вам сохранить незавершенную партию и вернуться в главное меню.
"""





    