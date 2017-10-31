"""empty message

Revision ID: 6f6081051336
Revises: 9c84e07108b0
Create Date: 2017-10-31 09:58:42.940054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f6081051336'
down_revision = '9c84e07108b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stock_exchanges', sa.Column('active', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stock_exchanges', 'active')
    # ### end Alembic commands ###
