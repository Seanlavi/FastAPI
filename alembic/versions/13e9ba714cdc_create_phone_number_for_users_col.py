"""create phone number for users col

Revision ID: 13e9ba714cdc
Revises: 
Create Date: 2022-08-29 16:14:55.704071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13e9ba714cdc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade():
    op.drop_column('users', 'phone_number')
