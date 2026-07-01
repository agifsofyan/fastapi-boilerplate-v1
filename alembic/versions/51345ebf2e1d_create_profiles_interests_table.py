"""create profiles_interests_table

Revision ID: 51345ebf2e1d
Revises: 890a25ffcb02
Create Date: 2026-07-01 09:21:24.899810

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51345ebf2e1d'
down_revision: Union[str, Sequence[str], None] = '890a25ffcb02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "profiles_interests",
        sa.Column(
            "profile_id",
            sa.Integer(),
            sa.ForeignKey("profiles.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column(
            "interest_id",
            sa.Integer(),
            sa.ForeignKey("interests.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )
    
    op.create_index(
        "ix_profiles_interests_profile_id",
        "profiles_interests",
        ["profile_id"],
    )

    op.create_index(
        "ix_profiles_interests_interest_id",
        "profiles_interests",
        ["interest_id"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        "ix_profiles_interests_interest_id",
        table_name="profiles_interests",
    )

    op.drop_index(
        "ix_profiles_interests_profile_id",
        table_name="profiles_interests",
    )

    op.drop_table("profiles_interests")
