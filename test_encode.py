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

def test_multiple_repeating_characters():
    assert encode("ttttrryyyyyyy") == "t4r2y7"
    assert encode("wwooooeeehhhhhccc") == "w2o4e3h5c3"

def test_lowercase_and_uppercase_characters():
    assert encode("AAaaaIIIIIww") == "A2a3I5w2"
    assert encode("rrTTTTTwwwKKKll") == "r2T5w3K3l2"
