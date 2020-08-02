from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome(r'D:\360极速浏览器下载\chromedriver_win32\chromedriver.exe')
    driver.get('http://www.dianping.com/shop/130675258')
    driver.maximize_window()
    print(driver.page_source)