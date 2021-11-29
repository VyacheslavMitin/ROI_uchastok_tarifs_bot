# Бот для смены тарифов Аграторга и прочих "больших" клиентов.
# Заранее открыть договор с карточками обслуживания, отфильтровать по тарифам которые нужно поменять и запустить

import pyautogui as pg
import time
import os
import sys

# Проверка подразделения
if os.getlogin() == 'sonic':
    CITY = 'ulyanovsk'
    x, y = 436, 273
elif os.getlogin() == 'user':
    CITY = 'dimitrovgrad'
    x, y = 493, 462
else:  # выход с ошибкой если не то имя логина в систему
    sys.exit("Ошибка: не подходящий логин в систему!")

pg.FAILSAFE = True  # выход из скрипта, не понятно как работает
# Агроторг
inkas_agrotog_min = '276'
inkas_agrotorg_percentage = '0,05'
razmen_agrotog = '551'
# Перекресток
inkas_perekrestok_min = '276'
inkas_perekrestok_percentage = '0,03'
razmen_perekrestok = '551'
# Переменные с тарифами
first_coef = inkas_agrotog_min
second_coef = inkas_agrotorg_percentage
third_coef = razmen_agrotog

# Начало работы скрипта
time.sleep(1)  # время на ожидание
cycle = int(pg.prompt(text='Введите количество шагов', title='Количество шагов', default='20'))
pg.keyDown('alt')  # переключение на окно участка
pg.press('tab')
pg.keyUp('alt')
time.sleep(1)  # время на ожидание


def bot_tarif(services: str = 'inkas') -> None:
    """Функция бота"""
    pg.click(x, y)  # кликнуть в первую строку списка
    time.sleep(0.5)
    pg.press('pageup', presses=10)  # подняться в списке максимально высоко на верхнюю строку
    pg.keyDown('shift')  # прощелкивание до кнопки с тарифами
    pg.press('tab', presses=3, interval=0.5)
    pg.keyUp('shift')
    pg.press('enter')  # сменить тариф
    pg.press('tab', presses=6, interval=0.5)  # прощелкивание до смены тарифы
    pg.press('enter')  # переход в окно с периодом и налогом
    pg.write('01.10.2021', interval=0.25)
    pg.press('tab', presses=3, interval=0.5)
    pg.press('down', presses=2, interval=0.5)
    pg.hotkey('ctrl', 'tab')  # переход в окно с коэффециентами
    down_list = ''
    if services == 'inkas':
        if CITY == 'ulyanovsk':
            down_list = 5
        else:
            down_list = 2
    elif services == 'razmen':
        if CITY == 'ulyanovsk':
            down_list = 30
        else:
            down_list = 15
    pg.press('down', presses=down_list)
    pg.press('tab', presses=2, interval=1)  # прощелкивание до коэффициентов
    if services == 'inkas':
        pg.write(first_coef, interval=0.25)
        pg.press('down')
        pg.write(second_coef, interval=0.25)
    elif services == 'razmen':
        pg.write(third_coef, interval=0.25)
    pg.press('tab')  # прокликивание окна с текстовым описанием тарифа
    pg.press('tab', presses=2, interval=0.5)  # поправить на 2
    pg.press('enter')  # сохранить изменения
    pg.press('tab', presses=4, interval=0.5)  # поправить на 4
    pg.press('enter')  # сохранить изменения
    time.sleep(1.5)


i = 0
for i in range(cycle):
    bot_tarif(services='inkas')
    print(f'Шаг {i}')
    i += 1
pg.alert(text=f'Исполнено {cycle} раз', title='Исполнено', button='OK')
