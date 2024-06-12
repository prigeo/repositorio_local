import pyautogui as auto
import time

auto.PAUSE = 0.5

auto.hotkey('ctrl', 'j')
auto.hotkey('ctrl', 'j')

nome_repositorio = input('Nome do repositório: ')
auto.press("enter")

auto.write('git init')
auto.press("enter")
auto.write('git add .')
auto.press("enter")
auto.write(f'git commit -m "{nome_repositorio}"')
auto.press("enter")
time.sleep(3)

auto.write('cxfreeze main.py --target-dir pasta-repositorio')

auto.press('enter')
auto.write('git push')

time.sleep(3)

auto.press('win')
auto.write("edge")
auto.press("enter")

auto.hotkey('alt', 'space')
auto.press('x')

auto.write('github.com')
auto.press("enter")