"""nova migração, usando postgresql

Revision ID: 6bec54f63c4c
Revises: 7d9abbe1bca3
Create Date: 2024-08-24 11:50:35.942935

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6bec54f63c4c'
down_revision: Union[str, None] = '7d9abbe1bca3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
