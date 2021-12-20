#sms bombing new version :
import pyautogui
from pystyle import Box , Colors , Colorate
from time import sleep
from pynput.keyboard import Key, Listener
from colorama import Fore
print(Fore.GREEN+(Box.Lines("Hello , Welcome to All ")))
print(Colorate.DiagonalBackwards(Colors.yellow_to_red,"""
 ____            ____     ____                  ____  _             
/ ___| _ __ ___ / ___|   | __ )  ___  _ __ ___ | __ )(_)_ __   __ _ 
\___ \| '_ ` _ \\___ \   |  _ \ / _ \| '_ ` _ \|  _ \| | '_ \ / _` |
 ___) | | | | | |___) |  | |_) | (_) | | | | | | |_) | | | | | (_| |
|____/|_| |_| |_|____/___|____/ \___/|_| |_| |_|____/|_|_| |_|\__, |
                    |_____|                                   |___/ 
      """))
print(Colorate.Horizontal(Colors.green_to_red , " \t\t\t*** Coded_By_Nidhal *** "))
sleep(2)
print("\n")
try:
 NbrMsg=int(input(Fore.CYAN+"choose a number of sms you want to send to your victim :"))
 k=input((Fore.BLUE+"the default message is 'are you connected' , whould you change it ! [y/n] > "))
 if k=="y" or k=="Y":
    sms=input(Fore.YELLOW+"whrite your message : ")
 elif k=="n" or k=="N":
    sms="Are You Connected"
 else:
     exit()
 print(Fore.MAGENTA+"Click [enter] To Start Sending ..")
 def Know_key(key):
     if key == key.enter:
         for i in range(NbrMsg):
            pyautogui.write(sms)
            sleep(0.1)
            pyautogui.press('enter')
            sleep(0.1)
         sleep(2)
         print(Fore.MAGENTA+"sms sended successfully :)")
         sleep(1)
 with Listener(on_press=Know_key) as listener:
    listener.join()

except ValueError:
    print("please choose a correct number :(")
finally:
    print("program finished ")
