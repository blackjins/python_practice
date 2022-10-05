'''
사용자의 이름과 전화번호를 입력 받으면 다음과 같이 반환하는 
`phone_book()` 함수를 구현하라.
단, 사용자의 이름은 두 글자에서 네 글자 사이며, 
핸드폰 번호는 9개에서 11개의 숫자가 다양한 방식으로 주어진다.
'''
# pass 와  None을 적절한 명령문과 표현식으로 대체하라.


def phone_book(name, phone):
    name = list(name)
    name[1] = "*"
    name = "".join(name)
    return (name, int(phone[len(phone)-4:len(phone)]))
assert phone_book('김강현', '010-1234-5678') == ('김*현', 5678)
assert phone_book('강현', '01012345678') == ('강*', 5678)
assert phone_book('김강현이', '031-123-5678') == ('김*현이', 5678)
assert phone_book('강현이', '02-123-5678') == ('강*이', 5678)
assert phone_book('김강현', '010.1234.5678') == ('김*현', 5678)