'''
상품명과 가격을 키-값의 쌍으로 갖는 아래 모양의 딕셔너리를 만들어라.
단, 오타가 수정된 파일을 이용해야 한다.

```python
{'우유': 2540,
 '계란': 7480,
 '생수': 980,
 '짜장라면': 3220,
 '두부': 1450,
 '콩나물': 1680,
 '김': 5480,
 '닭고기': 5980,
 '식빵': 2480,
 '바나나': 4980,
 '오렌지': 990,
 '카레': 2480,
 '만두': 6980,
 '어묵': 7980,
 '참치': 11880,
 '김치': 7980,
 '간장': 10800}
```
'''


store_dic = {}
with open("./data/shopA.txt", 'r', encoding='utf-8') as f:
    for line in f:
        if len(line) > 1:
            name, price = line.strip().split()
        if price != 'A':
            store_dic[name] = price
print(store_dic)