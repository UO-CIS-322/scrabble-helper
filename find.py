"""
Simple scrabble word finder

Given a pattern like __i, and a
scrabble tray, finds matching
words in the wordlist
"""

import sys # to get pattern from argv
import letterbag
import re  # (added after class ... regular expression package) 

def search(f, pattern, tray):
    results = [ ]
    for word in f:
        word = word.strip()
        if matches(word, pattern, tray):
            results.append(word)
    return results

def matches(word, pattern, tray):
    """
    Word matches pattern with tray.
    Returns True if the word can be made from the
    letters in the tray and pattern, and if it also
    matches the pattern (see matchpat).
    """
    return matchpat(word, pattern) and made_from(word, pattern+tray)

def made_from(word, letters):
    bag = letterbag.LetterBag(letters)
    return bag.contains(word)

def matchpat(word, pattern):
    """
    A letter x matches that letter.
    - (hyphen) matches any letter
    _ (underscore) matches any sequence of letters
    if X matches A, and Y matches B, then
    XY matches AB.
    For example '_ch-s' matches 'branches' but not 'branchings'
    """
    pat = re.sub("_", ".+", pattern)
    pat = re.sub("-", ".", pat)
    return re.fullmatch(pat, word)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:  python3 find.py _ch-p_  aebxyqrz'")
        exit(0)
    words = open("dict.txt")
    pattern = sys.argv[1]
    tray = sys.argv[2]
    result = search(words, pattern, tray)
    on_line = 0
    for w in result:
        if on_line >= 4:
            print()
            on_line = 0
        print(w, end="\t")
        on_line += 1
    print()
    print("{} matches".format(len(result)))
    
