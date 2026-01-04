# You import all the IOs of your board
import board

# These are imports from the kmk library - adding what you need for the keyboard to know what to do
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension and add the layers and media keys modules
macros = Macros()
keyboard.modules.append(macros)
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

# Define your pins in order from one to the last key
PINS = [board.D10, board.D2, board.D6, board.D1, board.D0, board.D7, board.D8, board.D9]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Add some Variables for easier reading instead of writing the full keycodes
LAYERTOGGLE = KC.TG(1)
WINLOCK = KC.RGUI(KC.L)
PRINT = KC.MACRO("System.out.println();")
MUTE = KC.MUTE

# Define the keymap
keyboard.keymap = [
    [MUTE, KC.NUMLOCK, KC.BRIU, KC.VOLU, KC.NO, PRINT, WINLOCK, LAYERTOGGLE],  # Layer 0
    [MUTE, KC.NUMLOCK, KC.BRID, KC.VOLD, KC.NO, PRINT, WINLOCK, LAYERTOGGLE],
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
