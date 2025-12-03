import allure


class BasePage:
    def __init__(self, page):
        self.page = page

    @allure.step("Открыть URL: {url}")
    def open(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        with allure.step(f"Клик по элементу: {locator}"):
            self.page.locator(locator).click()

    def get_text(self, locator: str) -> str:
        with allure.step(f"Получить текст элемента: {locator}"):
            return self.page.locator(locator).inner_text()
