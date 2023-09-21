import argparse

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from OCR import CaptchaBroker
from datetime import date,  timedelta
import re
import os
from argparse import ArgumentParser
import argparse

court = {'badminton':'2-13','tennis':'14-17','table tennis':'18-32'}

def main(args):

    account = args.account
    passwd = args.passwd
    file_dir = args.file_dir
    user_tesseract_cmd = args.OCR_path
    target = args.target

    print("Account : {}\nTarget : borrow {} court".format(account,target))
    driver = webdriver.Chrome()
    url = 'https://rent.pe.nchu.edu.tw/nchugym/login.php'
    driver.get(url)
    driver.maximize_window()
    window_before = driver.window_handles[0]
    select = Select(driver.find_element_by_name('s_logintype'))
    select.select_by_index(2)
    input_account = driver.find_element_by_id('tx_account')
    input_account.send_keys(account)

    capacheBroker = CaptchaBroker()

    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]°')
    while True:
        input_passwd = driver.find_element_by_id('tx_password')
        input_passwd.send_keys(passwd)

        driver.find_element_by_id('captchaImage').screenshot(os.path.join(file_dir,'web_screen.png'))
        capache = capacheBroker.decode(image_path=os.path.join(file_dir,'web_screen.png'),user_tesseract_cmd=user_tesseract_cmd)
        capache.replace(' ','')

        if (regex.search(capache) == None and len(capache) != 0):
            input_capache = driver.find_element_by_id('captchacode')
            input_capache.send_keys(capache)
            print("trying capache ...")
            try:
                alert = driver.switch_to_alert()
                alert.accept()
                continue
            except:
                break
        else:
            driver.find_element_by_id('captchaImage').click()
    driver.find_element_by_id('Stm0p0i1eTX').click()
    driver.find_element_by_id('Stm0p2i0eTX').click()

    # aTagsList [None, None, gym_info.php#, ...]
    aTagsList = driver.find_elements_by_css_selector('td a')

    court_num = court[target].split('-')

    flag = False
    for num in range(int(court_num[0]),int(court_num[1])+1):

        aTagsList[num].click()
        window_after = driver.window_handles[1+(num-int(court_num[0]))]
        driver.switch_to.window(window_after)

        inputs = driver.find_elements_by_tag_name('input')

        for input in inputs:
            try:
                if int(input.get_attribute('value')) >= 1700 and int(input.get_attribute('value')) <= 2130:
                    input.click()
                    driver.find_element_by_id('bu_save').click()
                    print("done!",input.get_attribute('id'),input.get_attribute('value'))
                    flag = True
                    break
            except:
                pass
        if flag:
            break
        driver.switch_to.window(window_before)
        driver.quit()


if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--file_dir', type=str, default='C:/.../NCHU-borrow-court', help='Path to directory')
    parser.add_argument('--account', type=str, default='410xxxxxxx', help='Enter NCHU account')
    parser.add_argument('--passwd', type=str, default='', help='Enter NCHU passwd')
    parser.add_argument('--OCR_path', type=str, default='C:/Program Files/.../tesseract.exe', help='Path to user tesseract cmd')
    parser.add_argument('--target', type=str, default='tennis', help='badminton, tennis, table tennis')
    args = parser.parse_args()
    main(args)