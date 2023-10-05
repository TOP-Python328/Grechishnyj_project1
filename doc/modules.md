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
        utils
            itertools import compres
            data
            view
        view
            shutil import get_terminal_size
        help
            data
            view
-->
    
main (точка входа)
data (глобальные переменные, условные константы)
files (чтение запись данных файлов)
user (получаем пользователя, авторизация)
game (игровой процесс, обновление файлов)
bot (виртуальный игрок - бот)
view (вывод в консоль в форматированном виде)
utils (дополнительные функции)
