import enum


class DetailedState(enum.IntEnum):
    DISABLEDSTATE = 1
    ENABLEDSTATE = 2
    FAULTSTATE = 3
    OFFLINESTATE = 4
    STANDBYSTATE = 5
    NOTREADINGSTATE = 6
    CONFIGURINGSTATE = 7
    MANUALREADINGSTATE = 8
    READINGBUFFERSTATE = 9
    SETDURATIONREADINGSTATE = 10


class Units(enum.IntEnum):
    current = 1
    charge = 2
