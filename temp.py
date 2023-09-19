import menu
import players
import utils

SIZE = 3 
WIN = utils._wincheck
WINS = utils._wins(SIZE) 
ADDSTEP = utils._addstep
STROUT = utils._template(SIZE)
TURNS = [' ' for _ in range(SIZE**2)]
TOKENS = ('O', 'X')
STEPS = []
 
while True:
    STEP = int(input('Введите число: > '))
    try:
        ADDSTEP(STEP, STEPS, SIZE)
        TURNS[STEP - 1] = TOKENS[len(STEPS)%2]
        print(STROUT.format(*TURNS))
        if WIN(STEPS, WINS):
            break       
    except:
        break
        # print('Вы ввели не число')
        # continue

# 16:58:56 > python -i temp.py
# Введите число: > 1
#  X |   |
# ————————————
#    |   |
# ————————————
#    |   |

# Игра продолжается...
# Введите число: > 4
#  X |   |
# ————————————
#  O |   |
# ————————————
#    |   |

# Игра продолжается...
# Введите число: > 2
#  X | X |
# ————————————
#  O |   |
# ————————————
#    |   |

# Игра продолжается...
# Введите число: > 5
#  X | X |
# ————————————
#  O | O |
# ————————————
#    |   |

# Игра продолжается...
# Введите число: > 3
#  X | X | X
# ————————————
#  O | O |
# ————————————
#    |   |

# Победил игрок 1
# >>>



 
# ==================================================================
# ПРОЦЕСС ИГРЫ
# ==================================================================


# ГЛАВНОЕ МЕНЮ

    # menu._command()


# ИГРОКИ

    # # Получаем игоков
    # players = read_players() 

    # # Получаем имена игроков для игры
    # player1_name = input()
    # player2_name = input()

    # # Проверяем наличие игроков в списке всех игроков
    # # Если если кого-то нет, то создаем с новым именем
    # if player1_name not in players:
        # create_player(player1_name)

    # if player2_name not in players:
        # create_player(player2_name)
    
# ИГРА

    # Проверяем наличие неоконченной партии для игроков
    # Запуск новой игры или загрузка существующей

# ХОДЫ

    # Загрузка ходов если загружена не оконченная игра
    # Подсчет ходов, продолжение подсчета ходов

# ПОБЕДА

    # Проверка после каждого хода на победу игрока сделавшего ход
    # Проверка на ничью из оставшихся комбинаций

# РЕЗУЛЬТАТЫ

    # Обновление данных игравших игроков в файле players.ini
    # Обновление файла games.ini с внесением новой партии, либо изменения существующей

# ПОВТОРНЫЙ ЗАПУСК

    # Сообщение об окончании игры
    # Продолжить | Показать результаты | Выход