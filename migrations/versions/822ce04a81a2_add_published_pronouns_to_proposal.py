"""Add published pronouns to proposal

Revision ID: 822ce04a81a2
Revises: 1012d60b8c68
Create Date: 2022-05-10 20:02:47.453592

"""

# revision identifiers, used by Alembic.
revision = '822ce04a81a2'
down_revision = '1012d60b8c68'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('proposal', sa.Column('published_pronouns', sa.String(), nullable=True))
    op.add_column('proposal_version', sa.Column('published_pronouns', sa.String(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('proposal_version', 'published_pronouns')
    op.drop_column('proposal', 'published_pronouns')
    # ### end Alembic commands ###