import numpy as np
from mymodule import energy_conversion

def test_regression_behavior():
    """Check that energy_conversion gives stable outputs for fixed inputs."""
    inputs = np.array([0, 4184, 2092])
    expected = np.array([0.0, 1.0, 0.5])
    outputs = np.array([round(energy_conversion(x), 2) for x in inputs])
    assert np.allclose(outputs, expected)