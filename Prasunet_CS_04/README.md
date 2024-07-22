# Running the Python Keylogger Program

## Overview

This guide provides instructions on how to execute a simple keylogger program written in Python using the `pynput` library. The keylogger captures keystrokes and logs them to a file named `keylog.txt`. The `logging` module is used for logging keystrokes with timestamps.

## Requirements

1. **Python**: Ensure Python is installed on your system. You can download and install it from the [official Python website](https://www.python.org/downloads/).

2. **pynput Library**: This script requires the `pynput` library to capture keyboard events. You can install it using `pip`.

## Installing the Requirements

1. **Install Python**:
   - Download and install Python from [Python's official website](https://www.python.org/downloads/).
   - Ensure Python is added to your system's PATH during installation.

2. **Install pynput**:
   - Open your terminal or command prompt.
   - Run the following command to install the `pynput` library:

     ```sh
     pip install pynput
     ```

## How to Run the Program:

1. Open terminal and navigate to the directory where this script is saved!
2. Run the Script, execute the following command to start the keylogger:
```
python Simple Keylogger.py
```
3. The keylogger will start and begin capturing keystrokes.

## Stopping the Keylogger:

1. To stop the keylogger, press the *esc* key on your keyboard or terminate the terminal.
2. The program will terminate and stop capturing keystrokes.
3. Verify Logs:

- After stopping the script, open keylog.txt in the same directory as keylogger.py to view the logged keystrokes.
- The log entries will include timestamps and details of each key pressed.

#### Thank you!