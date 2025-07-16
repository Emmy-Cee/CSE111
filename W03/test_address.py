from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    address = "123 Main St, Springfield, IL 62704"
    assert extract_city(address) == "Springfield"

def test_extract_state():
    address = "123 Main St, Springfield, IL 62704"
    assert extract_state(address) == "IL"

def test_extract_zipcode():
    address = "123 Main St, Springfield, IL 62704"
    assert extract_zipcode(address) == "62704"
    
pytest.main(["-v", "--tb=line", "-rN", __file__])
