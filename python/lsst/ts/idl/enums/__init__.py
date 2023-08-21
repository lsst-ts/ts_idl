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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import warnings

warnings.warn(
    """
    ts_idl package is going to be deprecated once we upgrade to salobj 8 (the
    initial release of the kafka version of salobj). The enumerations will move
    to ts_xml package. For now they will continue to be re-exported here but
    you should start moving your imports to use lsst.ts.xml instead of
    lsst.ts.idl.
    """,
    DeprecationWarning,
)

from lsst.ts.xml.enums import *
