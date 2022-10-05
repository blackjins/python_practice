'''
`time` 모듈에 UTC(Coordinated Universal Time)를 알려주는 `time()` 함수가 포함되어 있다.
`time()` 함수는 일종의 컴퓨터 시간의 생일인 1970년 1월 1일을 기준으로 
함수의 호출 순간까지 흐른 시간을 초 단위로 반환한다.

현재의 UTC를 시, 분, 초 단위로 변환하는
함수 `time_convert()` 함수를 구현하라.
단, 반환값은 아래 포맷을 갖춘 문자열이어야 하며,
초는 반올림해서 계산한다.

시-분-초

힌트: `divmod()` 함수를 활용할 수 있다.
'''
import time
def time_convert():
    x = time.time()
    hour = int(divmod(x,3600)[0])
    x = x%3600
    min = int(divmod(x, 60)[0])
    sec = int(x%60)
    result = print(f"{hour}-{min}-{sec}")
    return result
time_convert()

