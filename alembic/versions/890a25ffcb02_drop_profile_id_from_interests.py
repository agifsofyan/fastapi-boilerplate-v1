"""drop profile_id from interests

Revision ID: 890a25ffcb02
Revises: 2a3f3f9f8b63
Create Date: 2026-07-01 09:18:41.666522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '890a25ffcb02'
down_revision: Union[str, Sequence[str], None] = '2a3f3f9f8b63'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_index(
        "ix_interests_profile_id",
        table_name="interests",
    )

    # Baru hapus kolom
    op.drop_column(
        "interests",
        "profile_id",
    )


def downgrade() -> None:
    """Downgrade schema."""
    # Tambahkan kembali kolom
    op.add_column(
        "interests",
        sa.Column(
            "profile_id",
            sa.Integer(),
            nullable=False,
        ),
    )

    # Tambahkan kembali foreign key
    op.create_foreign_key(
        "fk_interests_profile_id_profiles",
        "interests",
        "profiles",
        ["profile_id"],
        ["id"],
        ondelete="CASCADE",
    )

    # Tambahkan kembali index
    op.create_index(
        "ix_interests_profile_id",
        "interests",
        ["profile_id"],
    )
