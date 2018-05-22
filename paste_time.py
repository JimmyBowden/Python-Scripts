import pyperclip
import time

def paste_time():
    current_time = time.localtime()
    pyperclip.copy(time.strftime("%H:%M", current_time))

if __name__ == "__main__":
    paste_time()
