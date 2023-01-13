# 파이썬으로 웹 요청 보낼 수 있는 라이브러리 불러오기

# 동행복권 로또 당첨 번호 api 사용하기
# (회차 직접 입룍)
# 입력받은 회차에 해당하는 당첨번호 확인하기 -> 6개 (보너스번호 제외)
# (선택사항) - 보너스 번호 확인하기

import requests
import random

number = input('회차를 입력해 주세요 : ')

r = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={number}').json()
print(r)
print(type(r))
AA = []
for i in range(1,7):
    AA.append(r[f'drwtNo{i}'])

'''first = 0
third = 0
fourth = 0
fifth = 0
fail = 0'''

count_dict = {'1등':0, '3등':0, '4등':0, '5등':0, '꽝':0}

# 4. 이걸 1000번 반복한다.
    # 1. 로또 번호 6개를 추첨 받는다
    # 2. 내가 추첨받은 번호가 1049회차 당첨 번호와 일치하는지 확인한다.
        # 2-1. 확인하는 방법은 내 번호 6개를 순차적으로 순회하며
            #  1049회 번호목록에 해당 숫자가 있는지
            #  있다면 적중 횟수 +1
    # 그래서 적중 횟수가 6개면 1등
    # 5개면 3등
    # 4개면 4등
    # 3개면 5등
    # 2개 이하면 꽝을 출력한다.
for i in range(1000):
    count = 0
    N = list(range(1,46))
    A = []
    for i in range(6):
        B = random.choice(N)
        A.append(B)
        N.remove(B)
    print(AA)
    print(A)
    # for i in range(6):
    #     for j in range(6):
    #         if AA[i] == A[j]:
    #             count += 1
    for i in AA:
        if i in A:
            count += 1
    print('맞은 개수 =', count, '개')


    if count == 6:
        print ('당첨 결과:','1등')
        # first += 1
        count_dict['1등'] = count_dict['1등'] + 1
    elif count == 5:
        print('당첨 결과:','3등')
        # third += 1
        count_dict['3등'] = count_dict['3등'] + 1
    elif count == 4:
        print('당첨 결과:','4등')
        # fourth += 1
        count_dict['4등'] = count_dict['4등'] + 1
    elif count == 3:
        print('당첨 결과:','5등')
        # fifth += 1
        count_dict['5등'] = count_dict['5등'] + 1
    elif count <= 2:
        print('당첨 결과:','꽝')
        # fail += 1
        count_dict['꽝'] = count_dict['꽝'] + 1

# print('1등 당첨 횟수:', first)
# print('3등 당첨 횟수:', third)
# print('4등 당첨 횟수:', fourth)
# print('5등 당첨 횟수:', fifth)
# print('꽝 당첨 횟수:', fail)

print(count_dict)
