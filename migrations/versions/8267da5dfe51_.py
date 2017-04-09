"""empty message

Revision ID: 8267da5dfe51
Revises: 0cb3c0126a43
Create Date: 2017-04-09 12:17:30.177978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8267da5dfe51'
down_revision = '0cb3c0126a43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('carpools', sa.Column('from_latitude', sa.Float(), nullable=True))
    op.add_column('carpools', sa.Column('from_longitude', sa.Float(), nullable=True))
    op.add_column('carpools', sa.Column('to_latitude', sa.Float(), nullable=True))
    op.add_column('carpools', sa.Column('to_longitude', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('carpools', 'to_longitude')
    op.drop_column('carpools', 'to_latitude')
    op.drop_column('carpools', 'from_longitude')
    op.drop_column('carpools', 'from_latitude')
    # ### end Alembic commands ###