"""add content column to post

Revision ID: 372861979fc8
Revises: 19bbc261d4d0
Create Date: 2022-09-17 17:55:31.156976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "372861979fc8"
down_revision = "19bbc261d4d0"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
