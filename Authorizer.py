import pyautogui as pag
import pyperclip as ppc
import time as t

while True:
    pixel_1, pixel_2, pixel_3 = pag.pixel(150, 570), pag.pixel(1895,112), pag.pixel(1895,160)
    match_1 = pixel_1 == (25, 28, 33)
    match_2 = pixel_2 == (0, 160, 223)
    match_3 = pixel_3 == (0,160, 223)
    # проверка авторизована ли страница
    if (not match_1) and (match_2 or match_3):
        pag.hotkey('ctrl', 'shift', 'j')
        pag.click(1700, 860)
        pag.write("allow pasting")
        pag.press("enter")
        v = open('jsscript.txt', 'r')
        a = v.read()
        ppc.copy(a)
        pag.hotkey('ctrl', 'v')
        pag.press('enter')
        pag.press('f12')
    #каждые 10 минут страница обновляется и каждый час цикл начинается с начала
    for i in range(0,5):
        pag.press('f5') 
        t.sleep(600) 
    
# py -m pyinstaller --one-file --hidden-import pyautogui --hidden-import pyperclip --hidden-import time authorizer.py

