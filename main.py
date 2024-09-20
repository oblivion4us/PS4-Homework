from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def search_wikipedia(query):
    # Инициализируем драйвер для Microsoft Edge
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    try:
        driver.get("https://www.wikipedia.org/")

        search_box = driver.find_element(By.NAME, "search")

        search_box.send_keys(query + Keys.RETURN)

        input("Нажмите Enter, чтобы завершить выполнение программы после закрытия браузера...")

    finally:
        driver.quit()


if __name__ == "__main__":
    user_query = input("Введите запрос для поиска на Википедии: ")
    search_wikipedia(user_query)