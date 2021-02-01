"""empty message

Revision ID: 37ae3fe1a693
Revises: e6e9377fbd46
Create Date: 2021-01-31 21:38:20.723479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37ae3fe1a693'
down_revision = 'e6e9377fbd46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.ARRAY(sa.String(length=120)), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###
