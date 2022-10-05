def shopping(shop_file):
    shop_dict = {} # 생성할 사전 객체
    with open(f"./data/{shop_file}", 'r', encoding='utf-8') as f:
        for line in f:
            if len(line) > 1:
                name, price = line.strip().split()
            if name != '#쇼핑몰':
                shop_dict[name] = price
    return shop_dict

def item_price(shop_file, item):
    shop_dict = shopping(shop_file)
    price = shop_dict[item]
    return price