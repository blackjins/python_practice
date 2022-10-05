'''
500원, 100원, 50원, 10원 짜리 동전으로 거스름돈을 지급할 때
동전의 개수를 최소화하고자 한다.
거슬러 줘야 하는 금액이 n 원일 때, 필요한 동전의 최소 개수를 반환하는
`change()` 함수를 구현하라.
단, n 은 10의 배수이며 5000보다 작은 정수고, 모든 동전은 무한히 많이 있다고 가정한다. 

힌트: [탐욕 알고리즘](https://code-lab1.tistory.com/11) 참고. `while` 반복문 활용.
'''
# pass 와 None 을 각각 적절한 명령문과 반환값으로 대체하라.
def change(n):
    assert (n%10 == 0 and n < 5000)
    sum = 0
    while n != 0:
        if n > 500:
            n = n - 500
            sum = sum + 1
        elif 100 < n < 500:
            n = n - 100
            sum = sum + 1
        elif 50 < n < 100:
            n = n - 50
            sum = sum + 1
        elif 0 < n < 50:
            n = n - 10
            sum = sum + 1
    return sum

assert change(1730) == 8