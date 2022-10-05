'''
5미터 다이빙 기록과 10미터 다이빙 기록의 합에 대해 등수를 확인하는 코드를 작성하라.
'''

def diving_result(dive_file):
    dive_result_dict = {} # 생성할 사전 객체
    with open(f"./data/{dive_file}", 'r', encoding='utf-8') as f:
        for line in f:
            if len(line) > 1:
                name, score = line.strip().split()
            if name != '이름':
                dive_result_dict[name] = score
    return dive_result_dict

diving5m_result_dict = diving_result("results5m.txt")
diving10m_result_dict = diving_result("results10m.txt")
diving_results_dict = {}

for name in diving5m_result_dict:
    score_5m = diving5m_result_dict[name]
    score_10m = diving10m_result_dict[name]
    diving_results_dict[name] = (score_5m, score_10m)

for name in diving_results_dict:
    diving_results_dict[name] = map(float, diving_results_dict[name])
    diving_results_dict[name] = sum(diving_results_dict[name])
    diving_results_dict[name] = round(diving_results_dict[name], 3)

sorted_scores = sorted(diving_results_dict.items(), key = lambda item: item[1], reverse=True)
count = 1
for item in sorted_scores:
    print(f"{count:>3}등: {item[0]} {item[1]}")
    count += 1      
