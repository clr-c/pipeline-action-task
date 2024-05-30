# test_inverterstrg.py

from app import inverter_string

def test_inverter_string():
    assert inverter_string("hello") == "olleh"
    assert inverter_string("12345") == "54321"
    assert inverter_string("") == ""