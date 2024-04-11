from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService

# Путь к исполняемому файлу chromedriver.exe
chrome_driver_path = 'TestAutomation/practical4/chromedriver-win64/chromedriver.exe'

# Создание сервиса Chrome
chrome_service = ChromeService(executable_path=chrome_driver_path)

# Создание экземпляра браузера
driver = webdriver.Chrome(service=chrome_service)

try:
    # Открытие веб-сайта
    driver.get('https://habr.com/ru/feed/')

    # Ждем некоторое время (в данном случае, 5 секунд)
    time.sleep(5)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()