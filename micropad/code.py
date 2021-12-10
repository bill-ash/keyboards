import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC 
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.handlers.sequences import send_string, simple_key_sequence

keyboard = KMKKeyboard()

# right Side
keyboard.row_pins = (
    board.GP10,
    board.GP13,
    board.GP15,
    )

# left Side
keyboard.col_pins = (
    board.GP16, board.GP18, board.GP21,
    )

keyboard.diode_orientation = DiodeOrientation.COL2ROW

layers_ext = Layers()
keyboard.modules = [layers_ext]


# MAC 
SPOTLIGHT = KC.LCMD(KC.SPACE)
ZOOM_STRING = send_string('zoom')
START_ZOOM_MEETING =  KC.LCMD(KC.LCTL(KC.V))
ZOOM_INVITE = KC.LCMD(KC.I)
ZOOM_MUTE = KC.LCMD(KC.LSHIFT(KC.A))
ZOOM_VIDEO = KC.LCMD(KC.LSHIFT(KC.V))
ZOOM_FULL = KC.LCMD(KC.LSHIFT(KC.F))
ZOOM_SCREEN_SHARE = KC.LCMD(KC.LSHIFT(KC.S))
ZOOM_SCHEDULE = KC.LCMD(KC.J)
ZOOM_RAISE_HAND = KC.LALT(KC.Y)

ZOOM_LEAVE_SEQ = simple_key_sequence((KC.LCMD(KC.W), KC.ENTER))
ZOOM_START_SEQ = simple_key_sequence((SPOTLIGHT, ZOOM_STRING, KC.ENTER, START_ZOOM_MEETING, ZOOM_INVITE))
ZOOM_SCHEDULE_SEQ = simple_key_sequence((SPOTLIGHT, ZOOM_STRING, KC.ENTER, ZOOM_SCHEDULE))


#  Windows
W_SPOTLIGHT = KC.LGUI
W_ZOOM_FOCUS = KC.LCTRL(KC.LALT(KC.LSHIFT))

W_ZOOM_TOGGLE_CONTROL = KC.LALT
W_ZOOM_CLOSE = KC.LALT(KC.F4)
W_ZOOM_VIDEO = KC.LALT(KC.V)
W_ZOOM_MUTE = KC.LALT(KC.A)
W_ZOOM_SCREEN_SHARE = KC.LALT(KC.LSHIFT(KC.S))
W_ZOOM_SWITCH_CAMERA = KC.LALT(KC.N)
W_ZOOM_FULL = KC.LALT(KC.F)
W_ZOOM_CHAT = KC.LALT(KC.H)
W_ZOOM_INVITE = KC.LALT(KC.I)
W_ZOOM_RAISE_HAND = KC.LALT(KC.Y)

# W_ZOOM_TOGGLE_CONTROLS = KC.LCTRL(KC.LALT(KC.LSHIFT(KC.H)))

W_ZOOM_START_SEQ = simple_key_sequence((W_SPOTLIGHT, W_SPOTLIGHT, KC.SPACE, ZOOM_STRING, KC.ENTER, KC.ENTER))
W_ZOOM_LEAVE_SEQ = simple_key_sequence((W_ZOOM_CLOSE, KC.ENTER))

W_TOGGLE_LAYER = KC.TD(
    W_ZOOM_START_SEQ, 
    KC.TG(1)
    )

TOGGLE_LAYER = KC.TD(
    ZOOM_START_SEQ, 
    KC.TG(0)
    )

keyboard.keymap = [
    # layer 0 
    [
        W_TOGGLE_LAYER, W_ZOOM_VIDEO, W_ZOOM_MUTE,
        W_ZOOM_INVITE,  W_ZOOM_SCREEN_SHARE, W_ZOOM_LEAVE_SEQ,
        W_ZOOM_TOGGLE_CONTROL, W_ZOOM_RAISE_HAND, W_ZOOM_FULL,
    ],
    # layer 1 
    [
        TOGGLE_LAYER, ZOOM_VIDEO, ZOOM_MUTE,
        ZOOM_INVITE,  ZOOM_SCREEN_SHARE, ZOOM_LEAVE_SEQ,
        ZOOM_SCHEDULE_SEQ, ZOOM_RAISE_HAND, ZOOM_FULL,
    ],
]

if __name__ == '__main__':
    keyboard.go()

