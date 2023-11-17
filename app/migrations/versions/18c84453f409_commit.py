"""Commit

Revision ID: 18c84453f409
Revises: f95a66b898f2
Create Date: 2023-11-17 13:54:01.012866

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18c84453f409'
down_revision: Union[str, None] = 'f95a66b898f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rooms', sa.Column('quantity', sa.Integer(), nullable=False))
    op.drop_column('rooms', 'quanity')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rooms', sa.Column('quanity', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('rooms', 'quantity')
    # ### end Alembic commands ###