"""Inserting measurement blueprints

Revision ID: 6fa8afbdbe48
Revises: 6802fd9b1050
Create Date: 2025-06-01 16:17:19.907233

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime, timezone


# revision identifiers, used by Alembic.
revision: str = '6fa8afbdbe48'
down_revision: Union[str, None] = '6802fd9b1050'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

blueprints_table = sa.table(
    'measurement_blueprints',
    sa.column('name', sa.String()),
    sa.column('unit', sa.String()),
    sa.column('created_at', sa.DateTime())
)

def upgrade() -> None:
    time_stamp_now = datetime.now(timezone.utc)
    op.bulk_insert(
    blueprints_table, 
    [
            {"name": "weight", "unit" : "kg", "created_at": time_stamp_now},
            {"name": "height", "unit" : "cm", "created_at": time_stamp_now},
            {"name": "fat", "unit" : "%", "created_at": time_stamp_now},
            {"name": "shoulders", "unit" : "cm", "created_at": time_stamp_now},
            {"name": "chest", "unit" : "cm", "created_at": time_stamp_now},
            {"name": "waist", "unit" : "cm", "created_at": time_stamp_now},
            {"name": "upper arm (general)", "unit" : "cm", "created_at": time_stamp_now},
            {"name": "right upper arm", "unit" : "cm", "created_at": time_stamp_now},
            {"name": "left upper arm", "unit" : "cm", "created_at": time_stamp_now},
            {"name": "upper leg (general)", "unit" : "cm", "created_at": time_stamp_now},
            {"name": "right upper leg", "unit" : "cm", "created_at": time_stamp_now},
            {"name": "left upper leg", "unit" : "cm", "created_at": time_stamp_now},
            {"name": "calf (general)", "unit" : "cm", "created_at": time_stamp_now},
            {"name": "right calf", "unit" : "cm", "created_at": time_stamp_now},
            {"name": "left calf", "unit" : "cm", "created_at": time_stamp_now},
            
        ])

def downgrade() -> None:
     op.execute(
        """
    DELETE FROM diets WHERE name IN (
        'weight', 'height', 'fat', 'shoulders', 'chest',
        'waist', 'upper arm (general)', 'right upper arm',
        'left upper arm', 'upper leg (general)', 'right upper leg',
        'left upper leg', 'calf (general)', 'right calf', 'left calf'
    )
    """
    )

