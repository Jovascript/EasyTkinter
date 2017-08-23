import shutil
from os import path

from setuptools import setup


try:
    shutil.rmtree('dist/')
except:
    pass

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="EasyTkinter",

    version="1.2.0",

    description="A python library to give tkinter a friendly face.",
    long_description=long_description,

    author="Joe Bell",
    author_email="joe@jb-labs.uk",

    url="https://github.com/Jovascript/EasyTkinter",
    license="MIT",

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],

    keywords="tkinter gui easy wrapper",

    packages=['easytkinter'],
    python_requires='>=3'

)
