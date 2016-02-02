"""
Test suite for 'find.py' (Fall 2015 version)
"""

from find15F import matches

def test_find_no_wildcards():
    ## Matches without wildcards
    assert matches("abc", "abc", "abc") 
    assert matches("abc", "abc", "xxx")  # Uses nothing from tray
    assert not matches("abx", "abc", "abc")  # x doesn't match c
    assert not matches("abcd", "abc", "abc") # too long
    assert not matches("abc", "abcd", "abc") # too short 

def test_find_with_wildcards():
    # Matches with wildcards: 
    # Add at least three good test cases here
    assert matches("abc", "__c", "xaxbx")
    assert not matches("abbc", "a__c", "xbx")
    assert not matches ("abc", "a_x", "bc")
    assert not matches("abc", "a_c", "xyz")

    

    


