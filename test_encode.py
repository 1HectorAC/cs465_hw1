from encode import encode

def test_empty_string():
    assert encode("") == ""

def test_no_repeat_characters():
    assert encode("abcd") == "abcd"
    assert encode("test") == "test"

def test_single_repeating_character():
    assert encode("qqqq") == "q4"
    assert encode("tttttttt") == "t8"

def test_two_repeating_characters():
    assert encode("eerrrr") == "e2r4"
    assert encode("nnnnoooooo") == "n4o6"
