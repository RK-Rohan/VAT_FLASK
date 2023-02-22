"""receivable_voucher_table

Revision ID: 19d047013dbb
Revises: 168e6d38a367
Create Date: 2022-11-09 18:27:14.097743

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '19d047013dbb'
down_revision = '168e6d38a367'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('receivable_voucher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('receivable_desc', sa.String(length=100), nullable=True),
    sa.Column('chalan_no', sa.String(length=100), nullable=True),
    sa.Column('receivable_amount', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('vat_amount', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('chalan_date', sa.DATE(), nullable=True),
    sa.Column('execute_date', sa.DATE(), nullable=True),
    sa.Column('business_type', sa.Integer(), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('receivable_voucher')
    # ### end Alembic commands ###
