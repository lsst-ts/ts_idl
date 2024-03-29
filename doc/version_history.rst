.. py:currentmodule:: lsst.ts.idl

.. _lsst.ts.idl.version_history:

===============
Version History
===============

.. warning::

  This package is now marked for deprecation and will be removed once we transition to kafka for the middleware.
  Please, do not add any new enumerations to this package.
  All enumerations should be in ts-xml.

v4.7.1
------

* Remove all enums definitions.
  These are now moved into ts-xml package.
* Re-export all enums from ts-xml for backward compatibility.
* Add ts-xml as a host and run dependency.
* Add deprecation warning.

v4.7.0
------

* Switch to ts-pre-commit-config.
* Remove dependency on the python version from the conda recipe.
* HVAC: Add Dynalene enum items.
* MTM2: Add the enums: ``PowerType``, ``PowerSystemState``, ``ClosedLoopControlMode``, and ``InnerLoopControlMode``.
* Fix conda build script.

v4.6.0
------

* MTM1M3: Add EnableDisableForceComponent enum.

v4.5.0
------

* `enums.MTMount`:

    * Add ``ThermalCommandState``.
    * ``System``: rename two thermal system items, leaving deprecated aliases.

* Add ``AlignComponent`` enum class to `enums.LaserTracker`.
* `enums.HVAC`:

    * Remove ``DynaleneSafetyState``.
    * Add ``DynaleneTankLevel``.

v4.4.0
------

* `enums.ATWhiteLight`: expand ``BasicState`` values.
  Also remove ``ErrorCode`` enum: use the version in ts_atwhitelight instead.
* HVAC: Add Dynalene DeviceId, DynaleneSafetyState and DynaleneState.
* Apply isort.

v4.3.0
------

* Add ``TelescopeVignetted`` enum class to `enums.ATDomeTrajectory` and `enums.MTDomeTrajectory`.
* `enums.MTDome.MotionState`: add ``DISABLED`` value.
* Add missing setup.cfg.
* pre-commit: update black to 23.1.0, isort to 5.12.0, mypy to 1.0.0, and pre-commit-hooks to v4.4.0.
* ``Jenkinsfile``: modernize do not run as root.

v4.2.0
------

* Add ``enums.LaserTracker``.
* `enums.TunableLaser.LaserDetailedState`: add PROPAGATINGBURSTMODEWAITINGFORTRIGGER and PROPAGATINGBURSTMODETRIGGERED.
* `enums.ATMonochromator.Grating`: fix enum values.

v4.1.0
------

* Add new ``DetailedState`` enumeration for the Scheduler.
* Add new ``Script.ScriptState.CONFIGURE_FAILED`` enum item, to match ts_xml 12.1.
* Add new ``ScriptQueue.ScriptProcessState.CONFIGURE_FAILED`` enum item and retained ``CONFIGUREFAILED`` as a deprecated alias.
* Update ``ATMCS.M3ExitPort``.

v4.0.1
------

* `enums.ATWhiteLight`: fix some alarm enum values and add a note about provenance and order.

v4.0.0
------

* Move the 'idl' directory into a new 'data' directory and adjust source and test code to that.
* Convert to 'noarch: python' according to the conda build specifications.
* Migrate from setup.py + setup.cfg to pyproject.toml + a much smaller setup.py.
* Set the XML and SAL versions in the build hash.
* Update the versions in .pre-commit-config.yaml.
* `enums.MTMount.System`: rename one entry.

v3.8.3
------

* MTMount LimitsMask: document the sign of ``CAMERA_CABLE_WRAP_FOLLOW_L3_MIN``.

v3.8.2
------

* Fix MTMount LimitsMask enum.

v3.8.1
------

* Fix two ATWhiteLight enums.

v3.8.0
------

* Add ATWhiteLight enum module.

v3.7.0
------

* ESS: Overhaul ErrorCode enum values.
* MTDome: Add new MotionStates.

v3.6.0
------

* Add ErrorCode enum to ATMonochromator.
* Add ErrorCode.NO_CONFIG to MTHexapod and MTRotator.

v3.5.0
------

* Added SalIndex enum to FiberSpectrograph, Guider, OCPS, Scheduler and ScriptQueue enums modules.
  Tweak doc string for SalIndex in MTHexapod enums module.
* Modernize unit tests to use bare asserts.
* Added ESS ErroCode enum.

v3.4.0
------

* Add ErrorCode enums to MTHexapod and MTRotator.
* Update MTDome enum values.
* Use pytest-black instead of a dedicated unit test.
* Modernize setup.cfg.
* Fix a flake8 error in HVAC: doc string too long.

v3.3.0
------

* Added GIS enums.
* Added OCPS enum.

v3.2.0
------

Changes:

* Overhauled MTMount enums to match ts_xml 10.0.
  These changes require ts_xml 10.0.
* Added BumpTestProgress enum to MTM1M3.
* Deleted deprecated ``enums.MTHexapod.ApplicationStatus.HEX_MOVE_COMPLETE_MASK``.

v3.1.3
------

Changes:

* Added enums and dictionaries for HVAC.
* Added enum values for MTDome.

v3.1.2
------

Changes:

* Format the code with black 20.8b1.

v3.1.1
------

Changes:

* Updated the conda build recipe to create a `noarch` package.

v3.1.0
------

Deprecated:

* `enums.MTHexapod.ApplicationStatus.HEX_MOVE_COMPLETE_MASK` is deprecated;
  use `enums.MTHexapod.ApplicationStatus.MOVE_COMPLETE` instead.

Changes:

* Added `enums.MTHexapod.SalIndex`.
* Updated `enums.MTHexapod.ApplicationStatus`:

    * Added ``EUI_CONNECTED``, ``RELATIVE_MOVE_MODE``, ``SYNC_MODE``, and ``DDS_CONNECTED``.
    * Changed incorrect ``ENCODER_FAULT`` to ``LUT_TABLE_INVALID``.
    * Renamed ``HEX_MOVE_COMPLETE_MASK`` to ``MOVE_COMPLETE``,
      but also retain the old name, for now, because it is used in code.
    * Renamed ``HEX_FOLLOWING_ERROR`` to ``FOLLOWING_ERROR``.
* Updated `enums.MTRotator.ApplicationStatus`:

    * Added ``EUI_CONNECTED`` and ``DDS_CONNECTED``.
    * Removed values that only apply to MTHexapod: ``HEX_MOVE_COMPLETE_MASK``, ``HEX_FOLLOWING_ERROR``, and ``MOTION_TIMEOUT``.

v3.0.0
------

Changes:

* Removed the quality of service file `qos/QoS.xml` and function `get_qos_path`.
  Use the quality of service file in ts_ddsconfig instead.
* Import all enums modules when lsst.ts.idl is imported.
  This catches any errors that would prevent import.
* Added enumeration modules `enums.Guider`, `enums.MTAOS`, and `enums.PMD`.
* Updated enumeration modules `enums.ATPtg` and `enums.MTPtg` for ts_xml 8.
* Add unit tests.
* Add API documentation to the developer's guide.
* Updated ``doc/conf.py`` for documenteer 0.6.

v2.4.0
------

Changes

* ATMCS: update enumerations.
* MTMount: add `SubsystemId` and update `AxisState` to match new information from Tekniker.
* MTM1M3: add `HardpointActuatorMotionStates`.
* Add support for ``pre-commit``.
  See README.rst for instructions.
* Convert Jenkinsfile.conda to use the shared library.

v2.3.0
------

Changes:

* Add ``MTMount`` enums.

v2.2.1
------

Changes:

* Fill out the documentation.

v2.2.0
------

Backwards-incompatible changes:

* Rename the following enum modules to match changes in ts_xml 7:

    * Rename ``Dome`` to ``MTDome``.
    * Rename ``Hexapod`` to ``MTHexapod``.
    * Rename ``Rotator`` to ``MTRotator``.

Other changes:

* Add this version history.

v2.1.0
------

Changes:

* Add ``MTM1M3`` enums.
* Update ``Jenkinsfile.conda`` to prevent artifacts from piling up.

v2.0.0
------

Backwards-incompatible changes:

* Overhaul the DDS quality of service file:

    * Rename it to ``qos/QoS.xml``
    * Include a named profile for each topic category.
    * Set telemetry durability to VOLATILE instead of TRANSIENT

* Remove deprecated misspelled ``ApplicationStatus`` enum from ``Hexapod`` and ``Rotator``.

Other changes:

* Add documentation.
* Add ``LinearStage`` enums.
* Update ``Dome`` enums for changes in ts_xml 6.2.
* Remove unnecessary ``__init__.py`` files from ``idl`` and ``qos`` folders and update ``setup.py`` accordingly.
* Add ``Jenkinsfile``.

v1.4.0
------

Changes:

* Correct spelling of one ``Hexapod`` and ``Rotator`` ``ApplicationStatus`` enum to ``SAFETY_INTERLOCK``,
  while leaving the old spelling for backwards compatibility.

v1.3.1
------

Changes:

* Modify ``Jenkinsfile.conda`` to use ``yum clean all``.

v1.3.0
------

Changes:

* Add ``MTM2`` enums.
* Add ``Dome`` enums.
* Modify the build files.
