import numbers
import json

from scipy import stats

import numpy as np
from scipy.linalg import eigh

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.extmath import stable_cumsum

from timeflux.core.node import Node
from timeflux.helpers.port import get_meta

class Output(Node):

    def update(self):
        if self.i.ready():
            predictions = self.i.data["data"].apply(lambda x: json.loads(x)["result"])
            self.o.data = predictions.to_frame(name="result")


