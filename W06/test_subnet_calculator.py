import pytest
from subnet_calculator import get_prefix_from_ips, get_total_ips, get_subnet_mask

def test_get_prefix_from_ips():
    assert get_prefix_from_ips(1) == 32
    assert get_prefix_from_ips(2) == 31
    assert get_prefix_from_ips(14) == 28
    assert get_prefix_from_ips(50) == 26
    assert get_prefix_from_ips(200) == 24

def test_get_total_ips():
    assert get_total_ips(30) == 4
    assert get_total_ips(28) == 16
    assert get_total_ips(26) == 64
    assert get_total_ips(24) == 256
    assert get_total_ips(27) == 32

def test_get_subnet_mask():
    assert get_subnet_mask(30) == "255.255.255.252"
    assert get_subnet_mask(28) == "255.255.255.240"
    assert get_subnet_mask(26) == "255.255.255.192"
    assert get_subnet_mask(24) == "255.255.255.0"
    assert get_subnet_mask(27) == "255.255.255.224"


pytest.main(["-v", "--tb=line", "-rN", __file__])
