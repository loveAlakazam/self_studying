# 지니뮤직 크롤링

### 1. 프로젝트 정보
- 진행기간: 2020.05.01
- 사용한 언어: python3
- 사용한 기술 libraries : Beautiful Soup bs4, requests, openpyxl, datetime
- 참고: 스파르타 코딩클럽 혼자놀기 패키지 따라해보기

### 2. 프로젝트 설명
- 어떤 프로젝트인가?
  - 지니 뮤직 사이트의 일일차트에서 1위~50위 곡정보(순위 ,제목, 아티스트 이름)를 수집한다.
  - 현재로부터 2달전 1일 ~ 어제 까지의 음원차트 순위에 대한 정보이다.
  - 일일 차트 정보를 엑셀파일에 저장하고 opnepyxl 라이브러리로 엑셀파일을 관리한다.
  - 관심있는 노래 2곡(이태원클라쓰 OST 2곡: 돌덩이, 시작)의 순위변동을 확인한다.
  
- 왜 이 프로젝트를 했는가?
  - 파이썬 웹크롤링에 다시 재미를 느끼고 싶다. 
  - 요즘 너무 게으르고 모든걸 귀찮아하는 거같아서 정신차려야 될거같아 싶어서 ^^;
  - 혼자서 코딩하면서 놀아보고 싶어서.

### 3. 프로젝트 코드와 결과
- 프로젝트 코드 (Python3)

```python3
# 2020년 3월 1일 ~ 2020년 5월 1일 까지의 순위를 알아본다.
import requests
import pandas
from bs4 import BeautifulSoup
from openpyxl import load_workbook, styles

# 엑셀파일 불러오기
load_wb= load_workbook('mystock.xlsx', data_only=True)
load_ws= load_wb['Sheet1']

# 음악차트 기간을 구한다.(두달전 1일 ~ 어제)
today=datetime.now()
start='%d%02d%02d' %(today.year, today.month-2, 1)
end='%d%02d%02d' %(today.year, today.month, today.day)

dt_index= pandas.date_range(start=start, end=end)
dates= dt_index.strftime('%Y%m%d').tolist()[:-1]

j=2 #2번 부터 시작(열)
for date in dates:
    #url을 읽어서 HTML을 받아온다.
    headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data=requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd='+date,
                      headers=headers)
    
    #html을 이용하여 BeautifulSoup라는 라이브러리를 활용해 검색하기 용이한 상태로 만든다.
    soup= BeautifulSoup(data.text, 'html.parser')
    
    #select를 이용해서 tr을 모은다.
    songs= soup.select('#body-content > div.newest-list > div > table > tbody > tr')
    
    #날짜 찍기
    load_ws.cell(1, j, date)
    
    #date 노래 차트 1위~50위정보를 반복문으로 돌리기
    i=2 #행
    for song in songs:
        #랭크
        rank=song.select_one('td.number').text[0:2].strip()
        
        title=song.select_one('td.info > a.title.ellipsis').text.strip()
        
        artist=song.select_one('td.info > a.artist.ellipsis').text
        
        # 하현우 - 돌덩이 => 색칠
        if title=='돌덩이' and artist=='하현우 (국카스텐)':
            color=styles.colors.Color(rgb='EEEEEE00')
            fill=styles.fills.PatternFill(patternType='solid', fgColor=color)
            load_ws.cell(i,j, title+'-'+artist).fill=fill
            
        # 가호 - 시작 => 색칠
        elif title=='시작' and artist=='가호 (Gaho)':
            color=styles.colors.Color(rgb='CCEEFF00')
            fill=styles.fills.PatternFill(patternType='solid', fgColor=color)
            load_ws.cell(i,j, title+'-'+artist).fill=fill
           
            
        else:
            load_ws.cell(i, j, title+'-'+artist)
        i+=1
    j+=1

load_wb.save('mystock.xlsx')
```

- 프로젝트 결과
![프로젝트결과 사진 일부](./final_result.JPG)
