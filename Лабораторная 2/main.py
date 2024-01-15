from typing import Optional


class Book:
    def __init__(self, ident: int, name: str, pages: int):
        self.ident = ident
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id={self.ident}, name={self.name}, pages={self.pages})'


class Library:
    def __init__(self, books: Optional[list[Book]] = None):
        self.books: list[Book] = books or []

    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        return self.books[-1].ident + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        for index, book in enumerate(self.books):
            if book.ident == book_id:
                return index
        raise ValueError(f"Книги с id {book_id} не существует")


