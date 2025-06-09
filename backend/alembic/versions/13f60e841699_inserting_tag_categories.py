"""Inserting tag categories

Revision ID: 13f60e841699
Revises: 6fa8afbdbe48
Create Date: 2025-06-01 23:36:38.603232

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13f60e841699'
down_revision: Union[str, None] = '6fa8afbdbe48'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

tag_category_table = sa.table(
    'tag_categories',
    sa.column('name', sa.String())
)

def upgrade() -> None:
     op.bulk_insert(
        tag_category_table, 
        [
            {"name": "Diet Type"},
            {"name": "Macronutrient Focus"}, #high-protein, "high-carb", "high-fat"
            {"name": "Calorie Density"}, #high-calorie, medium-calorie, low-calorie
            {"name": "Allergen"}, 
            {"name": "Flavor"}, 
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
    
