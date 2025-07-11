# Book Class Definition

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"'{self.title}' by {self.author}, published in {self.year}."

    def is_classic(self):
        return self.year < 2000

    def __del__(self):
        # print(f"Book '{self.title}' by {self.author} is being deleted.")
        print(f"Deleting {self.title}")

    def __str__(self):
       # return f"{self.title} by {self.author} ({self.year})"
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # return f"Book('{self.title}', '{self.author}', {self.year})"
        return f"Book('{self.title}', '{self.author}', {self.year})"
