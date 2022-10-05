'''
`findChar_pos()` 함수를 `for` 반복문을 이용하여 구현하라.
'''
# pass 와 None 을 각각 적절한 명령문과 반환값으로 대체하라.

def findChar_pos_for(word, char, pos):
    word = word[pos:]
    for letter in word:
        if letter == char:
            return pos
        pos = pos + 1
    return -1


assert findChar_pos_for("hello world", "o", 0) == 4
assert findChar_pos_for("hello world", "o", 5) == 7