import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent


# This call to setup() does all the work
setup(
    name="Topsis-Ritika-101903259",
    version="0.1",
    description="Topsis in python which takes csv file as input and also outputs csv file",
    long_description_content_type="text/markdown",
    url="https://github.com/Ritika6865/topsis-Ritika-101903259-.git",
    author="Ritika Kapoor",
    author_email="ritikakapoor6865@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=["pandas"],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main",
        ]
    },
)