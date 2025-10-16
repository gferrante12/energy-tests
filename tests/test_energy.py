import pytest
from mymodule import energy_conversion

def test_energy_conversion_basic():
    assert energy_conversion(4184) == 1
    assert energy_conversion(0) == 0

def test_energy_conversion_fractional():
    assert round(energy_conversion(2092), 2) == 0.5

def test_energy_conversion_negative():
    import pytest
    with pytest.raises(ValueError):
        energy_conversion(-10)