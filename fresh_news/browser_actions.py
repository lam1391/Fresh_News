from RPA.Browser.Selenium import Selenium
from selenium.webdriver.common.by import By

import os
import time

import modules.news.news as news
import modules.operations.operations as operations


# Step 1: Open a new instance of a web browser and Navigate to the desired URL
def open_the_website(browser_lib, url):
    browser_lib.open_available_browser(url)


# Step 2: Locate the search field and enter the search phrase
def search_for(browser_lib, term):
    search_field = "css:input"
    browser_lib.click_button("css:button.css-tkwi90.e1iflr850")
    browser_lib.input_text(search_field, term)
    browser_lib.press_keys(search_field, "ENTER")


# Step 3: Locate the news category filter and select the desired option
def select_category(browser_lib, term):
    try:
        browser_lib.click_button("css:button.css-4d08fs")
        elements = browser_lib.find_elements(
            "xpath://div[@class='css-tw4vmx']//input[@type='checkbox']"
        )
        for element in elements:
            name_element = element.accessible_name
            if name_element.find(term) >= 0:
                element.click()
                break
    except:
        print("no section found")


# Step 4: Locate the date filter and select the latest news option
def filter_dates(browser_lib, term):
    browser_lib.click_button(
        "xpath://div[@class='css-wsup08']//div//div[@class='css-trpop8']//button"
    )
    browser_lib.click_button(
        "xpath://div[@class='css-91q1y8']//ul[@class='css-vh8n2n']//li[@class='css-guqk22']//button[@value='Specific Dates']"
    )
    startDate, endDate = operations.get_date_range(term)
    browser_lib.input_text(
        "xpath://div[@class='css-79elbk']//label[@for='startDate']//input[@id='startDate']",
        startDate,
    )
    browser_lib.input_text(
        "xpath://div[@class='css-79elbk']//label[@for='endDate']//input[@id='endDate']",
        endDate,
    )
    browser_lib.press_keys(
        "xpath://div[@class='css-79elbk']//label[@for='endDate']//input[@id='endDate']",
        "ENTER",
    )


# step 5 Order the result by newest
def order_by_newest(browser_lib):
    browser_lib.select_from_list_by_value(
        "xpath://div[@class='css-hrdzfd']//div[@class='css-1e67xgz']//select[@class='css-v7it2b']",
        "newest",
    )


# Step 6 : Display all avaible news
def display_all_news(browser_lib):
    while True:
        try:
            browser_lib.click_button(
                "xpath://div[@class='css-1t62hi8']//div[@class='css-vsuiox']//button"
            )
            time.sleep(0.5)
        except:
            break


# Step 7 get the list of news
def get_news_items(browser_lib, search_phrase):
    news_items = browser_lib.find_elements(
        "xpath://div[@class='css-46b038']//ol//li[@class='css-1l4w6pd']"
    )
    if len(news_items) == 0:
        raise Exception(f"Showing 0 results for : {search_phrase} Excel no generated")

    return news_items


# Step 8: Find the news items and extract the title, date, and descriptions
def find_info_news(news_items, phrase):
    list_news = []

    for item in news_items:
        title = operations.get_description(item, By.TAG_NAME, "h4", "desc")

        description = operations.get_description(
            item, By.CLASS_NAME, "css-16nhkrn", "desc"
        )

        date = operations.get_description(item, By.CLASS_NAME, "css-17ubb9w", "desc")
        picture_file_name = operations.get_description(item, By.TAG_NAME, "img", "id")
        count_phrases = operations.count_phrases(title, description, phrase)
        has_money = operations.has_money(title, description)

        news_info = news.NewsInfo(
            title,
            date,
            description,
            picture_file_name,
            count_phrases,
            has_money,
        )

        list_news.append(news_info)

    return list_news


# Step 9: Store the extracted data in an Excel file
def generate_excel(list_news, directory):
    # Initialize a list to store the data
    data = []

    for new in list_news:
        # Append the data to the list
        data.append(
            [
                new.title,
                new.date,
                new.description,
                new.has_money,
                new.count_of_phrases,
                new.picture_name,
            ]
        )

    # download the news in excel format
    operations.download_excel(data, directory)


# Step 10: Locate the news picture and download it
def download_img(news_items, directory):
    for item in news_items:
        picture_file_name = operations.get_description(item, By.TAG_NAME, "img", "id")

        if picture_file_name != "":
            picture = item.find_element(By.TAG_NAME, "img")
            path = os.path.join(directory, f"{picture_file_name}.png")
            picture.screenshot(path)


# main process
def download_news(site: str, search_phrase: str, category: str, months: int):
    browser_lib = Selenium()

    list_news = []
    try:
        # Step 1: Open a new instance of a web browser and Navigate to the desired URL
        open_the_website(browser_lib, site)
        # Step 2: Locate the search field and enter the search phrase
        search_for(browser_lib, search_phrase)
        # Step 3: Locate the news category filter and select the desired option
        select_category(browser_lib, category)
        # Step 4: Locate the date filter and select the latest news option
        filter_dates(browser_lib, months)
        # Step 5 Order by newest
        order_by_newest(browser_lib)
        # Step 6 : Display all avaible news
        display_all_news(browser_lib)
        # Step 7 get the list of news
        news_items = get_news_items(browser_lib, search_phrase)
        # Step 8 : Get all information news
        list_news = find_info_news(news_items, search_phrase)

        if list_news != []:
            # create direcroty
            directory = "output/"
            # Step 9: Store the extracted data in an Excel file
            generate_excel(list_news, directory)
            # Step 10: Locate the news picture and download it
            download_img(news_items, directory)

            print("process completed successfully")

    except Exception as e:
        print(e)

    finally:
        browser_lib.close_all_browsers()
