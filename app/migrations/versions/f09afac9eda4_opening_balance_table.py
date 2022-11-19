"""opening_balance_table

Revision ID: f09afac9eda4
Revises: 817f6bef9a5c
Create Date: 2022-11-15 11:43:43.855041

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f09afac9eda4'
down_revision = '817f6bef9a5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('opening_balance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('opening_vat', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('opening_sd', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('closing_date', sa.DATE(), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('opening_balance')
    # ### end Alembic commands ###