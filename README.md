# Fresh news

this project is about automate the process of extracting data from the news site www.nytimes.com

When run, the robot will::
  1. Open the site by following the link
  2. Enter a phrase in the search field
  3. On the result page, apply the following filters:
    - select a news category or section
    - choose the latest news
  4. Get the values: title, date, and description.
  5. Store in an excel file:
    - title
    - date
    - description (if available)
    - picture filename
    - count of search phrases in the title and description
    - True or False, depending on whether the title or description contains any amount of money
        
        > Possible formats: $11.1 | $111,111.11 | 11 dollars | 11 USD
6. Download the news picture and specify the file name in the excel file
7. Follow the steps 4-6 for all news that fall within the required time period
## Run Locally

Clone the project

```bash
  git clone https://github.com/lam1391/Fresh_News.git
```

Go to the project directory

```bash
  cd Fresh_News
```

Install dependencies

```bash
  pip install -r requirements.txt
```

run the robot

```bash
  python tasks.py
```

