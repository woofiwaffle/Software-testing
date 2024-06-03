from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import time

# Путь к исполняемому файлу chromedriver.exe
chrome_driver_path = ("C:/Users/User/PycharmProjects/software_testing/TestAutomation/coursework/chromedriver-win64/chromedriver.exe")

# Создание сервиса Chrome
chrome_service = ChromeService(executable_path=chrome_driver_path)

# Создание экземпляра браузера
driver = webdriver.Chrome(service=chrome_service)

try:
    # Открытие веб-сайта YouTube
    driver.get('https://www.youtube.com/')

    # Нахождение элемента поля поиска
    search_box = driver.find_element(By.CSS_SELECTOR, 'input#search')

    # Ввод запроса в поле поиска
    search_query = 'Python programming tutorial'
    search_box.send_keys(search_query)
    time.sleep(4)

    # Отправка формы поиска
    search_box.send_keys(Keys.RETURN)

    # Ожидание загрузки результатов поиска
    time.sleep(8)  # Подождем несколько секунд для загрузки результатов

    # Проверка релевантности результатов поиска
    results = driver.find_elements(By.CSS_SELECTOR, 'ytd-video-renderer')  # Находим все элементы результатов поиска

    # Вывод количества найденных результатов
    print(f'Найдено результатов: {len(results)}')

    # Проверка первых нескольких результатов на релевантность
    for i, result in enumerate(results[:5]):
        title = result.find_element(By.CSS_SELECTOR, 'h3.title-and-badge.style-scope.ytd-video-renderer').text
        print(f'Результат {i + 1}: {title}')
        assert 'Python' in title or 'programming' in title.lower(), f'Нерелевантный результат: {title}'

finally:
    # Закрытие браузера
    driver.quit()
