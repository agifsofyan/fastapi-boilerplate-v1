"""merge multiple heads

Revision ID: af1c2986f10f
Revises: 140000047227, feae8b8063cf
Create Date: 2026-07-14 13:48:43.364552

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af1c2986f10f'
down_revision: Union[str, Sequence[str], None] = ('140000047227', 'feae8b8063cf')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
