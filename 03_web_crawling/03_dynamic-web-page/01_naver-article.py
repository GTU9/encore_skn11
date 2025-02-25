from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# 1. chrome 실행
driver= webdriver.Chrome()

# 2. 특정 url 접근
# driver.get('https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=방어')
driver.get('http:/www.naver.com')
time.sleep(1)

# 3. 검색어 처리ㅔㅐㅕㅑㅣ
search_box=driver.find_element(By.ID,'query')
search_box.send_keys('참치')
search_box.send_keys(Keys.RETURN)
time.sleep(1)

# - 뉴스 탭 이동
news_btn=driver.find_element(By.XPATH,'//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[8]/a')
news_btn.click()
time.sleep(1)


# 4. 스크롤 처리
for _ in range(2):
    body=driver.find_element(By.TAG_NAME,'body')
    body.send_keys(Keys.END)
    time.sleep(1)

# 5. 특정 요소에 접근
news_area_elems=driver.find_elements(By.CSS_SELECTOR, '.news_area')
news_data=[]

for news_area_elem in news_area_elems:
    news_info_elem=news_area_elem.find_element(By.CSS_SELECTOR,'.news_info')
    news_cotents_elem=news_area_elem.find_element(By.CSS_SELECTOR,'.news_contents')

    info_elem=news_info_elem.find_elements(By.CSS_SELECTOR, 'a.info')

    if len(info_elem) > 1 and '네이버뉴스' in info_elem[1].text:
        a_tag=news_cotents_elem.find_element(By.CSS_SELECTOR,'.news_tit')
        title=a_tag.text
        href=a_tag.get_attribute('href')
        # print(f'제목 : {title}\n링크 : {href}\n')

        driver.execute_script('window.open("");')
        driver.switch_to.window(driver.window_handles[1])
        driver.get(href)
        time.sleep(1)

        content=driver.find_element(By.TAG_NAME,'div').text

        news_data.append({
            'title':title,
            'link': href,
            'content':content

        })

        # driver.back()
        driver.close()

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

with open('news_data.txt','w',encoding='utf-8') as file:
    for news in news_data:
        file.write(f'제목 : {news['title']}\n')
        file.write(f'링크 : {news['link']}\n')
        file.write(f'내용 : {news['content']}\n')

driver.quit()