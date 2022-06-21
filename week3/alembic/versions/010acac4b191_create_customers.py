"""create customers

Revision ID: 010acac4b191
Revises: 
Create Date: 2022-06-12 19:30:27.363197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '010acac4b191'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE customers(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE customers;
        """
    )
