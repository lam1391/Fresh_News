import browser_actions
import os

import modules.operations.validations as validation


# get and validation of input parameters
def get_input_variables():
    # Set an environment variable for run locally
    # os.environ["URL"] = "https://www.nytimes.com/"
    # os.environ["SEARCH_PHRASE"] = "Honduras"
    # os.environ["NEWS_CATEGORY"] = "Any"
    # os.environ["NUMBER_OF_MONTHS"] = "12"

    # Get an environment variable
    site = os.getenv("URL")
    search_phrase = os.getenv("SEARCH_PHRASE")
    category = os.getenv("NEWS_CATEGORY")
    months = os.getenv("NUMBER_OF_MONTHS")
    months_num = int(months)

    return site, search_phrase, category, months_num


def validations(site, search_phrase, category, months):
    validation.validate_url(site)
    validation.validate_phrase(search_phrase)
    validation.validate_category(category)
    validation.validate_months(months)


def run():
    # def run():
    try:
        # get input parameters
        site, search_phrase, category, months = get_input_variables()

        # validations
        validations(site, search_phrase, category, months)

        # download all matched news and images related
        browser_actions.download_news(site, search_phrase, category, months)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    run()
