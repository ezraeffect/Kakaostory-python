from selenium import webdriver
import time

print("크롬 웹 드라이버를 불러오는 중 입니다")
chromedriver_dir = r'Your Webdriver DIR'
print(chromedriver_dir)
driver = webdriver.Chrome(chromedriver_dir)

# 서비스 로그인
print("로그인을 시도합니다")
driver.get('https://accounts.kakao.com/login/kakaostory')
print("계정 정보를 입력합니다")
time.sleep(1)
driver.find_element_by_name("email").send_keys('ID') #계정 정보 입력
driver.find_element_by_name("password").send_keys('PS')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/button').click() #로그인
time.sleep(1)
driver.find_element_by_xpath('//*[@id="kakaoGnb"]/ul/li[1]/a').click() #글쓰기 클릭
time.sleep(1)
driver.find_element_by_xpath('//*[@id="contents_write"]').send_keys('파이썬 Selenium 로그인 + 글쓰기 테스트 입니다.') #글 내용 입력
time.sleep(1)
driver.find_element_by_xpath('//*[@id="kakaoBody"]/div[1]/div/div[3]/div[2]/div[1]/div/div[9]/div[2]/a[2]').click() # 올리기 클릭
time.sleep(1)