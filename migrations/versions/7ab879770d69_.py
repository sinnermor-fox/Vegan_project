"""empty message

Revision ID: 7ab879770d69
Revises: 
Create Date: 2021-02-25 21:21:57.064900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ab879770d69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('food_group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=180), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nutritions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unit', sa.String(length=80), nullable=False),
    sa.Column('tag', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('food',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=180), nullable=False),
    sa.Column('food_group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['food_group_id'], ['food_group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('food_nutrients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nutrition_value', sa.Float(), nullable=False),
    sa.Column('food_id', sa.Integer(), nullable=False),
    sa.Column('nutrition_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['food_id'], ['food.id'], ),
    sa.ForeignKeyConstraint(['nutrition_id'], ['nutritions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('food_nutrients')
    op.drop_table('food')
    op.drop_table('nutritions')
    op.drop_table('food_group')
    # ### end Alembic commands ###