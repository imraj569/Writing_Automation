from pynput import keyboard 
from time import sleep 
import os
from colorama import Fore,init
init(autoreset=True)
import pyautogui
os.system("cls")
from keyboard import press_and_release


def banner():
    os.system("cls")
    print(Fore.GREEN+'''
╭╮╭╮╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮
┃┃┃┃┃┃╱╭╯╰╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱╭╯╰╮
┃┃┃┃┃┣━╋╮╭╋━━╮╭━━┳━━┳━━┳┳━┻╮╭╋━━┳━╋╮╭╯
┃╰╯╰╯┃╭╋┫┃┃┃━┫┃╭╮┃━━┫━━╋┫━━┫┃┃╭╮┃╭╮┫┃
╰╮╭╮╭┫┃┃┃╰┫┃━┫┃╭╮┣━━┣━━┃┣━━┃╰┫╭╮┃┃┃┃╰╮
╱╰╯╰╯╰╯╰┻━┻━━╯╰╯╰┻━━┻━━┻┻━━┻━┻╯╰┻╯╰┻━╯ 
________________________________________
Author-Rajkishor Patra
Version-1.0
________________________________________''')
    print(Fore.YELLOW+'''
*Click anywhere you want to write the lines present in the text.txt file
*it works globally so just go where you want then press F2 to write the lines
 ''')    

file_path = "text.txt" 
def read_first_line(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        if len(lines) > 0:
            first_line = lines[0]
            remaining_lines = lines[1:]
            with open(file_path, "w") as updated_file:
                updated_file.writelines(remaining_lines)
            return first_line
        return None

is_paused = False

#for 1st year students
def read_first_line(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        if len(lines) > 0:
            first_line = lines[0]
            remaining_lines = lines[1:]
            with open(file_path, "w") as updated_file:
                updated_file.writelines(remaining_lines)
            return first_line
        return None

def on_press(key):
    global is_paused
    if key == keyboard.Key.f2:
        first_line = read_first_line(file_path)
        if first_line:
            press_and_release("ctrl+a")
            press_and_release("backspace")
            sleep(0.10)
            pyautogui.write(first_line)
            print(f"Text Data - {first_line} completed✅")

        else:
            print(Fore.RED+"No more texts in the text file. Press Esc to exit.'❌")

def on_release(key):
    global is_paused
    if key == keyboard.Key.esc:
        # Stop the listener
        return False
    elif key == keyboard.Key.f1:
        is_paused = True

if __name__ == "__main__":
    banner()
    # Create a listener for key presses
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
