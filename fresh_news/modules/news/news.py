class NewsInfo:
    def __init__(
        self,
        title: str,
        date: str,
        description: str,
        picture_name: str,
        count_of_phrases: int,
        has_money: bool,
    ) -> None:
        self.title = title
        self.date = date
        self.description = description
        self.picture_name = picture_name
        self.count_of_phrases = count_of_phrases
        self.has_money = has_money
