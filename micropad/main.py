import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC 
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.handlers.sequences import send_string, simple_key_sequence

keyboard = KMKKeyboard()

# Left Side
keyboard.col_pins = (
    board.GP15,board.GP13,board.GP10,
    )

# Right Side
keyboard.row_pins = (
    board.GP21,
    board.GP18,
    board.GP16,
    )

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# layers_ext = Layers()
# keyboard.modules = [layers_ext]



SPOTLIGHT = KC.LCMD(KC.SPACE)
ZOOM_STRING = send_string('zoom')
START_ZOOM_MEETING =  KC.LCMD(KC.LCTL(KC.V))
ZOOM_INVITE = KC.LCMD(KC.I)
ZOOM_MUTE = KC.LCMD(KC.LSHIFT(KC.A))
ZOOM_VIDEO = KC.LCMD(KC.LSHIFT(KC.V))
ZOOM_FULL = KC.LCMD(KC.LSHIFT(KC.F))
ZOOM_SCREEN_SHARE = KC.LCMD(KC.LSHIFT(KC.S))
ZOOM_LEAVE = KC.LCMD(KC.W)
ZOOM_SCHEDULE = KC.LCMD(KC.J)
ZOOM_RAISE_HAND = KC.LALT(KC.Y)

ZOOM_START_SEQ = simple_key_sequence((SPOTLIGHT, ZOOM_STRING, KC.ENTER, START_ZOOM_MEETING,ZOOM_INVITE))
ZOOM_SCHEDULE_SEQ = simple_key_sequence((SPOTLIGHT, ZOOM_STRING, KC.ENTER, ZOOM_SCHEDULE))


keyboard.keymap = [
    [
        ZOOM_START_SEQ, ZOOM_MUTE, ZOOM_VIDEO, 
        ZOOM_INVITE, ZOOM_FULL, ZOOM_LEAVE,
        ZOOM_SCHEDULE_SEQ, ZOOM_RAISE_HAND, ZOOM_SCREEN_SHARE,
    ]
]


if __name__ == '__main__':
    keyboard.go()

