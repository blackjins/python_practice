'''
[반복문](https://codingalzi.github.io/pybook/iterations.html)에서 소개한 
`collatz()` 함수는 다음과 같다.

```python
def collatz(n):
    while n != 1:
        print(n, end=" -> ")
        if n%2 == 0:
            n = n//2
        else:
            n = n*3 + 1
            
    print(1)
```

`while` 반복문이 실행된 횟수를 반환하도록 위 함수를 수정하라.
단, 100번 이상 반복하면 실행을 멈추고 -1을 반환하도록 한다.
'''

# pass 와 None 을 각각 적절한 명령문과 반환값으로 대체하라.

def collatz(n):
    num = 0
    while n != 1:
        if n%2 == 0:
            n = n//2
            num = num + 1
        else:
            n = n*3 + 1
            num = num + 1
        if num > 100:
            return -1
    return num
    
assert collatz(17) == 12
assert collatz(117) == 20
assert collatz(1117) == 44
assert collatz(11117) == -1