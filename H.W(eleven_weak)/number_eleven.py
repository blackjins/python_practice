'''
ROT13 은 단어의 각 문자를 13 자리만큼 회전시키는 방식의 간단한 암호 법이다. 

문자를 회전한다는 것은 알파벳 상의 위치를 이동한다는 뜻이다. 
예를 들어, `'a'` 를 3 만큼 이동하면 `'d'` 가, 
`'z'` 를 1 만큼 이동하면 `'a'` 가 된다.
음수에 대해서는 역으로 회전한다.
예를 들어, `'d'` 를 -3 만큼 이동하면 `'a'` 가 되고, `'a'` 를 -2 만큼 회전시키면 
`'y'` 가 된다.

다음 조건을 만족하는 `rotateWord()` 함수를 구현하라.

- 문자열과 정수를 인자로 사용한다.
- 지정된 정수만큼 문자열을 회전시킨다.

힌트: 알파벳과 아스키 코드 사이의 관계를 이어주는
[`ord()` 함수와 `chr()` 함수](https://ghdwn0217.tistory.com/60)를 이용한다.
'''
# pass 와 None 을 각각 적절한 명령문과 반환값으로 대체하라.

def rotateWord(word, num):
    tmp_list = []
    word = list(word)
    for letter in word:
        tmp = ord(letter)
        for i in range(num):
            tmp = tmp + 1
            if tmp ==123:
                tmp = 97
        if num < 0:
            for i in range(-num):
                tmp = tmp - 1
                if tmp ==97:
                    tmp = 123
        letter = chr(tmp)
        tmp_list.append(letter)

    return "".join(tmp_list)

assert rotateWord("cheer", 7) == "jolly"
assert rotateWord("melon", -10) == "cubed"