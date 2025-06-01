"""Inserting allergy types

Revision ID: cf5851d8ffe0
Revises: c618cf94e38e
Create Date: 2025-06-01 12:34:56.366699

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime, timezone

# revision identifiers, used by Alembic.
revision: str = 'cf5851d8ffe0'
down_revision: Union[str, None] = 'c618cf94e38e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

allergy_table = sa.table(
    'allergies',
    sa.column('name', sa.String()),
    sa.column('created_at', sa.DateTime()), 
    sa.column('updated_at', sa.DateTime())
)


def upgrade() -> None:
    time_stamp_now = datetime.now(timezone.utc)
    op.bulk_insert(
    allergy_table, 
    [
        {'name': 'Milk', 'created_at': time_stamp_now, 'updated_at': time_stamp_now}, 
        {'name': 'Eggs', 'created_at': time_stamp_now, 'updated_at': time_stamp_now},
        {'name': 'Nuts', 'created_at': time_stamp_now, 'updated_at': time_stamp_now},
        {'name': 'Peanuts', 'created_at': time_stamp_now, 'updated_at': time_stamp_now},
        {'name': 'Shellfish', 'created_at': time_stamp_now, 'updated_at': time_stamp_now},
        {'name': 'Wheat', 'created_at': time_stamp_now, 'updated_at': time_stamp_now},
        {'name': 'Soy', 'created_at': time_stamp_now, 'updated_at': time_stamp_now},
        {'name': 'Fish', 'created_at': time_stamp_now, 'updated_at': time_stamp_now},
        {'name': 'Sesame', 'created_at': time_stamp_now, 'updated_at': time_stamp_now},
        {'name': 'Peach', 'created_at': time_stamp_now, 'updated_at': time_stamp_now},
        {'name': 'Banana', 'created_at': time_stamp_now, 'updated_at': time_stamp_now},
        {'name': 'Strawberry', 'created_at': time_stamp_now, 'updated_at': time_stamp_now},
        {'name': 'Garlic', 'created_at': time_stamp_now, 'updated_at': time_stamp_now},
        {'name': 'Celery', 'created_at': time_stamp_now, 'updated_at': time_stamp_now},
        {'name': 'Avocado', 'created_at': time_stamp_now, 'updated_at': time_stamp_now},
        ])


def downgrade() -> None:
    op.execute(
        """
    DELETE FROM allergies WHERE name IN (
        'Milk', 'Eggs', 'Nuts', 'Peanuts', 'Shellfish',
        'Wheat', 'Soy', 'Fish', 'Sesame', 'Peach',
        'Banana', 'Garlic', 'Celery', 'Avocado', 'Strawberry''
    )
    """
    )
    pass
