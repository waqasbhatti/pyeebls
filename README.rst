This is a module that wraps Geza Kovacs' eebls.f. Taken from Daniel
Foreman-Mackey's python-bls_ module, and broken out for easier use by other
packages. This is used by the astrobase_ module.


eebls.f
=======

- Kovacs, Zucker & Mazeh 2002, A&A, Vol. 391, 369
- http://arxiv.org/abs/astro-ph/0206099
- http://www.konkoly.hu/staff/kovacs/eebls.f


python-bls
==========

- Foreman-Mackey, D., Angus, R., et al. 2012
- https://github.com/dfm/python-bls.git


pyeebls
=======

- Bhatti, W., et al. 2017
- https://github.com/waqasbhatti/pyeebls


Installation
------------

This package is available from PyPI: https://pypi.python.org/pypi/pyeebls

You'll need numpy installed, along with a Fortran compiler: ::

  (venv)$ pip install numpy # in a virtualenv
  # or use dnf/yum/apt install numpy to install systemwide

  ## you'll need a Fortran compiler to install pyeebls!         ##
  ## on Linux: dnf/yum/apt install gcc gcc-gfortran             ##
  ## on OSX (using homebrew): brew install gcc && brew link gcc ##

Then, install pyeebls using pip (preferably in a virtualenv or use the --user
flag): ::

  (venv)$ pip install pyeebls

Or download the tarball from PyPI, extract the files, and run setup.py: ::

  (venv)$ python setup.py install


Documentation
-------------

There's only one function to use in this module. ::

  def pyeebls.eebls(times, mags, workarr_u, workarr_v,
                    nfreq, freqmin, stepsize,
                    nbins, minduration, maxduration):

Calculates the BLS spectrum for the input times and mags arrays.

**Parameters**

``times`` : *ndarray*
        A numpy array containing the times of the measurements.

``mags`` : *ndarray*
        A numpy array containing the mags or fluxes to use as measurements.

``workarr_u``, ``workarr_v`` : *ndarray*
        Numpy arrays that must be the same size as times, used as temp
        workspaces by the Fortran function.

``nfreq`` : *int*
        The number of frequencies to search for the best period.

``freqmin`` : *float*
        The minimum frequency to use.

``stepsize`` : *float*
        The stepsize in frequency units to use while searching.

``nbins`` : *int*
        The number of bins to use when phasing up the light curve at a
        single test period.

``minduration`` : *float*
        The minimum transit duration in phase units to consider when testing for
        a transit.

``maxduration`` : *float*
        The minimum transit duration in phase units to consider when testing for
        a transit.


**Returns**

A sequence of results: ::

  (power, bestperiod, bestpower, transdepth,
   transduration, transingressbin, transegressbin)

``power`` : *ndarray*
        A numpy array containing the values of the BLS spectrum at each tested
        frequency.

``bestperiod`` : *float*
        The period at the highest peak in the frequency spectrum.

``bestpower`` : *float*
        The power at the highest peak in the frequency spectrum.

``transdepth`` : *float*
        The depth of the transit at the best period.

``transduration`` : *float*
        The length of the transit as a fraction of the phase. This is the
        so-called 'q' parameter.

``transingressbin`` : *int*
        The phase bin index for the start of the transit.

``transegressbin`` : *int*
        The phase bin index for the end of the transit.


See Also
--------

- the comments at the top of eebls.f in this package
- the kbls_ module in astrobase_ for a high-level serial and parallelized
  interface to this module


License
-------

The license for the Python files is the MIT License. eebls.f is provided by
G. Kovacs; it appears to be re-distributable, but please make sure to cite
Kovacs, et al. 2002 if you use this implementation.


.. _python-bls: https://github.com/dfm/python-bls.git
.. _astrobase: https://github.com/waqasbhatti/astrobase/tree/master/astrobase/periodbase
.. _kbls: https://github.com/waqasbhatti/astrobase/blob/master/astrobase/periodbase/kbls.py
