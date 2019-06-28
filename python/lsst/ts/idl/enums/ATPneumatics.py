# This file is part of ts_idl.
#
# Developed for the LSST Data Management System.
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

__all__ = ["MirrorCoverState", "CellVentState", "AirValveState"]

import enum


class MirrorCoverState(enum.IntEnum):
    CLOSED = 1
    OPENED = 2
    INMOTION = 3
    INVALID = 4


class CellVentState(enum.IntEnum):
    CELLVENTSOPENED = 1
    CELLVENTSCLOSED = 2
    INMOTION = 3


class AirValveState(enum.IntEnum):
    VALVEOPENED = 1
    VALVECLOSED = 2


class VentsPosition(enum.IntEnum):
    OPENED = 1
    CLOSED = 2
    PARTIALLYOPENED = 3