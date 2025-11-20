import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules macros import Press, Release, Tap, Marcos

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D3, board.D1]

keyboard.matrix = KeysScanner(
  pins = PIN,
  value_when_pressed = false,
)

copy = (
  Press(KC.LCTL),
  Tap(KC.C),
  Release(KC.LCTL),
)

paste = (
  Press(KC.LCTL),
  Tap(KC.V),
  Release(KC.LCTL),
)

keyboard.keymap = [
  [KC.A, KC.DELETE, KC.MACRO("Hello world!"), KC,Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD]
]

if __name__ == '__main__':
  keyboard.go()
