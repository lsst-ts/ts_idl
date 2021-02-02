# This file is part of ts_idl.
#
# Developed for Vera Rubin Observatory.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License

__all__ = ["AtMountState", "M3ExitPort", "M3State"]

import enum


class AtMountState(enum.IntEnum):
    REMOTECONTROL = 6
    HANDPADDLECONTROL = 7
    TRACKINGDISABLED = 8
    TRACKINGENABLED = 9
    STOPPING = 10


class M3ExitPort(enum.IntEnum):
    NASMYTH1 = 6
    NASMYTH2 = 7
    PORT3 = 8


class M3State(enum.IntEnum):
    REMOTECONTROL = 1
    HANDPADDLECONTROL = 2
    NASMYTH1 = 6
    NASMYTH2 = 7
    PORT3 = 8
    INMOTION = 9
    UNKNOWNPOSITION = 10
