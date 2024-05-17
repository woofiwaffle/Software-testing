import pytest
from TestAutomation.practical6.penguinsPage.pages.web import PenguinsPage
from selenium.webdriver import Chrome

# Реализация фикстуры
@pytest.fixture
def browser():
     driver = Chrome()
     driver.implicitly_wait(30)
     yield driver
     driver.quit()

#Функция по проверке осуществления перехода на страницу с вариантом
def test_penguin_page(browser):
    penguin_page = PenguinsPage(browser)
    penguin_page.load()
    penguin_page.find_variant()

    # Реализация проверок с помощью PyTest
    assert penguin_page.penguins_elements_count() > 0
    assert penguin_page.bang_elements_count() > 0
    assert penguin_page.coolBang_elements_count() > 0
    assert penguin_page.goldy_elements_count() > 0
    assert penguin_page.heading_images_count() > 0
    assert penguin_page.title_elements_count() > 0