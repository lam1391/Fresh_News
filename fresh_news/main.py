import browser_actions
import sys

import modules.operations.validations as validation


# validation of input parameters
def val_ini_arg(argv):
    validation.validate_num_arg(argv)
    validation.validate_url(argv[1])
    validation.validate_phrase(argv[2])
    validation.validate_category(argv[3])
    validation.validate_months(argv[4])


def run(argv):
    # def run():
    try:
        # validation of input parameters
        val_ini_arg(argv)

        # parameter assignment
        site = argv[1]
        search_phrase = argv[2]
        category = argv[3]
        months = argv[4]

        # download all matched news and images related
        browser_actions.download_news(site, search_phrase, category, months)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    run(sys.argv)
