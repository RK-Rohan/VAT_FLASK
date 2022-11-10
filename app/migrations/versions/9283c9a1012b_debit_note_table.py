"""debit_note_table

Revision ID: 9283c9a1012b
Revises: 19d047013dbb
Create Date: 2022-11-10 11:51:49.917375

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9283c9a1012b'
down_revision = '19d047013dbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('debit_note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('debit_note_no', sa.String(length=100), nullable=True),
    sa.Column('debit_note_type', sa.Integer(), nullable=True),
    sa.Column('dn_issue_date', sa.DATE(), nullable=True),
    sa.Column('purchase_id', sa.Integer(), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_info', sa.String(length=100), nullable=True),
    sa.Column('total_amount', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('total_vat', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('total_sd', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('note', sa.String(length=255), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('debit_note_line',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('debit_note_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.Column('rate', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('p_amount', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('p_vat_percent', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('p_vat_amount', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('p_sd', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('return_qty', sa.Integer(), nullable=True),
    sa.Column('return_amount', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('return_vat', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('return_sd', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('entry_date', sa.DATE(), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('debit_note_line')
    op.drop_table('debit_note')
    # ### end Alembic commands ###