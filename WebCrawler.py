import requests
from bs4 import BeautifulSoup


#카카오톡에서 서버로 전송받은 검색단어 저장부분 필요
searchWord=''

#실제 프로그램에 쓰일코드
#req=requests.get('https://ko.wikipedia.org/wiki/'+searchWord)

#CO2 예시 코드
req=requests.get('https://ko.wikipedia.org/wiki/CO2')

#html 데이터 파싱
html=req.text
soup=BeautifulSoup(html,'html.parser')

#파싱데이터중 원하는 정보 검색
table_trs=soup.select(
    'div#mw-content-text > div > table.infobox > tbody > tr  '
)

#위키에서 안정성이 있을때,없을때 구분
safety_Yes = 0;
#안정성은 여러가지 항목으로구성, List로 저장한다.
safety_Contents=[]

#여기 print2개는 자료입력을 확인하기위함이기때문에, 나중에 삭제 @@@@@@@@@@
for tr in table_trs:
    if tr.text.find("화학식")>-1:
        molecular_Formula=tr.select_one('td').text

        print("화학식")
        print(molecular_Formula)
    if tr.text.find("분자량") > -1:
        molecular_Weight = tr.select_one('td').text
        print("분자량")
        print(molecular_Weight)
    if tr.text.find("녹는점") > -1:
        melting_Point = tr.select_one('td').text
        print("녹는점")
        print(melting_Point)
    if tr.text.find("끊는점") > -1:
        boiling_Point = tr.select_one('td').text
        print("끓는점")
        print(boiling_Point)
    if tr.text.find("밀도") > -1:
        density = tr.select_one('td').text
        print("밀도")
        print(density)
    #if tr.select_one('th').text.find("안정성")>-1:
    if safety_Yes:
        safety_Contents.append(tr.select_one('th').text)
        safety_Contents.append(tr.select_one('td').text)
    if tr.text.find("안전성") > -1:
        safety_Yes = 1

#안정성 부분이 제대로 입력되나 확인하기위한 반복

if safety_Contents :

    iter=iter(safety_Contents)
    while True:
        try:
            str=next(iter)
            str+=" : "
            str+=next(iter)
            print(str)
        except StopIteration:
            break




# #img crawl 연습
# def get(max_count):
#
#     count =1
#
#     while count <= max_count:
#         base_url="http://10000img.com/"
#         req=requests.get('http://10000img.com/ran.php')
#
# #html 데이터 파싱
#         html=req.text
#         soup=BeautifulSoup(html,'html.parser')
#
#         img = soup.find("img")
#         img_src = img.get("src")
#         img_url = base_url + img_src
#         img_name=img_src.replace("/","")
#         print ("SRC : ",img_src)
#         print ("이미지 url: ",img_url)
#         print ("이미지 명 : ",img_name)
#         count+= 1
#         with open("image"+count,mode="wb") as f:
#             f.write(requests.get(img_url).text)
#             print("saved")
#
# get(5)