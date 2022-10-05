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
    