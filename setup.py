from setuptools import setup
import setuptools_scm


setup(
    version=setuptools_scm.get_version(),
    # This is necessary here because the .idl files are being copied from an
    # external location while the conda package is created and if this is put
    # in the pyproject.tomlo file the files are missing from the conda
    # package.
    package_data={
        "": ["*.idl"],
    },
)
