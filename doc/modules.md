### Текущая структура модулей

<!-- 
    main 
        data
            collections.abc import Sequence, Callable
            numbers import Real
            pathlib import Path
            sys import path, argv
        files
            configparser import ConfigParser
            data
        user
            data
            files
            view
        game
            data
            files
            utils
            view
            bot
        bot
            random import choice
            data
            matrix_st
        matrix_st
            data
        utils
            itertools import compres
            data
            view
        view
            shutil import get_terminal_size
-->
    
main (точка входа)
data (глобальные переменные, условные константы)
files (чтение запись данных файлов)
user (получаем пользователя, авторизация)
game (игровой процесс, обновление файлов)
bot (виртуальный игрок - бот)
matrix_st (начальные матрицы стратегий)
view (вывод в консоль в форматированном виде)
utils (дополнительные функции)
