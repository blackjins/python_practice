from pathlib import Path
from urllib.request import urlretrieve
base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"
# 데이터 저장위치 지정과 생성
data_path = Path() / "data"
data_path.mkdir(parents=True, exist_ok=True)
def myWget(path, filename):
    # 다운로드 대상 파일 경로
    file_url = base_url + filename

    # 저장 경로와 파일명
    target_path = path / filename

    return urlretrieve(file_url, target_path)
myWget(data_path, "shopA.txt")
'''
`shopA.txt` 파일은 쇼핑몰A에서 판매하는 상품의 가격을 담고 있음을 확인해보자.
먼저 해당 파일을 다운로드 한다.
이제 파일 전체 내용을 출력하는 코드를 작성하라.
힌트: `open()` 함수와 `with-as` 명령문 활용
'''
with open("./data/shopA.txt", mode='r', encoding='utf-8') as f:
    for line in f: 
        print(line.strip())
    