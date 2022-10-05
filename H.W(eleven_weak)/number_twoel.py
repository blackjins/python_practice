'''
다음과 같은 방법으로 (세 자리 수) $\times$ (세 자리 수) 를 계산할 수 있다.<br><br>

<div align="center">
<img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch04/pro01.png" style="width:150px;">
</div>  

두 개의 세 자리 수 a 와 b 가 주어질 때, &#9312;, &#9313;, &#9314;, &#9315;에 들어갈 값을 
각각 줄변경하여 출력하는 `mult()` 함수를 구현하라.
반환값은 두 수의 곱이다.

힌트: 문자열 인덱싱과 `for` 반복문 활용
'''
# pass 와 None 을 각각 적절한 명령문과 반환값으로 대체하라.
def mult(a, b):
    assert 100 <= a <= 999 
    assert 100 <= b <= 999     
    tmp = b
    b = str(b)[::-1]
    num = 1
    for i in range(len(b)):
        result = int(b[i]) * a
        print("(", num, ")" , result)
        num = num + 1
    print("(", num, ")" , a * tmp)
    return 
mult(265, 112)

