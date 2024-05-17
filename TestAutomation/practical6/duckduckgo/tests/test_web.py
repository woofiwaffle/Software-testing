import pytest
from TestAutomation.practical6.duckduckgo.pages.result import DuckDuckGoResultPage
from TestAutomation.practical6.duckduckgo.pages.search import DuckDuckGoSearchPage
from selenium.webdriver import Chrome
@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
def test_basic_duckduckgo_search(browser):
    # Настройте данные для тест-кейса
    PHRASE = 'cheetos'

    # Поиск фразы
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    # Проверка, что результаты появились
    result_page = DuckDuckGoResultPage(browser)

    assert result_page.search_results_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE