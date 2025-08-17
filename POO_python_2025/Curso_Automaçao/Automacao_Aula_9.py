# https://www.youtube.com/watch?v=h9vEE1KWsI4&list=PLpdAy0tYrnKyjrY1Fr72DhmrRmeWI_5C8&index=9&ab_channel=HashtagPrograma%C3%A7%C3%A3o

import pyautogui
import time

pyautogui.PAUSE = 0.3
# Pegar posiçoes do mouse e da tela
print(pyautogui.position())
time.sleep(5) # Espera 5 segundos para depois fazer o proximo passo
print(pyautogui.size())

# funçoes teclado
pyautogui.hotkey("win")
time.sleep(1)
pyautogui.write('chrome')
pyautogui.hotkey("enter")
time.sleep(1)
# funçoes do mouse
pyautogui.click(x=725, y=59)
time.sleep(1)
pyautogui.write("youtube.com")
pyautogui.hotkey("enter")
time.sleep(5)

posicao_click = pyautogui.locateCenterOnScreen("click1.PNG")
pyautogui.click(posicao_click)
time.sleep(0.3)
posicao_click2 = pyautogui.locateCenterOnScreen("click2.PNG")
pyautogui.click(posicao_click2)
time.sleep(10)
posicao_click3 = pyautogui.locateCenterOnScreen("click3.PNG")
pyautogui.click(posicao_click3)

# pyautogui.moveTo(x=1858, y=147, duration=1)
# pyautogui.click(x=1858, y=147)
# pyautogui.moveTo(x=1711, y=245, duration=1)
# pyautogui.click(x=1711, y=245)
time.sleep(0.5)
pyautogui.scroll(-200) # numero negativo = scroll para baixo
# time.sleep(10)
# pyautogui.moveTo(x=126, y=195, duration=1)
# pyautogui.click(x=126, y=195)
