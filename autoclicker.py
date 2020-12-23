# imports 
import time
import threading
from numpy import random
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# list of delays with random index selection
delays = [0.01, 0.05, 0.075, 0.001, 0.03, 0.005, 0.007, 0.08, 0.09, 0.085]
index = random.randint(0, 10)

# sets left mouse delay to randomized value from list
delay_0 = delays[index]

# right mouse delay constant
delay_1 = 0.01

# initialize buttons
button_0 = Button.left
button_1 = Button.right

# hotkeys
start_stop_key_left = KeyCode(char="r")
start_stop_key_right = KeyCode(char="f")
exit_key = KeyCode(char="c")

# autoclicker thread class
class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
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
                index = random.randint(0, 10)
                delay_0 = delays[index]
                time.sleep(delay_0)

# initialization
mouse = Controller()
click_thread_0 = ClickMouse(delay_0, button_0)
print("Right mouse button initialized!")
click_thread_1 = ClickMouse(delay_1, button_1)
print("Left mouse button initialized!")
click_thread_0.start()
click_thread_1.start()
print("Click threads initialized!")

# listener function
def on_press(key):
    if key == start_stop_key_left:
        if click_thread_0.running:
            click_thread_0.stop_clicking()
            print("Left button stopped.")
        else:
            click_thread_0.start_clicking()
            print("Left button started.")
    elif key == start_stop_key_right:
        if click_thread_1.running:
            click_thread_1.stop_clicking()
            print("Right button stopped.")
        else:
            click_thread_1.start_clicking()
            print("Right button started.")
    elif key == exit_key:
        click_thread_0.exit()
        click_thread_1.exit()
        listener.stop()

print("Listener initialized!")
print("Ready to use!")

# listener initialize 
with Listener(on_press=on_press) as listener:
    listener.join()

