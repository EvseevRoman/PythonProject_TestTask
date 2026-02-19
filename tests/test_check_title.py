import pytest
from playwright.sync_api import sync_playwright

# Список браузеров для тестирования
BROWSERS = ["chromium", "firefox"]


@pytest.mark.parametrize("browser_type", BROWSERS)
def test_playwright_title(browser_type):
    """
    Тест проверяет заголовок страницы playwright.dev
    Запускается в двух браузерах: Chromium и Firefox
    """
    with sync_playwright() as p:
        # Запускаем нужный браузер
        print(f"\n🚀 Запускаем тест в {browser_type}")

        if browser_type == "chromium":
            browser = p.chromium.launch(headless=False)  # headless=False чтобы видеть браузер
        else:  # firefox
            browser = p.firefox.launch(headless=False)

        # Создаем новую страницу
        page = browser.new_page()

        # Переходим на сайт
        page.goto("https://playwright.dev/")

        # Получаем заголовок
        actual_title = page.title()

        # Ожидаемый заголовок
        expected_title = "Fast and reliable end-to-end testing for modern web apps | Playwright"

        # Проверяем
        print(f"Полученный заголовок: {actual_title}")
        assert actual_title == expected_title, \
            f"❌ {browser_type}: заголовок не совпадает!\n" \
            f"   Ожидалось: {expected_title}\n" \
            f"   Получено: {actual_title}"

        print(f"✅ {browser_type}: тест пройден успешно!")

        # Закрываем браузер
        browser.close()


# Этот блок позволяет запускать тест без pytest (для отладки)
if __name__ == "__main__":
    print("=" * 50)
    print("Запуск тестов вручную")
    print("=" * 50)
    for browser in BROWSERS:
        test_playwright_title(browser)
    print("=" * 50)
    print("✅ Все тесты завершены!")