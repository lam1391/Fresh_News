from RPA.Browser.Selenium import Selenium
import browser_actions


def run():
    try:
        site = "https://www.nytimes.com/"
        search_phrase = "markets"
        category = "Any"
        months = 1

        browser_actions.download_news(site, search_phrase, category, months)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    run()
