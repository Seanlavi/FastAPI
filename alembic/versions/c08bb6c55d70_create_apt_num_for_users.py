"""create apt_num for users

Revision ID: c08bb6c55d70
Revises: da8a7fea7bed
Create Date: 2022-08-29 19:13:59.321169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c08bb6c55d70'
down_revision = 'da8a7fea7bed'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('address', sa.Column('apt_num', sa.String(), nullable=True))


def downgrade():
    op.drop_column('address', 'apt_num')
