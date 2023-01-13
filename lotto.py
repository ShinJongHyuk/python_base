import random

# 1~45 숫자를 담은 list 생성
# range(n,m) = n부터 m-1 까지의 숫자 생성
numbers = list(range(1,46))
print(numbers)

# numbers가 가진 숫자중에 무작위 값ㅇ르 하나씩 6번 뽑기
# 리스트가 가지고 있는 값중 무작위 값을 뽑는 법은?

n = 0
lotto = []
while n < 6:
    a = random.choice(numbers)
    numbers.remove(a)
    lotto.append(a)
    n = n + 1
print(lotto)


for i in range(5):
    print(random.sample(numbers,6))