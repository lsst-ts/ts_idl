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
# This program is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License

__all__ = [
    "ApplicationStatus",
    "ControllerState",
    "EnabledSubstate",
    "OfflineSubstate",
    "SalIndex",
]

import enum


# MTHexapod and MTRotator have the same enum values for
# ControllerState, OfflineSubstate, and EnabledSubstate.
from .MTRotator import (
    ControllerState,
    EnabledSubstate,
    OfflineSubstate,
)


class ApplicationStatus(enum.IntFlag):
    """Bit masks for the value reported in ``telemetry.application_status``.

    These are from https://github.com/lsst-ts/ts_hexapod_controller/blob/main/include/actuatorTlm.h  # noqa
    """

    FOLLOWING_ERROR = 0x1
    MOVE_COMPLETE = 0x2
    HEX_MOVE_COMPLETE_MASK = 0x2  # Backwards compatible name
    EUI_CONNECTED = 0x4
    RELATIVE_MOVE_MODE = 0x8
    SYNC_MODE = 0x10
    COMMAND_REJECTED = 0x20
    SAFETY_INTERLOCK = 0x40
    EXTEND_LIMIT_SWITCH = 0x80
    RETRACT_LIMIT_SWITCH = 0x100
    ETHERCAT_PROBLEM = 0x200
    DDS_COMMAND_SOURCE = 0x400
    """1=DDS is commanding, 0=EUI is commanding"""

    MOTION_TIMEOUT = 0x800
    """Motion timed out: one or more struts not settling
    or command values did not change.
    """

    DDS_CONNECTED = 0x1000
    DRIVE_FAULT = 0x2000
    SIMULINK_FAULT = 0x4000
    LUT_TABLE_INVALID = 0x8000


class SalIndex(enum.IntEnum):
    CAMERA_HEXAPOD = 1
    M2_HEXAPOD = 2
