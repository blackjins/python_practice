'''
어느 반 학생들의 이름이 리스트로 주어졌다.
students = ['Apeach', 'Ryan', 'Muzi', 'Choonsik', 'Neo', 'Tube']
번호와 이름을 키와 값으로 갖는 사전을 출력하는 코드를 작성하여라.
단, 번호는 이름의 오름차순으로 부여되고, 동명이인은 없다고 가정한다.  

힌트: `sorted()` 함수와 `enumerate()` 함수를 이용할 수 있다.
'''

# pass 와  None을 적절한 명령문과 표현식으로 대체하라.

students = ['Apeach', 'Ryan', 'Muzi', 'Choonsik', 'Neo', 'Tube']
students = sorted(students)
name_numbers = {}
for i in range(len(students)):
    name_numbers[str(i+1)] = students[i]
assert name_numbers == {'1': 'Apeach', '2': 'Choonsik', '3': 'Muzi', '4': 'Neo', '5': 'Ryan', '6': 'Tube'}
