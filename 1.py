# -*- encoding: utf-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class HomePage:
    timeout = 10
    loginVar="79225593111"
    passwordVar="**************"
    passwordField='//*[@id="passp-field-passwd"]'
    mailSearch="girok66@mail.ru"
    sendTo="kobalt18@gmail.com"
    desiredCapabilities = {"browserName": "chrome"}
    driver = webdriver.Remote(desired_capabilities=desiredCapabilities)

    def enter_in_mail(self):
        driver = self.driver
        driver.get("http://www.yandex.ru")
        driver.find_element_by_class_name("desk-notif-card__login-enter-expanded").click()
    def login_in_mail(self):
        driver = self.driver
        driver.find_element_by_name("login").send_keys(self.loginVar)
        t = driver.find_element_by_name("passwd")
        if t.is_displayed():
            t.send_keys(self.passwordVar)
            driver.find_element_by_class_name("passport-Button").click()
        else:
            driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div/div[1]/form/div[3]/button[1]').click()
            WebDriverWait(driver, self.timeout).until(EC.presence_of_element_located((By.XPATH,(self.passwordField))))
            driver.find_element_by_xpath(self.passwordField).send_keys(self.passwordVar)
            driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div/div/form/div[2]/button').click()
    def search_mail(self):
        driver = self.driver
        WebDriverWait(driver, self.timeout).until(EC.presence_of_element_located((By.XPATH,('/html/body/div[3]/div[5]/div/div[2]/div[3]/div[2]/div/div/span/input'))))
        driver.find_element_by_class_name('textinput__control').send_keys(self.mailSearch)
        driver.find_element_by_class_name('textinput__control').send_keys(u'\ue007')
        WebDriverWait(driver, self.timeout).until(EC.presence_of_element_located((By.XPATH,('/html/body/div[3]/div[5]/div/div[3]/div[3]/div[2]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/span/span'))))
        printvar=driver.find_element_by_xpath('/html/body/div[3]/div[5]/div/div[3]/div[3]/div[2]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/span/span').text
        return str(printvar)
    def write_send_mail(self, strprintvar):
        driver = self.driver
        driver.find_element_by_class_name('mail-ComposeButton').click()
        WebDriverWait(driver, self.timeout).until(EC.presence_of_element_located((By.XPATH,('/html/body/div[3]/div[5]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[1]/div/div[1]/label/div[3]/div'))))
        driver.find_element_by_xpath('/html/body/div[3]/div[5]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[1]/div/div[1]/label/div[3]/div').send_keys(self.sendTo)
        driver.find_element_by_xpath('/html/body/div[3]/div[5]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[1]/div/label/div[3]/input').send_keys("Тестовое задание. Колиниченко")
        driver.find_element_by_class_name('cke_wysiwyg_div').send_keys("Найдено писем:" + strprintvar)
    def exit(self):
        driver = self.driver
        driver.quit();

class RunTest:
    HomePage().enter_in_mail()
    HomePage().login_in_mail()
    strPrint=HomePage().search_mail()
    HomePage().write_send_mail(strPrint)
    HomePage().exit()
