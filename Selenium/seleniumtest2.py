# # -- coding: utf-8 --
# from flask import Flask, request
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
#
# # create a new chrome session
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
#
# def seleniumCrawling():
#     # 크롬 Webdriver open
#     driver = webdriver.Chrome(chrome_options=options, executable_path="./chromedriver")
#     driver.implicitly_wait(3)
#     # driver = webdriver.Chrome("C:/Users/DATALAB_3/AppData/Local/Programs/Python/Python36/chromedriver.exe")
#
#     siteList = [1,19,2,23,20]
#     areaList = ["기획아이디어", "디자인", "광고/마케팅", "문학/시나리오", "IT/소프트웨어"]
#     k = 0
#     rList = []
#     for i in siteList:
#         driver.implicitly_wait(20) # 15초 대기
#         print("crawling end!!")
#         driver.get(f"https://www.wevity.com/?c=find&s=1&gub=1&cidx=2")
#         print("crawling end!!")
#         driver.implicitly_wait(20) # 15초 대기
#     # driver.get("https://www.thinkcontest.com/Contest/CateField.html?c={zero}".format(zero=i))
#     # 찾는 사이트 주소
#     # driver.get("https://www.wevity.com/?c=find&s=1&gub=1&cidx=1") # 기획/아이디어
#     # driver.get("https://www.wevity.com/?c=find&s=1&gub=1&cidx=19") # 디자인
#     # driver.get("https://www.wevity.com/?c=find&s=1&gub=1&cidx=2") # 광고/마케팅
#     # driver.get("https://www.wevity.com/?c=find&s=1&gub=1&cidx=23") # 문학/수기
#     # driver.get("https://www.wevity.com/?c=find&s=1&gub=1&cidx=20") # IT/소프트웨어
#         list = []
#         for j in range(2, 12):
#             driver.find_element_by_xpath(f'//*[@id="container"]/div[2]/div[1]/div[2]/div[3]/div/ul/li[{j}]/div[1]/a').click()
#
#             CONTEST_NAME = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div/div[1]/h6').text # 공모전 이름
#             # CONTEST_IMG = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/img').get_attribute('src') # 이미지 주소
#             # CONTEST_HOST = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div/div[2]/div[2]/ul/li[3]').text  # 주최
#             # CONTEST_AREA = (areaList[k])  # 분야
#             # CONTEST_DAY = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div/div[2]/div[2]/ul/li[5]').text  # 기간
#             # CONTEST_PRIZE = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div/div[2]/div[2]/ul/li[6]').text # 총상금
#             # CONTEST_ADDR = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[2]/div/div[2]/div[2]/ul/li[8]/a').get_attribute('href')  # 홈페이지주소
#             # CONTEST_CONTENTS = driver.find_element_by_css_selector('#viewContents').get_attribute('innerHTML') # 공모전 내용
#
#             ContestDTO = {} #object
#             ContestDTO['contest_name'] = CONTEST_NAME
#             # ContestDTO['contest_img'] = CONTEST_IMG
#             # ContestDTO['contest_host'] = CONTEST_HOST
#             # ContestDTO['contest_area'] = CONTEST_AREA
#             # ContestDTO['contest_day'] = CONTEST_DAY
#             # ContestDTO['contest_prize'] = CONTEST_PRIZE
#             # ContestDTO['contest_addr'] = CONTEST_ADDR
#             # ContestDTO['contest_contents'] = CONTEST_CONTENTS
#
#
#             list.append(ContestDTO)
#
#             # print("CONTEST_NAME : ",CONTEST_NAME)
#             # print("CONTEST_IMG : ", CONTEST_IMG)
#             # print("CONTEST_HOST : ",CONTEST_HOST)
#             # print("CONTEST_AREA : ",CONTEST_AREA)
#             # print("CONTEST_DAY : ",CONTEST_DAY)
#             # print("CONTEST_PRIZE : ",CONTEST_PRIZE)
#             # print("CONTEST_ADDR : ",CONTEST_ADDR)
#             # print("CONTEST_CONTENT : ",CONTEST_CONTENTS)
#
#             driver.back()
#         rList.append(list)
#     k = k+1
#     print(rList)
#     return rList
