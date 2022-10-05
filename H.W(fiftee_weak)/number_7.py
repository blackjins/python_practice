'''
[5미터 다이빙 기록 에서 등수를 확인하는 작업](https://codingalzi.github.io/pybook/files.html#sec-exp-diving-5m)과 
동일한 작업을 10미터 다이빙 기록에 대해 진행하라.
'''

result_dive_dic = {}
with open(f"./data/results10m.txt", 'r', encoding='utf-8') as f:
    for line in f:
        if len(line) > 1:
            name, result = line.strip().split()
        if name != '이름':
            result_dive_dic[name] = result
sorted_scores_10m = sorted(result_dive_dic.items(), key = lambda item: item[1], reverse=True)
count = 1
for item in sorted_scores_10m:
    print(f"{count:>3}등: {item[0]} {item[1]}")
    count += 1      
