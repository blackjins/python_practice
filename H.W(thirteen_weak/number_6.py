'''
다음 월리스 공식Wallis formula을 이용하여 원주율 PI를 소수점 이하 다섯째 자리까지 구하라.
단, 조건제시법을 반드시 이용한다.

$$
\pi = 2 \prod_{i=1}^{\infty} \frac{4 i^2}{4 i^2 -1}
$$

힌트: range() 함수, math 모듈의 prod() 함수, functools 모듈의 reduce() 함수 등을 이용할 수 있다.
또한 소수점 이하 다섯째 자리까지 구하기 위해 필요한  i  의 최소값을 알아내야 한다.
'''
from functools import reduce
Wallis_formula = [((4*i**2)/(4*i**2-1)) for i in range(1, 300000)]
print(2 * reduce(lambda x, y:x*y, Wallis_formula))
