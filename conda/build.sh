$PYTHON -m pip install --no-deps --ignore-installed .

cp -v /opt/lsst/ts_sal/idl/*idl $($PYTHON -c 'from lsst.ts import idl; print(idl.get_idl_dir())')
