# /proc/bus/input/devices 
# /dev/input
# evdev API 

"""
 Linux has a special kernel module called uinput (userspace input) that allows programs to create virtual input devices.

 

 my understading sp far:

 mouse events are stored in a file and for each connected devices 
 there is unique file
 so i need to send virtual movements using the uinput so those
 movements are then sent to the real mouse file event handler.

 the mouse movement signals are saved as struc in the kernal inside the
 input event files, amd the GMOME is alwaus checking in infinite loop
 all the input files and rendering the screem



 to code:

 1) have the keyboard file ready
 2) take exclusive control of the keyboard to work just as i wish
 3) write the movements to a virtual mouse file event handler
4) all sjpw be nested in a loop until program is ended


file name event0 for keyboard
"""
import io

#!/usr/bin/python3

# Open the keyboard device file
keyboard_file = open('/dev/input/event2', 'rb')

print("Opened keyboard. Press keys to see raw data...")
print("Press Ctrl+C to exit\n")

"""when a key is pressed a 24 byte stucture is stored in the event
file , the 24 bytes are broken down into :
* first 16 bytes are timestamps
* 2 bytes for TYPE -what kind of event
/* 2 bytes for code - which key/button
* last 4  bytes for value - press/hold/release
"""
try:
    while True:

        # Read one event (24 bytes)
        full_event = keyboard_file.read(24)
        type_code_value = full_event[16:24]  # Gets bytes 16 through 23
        if type_code_value [0:2] == b'\x01\x00': 
            print(f"Type/Code/Value bytes: {type_code_value}")

except KeyboardInterrupt:
    print("\nExiting...")
    keyboard_file.close()



