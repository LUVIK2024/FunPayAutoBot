import pyautogui as gui
import time
from colorama import *
 #Исходный код бота для автоподнятия слотов
#После запуска бота нужно зайти на сайт FunPay и выбрать слот
init()
screenWidth, screenHeight = gui.size() # Получаем размер экрана.
gui.PAUSE = 2
def funStart():
       print(Fore.MAGENTA + "Created By LUVI | Public auto bot FunPay | Version: 1.0 Beta")
       time.sleep(5)
       gui.click(1232,192)
       gui.click(790,264)
       gui.click(792,281)
       gui.click(793,321)
       gui.click(795,335)
       gui.click(896,382)
       time.sleep(6)
       gui.click(1491,123)
       gui.click(1417,192)
       gui.click(1007,866)
while True:
       funStart()
       time.sleep(14400)









