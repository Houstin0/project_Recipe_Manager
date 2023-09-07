"""create ingredients table

Revision ID: 1f891463d8e3
Revises: eefe808526ed
Create Date: 2023-09-07 08:54:05.922496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f891463d8e3'
down_revision = 'eefe808526ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.Column('meal_plan_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['meal_plan_id'], ['meal_plans.id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ingredients')
    # ### end Alembic commands ###