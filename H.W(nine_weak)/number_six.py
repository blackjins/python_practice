'''
`to_bin()` 함수를 일반화하여 양의 수를 다양한 진법으로 변환하는 `to_base()` 회귀 함수를 구현하라.
단, 반환값은 지정된 진법으로 표현된 문자열이어야 한다.
또한 진법은 2진법, 8진법, 16진법으로 제한한다. 

* `n`: 정수를 받는 매개변수
* `base`: 진법을 정하는 매개변수

참고: 8진법인 경우엔 0부터 7까지의 수는 각각 '0', '1', ..., '7' 등으로 변환하며, 16진법인 경우엔 0부터 15까지의 수를 각각 '0', '1', ..., '9', 'A', 'B', ..., 'F'로 변환한다.
'''

i = 0
result = []
def to_bin(n):
    assert isinstance(n, int) and n > 0
    global i
    global result
    if i == 0:
        result = []
    a, b = divmod(n, 2)
    result.append(str(b))
    i = i + 1
    if a == 0:
        i = 0
        return "".join(result[::-1]) 
    else:
        return to_bin(a)




def to_base(n, base):
    assert isinstance(n, int) and n > 0
    assert base in [2, 8, 16]

    num_dic = {
        2: {
            0: '0',
            1: '1'
        },
        8: {
            0: '0',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7'
        },
        16: {
            0: '0',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }
    }
            
    for i in num_dic[base]:
        if n == i:
            return num_dic[base][i]
    return to_base(n//base, base) + num_dic[base][n%base]

assert to_base(46685, 2) == to_bin(46685)
assert to_base(46685, 8) == '133135'
assert to_base(46685, 16) == 'B65D' 