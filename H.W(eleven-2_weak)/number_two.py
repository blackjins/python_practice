'''
메뉴와 가격이 공백으로 구분된 두 개의 문자열로 주어졌다.
menu = "ham bread chicken egg"
prices = "1200 5000 17000 500"

가장 저렴한 메뉴와 가장 비싼 메뉴를 추천하는 문자열을 
다음과 같이 출력하는 프로그램을 구현하라.

```python
가장 저렴한 메뉴: egg  
가장 비  싼 메뉴: chicken  
```
'''
menu = "ham bread chicken egg"
prices = "1200 5000 17000 500"
menu = menu.split()
prices = prices.split()
prices = list(map(int, prices))
print("가장 저렴한 메뉴:", menu[prices.index(min(prices))])
print("가장 비  싼 메뉴:", menu[prices.index(max(prices))])
    
