import pyautogui as gui
import time
#Исходный код бота для автоподнятия слотов
#После запуска бота нужно зайти на сайт FunPay и выбрать слот

screenWidth, screenHeight = gui.size() # Получаем размер экрана.
mousePos = gui.position()
gui.PAUSE = 2
def funStart():
       print("Created By LUVI")
       print("Private auto bot FunPay")
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
       return 0
while True:
       funStart()
       time.sleep(14400)









