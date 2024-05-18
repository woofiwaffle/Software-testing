from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class YouTubePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.youtube.com"  # URL страницы YouTube
        self.search_box_selector = 'input#search'  # CSS-селектор для поля поиска
        self.video_container_selector = 'ytd-video-renderer'  # CSS-селектор для контейнера видео
        self.video_title_selector = 'h3.title-and-badge.style-scope.ytd-video-renderer'  # для заголовка видео

    def load(self):
        self.driver.get(self.url)

    def search(self, phrase):
        search_box = self.driver.find_element(By.CSS_SELECTOR, self.search_box_selector)
        search_box.send_keys(phrase)  # Вводим фразу в поле поиска
        search_box.send_keys(Keys.RETURN)

    def get_count_of_video_containers_with_phrase(self, phrase):
        time.sleep(5)
        # Находим все контейнеры с видео
        video_containers = self.driver.find_elements(By.CSS_SELECTOR, self.video_container_selector)
        count = 0
        for container in video_containers:
            # Получаем текст заголовка видео
            title = container.find_element(By.CSS_SELECTOR, self.video_title_selector).text
            if phrase.lower() in title.lower():  # Проверяем, содержится ли искомая фраза в заголовке
                count += 1
        return count  # Возвращаем количество видео, содержащих искомую фразу в заголовке

    def get_count_of_video_images(self):
        time.sleep(3)
        video_images = self.driver.find_elements(By.CSS_SELECTOR, f'{self.video_container_selector} img')
        return len(video_images)  # Возвращаем количество найденных изображений

    def get_count_of_play_buttons(self):
        time.sleep(3)
        play_buttons = self.driver.find_elements(
            By.CSS_SELECTOR,
            f'{self.video_container_selector} .yt-simple-endpoint.style-scope.ytd-thumbnail'
        )  # Находим все кнопки воспроизведения
        return len(play_buttons)  # Возвращаем количество найденных кнопок

    def open_first_video(self, phrase):
        time.sleep(3)
        video_containers = self.driver.find_elements(By.CSS_SELECTOR, self.video_container_selector)
        for container in video_containers:
            title = container.find_element(By.CSS_SELECTOR, self.video_title_selector).text
            if phrase.lower() in title.lower():  # Проверяем, содержится ли искомая фраза в заголовке
                container.click()  # Кликаем на первое найденное видео
                return 1
        return 0