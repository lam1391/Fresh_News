import urllib.request


# validate the numer of input arguments
def validate_num_arg(argv):
    # total arguments
    n = len(argv)
    if n > 5 or n < 5:
        raise Exception("number of arguments no valid")


# validate if the URL is correct
def validate_url(url):
    try:
        urllib.request.urlopen(url)
    except:
        raise Exception("url No valid")


# validate if the pharase is not empty
def validate_phrase(phrase):
    if not phrase:
        raise Exception("invalid phrase for search")


# validate if the category is valid
def validate_category(phrase):
    categories = (
        "Any",
        "Arts",
        "Automobiles",
        "Business",
        "Magazine",
        "New York",
        "Sports",
        "Technology",
        "Wirecutter",
        "World",
        "Opinion",
        "Travel",
        "Week In Review",
        "U.S.",
        "Real Estate",
        "Style",
        "Magazine",
        "Movies",
    )

    if phrase not in categories:
        raise Exception("invalid category")


# validate if the number of months is valid
def validate_months(months):
    if months < 0:
        raise Exception("number of months invalid")
