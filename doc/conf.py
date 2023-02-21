"""Sphinx configuration file for TSSW package"""

import lsst.ts.idl  # noqa
from documenteer.conf.pipelinespkg import *  # noqa

project = "ts_idl"
html_theme_options["logotext"] = project  # type: ignore # noqa
html_title = project
html_short_title = project
doxylink = {}  # Avoid warning: Could not find tag file _doxygen/doxygen.tag

intersphinx_mapping["ts_xml"] = ("https://ts-xml.lsst.io", None)  # type: ignore # noqa
