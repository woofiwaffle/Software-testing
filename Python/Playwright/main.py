# Тест проверки заполнения формы
#
# открыть https://demo.playwright.dev/todomvc/#/
# проверить что открыт корректный url
# найти поле ввода задачи
# проверить что оно пустое
# ввести задачу номер один
# ввести задачу номер два
# проверить что количество задач в списке равно двум
# отметить одну задачу выполненной
# проверить что эта задача отмечена выполненной

from playwright.sync_api import expect

def test_todo(page):
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
    input_field = page.get_by_placeholder('What needs to be done?')
    expect(input_field).to_be_empty()
    input_field.fill("Закончить курс по playwright")
    input_field.press('Enter')
    input_field.fill("Добавить в резюме, что умею автоматизировать")
    input_field.press('Enter')
    todo_item = page.get_by_test_id('todo-item')
    expect(todo_item).to_have_count(2)


# from playwright.sync_api import Playwright, sync_playwright, expect
#
#
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://demo.playwright.dev/todomvc/#/")
#     page.get_by_placeholder("What needs to be done?").click()
#     page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
#     page.get_by_placeholder("What needs to be done?").press("Enter")
#     page.get_by_role("checkbox", name="ToggleTodo").check()
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)