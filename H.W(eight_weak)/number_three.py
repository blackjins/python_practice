'''
오늘의 요일을 확인하여 0에서 6 사이의 정수를 반환하는 함수
`wday2num()` 함수를 구현하라.
단, 다음 조건을 만족해야 한다.

- 일(Sun), 월(Mon), 화(Tue), 수(Wed), 목(Thu), 금(Fri), 토(Sat) 순서대로 0, 1, 2, 3, 4, 5, 6 을 사용한다.
- 하나의 매개변수 `wday` 를 사용하며, 키워드 인자로 `"Sun"`을 사용한다.
- 지정된 `wday` 와 오늘의 요일이 일치하면 
    해당 요일도 함께 튜플로 반환한다.
    
힌트: `time.ctime()` 함수 활용.
'''
# 아래 코드에서 pass 를 적절한 명령문으로, None 을 적절한 표현식으로 대체하라.
from ctypes.wintypes import WIN32_FIND_DATAA
import time
def wday2num(wday=None):
    weak_list = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    day = time.ctime().split(" ")
    for i in range(0, 6):
        if day[0] == weak_list[i]:
            if day[0] == wday:
                return (i, wday)
            else:
                return i
wday2num(wday="Mon")
wday2num(wday="Sun")