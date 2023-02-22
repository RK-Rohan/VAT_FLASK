"""payable_voucher_table

Revision ID: 168e6d38a367
Revises: efa40090cc5a
Create Date: 2022-11-09 17:39:21.455165

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '168e6d38a367'
down_revision = 'efa40090cc5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payable_voucher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('payable_desc', sa.String(length=100), nullable=True),
    sa.Column('chalan_no', sa.String(length=100), nullable=True),
    sa.Column('payable_amount', sa.DECIMAL(precision=10, scale=2), nullable=True),
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
    op.drop_table('payable_voucher')
    # ### end Alembic commands ###
