'''
변수와 함수의 이름을 지정할 때 **카멜**<font size = "2">camel</font> 표기법 또는 
**팟홀**<font size="2">pothole</font> 표기법(**스네이크**<font size="2">snake</font> 표기법으로도 불림)을 
사용한다.

* 카멜 표기법 : 소문자로 시작하고, 이어지는 단어의 시작은 대문자로 작성하는 표기법.
    - 예제: `userName`, `printMessage`, `countA` 등. 

* 팟홀 표기법 또는 스네이크 표기법 : 모두 소문자를 사용하고, 단어 사이에 밑줄기호(`_`)를 사용하는 표기법. 
    - 예제: `user_name`, `print_message`, `count_a` 등.   


카멜 표기법을 팟홀 표기법으로 변환하는 `camel2pothole()` 함수를 구현하라.

힌트: `str.isupper()`메서드는 문자열이 대문자인지를 확인해준다.  
'''

# pass 와  None을 적절한 명령문과 표현식으로 대체하라.

def camel2pothole(s):
    num = 0
    for letter in s:
        if str.isupper(letter):
            break
        num = num + 1
    s = list(s)
    s.insert(num, "_")
    s = "".join(s)
    return s.lower()

assert camel2pothole("userName") == "user_name"
assert camel2pothole("printMessage") == "print_message"
assert camel2pothole("countA") == "count_a"