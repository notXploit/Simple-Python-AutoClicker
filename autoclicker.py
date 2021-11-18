import pyautogui as pa
from time import sleep
start = input('You Want Start The AutoClicker ? Y/N: ')
if start == 'Y':
    print('The AutoClicker will Start After 15 Seconds !')
    print('You cant Stop The AutoClicker !')
    sleep(15)
    while True:
        pa.click()
elif start == 'N':
    print('Close After 2 Seconds')
    sleep(0.5)
    print('to Open The Script Type\npython3 autoclicker.py')
    sleep(2)
    quit()
else:
    print('invalid option')
    quit()
# Python AutoClicker
# By Yasser Mob
# instagram : real.yassermob