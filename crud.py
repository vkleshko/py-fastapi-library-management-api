from typing import List

from sqlalchemy.orm import Session

import schemas
from db import models


def all_authors(db: Session) -> List[models.Author]:
    return db.query(models.Author).all()


def get_single_author_by_id(db: Session, author_id: int) -> models.Author:
    return (
        db.query(models.Author).filter(models.Author.id == author_id).first()
    )


def create_author(db: Session, author: schemas.AuthorCreate) -> models.Author:
    db_author = models.Author(
        name=author.name, bio=author.bio
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author
