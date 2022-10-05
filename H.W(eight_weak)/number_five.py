'''
세 개의 막대를 이용하여 삼각형을 만들 수 있는지 여부를 판단하는 함수
`triangle()` 함수를 구현하라.
단, 다음 조건을 만족해야 한다.

- 세 개의 양의 정수를 입력받는다.
- 삼각형을 만들 수 있으면 `True`, 아니면 `False`를 반환한다.

힌트: 막대 하나의 길이가 다른 두 막대의 길이의 합보다 크면 삼각형을 만들 수 없다.
'''
# 아래 코드에서 pass 를 적절한 명령문으로, None 을 적절한 표현식으로 대체하라.

def triangle(a, b, c):
    triangle_list = [a, b, c]
    triangle_list = sorted(triangle_list)
    if triangle_list[2] <= triangle_list[1] + triangle_list[0]:
        return True
    elif triangle_list[2] > triangle_list[1] + triangle_list[0]:
        return False

assert triangle(3, 5, 7) == True
assert triangle(17, 3, 22) == False

