### Текущая структура модулей

<!-- main                                           -->
<!--     data                                       -->
<!--         pathlib import Path                    -->
<!--         sys import path, argv                  -->
<!--     files                                      -->
<!--         configparser import ConfigParser       -->
<!--         data                                   -->
<!--     user                                       -->
<!--         data                                   -->
<!--         files                                  -->
<!--         view                                   -->
<!--     game                                       -->
<!--         data                                   -->
<!--         files                                  -->
<!--         utils                                  -->
<!--         view                                   -->
<!--     utils                                      -->
<!--         from itertools import compres          -->
<!--     view                                       -->
<!--         from shutil import get_terminal_size   -->
    
main (точка входа)
data (глобальные переменные, условные константы)
files (чтение запись данных файлов)
user (получаем пользователя, авторизация)
game (игровой процесс, обновление файлов)
view (вывод в консоль в форматированном виде)
utils (дополнительные функции)