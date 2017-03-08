'''setup.py - Waqas Bhatti (wbhatti@astro.princeton.edu) - Nov 2016

This sets up the package.

Stolen from http://python-packaging.readthedocs.io/en/latest/everything.html and
modified by me.

'''
__version__ = '0.1.2'

import sys, os.path

# for f2py extension building
try:
    from numpy.distutils.core import Extension, setup
except:
    raise ImportError(
        '\nYou need to have numpy installed before running setup.py,\n'
        'because we need its Extension functionality to make a\n'
        'compiled Fortran extension for eebls.f!\n'
    )


def readme():
    with open('README.rst') as f:
        return f.read()

INSTALL_REQUIRES = [
    'numpy',
]

########################
## DO THE FORTRAN BIT ##
########################

# adapted from github:dfm/python-bls.git/setup.py

# Define the Fortran extension.
pyeebls = Extension("pyeebls._pyeebls",
                    ["pyeebls/pyeebls.pyf", "pyeebls/eebls.f"])

setup(
    name='pyeebls',
    version=__version__,
    description=('Python f2py extension wrapping '
                 'eebls.f by Kovacs et al. 2002.'),
    long_description=readme(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    keywords='astronomy',
    url='https://github.com/waqasbhatti/pyeebls',
    author='Waqas Bhatti',
    author_email='wbhatti@astro.princeton.edu',
    license='MIT',
    packages=["pyeebls"],
    ext_modules=[pyeebls,],
    install_requires=INSTALL_REQUIRES,
)
