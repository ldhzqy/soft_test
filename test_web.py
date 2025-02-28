import time
from  webdriver_helper import get_webdriver
def test_shop():

    driver = get_webdriver()
    driver.get('https://www.bilibili.com/')
    driver.find_element('xpath','//*[@id="nav-searchform"]/div[1]/input').send_keys('软件测试')
    driver.find_element('xpath','//*[@id="nav-searchform"]/div[2]').click()

    time.sleep(2)

    driver.quit()
