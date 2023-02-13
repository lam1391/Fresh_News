import re
import os
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


# get the description of the element
def get_description(item, locator, id, term):
    description = ""
    try:
        element = item.find_element(locator, id)

        if term == "id":
            description = element.id
        else:
            description = element.text

    except:
        description = ""

    return description


# Count the number of search phrases in the title and description
def count_phrases(title: str, description: str, phrase: str):
    return len(re.findall(phrase.upper(), title.upper() + description.upper()))


# Check if the title or description contains any amount of money
def has_money(title: str, description: str):
    try:
        match = re.search(
            r"\$\d+(,\d{3})*(\.\d{2})?|\d+ dollars? (USD|usd)", title + description
        )
    except Exception as e:
        print(e)

    return True if match else False


# generate date range from today to N months
def get_date_range(term=0):
    try:
        if term == 0:
            Number_months = 1
        else:
            Number_months = term

        today = datetime.now()
        final_date = today.strftime("%m/%d/%Y")
        past = today + relativedelta(months=-Number_months)
        ini_date = past.strftime("%m/%d/%Y")

        return ini_date, final_date
    except Exception as e:
        print(e)


# downloads all news in excel format
def download_excel(data, directory):
    try:
        # Convert the list of data to a Pandas DataFrame
        df = pd.DataFrame(
            data,
            columns=[
                "Title",
                "Date",
                "Description",
                "Has Money",
                "Count of Phrases",
                "Picture Name",
            ],
        )

        if directory != "":
            path = os.path.join(directory, "news.xlsx")
            # Write the data to an Excel file
            df.to_excel(path, index=False)

    except Exception as e:
        print(e)


# validate if the directory exist if not, create a new one
def create_directory():
    path = ""
    today = datetime.now()
    new_directory = today.strftime("%m-%d-%Y-%H-%M-%S")
    parent_dir = "./Downloads/"

    if not os.path.exists(parent_dir):
        dir = os.path.join("./", "Downloads")
        os.mkdir(dir)

    try:
        # Path
        path = os.path.join(parent_dir, new_directory)
        os.mkdir(path)
    except OSError as error:
        print(error)

    finally:
        return path
