'''
아래 조건을 만족시키도록 `findChar()` 함수를 수정하여
`findChar_pos()` 함수를 구현하라.

* 정수를 입력받는 `position` 매개변수를 추가한다.
* `position`을 통해 전달된 정수는 탐색을 시작할 위치를 나타낸다.
즉, 앞서 정의된 `findChar()` 함수는 `position`이 0인 특수한 경우가 되도록 한다.
'''

# pass 와 None 을 각각 적절한 명령문과 반환값으로 대체하라.

def findChar_pos(word, char, pos):

    while pos < len(word):
        if word[pos] == char:
            return pos
        pos = pos + 1
    return -1    




assert findChar_pos("hello world", "o", 0) == 4
assert findChar_pos("hello world", "o", 5) == 7