'''
아래 조건을 만족하는 `zip_strings()` 함수를 구현하라.

* 세 개의 문자열을 각각 입력 받는 `str1`, `str2`, `str3` 매개 변수를 사용한다.
* `str3`가 가리키는 값이 `str1` 과 `str2` 이 가리키는 문자열에 포함된 문자들을
    번갈아가며 결합한 결과이면 `True`를, 아니면 `False` 를 반환한다.
* 두 문자열의 길이가 다르면, 가능한 데까지만 문자를 번갈아가며 결합하고 나머지는 그대로 적어준다.    

힌트: `zip()` 함수 활용 가능.
'''
# pass 와  None을 적절한 명령문과 표현식으로 대체하라.

def zip_strings(str1, str2, str3):
    result = ""
    if str1 > str2:
        for pair in zip(str1, str2):
            result = result +  "".join(pair)
        if len(str1) < len(str2):
            result = result + str2[len(str1):len(str2)]
        else:
            result = result + str1[len(str2):len(str1)]
    elif str1 == str2:
        for pair in zip(str1, str2):
            result = result +  "".join(pair)
        if len(str1) < len(str2):
            result = result + str2[len(str1):len(str2)]
        else:
            result = result + str1[len(str2):len(str1)]
    else:
        for pair in zip(str2, str1):
            result = result +  "".join(pair)
        if len(str1) < len(str2):
            result = result + str2[len(str1):len(str2)]
        else:
            result = result + str1[len(str2):len(str1)]
    # if result == str3:
        # return True
    return result
print(zip_strings('computing', 'math','cmoamtphuting'))
assert zip_strings('dog', 'cat', 'dcoagt') == True
assert zip_strings('cat', 'dog', 'dcoagt') == True
assert zip_strings('dog', 'cat', 'cdoagt') == False
assert zip_strings('computing', 'math','cmoamtphuting') == True
assert zip_strings('math', 'computing','cmoamtphuting') == True
assert zip_strings('math', 'computing', 'mcoamtphuting') == False

