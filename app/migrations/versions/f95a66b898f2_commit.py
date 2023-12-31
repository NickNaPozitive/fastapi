"""Commit

Revision ID: f95a66b898f2
Revises: dad071ee041d
Create Date: 2023-11-17 13:52:52.291347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f95a66b898f2'
down_revision: Union[str, None] = 'dad071ee041d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('rooms_quantity', sa.Integer(), nullable=False))
    op.drop_column('hotels', 'room_quanity')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('room_quanity', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('hotels', 'rooms_quantity')
    # ### end Alembic commands ###
