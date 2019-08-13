#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : __init__.py
# Author: Reinaldo Astudillo <r.a.astudillo@tudelft.nl>
"Iterative Solvers for Sparse Linear Systems"

from __future__ import division, print_function, absolute_import

#from info import __doc__
from .iterative import *
from .minres import minres
from .lgmres import lgmres
from .lsqr import lsqr
from .lsmr import lsmr
from ._gcrotmk import gcrotmk
from .idrs import idrs

__all__ = [s for s in dir() if not s.startswith('_')]

from scipy._lib._testutils import PytestTester
test = PytestTester(__name__)
del PytestTester
