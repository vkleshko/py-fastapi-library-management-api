"""Migrations 0002

Revision ID: d0f93b73d5e8
Revises: 05a719843ead
Create Date: 2024-06-26 23:14:48.297769

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0f93b73d5e8'
down_revision: Union[str, None] = '05a719843ead'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
