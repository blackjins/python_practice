'''
`shopA.txt` 파일의 내용을 확인하면, 오타가 있다. 
'오레ㄴ지' 를 '오렌지'로 변경한 후에
`shopA.txt` 파일을 열어 오타가 수정되었는지를 확인하여라.  

힌트: 파일의 `read()` 메서드, 문자열의 `replace()` 메서드
'''
# 파일내용을 하나의 문자열로 생성하는 코드를 작성하라.
with open("./data/shopA.txt", mode='r', encoding='utf-8') as f:
    lines = f.read()
    
lines
'''* 오타 수정: `replace()` 문자열 메서드 활용'''
# 오타를 수정하는 코드를 작성하라.
with open("./data/shopA.txt", mode='r', encoding='utf-8') as f:
    lines = f.read()
lines = lines.replace('오레ㄴ지', '오렌지')
print(lines)
'''* 파일 저장'''
# 오타가 수정된 문자열을 파일로 저장하는 코드를 작성하라.
with open("./data/shopA.txt", mode='r', encoding='utf-8') as f:
    lines = f.read()
    
lines = lines.replace('오레ㄴ지', '오렌지')
with open("./data/shopA.txt", mode='w', encoding='utf-8') as f:
    f.write(lines)
'''* 파일 내용 확인'''
# 오타가 수정되었음을 확인하는 코드를 작성하라.
with open("./data/shopA.txt", mode='r', encoding='utf-8') as f:
  lines = f.read()
print(lines)
