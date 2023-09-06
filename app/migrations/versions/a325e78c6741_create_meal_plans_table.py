"""create meal_plans table

Revision ID: a325e78c6741
Revises: 1bd872b4bff9
Create Date: 2023-09-06 14:51:26.662996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a325e78c6741'
down_revision = '1bd872b4bff9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meal_plans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meal_plans')
    # ### end Alembic commands ###