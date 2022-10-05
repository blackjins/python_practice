'''
아래 `findChar()` 함수는 문자열(`word`)에 특정 문자(`char`)가 포함되어 있으면
위치한 곳의 인덱스를, 그렇지 않으면 -1을 반환한다.
코드에 사용된 `len()` 함수는 주어진 문자열의 길이, 즉 문자열에
포함된 문자의 개수를 반환한다.
'''

# def findChar(word, char):
#     idx = 0

#     while idx < len(word):
#         if word[idx] == char:
#             return idx
    
#         idx = idx + 1
    
#     return -1


# pass 와 None 을 각각 적절한 명령문과 반환값으로 대체하라.

def findChar_for(word, char):
    i = 0
    for letter in word:
        if letter == char:
            return i
        i = i + 1
    return -1    


assert findChar_for("python", "o") == 4
assert findChar_for("파이썬이 좋아요", "아") == 6