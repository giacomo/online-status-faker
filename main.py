from pynput import keyboard
import pyautogui
import time

class OnlineStatusFaker:
    # define some pixels
    delay = 10
    pixel = 20
    condition = True

    def on_release(self, key):
        if key == keyboard.Key.esc:
            # Stop listener
            print('{0} released. Quitting the application.'.format(key))
            self.condition = False
            return False

    def start_mouse(self):
        print('Mouse started...')
        while self.condition:
            # jump vertically
            self.pixel *= -1
            # move the mouse cursor
            pyautogui.moveRel(0, self.pixel, duration=.2)

    def delay_start(self):
        for seq in range(self.delay):
            print(self.delay - seq)
            time.sleep(1)

    def __init__(self):
        print('Starting Online-Faker in {0} seconds...'.format(self.delay))
        print('You can quit the application pressing the ESC key.')
        listener = keyboard.Listener(on_release=self.on_release)
        listener.start()
        self.delay_start()
        self.start_mouse()

OnlineStatusFaker()