import pyperclip
import time

def greeting(recipient):
    current_time = time.localtime()
    if current_time[3] >= 12:
        to_copy = "Good afternoon %s," % recipient
        pyperclip.copy(to_copy)
    else:
        to_copy = "Good morning %s," % recipient
        pyperclip.copy(to_copy)

if __name__ == "__main__":
    name = pyperclip.paste()
    greeting(name.title())
