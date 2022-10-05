'''
문자열을 받아 순서를 거꾸로 하는 문자열을 반환하는 `reverse()` 회귀 함수를 
구현하라.
'''
i = 1
def reverse(s):
    global i
    assert isinstance(s, str) and len(s) > 1
    if i == 1:
        result = s[i] + s[0] + s[i+1:len(s)]    
    else:
        result = s[i] + s[0:i] + s[i+1:len(s)]
    i = i + 1
    if i == len(s):
        i = 0
        return result
    return reverse(result)
    
    
assert reverse('hello') == 'olleh'
assert reverse('core python') == 'nohtyp eroc'
assert reverse('radar') == 'radar'