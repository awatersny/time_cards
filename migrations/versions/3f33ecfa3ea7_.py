"""empty message

Revision ID: 3f33ecfa3ea7
Revises: 961d80e4d848
Create Date: 2022-04-11 15:37:13.063100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f33ecfa3ea7'
down_revision = '961d80e4d848'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('time_cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_in', sa.DateTime(), nullable=False),
    sa.Column('time_out', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('time_cards')
    # ### end Alembic commands ###