from selenium.webdriver.common.by import By
class PenguinsPage:
    URL = 'https://qa-test-selectors.netlify.app'
    VARIANT = 17
    HEADING = "Крутая челочка"
    TITLE_TEXT = "Златовласка"
    def __init__(self, browser):
        self.browser = browser
    def load(self):
        self.browser.get(self.URL)
    def find_variant(self):
        button = self.browser.find_element(By.CSS_SELECTOR, f'.variant__btn:nth-child({self.VARIANT})')

        # Нажатие на кнопку с вариантом
        button.click()
    def penguins_elements_count(self):
        # Поиск элементов с data-type="penguins"
        penguins_elements = self.browser.find_elements(By.XPATH, '//*[@data-type="penguins"]')
        return len(penguins_elements)
    def bang_elements_count(self):
        # Поиск элементов с id="bang"
        bang_elements = self.browser.find_elements(By.ID, 'bang')
        return len(bang_elements)
    def coolBang_elements_count(self):
        # Поиск элементов с class="coolBang"
        coolBang_elements = self.browser.find_elements(By.CLASS_NAME, 'coolBang')
        return len(coolBang_elements)
    def goldy_elements_count(self):
        # Поиск элементов с name="goldy-hair"
        goldy_elements = self.browser.find_elements(By.NAME, 'goldy-hair')
        return len(goldy_elements)
    def heading_images_count(self):
        # Поиск изображений с heading="Крутая челочка"
        heading_images = self.browser.find_elements(By.XPATH, f'//img[@heading="{self.HEADING}"]')
        return len(heading_images)
    def title_elements_count(self):
        # Поиск элементов с name="goldy-hair"
        title_elements = self.browser.find_elements(By.XPATH, f'//h1[text()="{self.TITLE_TEXT}"]')
        return len(title_elements)