# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome('/Users/Kobalt/Downloads/chromedriver')  # Optional argument, if not specified will search path.
driver.get("http://www.yandex.ru")
driver.find_element_by_class_name("desk-notif-card__login-enter-expanded").click()
driver.find_element_by_name("login").send_keys("79225593111")

timeout=10

t = driver.find_element_by_name("passwd")
if t.is_displayed():
    t.send_keys("password")
    driver.find_element_by_class_name("passport-Button").click()
else:
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div/div[1]/form/div[3]/button[1]').click()
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,('//*[@id="passp-field-passwd"]'))))
    driver.find_element_by_xpath('//*[@id="passp-field-passwd"]').send_keys("password")
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div/div/form/div[2]/button').click()

WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,('//*[@id="nb-1"]/body/div[2]/div[5]/div/div[2]/div[3]/div[2]/div/div/span/input'))))
driver.find_element_by_class_name('textinput__control').send_keys("girok66@mail.ru")
driver.find_element_by_class_name('textinput__control').send_keys(u'\ue007')

WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,('//*[@id="nb-1"]/body/div[2]/div[5]/div/div[3]/div[3]/div[2]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/span/span'))))

printvar=driver.find_element_by_xpath('//*[@id="nb-1"]/body/div[2]/div[5]/div/div[3]/div[3]/div[2]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/span/span').text
driver.find_element_by_xpath('//*[@id="nb-1"]/body/div[2]/div[5]/div/div[2]/div[2]/div/div/a').click()

WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,('//*[@id="nb-1"]/body/div[2]/div[5]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[1]/div/div[1]/label/div[3]/div'))))
driver.find_element_by_xpath('//*[@id="nb-1"]/body/div[2]/div[5]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[1]/div/div[1]/label/div[3]/div').send_keys("kobalt18@gmail.com")

driver.find_element_by_xpath('//*[@id="nb-1"]/body/div[2]/div[5]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[1]/div/label/div[3]/input').send_keys(u"Тестовое задание. Колиниченко")



driver.find_element_by_class_name('cke_wysiwyg_div').send_keys("Найдено писем:" + printvar)

driver.find_element_by_xpath('//*[@id="nb-18"]').click()


