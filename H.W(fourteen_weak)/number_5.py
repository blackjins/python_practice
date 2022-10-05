'''
다음 라이브니츠 공식<font size='2'>Leibniz formula</font>을 이용하여 
원주율 PI를 소수점 이하 다섯째 자리까지 구하라. 
단, 제너레이터 함수를 이용한다.

$$
\pi = 4 \sum_{i=1}^{\infty} \frac{(-1)^{n+1}}{2n-1}
$$

또한 소수점 5째 자리까지 구하기 위해 필요한 $i$ 의 최소값을 알아내야 한다.
'''
leibniz_formila = (((-1)**(i+1))/(2*i-1) for i in range(1, 300000))
leibniz_formila_sum = 4 * sum(list(leibniz_formila))
leibniz_formila_sum = str(leibniz_formila_sum)[:7]
print(float(leibniz_formila_sum))
