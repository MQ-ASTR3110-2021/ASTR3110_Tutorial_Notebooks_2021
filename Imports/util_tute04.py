#!/usr/bin/env python
#=============================================================================#
#                                                                             #
# NAME:     util_tute04.py                                                    #
#                                                                             #
# PURPOSE:  Utility code for AST3110 Tutorial 4  at Macquarie University.     #
#                                                                             #
# MODIFIED: 31-Mar-2020 by C. Purcell                                         #
#                                                                             #
#=============================================================================#
import numpy as np
from matplotlib import pyplot as plt


#-----------------------------------------------------------------------------#
def poly5(p):
    """
    When called, this function takes a vector of parameters
    and returns another functions to evaluate a polynomial
    with these coefficients fixed.
    """

    # Pad out p vectors smaller than len = 6 (longhand version)
    #numPad = 6 - len(p)
    #pad = np.zeros((numPad))
    #p = np.append(pad, p)

    # Pad out p vectors smaller than len = 6 (shorthand version)
    p = np.append(np.zeros((6-len(p))), p)

    def rfunc(x):
        """
        This function is returned by the poly5 function. It takes a
        vector of x values and evaluated the current polynomial.
        """
        y = (p[0]*x**5.0 + p[1]*x**4.0 + p[2]*x**3.0 +
             p[3]*x**2.0 + p[4]*x + p[5])

        # Note the indent here
        return y

    # Note the indent here
    return rfunc


#-----------------------------------------------------------------------------#
def plot_spec_poly5(xData, yData, dyData, p=None):
    """
    Function to plot a spectrum and (optionally) a model polynomial fit.
    """

    # Setup the figure
    fig = plt.figure()
    fig.set_size_inches([12,12])
    ax = fig.add_subplot(1,1,1)

    # First plot the data
    ax.errorbar(x=xData, y=yData, yerr=dyData, mfc="none",
                ms=4, fmt="D", ecolor="grey", label="Data",
                elinewidth=1.0, capsize=2)

    # Only plot the model curve if p has been specified
    if p is not None:

        # Make a model curve, sampled at small
        # intervals to appear smooth
        nSamples = 100
        xModel = np.linspace(start=np.min(xData),
                             stop=np.max(xData),
                             num=nSamples)
        yModel = poly5(p)(xModel)

        # Plot the model
        ax.plot(xModel, yModel, color="red", marker="None",
                mfc="w", mec="g", label="Model", lw=2.0)

    # Set the labels
    ax.set_xlabel('Frequency (GHz)')
    ax.set_ylabel('Amplitude (mJy)')
