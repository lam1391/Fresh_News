import urllib.request


def validate_num_arg(argv):
    # total arguments
    n = len(argv)
    if n > 5 or n < 5:
        raise Exception("number of arguments no valid")


def validate_url(url):
    try:
        urllib.request.urlopen(url)

    except:
        raise Exception("url No valid")


def validate_phrase(phrase):
    if not phrase:
        raise Exception("invalid phrase for search")


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


def validate_months(months):
    num_months = int(months)
    if num_months < 0:
        raise Exception("number of months invalid")
