# coding: utf-8
"""
Standard gamepad mappings.

Pulled in to Gamepad.py directly.
"""

class PS4(Gamepad):
    fullName = 'PlayStation 4 controller'

    def __init__(self, joystickNumber = 0):
        Gamepad.__init__(self, joystickNumber)
        self.axisNames = {
            0: 'LEFT-X',
            1: 'LEFT-Y',
            2: 'L2',
            3: 'RIGHT-X',
            4: 'RIGHT-Y',
            5: 'R2',
            6: 'DPAD-X',
            7: 'DPAD-Y'
        }
        self.buttonNames = {
            0:  'CROSS',
            1:  'CIRCLE',
            2:  'TRIANGLE',
            3:  'SQUARE',
            4:  'L1',
            5:  'R1',
            6:  'L2',
            7:  'R2',
            8:  'SHARE',
            9:  'OPTIONS',
            10: 'PS',
            11: 'L3',
            12: 'R3'
        }
        self._setupReverseMaps()


class Xbox360(Gamepad):
    fullName = 'Xbox 360 controller'

    def __init__(self, joystickNumber = 0):
        Gamepad.__init__(self, joystickNumber)
        self.axisNames = {
            0: 'LEFT-X',
            1: 'LEFT-Y',
            2: 'LT',
            3: 'RIGHT-X',
            4: 'RIGHT-Y',
            5: 'RT'
        }
        self.buttonNames = {
            0:  'A',
            1:  'B',
            2:  'X',
            3:  'Y',
            4:  'LB',
            5:  'RB',
            6:  'BACK',
            7:  'START',
            8:  'XBOX',
            9:  'LA',
            10: 'RA'
        }
        self._setupReverseMaps()

class XboxONE(Gamepad):
    fullName = 'Xbox ONE controller'

    def __init__(self, joystickNumber = 0):
        Gamepad.__init__(self, joystickNumber)
        self.axisNames = {
            0: 'LAS -X', #Left Analog Stick Left/Right
            1: 'LAS -Y', #Left Analog Stick Up/Down
            2: 'RAS -X', #Right Analog Stick Left/Right
            3: 'RAS -Y', #Right Analog Stick Up/Down
            4: 'RT', #Right Trigger
            5: 'LT', #Left Trigger
            6: 'DPAD -X', #D-Pad Left/Right
            7: 'DPAD -Y' #D-Pad Up/Down
        }
        self.buttonNames = {
            0:  'A', #A Button
            1:  'B', #B Button
            3:  'X', #X Button
            4:  'Y', #Y Button
            6:  'LB', #Left Bumper
            7:  'RB', #Right Bumper
            11: 'START', #Hamburger Button
            12: 'HOME', #XBOX Button
            13: 'LASB', #Left Analog Stick button
            14: 'RASB' #Right Analog Stick button
                
        }
        self._setupReverseMaps()
        
class Steam(Gamepad):
    fullName = 'Steam controller'

    def __init__(self, joystickNumber = 0):
        Gamepad.__init__(self, joystickNumber)
        self.axisNames = {
            0: 'AS -X', #Analog Stick Left/Right
            1: 'AS -Y', #Analog Stick Up/Down
            2: 'RTP -X', #Right Track Pad Left/Right
            3: 'RTP -Y', #Right Track Pad Up/Down
            4: 'LTP -Y', #Left Track Pad Up/Down
            5: 'LTP -X', #Left Track Pad Left/Right
            6: 'RTA', #Right Trigger Axis
            7: 'LTA' #Left Trigger Axis
        }
        self.buttonNames = {
            0:  'LPTBUTTON', #Left TrackPad button
            1:  'RTPBUTTON', #Right TrackPad button
            2:  'A', #A Button
            3:  'B', #B Button
            4:  'X', #X Button
            5:  'Y', #Y Button
            6:  'LB', #Left Bumper
            7:  'RB', #Right Bumper
            8:  'LT', #Left Trigger
            9:  'RT', #Right Trigger
            10: 'SELECT', #Select Button <
            11: 'START', #Start button >
            12: 'HOME', #Steam Button
            13: 'STICKBUTTON', #Analog Stick button
            15: 'LG', #Left Grip
            16: 'RG', #Right Grip
            17: 'LTP -DUP', #Left TrackPad D-PAD Up
            18: 'LTP -DDOWN', #Left TrackPad D-PAD Down
            19: 'LTP -DLEFT', #Left TrackPad D-PAD Left
            20: 'LTP -DRIGHT', #Left TrackPad D-PAD Right
        }
        self._setupReverseMaps()
    

class example(Gamepad):
    # This class must have self.axisNames with a map
    # of numbers to capitalised strings. Follow the
    # conventions the other classes use for generic
    # axes, make up your own names for axes unique
    # to your device.
    # self.buttonNames needs the same treatment.
    # Use python Gamepad.py to get the event mappings.
    fullName = 'Enter the human readable name of the device here'

    def __init__(self, joystickNumber = 0):
        Gamepad.__init__(self, joystickNumber)
        self.axisNames = {
            0: 'AXIS0',
            1: 'AXIS1',
            2: 'AXIS2'
        }
        self.buttonNames = {
            0: 'BUTTON0',
            1: 'BUTTON1',
            2: 'BUTTON2'
        }
        self._setupReverseMaps()
