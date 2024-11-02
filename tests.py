from playwright.sync_api import sync_playwright


def test_registration_negative():
    """
    Функция проверки негативных сценариев на странице регистрации.
    Тест включает следующие сценарии:
    1. Пустое поле Email
    2. Некорректный формат Email
    3. Пустое поле Password
    4. Слишком короткий Password
    """

    with sync_playwright() as p:
        # Запуск браузера
        browser = p.chromium.launch()
        page = browser.new_page()

        # Переход на страницу регистрации
        page.goto("https://koshelek.ru/registration")

        # Негативный тест: пустое поле Email
        page.fill("input[name='email']", "")
        page.fill("input[name='password']", "validPassword123")
        page.click("button[type='submit']")
        assert page.is_visible("text=Email is required"), "Ошибка: Email не был указан."

        # Негативный тест: некорректный Email
        page.fill("input[name='email']", "invalidEmail")
        page.fill("input[name='password']", "validPassword123")
        page.click("button[type='submit']")
        assert page.is_visible("text=Invalid email format"), "Ошибка: Неверный формат адреса электронной почты."

        # Негативный тест: пустое поле Password
        page.fill("input[name='email']", "test@example.com")
        page.fill("input[name='password']", "")
        page.click("button[type='submit']")
        assert page.is_visible("text=Password is required"), "Ошибка: Пароль не был указан."

        # Негативный тест: слишком короткий Password
        page.fill("input[name='email']", "test@example.com")
        page.fill("input[name='password']", "short")
        page.click("button[type='submit']")
        assert page.is_visible("text=Password must be at least 8 characters"), "Ошибка: Пароль слишком короткий."

        # Закрытие браузера
        browser.close()


if __name__ == "__main__":
    test_registration_negative()