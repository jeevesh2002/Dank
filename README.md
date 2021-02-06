# dankmemerbot
Bot to play the discord "Dank memer" bot game

## Running the bot

### Dependencies
- pynput: `pip install pynput`

Run the dank.py file, you have 5 seconds to put your text cursor on your discord message box.

## Options

You can edit the commands used by the bot by editing the `OPTIONS` variable
```
postmeme = lambda: "pls postmeme\n"+ choice(["n", "r", "e", "d"]) + "\n"

OPTIONS = [
    {"command": postmeme, "reset_time": 60},
    {"command": lambda: "pls fish\n", "reset_time": 45},
    {"command": lambda: "pls beg\n", "reset_time": 45}
]
```
The example above is the default options. 

To include a new option, create a new dictionary with the keys `"command"` and `"reset_time"`.

The value of `"command"` is a function that returns the string that you want to type, the simplest way to do so is using anoymous function expressions `lambda: <return value>`, you can also write functions like `postmeme` that include logic.

The value of `"reset_time"` is an integer representing the time to wait before typing out the value specified in `"command"` again.

Do include the `\n` as it tells the program to press ENTER.

## Terminating the Program

At the default settings, you can terminate the program by pressing the `END` key. You can change this by editing the `TERMINATE_KEY` variable.

```
TERMINATE_KEY = keyboard.Key.end # Terminate with 'end' key
TERMINATE_KEY = keyboard.key.esc # Terminate with escape key
TERMINATE_KEY = keyboard.key.backspace # Terminate with backspace
```

You can find the list of options in the docs of `pynput`: https://pynput.readthedocs.io/en/latest/keyboard.html#reference
