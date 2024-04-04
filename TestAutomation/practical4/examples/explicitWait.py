import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Явное ожидание для открытия браузера
time.sleep(5)

driver.get("https://test-selector-tree.netlify.app/")

# Явное ожидание для загрузки элементов страницы
time.sleep(6)
driver.find_element(By.ID, "birch")
print('Изображение найдено')

# Явное ожидание перед закрытием браузера
time.sleep(7)
driver.quit()