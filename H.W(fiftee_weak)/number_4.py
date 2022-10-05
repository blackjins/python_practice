'''
`shopA.txt` 와 같이 상품명과 가격으로 이루어진 쇼핑 리스트가 포함된 파일의 이름을 입력받으면
상품명과 가격을 각각 키와 값으로 갖는 사전 객체를 반환하는 함수 `shopping()` 을 구현하라.

힌트: 문제 3을 해결하기 위해 작성한 코드를 이용한다.
'''

# 아래 코드를 완성하라. 

def shopping(shop_file):
    shop_dict = {} # 생성할 사전 객체
    with open(f"./data/{shop_file}", 'r', encoding='utf-8') as f:
        for line in f:
            if len(line) > 1:
                name, price = line.strip().split()
            if name != '#쇼핑몰':
                shop_dict[name] = price
    return shop_dict

print(shopping("shopA.txt"))

