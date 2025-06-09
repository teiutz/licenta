"""Inserting food categories

Revision ID: 20b43c8ef611
Revises: fdbd6bda050e
Create Date: 2025-05-31 19:35:25.707339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20b43c8ef611'
down_revision: Union[str, None] = 'fdbd6bda050e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

category_table = sa.table(
    'base_food_categories',
    sa.column('name', sa.String())
)

def upgrade() -> None:
    op.bulk_insert(
        category_table, 
        [
            {"name": "Fruits"},
            {"name": "Cereal & Pasta"},
            {"name": "Fats & Oils"},
            {"name": "Meat"},
            {"name": "Fish"},
            {"name": "Dairy & Egg"},
            {"name": "Plant-Based"},
            {"name": "Vegetables"},
            {"name": "Legumes"},
            {"name": "Nuts & Seeds"},
            {"name": "Baked Goods"},
            {"name": "Snacks"},
            {"name": "Sweets"},
            {"name": "Sugary Drinks"},
            {"name": "Restaurant Foods"},
            {"name": "Fast Foods"},
            {"name": "Alcoholic Beverages"},
            {"name": "Spices, Herbs & Condiments"},
            {"name": "Other"}
        ]
    )


def downgrade() -> None:
    op.execute(
        """
    DELETE FROM food_categories WHERE name IN (
        'Fruits', 'Cereal & Pasta', 'Fats & Oils', 'Meat', 'Fish',
        'Dairy & Egg', 'Plant-Based', 'Vegetables', 'Legumes', 'Nuts & Seeds',
        'Baked Goods', 'Snacks', 'Sweets',  'Sugary Drinks', 'Restaurant Foods', 'Fast Foods',
        'Alcoholic Beverages', 'Spices, Herbs & Condiments', 'Other'
    )
    """
)
    
