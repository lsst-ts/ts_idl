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

__all__ = ["ControllerState", "OfflineSubstate", "EnabledSubstate", "ApplicationStatus"]

import enum


class ControllerState(enum.IntEnum):
    """Controller state reported as ``telemetry.state``.

    The names and meanings are the same as SAL summary states
    but the numeric values are different.

    Value is ``telemetry.state``.

    Called ``States`` in Moog code.
    """

    STANDBY = 0
    DISABLED = enum.auto()
    ENABLED = enum.auto()
    OFFLINE = enum.auto()
    FAULT = enum.auto()


class OfflineSubstate(enum.IntEnum):
    """Controller substate for the OFFLINE state.

    Value reported in ``telemetry.offline_substate ``.

    This is enum ``OfflineSubStates`` in Moog code.
    """

    PUBLISH_ONLY = 0
    AVAILABLE = enum.auto()


class EnabledSubstate(enum.IntEnum):
    """Controller substate for the ENABLED state.

    Value reported in ``telemetry.enabled_substate``.

    This is enum ``EnabledSubStates`` in Moog code.
    """

    STATIONARY = 0
    MOVING_POINT_TO_POINT = enum.auto()
    SLEWING_OR_TRACKING = enum.auto()
    CONTROLLED_STOPPING = enum.auto()
    INITIALIZING = enum.auto()
    RELATIVE = enum.auto()
    CONSTANT_VELOCITY = enum.auto()


class ApplicationStatus(enum.IntFlag):
    """Bit masks for the value reported in ``telemetry.application_status``.

    These are constants, with the same names and values, in Moog code.
    """

    HEX_FOLLOWING_ERROR_MASK = 0x00000001
    HEX_MOVE_COMPLETE_MASK = 0x00000002
    COMMAND_REJECT_MASK = 0x00000020
    SAFETY_INTERLOCK = 0x00000040
    EXTEND_LIMIT_SWITCH = 0x00000080
    RETRACT_LIMIT_SWITCH = 0x00000100
    ETHERCAT_PROBLEM = 0x00000200
    DDS_COMMAND_SOURCE = 0x00000400
    MOTION_TIMEOUT = 0x00000800
    DRIVE_FAULT = 0x00002000
    SIMULINK_FAULT = 0x00004000
    ENCODER_FAULT = 0x00008000
