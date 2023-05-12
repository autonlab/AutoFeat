import numpy as np
from autofeat.functional import mean_tf
import pytest


def test_mean():
    """
    Test mean functional form transform.
    """

    x = np.random.rand(100)
    y_hat = mean_tf(x)
    y = 0.0
    for i in range(len(x)):
        y += x[i]
    y /= len(x)
    assert pytest.approx(y_hat) == y
