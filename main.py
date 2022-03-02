from pynput import keyboard
import pyautogui
import time
import sys

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

    def start_keyboard(self):
        print('Keyboard started...')
        while self.condition:
            # press and release the space key
            controller = keyboard.Controller()
            controller.press(keyboard.Key.space)
            controller.release(keyboard.Key.space)
            time.sleep(.5)
            controller.press(keyboard.Key.backspace)
            controller.release(keyboard.Key.backspace)
            time.sleep(.5)
        

    def delay_start(self):
        for seq in range(self.delay):
            print(self.delay - seq)
            time.sleep(1)

    def __init__(self):
        mode = input('Choose mode: (m)ouse or (k)eyboard: ')
        print('Starting Online-Faker in {0} seconds...'.format(self.delay))
        print('You can quit the application pressing the ESC key.')
        listener = keyboard.Listener(on_release=self.on_release)
        listener.start()
        self.delay_start()
        if mode == 'm':
            self.start_mouse()
        elif mode == 'k':
            self.start_keyboard()

OnlineStatusFaker()