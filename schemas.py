from typing import List
from datetime import date
from pydantic import BaseModel

from db.models import Book


class AuthorBase(BaseModel):
    name: str
    bio: str
    books: List[Book] | None


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    summary: str
    publication: date


class BookCreate(BookBase):
    author_id: int


class Book(BookBase):
    id: int
    author: Author

    class Config:
        orm_mode = True
