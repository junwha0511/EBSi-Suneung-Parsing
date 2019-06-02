from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

y = input('년:')
m = input('월:')
s = input('과목(국어: ko, 영어: eng, 수학: math, 과학: sci):')
#원 숫자 변환 딕셔너리
roundToN = {'①':1,'②':2,'③':3,'④':4,'⑤':5}

#크롬 실행
driver = webdriver.Chrome('chromedriver.exe')

#3초 대기
driver.implicitly_wait(3)

#EBSi 로그인 페이지 접속
driver.get('http://www.ebsi.co.kr/ebs/pot/potl/login.ebs?destination=/index.jsp&alertYn=N')

#아이디, 비밀번호 입력
driver.find_element_by_name('userid').send_keys('encoder0511')
driver.find_element_by_name('passwd').send_keys('paekun0511')

#로그인 버튼 클릭
driver.find_element_by_class_name('loginWrap').find_element_by_tag_name('button').click()

#기출문제 페이지 접속
driver.get('http://www.ebsi.co.kr/ebs/xip/xipc/previousPaperList.ebs')

#Select 박스에서 연도 선택
select = Select(driver.find_element_by_id('yearNum'))
select.select_by_value(y)

#체크 박스에서 월 선택
driver.find_element_by_name('mAllChk').click()
driver.find_element_by_id('m'+m).click()

#ko, math, eng, koh, sci
driver.find_element_by_id('subTab_'+s).click()
sub = ''
if m == 11:
    if s == 'sci':
        sub = input('과목(물리1:1, 물리2:2, 화학1:3, 화학2:4, 생명1:5, 생명2:6, 지구1:7, 지구2:8:')
    elif s == 'ko' or s == 'eng':
        input('(홀수:1, 짝수:2):')
        sub = 1
    elif s == 'math':
        sub = input('(가형:1, 나형:2, 가형(짝):3, 나형(짝):4):')
elif m == 3:
    if s == 'sci':
        sub = input('과목(물리1:1, 화학1:2, 생명1:3, 지구1:4):')
    elif s == 'ko' or s == 'eng':
        sub = 1
    elif s == 'math':
        sub = input('(가형:1, 나형:2):')
else: 
    if s == 'sci':
        sub = input('과목(물리1:1, 물리2:2, 화학1:3, 화학2:4, 생명1:5, 생명2:6, 지구1:7, 지구2:8:')
    elif s == 'ko' or s == 'eng':
        sub = 1
    elif s == 'math':
        sub = input('(가형:1, 나형:2):')
sub = int(sub)
scr = driver.find_elements_by_tag_name('tr')[sub].find_element_by_class_name('btn_apply').get_attribute('href')
driver.execute_script(scr)
sleep(1)
driver.switch_to.window(driver.window_handles[-1]) #창 전환
driver.find_element_by_id('mode2').click()
study = driver.find_element_by_class_name('study-mode')
result = []
num = input('번호:')
result = roundToN[study.find_element_by_id('boardcorrect_'+num).find_element_by_class_name('red').get_attribute("textContent")]

if s != 'math':
        txt = []
        for text in study.find_element_by_id('Explanation_'+num).find_elements_by_css_selector('span'):
            txt.append(text.get_attribute("textContent"))
        print(str(txt))
print(result)







