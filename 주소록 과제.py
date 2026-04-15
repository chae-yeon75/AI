#전화부 과제
import json
import os

name = None

if os.path.exists("addressbook.json"): #원래 파일 존재하면 기존 데이터 불러옴
    with open("addressbook.json", "r", encoding="utf-8") as f:
        addressbook = json.load(f)
else:
    addressbook = dict() #빈주소록
    
while True:
    name = input('이름을 입력하세요:')
    if name == '끝':
        break
    phoneNum = input('전화번호를 입력하세요:')
    if name in addressbook:
        if addressbook[name] == phoneNum:
            print(f"{name}은(는) 이미 동일한 번호가 저장되어 있습니다.")
        else:
            print(f"{name}의 번호를 수정합니다.") 
            addressbook[name] = phoneNum
    
    else:
        addressbook[name] = phoneNum
    
with open("addressbook.json","w",encoding="utf-8") as f:
    json.dump(addressbook,f,ensure_ascii=False,indent=4)
    
print('주소록이 저장되었습니다.')

