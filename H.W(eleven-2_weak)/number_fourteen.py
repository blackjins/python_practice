'''
교육 참가자 명단과 수료자 명단이 아래처럼 리스트로 주어다.
participant = ['Apeach', 'Ryan', 'Muzi', 'Choonsik', 'Neo', 'Tube']
completion = ['Ryan', 'Muzi', 'Neo', 'Choonsik']
수료하지 못한 사람들의 명단을 리스트로 출력하는 코드를 작성하여라.
단, 참여자 중 동명이인은 없고, 순서는 중요하지 않다. 
'''
participant = ['Apeach', 'Ryan', 'Muzi', 'Choonsik', 'Neo', 'Tube']
completion = ['Ryan', 'Muzi', 'Neo', 'Choonsik']
unfinished = []
for letter in participant:
    tmp = 0
    for i in completion:
        if letter == i:
            tmp = tmp + 1    
    if tmp == 0:
        unfinished.append(letter)
assert unfinished == ['Apeach', 'Tube']