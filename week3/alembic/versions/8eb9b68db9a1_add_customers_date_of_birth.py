"""add customers date_of_birth

Revision ID: 8eb9b68db9a1
Revises: 010acac4b191
Create Date: 2022-06-12 19:41:12.005961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8eb9b68db9a1'
down_revision = '010acac4b191'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )
