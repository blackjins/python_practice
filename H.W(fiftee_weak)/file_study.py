from pathlib import Path
from urllib.request import urlretrieve
import os
base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"
file_name_5m = "results5m.txt"
def myWget(filename):
    # 다운로드 대상 파일 경로
    file_url = base_url + filename

    # 저장위치 지정과 생성
    data_path = Path() / "data"
    data_path.mkdir(parents=True, exist_ok=True)
    
    # 저장 경로와 파일명
    target_path = data_path / filename
    return urlretrieve(file_url, target_path)
myWget("results5m.txt")
myWget("shopB.txt")
myWget("results10m.txt")
print(os.path.abspath("data"))


