"""

Revision ID: 2628a398bab8
Revises: 5a5373c0d0d0
Create Date: 2018-08-23 00:44:05.495949

"""

# revision identifiers, used by Alembic.
revision = '2628a398bab8'
down_revision = '5a5373c0d0d0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('volunteer', sa.Column('allow_comms_during_event', sa.Boolean(), nullable=False))
    op.add_column('volunteer_version', sa.Column('allow_comms_during_event', sa.Boolean(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('volunteer_version', 'allow_comms_during_event')
    op.drop_column('volunteer', 'allow_comms_during_event')
    # ### end Alembic commands ###
