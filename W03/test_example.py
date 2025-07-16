from example import miles_per_gallon
from pytest import approx
import pytest

def test_miles_per_gallon():
    assert miles_per_gallon(1030, 2010, 30) == approx(float(32.666666666666664))
    

pytest.main(["-v", "--tb=line", "-rN", __file__])