'''
거꾸로 노래 부르기 좋아하는 청개구리는 아래와 같이 노래를 부른다.  

> 끼토산 야끼토 로디어 냐느가 총깡총깡 서면뛰 를디어 냐느가

문자열이 주어졌을 때, 공백을 단위로 각 단어를 거꾸로 뒤집은 문자열을 반환하는 
`revers_words()` 함수를 작성하라.
단, 입력 문자열은 줄바꿈 없이 주어진다고 가정한다.
'''

# pass 와  None을 적절한 명령문과 표현식으로 대체하라.

def reverse_words(s):
    s = s.split()
    for i in range(len(s)):
        s[i] = s[i][::-1]
    return ' '.join(s)

lyrics = '산토끼 토끼야 어디로 가느냐'
rev_lyrics = '끼토산 야끼토 로디어 냐느가'
assert reverse_words(lyrics) == rev_lyrics

lyrics2 = '깡총깡총 뛰면서 어디를 가느냐'
rev_lyrics2 = '총깡총깡 서면뛰 를디어 냐느가'

assert reverse_words(lyrics2) == rev_lyrics2
