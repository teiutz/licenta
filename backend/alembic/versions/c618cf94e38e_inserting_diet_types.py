"""Inserting diet types

Revision ID: c618cf94e38e
Revises: 20b43c8ef611
Create Date: 2025-06-01 12:28:09.470754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c618cf94e38e'
down_revision: Union[str, None] = '20b43c8ef611'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

diet_table = sa.table(
    'diets',
    sa.column('name', sa.String())
)

def upgrade() -> None:
    op.bulk_insert(
    diet_table, 
    [
            {"name": "Vegetarian"},
            {"name": "Vegan"},
            {"name": "Keto"},
            {"name": "Pescetarian"},
            {"name": "None"},
        ])


def downgrade() -> None:
    op.execute(
        """
    DELETE FROM diets WHERE name IN (
        'Vegetarian', 'Vegan', 'Keto', 'Pescetarian', 'None'
    )
    """
    )
