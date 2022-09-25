"""Countries

Revision ID: 6c62fcf25241
Revises: e071abe05558
Create Date: 2022-09-25 18:06:43.610160

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6c62fcf25241'
down_revision = 'e071abe05558'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('countries',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('sortname', mysql.VARCHAR(length=3), nullable=False),
    sa.Column('country_name', mysql.VARCHAR(length=150), nullable=False),
    sa.Column('phonecode', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )


def downgrade():
    op.drop_table('countries')

