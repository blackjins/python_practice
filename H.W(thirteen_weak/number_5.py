'''
A대학의 일반차량에 대한 주차요금은 아래와 같다.   

* 2,000원/최초 30분, 초과 10분마다 500원, 1일(24시간)은 40,000원   

일반차량에 대한 입출차 기록이 리스트로 주어졌다.
car_in_out = ['07:30 1234 IN', 
              '07:35 2580 IN',
              '08:15 0328 IN',
              '08:45 2580 OUT',
              '08:55 9876 IN',
              '11:00 1597 IN',
              '15:15 1234 OUT',
              '21:00 0328 OUT',
              '23:45 9876 OUT']
차량별로 주차시간과 주차요금이 사전 자료형으로 정리하는 코드를 작성하라.
단, 아래 사항을 가정한다.

* 차량번호는 차량 뒷번호 4자리를 기록하고, 동일한 차량번호는 없다.
* 시간은 24시간제를 사용하고, 모든 차량은 00:00부터 23:59분 사이에 한 번씩만 입출차 한다.
* 아직 출차하지 않은 차량에 대해서는 주차시간과 주차요금을 정리할 수 없다.  
'''
def fee_cal_func(Parking_Duration):
    tm = 0
    while Parking_Duration > 0:
        if tm == 0 and Parking_Duration < 790:
            Parking_Duration = Parking_Duration - 30
            fee = 0
            fee = fee + 2000
            tm = tm + 1
        elif tm == 0 and Parking_Duration >=790:
            Parking_Duration = 0
            fee = 40000
        else:
            Parking_Duration = Parking_Duration - 10
            fee = fee + 500
    return fee
answer = {}
car_in_out = ['07:30 1234 IN', 
              '07:35 2580 IN',
              '08:15 0328 IN',
              '08:45 2580 OUT',
              '08:55 9876 IN',
              '11:00 1597 IN',
              '15:15 1234 OUT',
              '21:00 0328 OUT',
              '23:45 9876 OUT']
car_num_list = []
for letter in car_in_out:
    if letter[11:] == 'IN':
        car_num_list.append(letter[6:10])
for num_list in car_num_list:
    answer[num_list] = {}
tmp = []
for numbers in car_num_list:
    for In_Out_letter in car_in_out:
        if numbers == In_Out_letter[6:10]:
            tmp.append(In_Out_letter[:2])
            tmp.append(In_Out_letter[3:5])
            answer[numbers][In_Out_letter[11:]] = In_Out_letter[:5]
parking_duration_list = []
tmp = tmp[:len(tmp)-2]
ttmp = 0
for i in range(len(tmp)):
    parking_duration_list.append(int(tmp[ttmp])*60 + int(tmp[ttmp+1]))
    ttmp += 2
    if ttmp == len(tmp):
        ttmp = 0
        break
print(parking_duration_list)
new_parking_duration_list = []
parking_duration_fee = []
for t in range(0,4):
    new_parking_duration_list.append(parking_duration_list.pop(ttmp+1) - parking_duration_list.pop(ttmp))
fee_list = []
for y in new_parking_duration_list:
    fee_list.append(fee_cal_func(y))
for x in range(len(new_parking_duration_list)):
    answer[car_num_list[x]]['parking_duration'] = new_parking_duration_list[x]
    answer[car_num_list[x]]['parking_fee'] = fee_list[x]
print(answer)