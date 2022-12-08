from setuptools import setup, find_packages, Extension
import os
import sys

import Adafruit_DHT.platform_detect as platform_detect


BINARY_COMMANDS = [
    'build_ext',
    'build_clib',
    'bdist',
    'bdist_dumb',
    'bdist_rpm',
    'bdist_wininst',
    'bdist_wheel',
    'install'
]
