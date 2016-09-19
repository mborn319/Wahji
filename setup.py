"""A setuptools based setup module.
"""

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path


setup(
    name='wahji',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1a',

    description='Static Site Generator',
    long_description='Static site generator...',

    # The project's main homepage.
    url='https://github.com/mborn319/Wahji',

    # Author details
    author='Michael Born, John Happel, Tea Drincic, David Deeley, Carl Bennett, Paul Bressette',
    author_email='drincit@sunyit.edu',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='static site generation',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    install_requires=['PyYAML', 'markdown'],



    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'wahji=wahji_install.wahji:wahji',
        ],
    },
)
