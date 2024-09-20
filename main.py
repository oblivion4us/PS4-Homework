from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


def search_wikipedia(query):
    # Инициализируем драйвер для Microsoft Edge
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    try:
        driver.get("https://www.wikipedia.org/")
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys(query + Keys.RETURN)

        # Даем странице загрузиться
        time.sleep(2)

        while True:
            print("Выберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")

            choice = input("Введите номер действия: ")

            if choice == '1':
                # Листаем параграфы текущей статьи
                paragraphs = driver.find_elements(By.TAG_NAME, "p")
                for i, paragraph in enumerate(paragraphs):
                    print(f"Параграф {i + 1}: {paragraph.text}")

            elif choice == '2':
                # Получаем ссылки на связанные статьи
                links = driver.find_elements(By.XPATH, "//a[contains(@href, '/wiki/')]")
                for i, link in enumerate(links[:10]):  # Ограничиваем до 10 ссылок для наглядности
                    print(f"{i + 1}. {link.text} ({link.get_attribute('href')})")

                link_choice = input("Введите номер ссылки для перехода или 'назад' для возврата: ")
                if link_choice.isdigit() and 1 <= int(link_choice) <= len(links):
                    selected_link = links[int(link_choice) - 1]
                    driver.get(selected_link.get_attribute('href'))
                    time.sleep(2)
                elif link_choice.lower() == 'назад':
                    continue
                else:
                    print("Неверный выбор, попробуйте снова.")

            elif choice == '3':
                print("Выход из программы.")
                break

            else:
                print("Неверный выбор, попробуйте снова.")

    finally:
        driver.quit()

if __name__ == "__main__":
    user_query = input("Введите запрос для поиска на Википедии: ")
    search_wikipedia(user_query)