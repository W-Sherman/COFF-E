'''
COFF-E - Cislunar Optimization of Formation Flight Experiment
by Will Sherrman - 2023

link: https://github.com/W-Sherman/COFF-E/tree/main


Numerical Tools Library
'''

# Python standard libraries
import math

# 3rd Party Libraries
import numpy as np
import spiceypy as spice


def norm(x):
    return  np.linalg.norm(x)

def r2d(x):
    return x * 180.0/np.pi
def d2r(x):
    return x * np.pi/180.0
