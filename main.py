# Бот для смены тарифов агроторга. Заранее открыть договор, отфилтровать по услугам

import pyautogui as pg
import time

pg.FAILSAFE = True  # выход из скрипта
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
pg.keyDown('alt')  # переключение на окно участка
pg.press('tab')
pg.keyUp('alt')
time.sleep(1)  # время на ожидание


def bot_tarif(services:str='inkas') -> None:
    """Функция бота"""
    pg.click(x=436, y=273)  # кликнуть в первую строку списка
    time.sleep(0.5)
    pg.press('pdup', presses=10)  # подняться в спсике максмально высоко на верхнюю строку
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
    if services == 'inkas':
        down_list = 5
    elif services == 'razmen':
        down_list = 30
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
    # time.sleep(1.5)
    pg.press('enter')  # сохранить изменения
    pg.press('tab', presses=4, interval=0.5)  # поправить на 4
    # time.sleep(1.5)
    pg.press('enter')  # сохранить изменения
    time.sleep(1.5)


i = 0
for i in range(20):
    bot_tarif(services='inkas')
    i += 1