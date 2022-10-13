"""Item Table

Revision ID: 46d8e1fd13d2
Revises: 611d81deda3b
Create Date: 2022-10-12 13:05:15.112091

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '46d8e1fd13d2'
down_revision = '611d81deda3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hs_code',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('heading', sa.String(length=100), nullable=True),
    sa.Column('hs_code', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('cd', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('sd', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('vat', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('ait', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('rd', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('at', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('tti', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('schedule', sa.String(length=255), nullable=True),
    sa.Column('vat_type', mysql.TINYINT(), nullable=True),
    sa.Column('type', mysql.TINYINT(), nullable=True),
    sa.Column('year_start', sa.Date(), nullable=True),
    sa.Column('year_end', sa.Date(), nullable=True),
    sa.Column('calculate_year', mysql.YEAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(length=100), nullable=True),
    sa.Column('item_type', sa.String(length=100), nullable=True),
    sa.Column('hs_code', sa.String(length=100), nullable=True),
    sa.Column('hs_code_id', sa.String(length=100), nullable=True),
    sa.Column('calculate_year', sa.String(length=100), nullable=True),
    sa.Column('unit_id', sa.String(length=100), nullable=True),
    sa.Column('stock_status', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('hs_code')
    # ### end Alembic commands ###