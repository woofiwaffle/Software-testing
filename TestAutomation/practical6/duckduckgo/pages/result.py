from selenium.webdriver.common.by import By
class DuckDuckGoResultPage:
    SEARCH_RESULTS = (By.CSS_SELECTOR, "li[data-layout='organic']")
    SEARCH_INPUT = (By.ID, 'search_form_input')
    @classmethod
    def PHRASE_RESULTS(cls, phrase):
        xpath = f"//li[@data-layout='organic']//a[contains(@href, '{phrase}')]"
        return (By.XPATH, xpath)
    def __init__(self, browser):
        self.browser = browser
    def search_results_count(self):
        search_results = self.browser.find_elements(*self.SEARCH_RESULTS)
        return len(search_results)
    def phrase_result_count(self, phrase):
        phrase_results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
        return len(phrase_results)
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')