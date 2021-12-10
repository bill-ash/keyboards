# import board 
# import digitalio
# import storage
import supervisor

# Rename board 
# https://learn.adafruit.com/welcome-to-circuitpython/renaming-circuitpy
 
 # disable usb on startup 
# try:
#     button = digitalio.DigitalInOut(board.GP15)
#     storage.disable_usb_drive()
# except: 
    # storage.enable_usb_drive() 

# if storage.getmount('/').label == 'CIRCUITPY':
#     m = storage.getmount("/", readonly=False)
#     m.label = "ZOOM_BOARD"
#     storage.remount("/", readonly=False)
# # storage.enable_usb_drive()

supervisor.set_next_stack_limit(4096 + 4096)

# disable repl 
# usb_cdc.disable()  