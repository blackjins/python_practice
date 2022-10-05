from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request

img_urls = []

#크롬 드라이버 위치 설정 후 구글 페이지 열기
driver = webdriver.Chrome('C:\\Users\\dndud\\OneDrive\\바탕 화면\\project\\python_practice\\persnal_project\\chromedriver.exe')
driver.get("https://www.google.co.kr/")

#구글 검색창에 "no copyright image beach" 입력 후 검색
elem = driver.find_element_by_css_selector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
elem.send_keys("바다")
elem.send_keys(Keys.RETURN)

#이미지 탭으로 넘어가기
elem2 = driver.find_element_by_css_selector("#hdtb-msb > div:nth-child(1) > div > div:nth-child(2) > a")
elem2.send_keys(Keys.RETURN)

#이미지 탭에서 이미지 주소를 가져와서 img_urls 리스트에 저장
imgelem = driver.find_elements_by_css_selector("#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img")
for img in imgelem:
    if img.get_attribute('src') is not None:
        img_urls.append(img.get_attribute('src'))

#저장된 주소에서 사진을 다운로드
for i,k in enumerate(img_urls):
    url = k
    urllib.request.urlretrieve(url, "C:\\Users\\dndud\\OneDrive\\바탕 화면\\project\\python_practice\\persnal_project\\해변 사진 저장\\" + str(i) + ".jpg")
