from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
)

from db.database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    bio = Column(String(511), nulable=False)


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nulable=False)
    summary = Column(String(511), nulable=False)
    publication_date = Column(Date, nulable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

    author = relationship(Author, backref="books")
