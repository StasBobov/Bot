import pyautogui, time

time.sleep(5)

f = open('my_text.txt', 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')