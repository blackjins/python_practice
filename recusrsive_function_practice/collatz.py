def collatz(num):
    if num == 1:                        # 기저 조건
        print(1)
    elif num%2 == 0:                  # 짝수인 경우
        print(num, end=' -> ')
        collatz(num//2)
    else:                               # 홀수인 경우
        print(num, end=' -> ')
        collatz(num*3 + 1)