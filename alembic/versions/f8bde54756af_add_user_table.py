"""Add user table

Revision ID: f8bde54756af
Revises: 372861979fc8
Create Date: 2022-09-17 18:00:30.316483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f8bde54756af"
down_revision = "372861979fc8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("NOW()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
