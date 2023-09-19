import menu
import players
import utils

# ИГРОКИ
PLAYERS = players._read() 
name_01 = input('Введите имя игрока 1: > ')
name_02 = input('Введите имя игрока 2: > ')
check_names = False

if name_01 not in PLAYERS:
    players._create(name_01)
    check_names = True
if name_02 not in PLAYERS:
    players._create(name_02)
    check_names = True
if check_names:
    PLAYERS = players._read() 
    
PLAYER_01 = PLAYERS[name_01]
PLAYER_02 = PLAYERS[name_02]

print(PLAYER_01, PLAYER_02)

# ПРОЦЕСС ИГРЫ
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
        # ПОБЕДА
        end_game = WIN(STEPS, WINS)
        if end_game:
            if len(STEPS) % 2:
                players._update(name_01, 'wins', str(int(PLAYER_01['wins']) + 1))
                players._update(name_02, 'loses', str(int(PLAYER_02['loses']) + 1))
            else:
                players._update(name_01, 'loses', str(int(PLAYER_01['loses']) + 1))
                players._update(name_02, 'wins', str(int(PLAYER_02['wins']) + 1))
            break       
    except:
        break
        # print('Вы ввели не число')
        # continue

# 22:44:59 > python -i temp.py
# Введите имя игрока 1: > QWE
# Введите имя игрока 2: > ASD

# Введите число: > 1
#   X |   |
# ————————————
#     |   |
# ————————————
#     |   |

# Игра продолжается...
# Введите число: > 2
#   X | O |
# ————————————
#     |   |
# ————————————
#     |   |

# Игра продолжается...
# Введите число: > 3
#   X | O | X
# ————————————
#     |   |
# ————————————
#     |   |

# Игра продолжается...
# Введите число: > 4
#   X | O | X
# ————————————
#   O |   |
# ————————————
#     |   |

# Игра продолжается...
# Введите число: > 5
#   X | O | X
# ————————————
#   O | X |
# ————————————
#     |   |

# Игра продолжается...
# Введите число: > 6
#   X | O | X
# ————————————
#   O | X | O
# ————————————
#     |   |

# Игра продолжается...
# Введите число: > 7
#   X | O | X
# ————————————
#   O | X | O
# ————————————
#   X |   |

# Победил игрок 1

 
# ==================================================================
# ПРОЦЕСС ИГРЫ
# ==================================================================


# ГЛАВНОЕ МЕНЮ

    # menu._command()


# ИГРОКИ

    # # Получаем всех игоков
    # # Получаем имена игроков для игры
    # # Проверяем наличие игроков в списке всех игроков
    # # Если если кого-то нет, то создаем с новым именем
   
    
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