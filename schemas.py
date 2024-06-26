from typing import List

from pydantic import BaseModel

from db.models import Book


class AuthorBase(BaseModel):
    name: str
    bio: str
    books: List[Book] | None


class AuthorCreate(BaseModel):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True
