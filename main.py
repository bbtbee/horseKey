import keyboard
import threading

count = 0
horse = "horse"
# prevents recursive calls to onKeyEvent just in case
# stops program from horsing around
horsing = False
stopEvent = threading.Event()


def onKeyEvent(event):
    global count
    global horsing
    if horsing or event.event_type != keyboard.KEY_DOWN:
        return
    if event.name == 'esc':
        stopEvent.set()
        return

    horsing = True
    if count >= 5:
        count = 0
    try:
        keyboard.write(horse[count])
        count += 1
    finally:
        horsing = False


if __name__ == '__main__':
    hook = keyboard.hook(onKeyEvent, suppress=True)
    stopEvent.wait()
    keyboard.unhook(hook)
    quit()
