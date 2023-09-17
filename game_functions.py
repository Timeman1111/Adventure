import os
import sys
import time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return True


def scrollTxt(text,delay = 0.1):
   for char in text:
       sys.stdout.write(char)
       sys.stdout.flush()
       time.sleep(delay)