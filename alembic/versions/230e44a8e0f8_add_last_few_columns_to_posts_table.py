"""Add last few columns to posts table

Revision ID: 230e44a8e0f8
Revises: e1f1516beee3
Create Date: 2022-09-18 10:50:01.531643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "230e44a8e0f8"
down_revision = "e1f1516beee3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column(
            "published",
            sa.Boolean(),
            nullable=False,
            server_default="TRUE"
        ),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )

    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
