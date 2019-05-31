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

__all__ = ["Grating", "Slit", "LightStatus", "Device"]

import enum


class Grating(enum.IntEnum):
    BLUE = 1
    RED = 2
    MIRROR = 3


class Slit(enum.IntEnum):
    FRONTENTRANCE = 1
    FRONTEXIT = 2


class LightStatus(enum.IntEnum):
    ON = 1
    OFF = 2


class Device(enum.IntEnum):
    MONOCHROMATOR = 1
    LIGHTSOURCE = 2
    THERMOELECTRICCOOLER = 3
