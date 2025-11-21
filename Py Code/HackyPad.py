import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules macros import Press, Release, Tap, Marcos

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D1, board.D2, board.D3, board.D4, board.D6, board.D8, board.D9, board.D10, board.D11]

keyboard.matrix = KeysScanner(
  pins = PINS,
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
  #[KC.A, KC.DELETE, KC.MACRO("Hello world!"), KC,Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD]
  [copy, paste, KC.ENTER,KC.ESC,KC.UP_ARROW,KC.DOWN_ARROW,KC.RIGHT_ARROW,KC.LEFT_ARROW]
]

if __name__ == '__main__':
  keyboard.go()
