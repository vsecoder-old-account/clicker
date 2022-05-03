import time
import threading
from pynput.mouse import Button, Controller
from pynput.mouse import Listener

delay = 0.08
button = Button.left
button1 = Button.right
k1 = 'Button.button9'
k2 = 'Button.button8'

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

mouse = Controller()
click_thread_left = ClickMouse(delay, button)
click_thread_left.start()
click_thread_right = ClickMouse(delay, button1)
click_thread_right.start()

def on_click(x, y, button, pressed):
    if str(button) == k1 and pressed:
        click_thread_left.start_clicking()
    elif str(button) == k1 and not pressed:
        click_thread_left.stop_clicking()

    elif str(button) == k2 and pressed:
        click_thread_right.start_clicking()
    elif str(button) == k2 and not pressed:
        click_thread_right.stop_clicking()

# Collect events until released
with Listener(
        on_click=on_click
       ) as listener:
    listener.join()
