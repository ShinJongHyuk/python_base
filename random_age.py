import requests

name = input('이름을 입력해 주세요 : ')
print(name)

# f-string
# f'문자열{변수}'

r = requests.get(f'https://api.agify.io/?name={name}').json()
print(r)
print(type(r))
print(r['name'], '의 나이는', r['age'], '입니다')