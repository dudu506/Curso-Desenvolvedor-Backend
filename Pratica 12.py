import pyautogui
import time 

pyautogui.pause = 1
pyautogui.FAILSAFE = True


pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)



pyautogui.click(x=679, y=418)


pyautogui.click(x=298, y=59)

pyautogui.write('https://dpedriali.com.br')
pyautogui.press('enter')
time.sleep(3)