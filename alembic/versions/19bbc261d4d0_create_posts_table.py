"""create posts table

Revision ID: 19bbc261d4d0
Revises: 
Create Date: 2022-09-17 17:48:25.014259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "19bbc261d4d0"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),

    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
