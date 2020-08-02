from selenium import webdriver
import time

def login():
    driver.find_element_by_xpath('//*[@id="q"]').send_keys('小米8')
    driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
    driver.find_element_by_xpath('//*[@id="login"]/div[1]/i').click()

    # 扫码登录
    time.sleep(15)

# 滑动滑条，加载全部信息
def drop_down():
    for x in range(1, 11, 2):
        time.sleep(0.5)# 防止被预测到反爬
        h = x/10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % h
        driver.execute_script(js)

def get_product_info(number):
    pre = '//*[@id="mainsrp-itemlist"]/div/div/div[1]/div['
    xpath_price = pre + str(number) + ']/div[2]/div[1]/div[1]/strong'
    xpath_sell = pre + str(number) + ']/div[2]/div[1]/div[2]'
    xpath_store = pre + str(number) + ']/div[2]/div[3]/div[1]/a/span[2]'
    xpath_location = pre + str(number) + ']/div[2]/div[3]/div[2]'

    price = driver.find_element_by_xpath(xpath_price).text
    sell = driver.find_element_by_xpath(xpath_sell).text
    store = driver.find_element_by_xpath(xpath_store).text
    location = driver.find_element_by_xpath(xpath_location).text
    a = driver.find_element_by_xpath(xpath_sell)
    print(type(a))
    print(price)
    print(sell)
    print(store)
    print(location)

def next_page():
    driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]').click()

if __name__ == '__main__':
    driver = webdriver.Chrome(r'D:\360极速浏览器下载\chromedriver_win32\chromedriver.exe')
    driver.get('https://www.taobao.com/')
    login()
    drop_down()
    for i in range(1, 10):
        get_product_info(i)
        time.sleep(0.5)
    next_page()