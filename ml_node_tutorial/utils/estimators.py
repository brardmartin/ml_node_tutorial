import numbers
import json

from scipy import stats

import numpy as np
from scipy.linalg import eigh

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.extmath import stable_cumsum

from timeflux.core.node import Node
from timeflux.helpers.port import get_meta

class Slope(BaseEstimator, TransformerMixin):
    """Extract the slope of a 1D signal
    """

    def __init__(self):
        return


    def fit(self, X, y=None, sample_weight=None):

        return self

    def transform(self, X):
        """Extracts slope of a signal
        Parameters
        ----------
        X : ndarray, shape (n_trials, n_samples)
            Windowed signal
        Returns
        -------
        Xslopes: ndarray, shape (n_trials, 1)
            Slopes
        """
        winSize = X.shape[1]
        Xslopes = np.array([ stats.linregress(range(winSize), Xwin)[0] for Xwin in X] )


        return Xslopes.reshape(-1,1)
