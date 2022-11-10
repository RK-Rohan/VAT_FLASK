"""payable_mushak_table

Revision ID: efa40090cc5a
Revises: 4f7dd2555c62
Create Date: 2022-11-09 12:42:49.102810

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'efa40090cc5a'
down_revision = '4f7dd2555c62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payable_mushak',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pay_type', sa.Integer(), nullable=True),
    sa.Column('pay_date', sa.DATE(), nullable=True),
    sa.Column('pay_amount', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('business_type', sa.Integer(), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payable_mushak')
    # ### end Alembic commands ###