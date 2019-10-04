from encode import encode

def test_empty_string():
    assert encode("") == ""

def test_no_repeat_characters():
    assert encode("abcd") == "abcd"
    assert encode("test") == "test"
