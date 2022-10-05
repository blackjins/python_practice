'''
`shopB.txt` 파일은 쇼핑몰B에서 판매하는 상품의 가격을 담고 있으며,

`shopA.txt` 파일과 동일한 방식으로 다운로드할 수 있다.

사용자가 상품을 입력하면, 쇼핑몰A와 쇼핑몰B 중 어느 쇼핑몰에서 구입하는 것이 얼마나 저렴한지를 보여주는
함수 `price_comparison()`를 작성하라.
'''
# 코드를 완성하라.
def shopping(shop_file):
    shop_dict = {} # 생성할 사전 객체
    with open(f"./data/{shop_file}", 'r', encoding='utf-8') as f:
        for line in f:
            if len(line) > 1:
                name, price = line.strip().split()
            if name != '#쇼핑몰':
                shop_dict[name] = price
    return shop_dict

def price_comparison(item):
    shop_dict_A = shopping("shopA.txt")
    shop_dict_B = shopping("shopB.txt")
    shopA_price = shop_dict_A[item]
    shopB_price = shop_dict_B[item]
    shopA_price = int(shopA_price[:len(shopA_price)-1])
    shopB_price = int(shopB_price[:len(shopB_price)-1])
    if shopA_price > shopB_price:
        return "shopB에서 사는게 더 저렴합니다"
    elif shopA_price < shopB_price:
        return "shopA에서 사는게 더 저렴합니다"
    else:
        return "두곳에서 사도 가격이 같습니다."
print(price_comparison('김치'))
