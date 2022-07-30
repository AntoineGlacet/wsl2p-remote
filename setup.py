from setuptools import find_packages, setup

setup(
    name="wsl2p_remote",
    packages=find_packages(),
    entry_points={"console_scripts": ["wsl2p_remote = wsl2p_remote.main:main"]},
    version="0.1.0",
    description="remote WakeOnLan and update WSL2preview ip",
    author="Antoine Glacet",
    license="GNU GPLv3",
)
