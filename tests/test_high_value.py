from lib.high_value import HighValue

def test_first_value_is_higher():
    highVal = HighValue(10,5)
    result = highVal.get_highest()
    assert result == "First value is higher"

def test_second_value_is_higher():
    highVal = HighValue(5,10)
    result = highVal.get_highest()
    assert result == "Second value is higher"

def test_values_are_equal():
    highVal = HighValue(10,10)
    result = highVal.get_highest()
    assert result == "Values are equal"

def test_add_first():
    highVal = HighValue(5,10)
    highVal.add(3,"first")
    assert highVal.value_first == 8

def test_add_second():
    highVal = HighValue(10,5)
    highVal.add(3,"second")
    assert highVal.value_second == 8