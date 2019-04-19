Repository of IDL files used by for ts_salobj.

Contents:

* idl: IDL files. There should be one file for each SAL component you want to communication with using ``ts_salobj``.
* qos: The default DDS quality of service file used by ``ts_salobj``.
* ups: Files for using this package with eups.

To use this package:

* Define environment variable ``$TS_IDL_DIR`` pointing to the root directory of this package.
  If using eups this will happen automatically when you setup the package.

To generate new IDL files:

* Make sure the ``ts_sal`` package and ``ts_xml`` packages are both setup, e.g. ``setup ts_sal``.
  Alternatively you can define environment variables ``$TS_SAL_DIR`` and ``$TS_XML_DIR``
  and make sure that ``$TS_SAL_DIR/bin`` is on your ``$PATH``.
* Make sure environment variable ``$SAL_WORK_DIR`` is defined.
* Run ``make_idl_files.py sal_component_name1 [sal_component_name12 [...]]``.
  For example: ``make_idl_files.py Test Script ScriptQueue``
