import json
from pathlib import Path
import logging
from .book import Book

logging.basicConfig(filename="library.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class LibraryInventory:
    def __init__(self, file_path="catalog.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            if not self.file_path.exists():
                self.save_books()
                return

            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.books = [Book(**entry) for entry in data]

        except Exception as e:
            logging.error("Error loading file: %s", e)
            self.books = []
            self.save_books()

    def save_books(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)
        except Exception as e:
            logging.error("Error saving file: %s", e)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return self.books