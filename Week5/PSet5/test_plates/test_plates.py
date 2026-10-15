from plates import is_valid

def test_valid():
    assert is_valid("AB") == True
    assert is_valid("ABC123") == True
    assert is_valid("AB12") == True

def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_invalid_start():
    assert is_valid("12") == False
    assert is_valid("A1") == False

def test_invalid_number_zero():
    assert is_valid("AB0") == False
    assert is_valid("AB01") == False

def test_invalid_number_placement():
    assert is_valid("AB12C") == False
    assert is_valid("A1B2") == False

def test_invalid_punctuation():
    assert is_valid("AB1@") == False
    assert is_valid("AB C") == False

