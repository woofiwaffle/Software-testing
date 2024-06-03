import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import os

from TestAutomation.coursework.pages.web_page import YouTubePage


chrome_driver_path = os.path.abspath("C:/Users/User/PycharmProjects/software_testing/TestAutomation/"
                                     "coursework/chromedriver-win64/chromedriver.exe")

if not os.path.exists(chrome_driver_path):
    raise FileNotFoundError(f"Chromedriver not found at path: {chrome_driver_path}")


# Создание объекта сервиса с указанием пути до chromedriver
service = Service(executable_path=chrome_driver_path)

@pytest.fixture
def browser():
    # Инициализация драйвера Chrome с использованием созданного объекта сервиса
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_page(browser):
    PHRASE = 'Тестировщик'  # Фраза для тестов
    page = YouTubePage(browser)
    page.load()  # Загрузка страницы
    page.search(PHRASE)  # Поиск фразы
    # Проверки
    assert page.get_count_of_video_containers_with_phrase(PHRASE) > 0
    assert page.get_count_of_video_images() > 0
    assert page.get_count_of_play_buttons() > 0
    assert page.open_first_video(PHRASE) == 1