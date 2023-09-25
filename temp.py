import menu
import players
import utils
import xprint
import saves

# ПЕРВЫЙ ЗАПУСК
TITLE = 'Крестики-Нолики'
HELP = menu.options
xprint._message(TITLE)
print('version 0.0.2')
xprint._table(HELP)

# ИГРОК
# ==========================
# читаем проверяем добавляем
db_players = players._read() 
name_01 = input('Введите имя игрока 1: > ')
print()
# ДОБАВЛЯЕМ ИГРОКА ЕСЛИ НЕТ В БАЗЕ
if name_01 not in db_players:
    players._create(name_01)
# читаем проверяем добавляем
# ==========================
# РЕЖИМ ИГРЫ
xprint._table([('ОДИНОЧНАЯ ИГРА', 1), ('ИГРА С СОПЕРНИКОМ', 2)])
game_mod = input('Выберете режим игры: > ')
print()
# ОДИН ИГРОК
if game_mod == '1':
    # УРОВЕНЬ СЛОЖНОСТИ
    xprint._table([('ПРОСТО', 1), ('СЛОЖНО', 2)])
    difficulty = input('Выберете уровень сложности: > ')
    print()
    if difficulty == '1':
        name_02 = 'EASYBOT'
    else:
        name_02 = 'HARDBOT'
# ДВА ИГРОКА
# ==========================
# читаем проверяем добавляем
if game_mod == '2':
    name_02 = input('Введите имя игрока 2: > ')
    print()
# ДОБАВЛЯЕМ ВТОРОГО ИГРОКА ЕСЛИ НЕТ В БАЗЕ
if name_02 not in db_players:
    players._create(name_02)
db_players = players._read() 
names = (name_01, name_02)
# читаем проверяем добавляем
# ==========================

# ВЫБОР ТОКЕНА
xprint._table([('Играть X', 1), ('Играть O', 2)]) 
player_01_token = input(f'{name_01} выберете чем будете играть: > ')   
if player_01_token == '2':
    reversed(names)


SIZE = 3
CMD = input('КОМАНДА МЕНЮ: > ')
TOKENS = ('O', 'X')
#ВКЛ/ВЫКЛ
while True:
    if CMD == 'dim':
        SIZE = menu._dim()
    # ПРОЦЕСС ИГРЫ
    if CMD == 'new':
        TURNS = [' ' for _ in range(SIZE**2)]
        STEPS = []
        WINS = utils._wins(SIZE)
        STROUT = xprint._template(SIZE)
        print(f'\n{STROUT.format(*TURNS)}', end='')
        
        SAVE = {tuple(names):(STEPS, TURNS)}
        print(SAVE)
        
        while True:
            try:
                # ХОД
                
                STEP = input(f'Ход {names[len(STEPS) % 2]}... ')
                
                # if not STEP:
                if STEP == 'save':
                    #SAVE[names] = (STEPS, TURNS)
                    print(SAVE)
                    STR_SAVE = f'{saves._parse_ts(SAVE)}\n'
                    saves._write_save(STR_SAVE)
                    xprint._message('Игра сохранена!')
                    break
                else:
                    STEP = int(STEP)
                    utils._addstep(STEP, STEPS, SIZE)
                    TURNS[STEP - 1] = TOKENS[len(STEPS)%2]
                # ВЫВОД ПОЛЯ
                print(f'\n{STROUT.format(*TURNS)}', end='') 
                # НИЧЬЯ
                if utils.isDraw(STEPS, WINS):
                    # ОБНОВЛЕНИЕ ДАННЫХ
                    players._update(name_01, 'draws', str(int(db_players[name_01]['draws']) + 1))
                    players._update(name_02, 'draws', str(int(db_players[name_02]['draws']) + 1))
                    xprint._message(f'The game ended in a draw...')
                    break            
                # ПОБЕДА
                if utils.isWin(STEPS, WINS):
                    # ОБНОВЛЕНИЕ ДАННЫХ
                    winner = names[len(STEPS) % 2 - 1]
                    loser = names[len(STEPS) % 2]
                    players._update(winner, 'wins', str(int(db_players[winner]['wins']) + 1))
                    players._update(loser, 'loses', str(int(db_players[loser]['loses']) + 1))
                    xprint._message(f'Congratulations winner - {winner} !!!')
                    break  
            except:
                print('except')


                print('Вы ввели не число')
                continue
    if CMD == 'load':
        print('load')
        SAVESGAME = saves._read_save()
        if names in SAVESGAME:
        
            print(f'{SAVESGAME[names]=}')
            STEPS = SAVESGAME[names][0]
            TURNS = SAVESGAME[names][1]
            SIZE = int(len(TURNS)**0.5)
            print(f'{STEPS=}, {TURNS=}')
            WINS = utils._wins(SIZE)
            STROUT = xprint._template(SIZE)
            print(f'\n{STROUT.format(*TURNS)}', end='')
            while True:
                try:
                    # ХОД
                    
                    STEP = input(f'Ход {names[len(STEPS) % 2]}... ')
                    
                    # if not STEP:
                    if STEP == 'save':
                        #SAVE[names] = (STEPS, TURNS)
                        print(SAVE)
                        STR_SAVE = f'{saves._parse_ts(SAVE)}\n'
                        saves._write_save(STR_SAVE)
                        xprint._message('Игра сохранена!')
                        break
                    else:
                        STEP = int(STEP)
                        utils._addstep(STEP, STEPS, SIZE)
                        TURNS[STEP - 1] = TOKENS[len(STEPS)%2]
                    # ВЫВОД ПОЛЯ
                    print(f'\n{STROUT.format(*TURNS)}', end='') 
                    # НИЧЬЯ
                    if utils.isDraw(STEPS, WINS):
                        # ОБНОВЛЕНИЕ ДАННЫХ
                        players._update(name_01, 'draws', str(int(db_players[name_01]['draws']) + 1))
                        players._update(name_02, 'draws', str(int(db_players[name_02]['draws']) + 1))
                        xprint._message(f'The game ended in a draw...')
                        break            
                    # ПОБЕДА
                    if utils.isWin(STEPS, WINS):
                        # ОБНОВЛЕНИЕ ДАННЫХ
                        winner = names[len(STEPS) % 2 - 1]
                        loser = names[len(STEPS) % 2]
                        players._update(winner, 'wins', str(int(db_players[winner]['wins']) + 1))
                        players._update(loser, 'loses', str(int(db_players[loser]['loses']) + 1))
                        xprint._message(f'Congratulations winner - {winner} !!!')
                        break  
                except:
                    print('except')


                    print('Вы ввели не число')
                    continue
            
        else:
            print('Игр нет')
    if CMD == 'player':
        # ==========================
        # читаем проверяем добавляем
        xprint._message('СМЕНИТЬ ИГРОКА')
        name_01 = input('Введите имя игрока 1: > ')
        print()
        # ДОБАВЛЯЕМ ИГРОКА ЕСЛИ НЕТ В БАЗЕ
        # if name_01 not in db_players:
            # players._create(name_01)
        # db_players = players._read() 
        # names = [name_01, name_02]
        # читаем проверяем добавляем
        # ==========================
    if CMD == 'table':
        xprint._message('ТАБЛИЦА РЕЗУЛЬТАТОВ')
        db_players = players._read()
        table_line = tuple('—' * 10 for _ in range(4))
        table_stat = [('PLAYER', 'WINS', 'DRAWS', 'LOSES'), table_line]
        for name, stat in db_players.items():
            if name in ('DEFAULT', 'HARDBOT','EASYBOT'):
                continue
            table_stat.append((name, *(value for value in stat.values()))) 
        xprint._table(table_stat) 
        # КОМАНДА МЕНЮ: > table
        #===========================================================================#
        #                                                                           #
        #                            ТАБЛИЦА РЕЗУЛЬТАТОВ                            #
        #                                                                           #
        #===========================================================================#
        #===========================================================================#
        #                                                                           #
        #     PLAYER      | WINS        | DRAWS       | LOSES                       #
        #     ——————————  | ——————————  | ——————————  | ——————————                  #
        #     USER        | 0           | 1           | 1                           #
        #     ADMIN       | 2           | 1           | 0                           #
        #     Pavel       | 0           | 0           | 1                           #
        #     Oleg        | 0           | 0           | 0                           #
        #     QWERTY      | 3           | 1           | 0                           #
        #     TREWQ       | 0           | 1           | 0                           #
        #     ASDFG       | 0           | 0           | 1                           #
        #     ZXCVB       | 1           | 1           | 0                           #
        #     MNBVC       | 0           | 1           | 1                           #
        #     ZENIT       | 1           | 0           | 0                           #
        #     QWERT       | 1           | 0           | 1                           #
        #     SDFG        | 0           | 0           | 0                           #
        #                                                                           #
        #===========================================================================#        

    if CMD == 'quit':
        break
    
    CMD = input('КОМАНДА МЕНЮ: > ')
xprint._message('ИГРА ЗАКОНЧЕНА!')

# 13:09:46 > python -i temp.py
#==========================================================================================================================#
#                                                                                                                          #
#                                                     Крестики-Нолики                                                      #
#                                                                                                                          #
#==========================================================================================================================#
# version 0.0.2
#==========================================================================================================================#
#                                                                                                                          #
#     начать новую партию                  | new     | n  | начать    | н                                                  #
#     загрузить существующую партию        | load    | l  | загрузка  | з                                                  #
#     отобразить раздел помощи             | help    | h  | помощь    | п                                                  #
#     создать или переключиться на игрока  | player  | p  | игрок     | и                                                  #
#     отобразить таблицу результатов       | table   | t  | таблица   | т                                                  #
#     изменить размер поля                 | dim     | d  | размер    | р                                                  #
#     выйти                                | quit    | q  | выход     | в                                                  #
#                                                                                                                          #
#==========================================================================================================================#

# Введите имя игрока 1: > USER

#==========================================================================================================================#
#                                                                                                                          #
#     ОДИНОЧНАЯ ИГРА     | 1                                                                                               #
#     ИГРА С СОПЕРНИКОМ  | 2                                                                                               #
#                                                                                                                          #
#==========================================================================================================================#

# Выберете режим игры: > 1

#==========================================================================================================================#
#                                                                                                                          #
#     ПРОСТО  | 1                                                                                                          #
#     СЛОЖНО  | 2                                                                                                          #
#                                                                                                                          #
#==========================================================================================================================#

# Выберете уровень сложности: > 1

#==========================================================================================================================#
#                                                                                                                          #
#     Играть X  | 1                                                                                                        #
#     Играть O  | 0                                                                                                        #
#                                                                                                                          #
#==========================================================================================================================#

# Выберете за кого играть: > 0
# ['BOTEASY', 'USER']
# КОМАНДА МЕНЮ: > dim
# Введите размер поля: 4
# КОМАНДА МЕНЮ: > new
#    |   |   |
# ————————————————
#    |   |   |
# ————————————————
#    |   |   |
# ————————————————
#    |   |   |

# Ход BOTEASY: > 6
#    |   |   |
# ————————————————
#    | X |   |
# ————————————————
#    |   |   |
# ————————————————
#    |   |   |

# Игра продолжается...
# Ход USER: > 7
#    |   |   |
# ————————————————
#    | X | O |
# ————————————————
#    |   |   |
# ————————————————
#    |   |   |

# Игра продолжается...
# Ход BOTEASY: > 11
#    |   |   |
# ————————————————
#    | X | O |
# ————————————————
#    |   | X |
# ————————————————
#    |   |   |

# Игра продолжается...
# Ход USER: > 10
#    |   |   |
# ————————————————
#    | X | O |
# ————————————————
#    | O | X |
# ————————————————
#    |   |   |

# Игра продолжается...
# Ход BOTEASY: > 4
#    |   |   | X
# ————————————————
#    | X | O |
# ————————————————
#    | O | X |
# ————————————————
#    |   |   |

# Игра продолжается...
# Ход USER: > 16
#    |   |   | X
# ————————————————
#    | X | O |
# ————————————————
#    | O | X |
# ————————————————
#    |   |   | O

# Игра продолжается...
# Ход BOTEASY: > 13
#    |   |   | X
# ————————————————
#    | X | O |
# ————————————————
#    | O | X |
# ————————————————
#  X |   |   | O

# Игра продолжается...
# Ход USER: > 1
#  O |   |   | X
# ————————————————
#    | X | O |
# ————————————————
#    | O | X |
# ————————————————
#  X |   |   | O

#==========================================================================================================================#
#                                                                                                                          #
#                                               The game ended in a draw...                                                #
#                                                                                                                          #
#==========================================================================================================================#
# КОМАНДА МЕНЮ: > quit
#==========================================================================================================================#
#                                                                                                                          #
#                                                     ИГРА ЗАКОНЧЕНА!                                                      #
#                                                                                                                          #
#==========================================================================================================================#



# Ход BOTEASY: > 100
#  X | X | X | X | X | X | X | X | X | O
# ————————————————————————————————————————
#  O |   |   |   |   |   |   |   |   | X
# ————————————————————————————————————————
#  O |   |   |   |   |   |   |   |   | X
# ————————————————————————————————————————
#  O |   |   |   |   |   |   |   |   | X
# ————————————————————————————————————————
#  O |   |   |   |   |   |   |   |   | X
# ————————————————————————————————————————
#  O |   |   |   |   |   |   |   |   | X
# ————————————————————————————————————————
#  O |   |   |   |   |   |   |   |   | X
# ————————————————————————————————————————
#  O |   |   |   |   |   |   |   |   | X
# ————————————————————————————————————————
#  O |   |   |   |   |   |   |   |   | X
# ————————————————————————————————————————
#  X | O | O | O | O | O | O | O | O | O

#==========================================#
#                                          #
#       The game ended in a draw...        #
#                                          #
#==========================================#