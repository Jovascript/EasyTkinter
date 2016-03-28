from setuptools import setup
from codecs import open
from os import path
import shutil

shutil.rmtree('dist/')

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="EasyTkinter",

    version="1.1.0",

    description="A module to greatly simplify tkinter applications.",
    long_description=long_description,

    author="Joe Bell",
    author_email="joe@jb-labs.uk",

    license="MIT",

    classifiers=[
        "Development Status :: 5 - Production/Stable",

        "Intended Audience :: Developers",

        "Topic :: Desktop Environment",
        "Topic :: Software Development :: Libraries",

        "Natural Language :: English",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python"
    ],

    keywords="tkinter gui easy wrapper",

    py_modules=["gui"],

)
