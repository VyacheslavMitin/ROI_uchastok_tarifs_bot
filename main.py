# Бот для смены тарифов агроторга. Заранее открыть договор, отфилтровать по услугам

import pyautogui as pg
import os
import sys
import time
from datetime import datetime
import subprocess

agrotog_min = '276'
agrotorg_percentage = '0,05'

minimal = agrotog_min
percentage = agrotorg_percentage

pg.keyDown('alt')  # переключение
pg.press('tab')
pg.keyUp('alt')
time.sleep(1)  # time for waiting

pg.click(x=881, y=446)
pg.press('pdup', presses=10)  # up list
pg.keyDown('shift')  # turn to change button
pg.press('tab', presses=3, interval=0.5)  # прощелкивание до кнопки с тарифами
pg.keyUp('shift')
pg.press('enter')  # enter change
pg.press('tab', presses=6, interval=0.5)  # прощелкивание до смены тарифы
pg.press('enter')  # переход в окно с периодом и налогом
pg.write('01.10.2021', interval=0.25)
pg.press('tab', presses=3, interval=0.5)
pg.press('down', presses=2, interval=0.5)
pg.hotkey('ctrl', 'tab')  # переход в окно с коэффециентами
pg.press('down', presses=5, interval=0.5)
pg.press('tab', presses=2, interval=1)  # прощелкивание до коэффициентов
pg.write(minimal, interval=0.25)
pg.press('down')
pg.write(percentage, interval=0.25)
pg.press('tab')  # прокликивание окна с текстовым описанием тарифа

# pg.press('enter')  # сохранить изменения

