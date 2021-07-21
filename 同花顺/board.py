from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup as bs
import pandas as pd
import time

def parse(dtime, driver):
    info_table = pd.DataFrame(
        columns=['代码', '名称', '现价', '涨跌幅%', '涨跌', '涨速%', '换手%', '量比', '振幅%', '成交额', '流通股', '流通市值', '市盈率'])
    row_cnt = 1
    try:
        for row in range(1, 21):
            xpath_head = '/html/body/table/tbody/tr[' + str(row) + ']/td['
            alist = []
            for i in range(2, 15):
                xpath = xpath_head + str(i) + ']'
                text = driver.find_element_by_xpath(xpath).text
                alist.append(text)
            info_table.loc[row_cnt] = alist
            row_cnt += 1
        info_table.to_csv('./data/test.csv', mode='a+', index=False, header=False, encoding = 'gb18030')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    date = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = r'D:\360极速浏览器下载\chromedriver_win32_88\chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

    for page in range(1, 210):
        url = 'http://q.10jqka.com.cn//index/index/board/all/field/zdf/order/desc/page/00000' + str(page) + '/ajax/1'
        driver.get(url)
        # time.sleep(1)
        parse(date, driver)
        print('finished', page)