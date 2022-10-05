'''
리스트 `['Life', 'is', 'too', 'short']` 를 이용하여
문자열 `"Life is too short"` 을 생성하는 코드를 작성하라.
단, 리스트의 `pop()` 메서드를 사용해야 한다.
'''
# pass 와  None을 적절한 명령문과 표현식으로 대체하라.
# 단, 문자열 "Life is too short" 이 직접 언급되지 않아야 한다.

input_list = ['Life', 'is', 'too', 'short']
output_str = ""
tmp = len(input_list)
for i in range(tmp):
    output_str = output_str + " " + input_list.pop(0)
output_str = output_str[1:]
assert output_str == "Life is too short"