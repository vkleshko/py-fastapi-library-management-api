from sqlalchemy import Column, Integer, String

from db.database import Base


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    bio = Column(String(511), nulable=False)
