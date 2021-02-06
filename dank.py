from math import gcd
from random import choice
from time import sleep
from pynput import keyboard

from bot import bot, findHCF, findLCM


# delcare the necessary information, change if necessary
# Commands need to be functions (no parameters)

postmeme = lambda: "pls postmeme\n"+ choice(["f", "r", "i", "c", "k"]) + "\n" 

OPTIONS = [
    {"command": postmeme, "reset_time": 50},
    {"command": lambda: "pls fish\n", "reset_time": 50},
    {"command": lambda: "pls beg\n", "reset_time": 50},
    {"command": lambda: "pls hunt\n", "reset_time": 50},
    {"command": lambda: "pls dep max\n", "reset_time": 50},
    {"command": lambda: "pls hl\n"+ choice(["high", "low"]) + "\n", "reset_time": 50}
]

# Choose the key to terminate the program
TERMINATE_KEY = keyboard.Key.end


# run the file
# do not edit below this line

if __name__ == "__main__":
    controller = keyboard.Controller()
    dankbot = bot(OPTIONS, controller)

    def on_press(key): # Check when "end" key is pressed
        if key == TERMINATE_KEY:
            dankbot.proceed = False
            print('Ending Program...')
            return False

    for i in range(11): # Countdown sequence
        if i == 10:
            print("Start!")
        else:
            print(10 - i)
            sleep(1)

    with keyboard.Listener(on_press=on_press) as listener: # Keyboard Event Listener
        while dankbot.proceed:
            dankbot.run_cycle()
        listener.join()

