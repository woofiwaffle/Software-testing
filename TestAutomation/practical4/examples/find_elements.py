from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# Путь к исполняемому файлу chromedriver.exe
chrome_driver_path = 'TestAutomation/practical4/chromedriver-win64/chromedriver.exe'

# Создание сервиса Chrome
chrome_service = ChromeService(executable_path=chrome_driver_path)

# Создание экземпляра браузера
browser = webdriver.Chrome(service=chrome_service)
URL = " https://test-selector-tree.netlify.app/"

try:
   # Открытие веб-страницы
   browser.get(URL)

   # Неявное ожидание для загрузки элементов страницы
   browser.implicitly_wait(10)

   # Элементы с тегом h1 (заголовки)
   elements_by_tag = browser.find_elements(By.TAG_NAME, "h1")
   print("Элементы с тегом h1:", len(elements_by_tag))

   # Элементы с именем birch-tree
   elements_by_name = browser.find_elements(By.NAME, "birch-tree")
   print("Элементы с именем birch-tree:", len(elements_by_name))

   # Элементы с классом imageContainer
   elements_by_class = browser.find_elements(By.CLASS_NAME, "imageContainer")
   print("Элементы с классом imageContainer:", len(elements_by_class))

   # Элементы с ID maple
   elements_by_id = browser.find_elements(By.ID, "maple")
   print("Элементы с ID maple:", len(elements_by_id))

   # Элементы с data-type="trees"
   elements_by_selector = browser.find_elements(By.CSS_SELECTOR,'[data-type="trees"]')
   print("Элементы с data-type trees:", len(elements_by_selector))

finally:
   # закрываем браузер после всех манипуляций
   browser.quit()