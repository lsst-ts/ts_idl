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

import pathlib
import unittest

from lsst.ts import idl


class UtilsTestCase(unittest.TestCase):
    def get_expected_data_dir(self) -> pathlib.Path:
        return (
            pathlib.Path(__file__).parent.parent
            / "python"
            / "lsst"
            / "ts"
            / "idl"
            / "data"
        )

    def test_get_data_dir(self):
        assert idl.get_data_dir() == self.get_expected_data_dir()

    def test_get_idl_dir(self):
        expected_idl_dir = self.get_expected_data_dir() / "idl"
        assert idl.get_idl_dir() == expected_idl_dir

    def test_enums_modules(self):
        enum_module_names = set(
            name for name in dir(idl.enums) if not name.startswith("_")
        )
        # These are the names as of 2021-02-22
        # Treat it as a subset to avoiding having to update this test
        # every time we add a module.
        expected_names_subset = set(
            (
                "ATCamera",
                "ATDome",
                "ATHexapod",
                "ATMCS",
                "ATMonochromator",
                "ATPneumatics",
                "ATPtg",
                "ATSpectrograph",
                "ATThermoelectricCooler",
                "Electrometer",
                "FiberSpectrograph",
                "Guider",
                "LinearStage",
                "MTAOS",
                "MTDome",
                "MTHexapod",
                "MTM1M3",
                "MTM2",
                "MTMount",
                "MTPtg",
                "MTRotator",
                "PMD",
                "Script",
                "ScriptQueue",
                "TunableLaser",
                "Watcher",
            )
        )
        assert expected_names_subset <= enum_module_names
