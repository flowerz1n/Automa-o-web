
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")
sleep(1)
barra_busca = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/form/input[1]")
barra_busca.send_keys("standard_user")
sleep(1) 
barra_busca = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/form/input[2]")
barra_busca.send_keys("secret_sauce")
sleep(1)
barra_busca.send_keys(Keys.ENTER)
sleep(1)
botao = driver.find_element(By.XPATH, '//button[@class="btn_primary btn_inventory"]')
botao.click()
sleep(1)
botao = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/a')
botao.click()
sleep(1)
input()


