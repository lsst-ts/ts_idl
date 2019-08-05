from setuptools import setup, find_namespace_packages

install_requires = []
tests_require = []
dev_requires = install_requires + tests_require + ["documenteer[pipelines]"]

setup(
    name="ts_idl",
    description="Contains helper functions for the generated idl library by ts_sal.",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    # install_requires=install_requires,
    package_dir={"": "python"},
    packages=find_namespace_packages(where="python"),
    package_data={"": ["*.rst", "*.yaml"]},
    # scripts=[],
    # tests_require=tests_require,
    extras_require={"dev": dev_requires},
    license="GPL",
    project_url={
        "Bug Tracker": "https://jira.lsstcorp.org/secure/Dashboard.jspa",
        "Source Code": "https://github.com/lsst-ts/ts_idl",
    }
)