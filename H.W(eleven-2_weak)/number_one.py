'''
문자열 `a:b:c:d` 을 이용하여 문자열 `a#b#c#d` 생성하는 코드를 작성하라.
단, 문자열의 메서드만 사용한다.
'''

# pass 와  None을 적절한 명령문과 표현식으로 대체하라.
# 단, 문자열 "a#b#c#d" 가 직접 언급되지 않아야 한다.

input_str = "a:b:c:d"

output_str = input_str.replace(':', "#")

assert output_str == "a#b#c#d"

