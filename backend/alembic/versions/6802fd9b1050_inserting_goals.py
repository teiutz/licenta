"""Inserting goals

Revision ID: 6802fd9b1050
Revises: cf5851d8ffe0
Create Date: 2025-06-01 15:02:11.691379

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6802fd9b1050'
down_revision: Union[str, None] = 'cf5851d8ffe0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

goal_table = sa.table(
    'goals',
    sa.column('name', sa.String())
)


def upgrade() -> None:
    op.bulk_insert(
        goal_table,
        [
            {"name": "Lose Weight"},
            {"name": "Maintain Weight"},
            {"name": "Put on Muscle Mass"},
            {"name": "Eat Healthier"},
            {"name": "Just Tracking"},
        ]
    )



def downgrade() -> None:
    op.execute(
        """
    DELETE FROM goals WHERE name IN (
        'Lose Weight', 'Maintain Weight', 'Put on Muscle Mass', 'Eat Healthier', 'Just Tracking'
    )
    """
    )
