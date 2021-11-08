print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.handlers.sequences import send_string, simple_key_sequence

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.GP28,
    board.GP27,
    board.GP26,
    board.GP5,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
    board.GP21,
    board.GP22,
    )

keyboard.row_pins = (
    board.GP15,
    board.GP14,
    board.GP13,
    board.GP8,
    board.GP7,
    board.GP6,
    )

keyboard.diode_orientation = DiodeOrientation.COL2ROW

layers_ext = Layers()
keyboard.modules = [layers_ext]

nokey = KC.NO

PRINT = simple_key_sequence(
    (
        KC.P,
        KC.R,
        KC.I,
        KC.N,
        KC.T,
    )
)

keyboard.keymap = [
    # Mac
    [    
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, nokey, KC.ESC,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC, KC.INS,
        KC.TAB,  KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.DELETE,
        KC.CAPS,  KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, nokey, KC.ENTER, KC.PGUP, 
        KC.LSFT,  KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, nokey, KC.RSHIFT, KC.UP, KC.PGDOWN,
        KC.LCTL, KC.LALT, KC.LGUI, nokey, nokey,  KC.SPC, nokey, nokey, nokey, KC.RGUI, KC.RALT, KC.MO(2), KC.LEFT, KC.DOWN, KC.RIGHT,
    ],
    # Windows 
    [    
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, nokey, KC.ESC,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC, KC.INS,
        KC.TAB,  KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.DELETE,
        KC.CAPS,  KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, nokey, KC.ENTER, KC.PGUP, 
        KC.LSFT,  KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, nokey, KC.RSHIFT, KC.UP, KC.PGDOWN,
        KC.LCTL, KC.LGUI, KC.LALT, nokey, nokey,  KC.SPC, nokey, nokey, nokey, KC.RGUI, KC.RALT, KC.MO(2), KC.LEFT, KC.DOWN, KC.RIGHT,
    ],
    # Functions 
    [    
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, nokey, PRINT,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC, PRINT,
        KC.TAB,  KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, PRINT,
        KC.CAPS,  KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, nokey, KC.ENTER, KC.AUDIO_VOL_UP, 
        nokey, nokey, nokey, nokey, nokey, nokey, nokey, nokey, nokey, nokey, nokey, nokey, KC.RSHIFT, KC.MEDIA_PLAY_PAUSE, KC.AUDIO_VOL_DOWN,
        KC.LCTL, KC.LGUI, KC.LALT, nokey, nokey,  KC.SPC, nokey, nokey, nokey, KC.TG(1), KC.TG(0), KC.MO(0), KC.MEDIA_REWIND, KC.DOWN, KC.MEDIA_FAST_FORWARD,
    ],
    
]


if __name__ == '__main__':
    keyboard.go()