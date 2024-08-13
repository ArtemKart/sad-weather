"""first revision

Revision ID: cda367eb55ed
Revises: 
Create Date: 2024-08-05 12:41:52.542997

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cda367eb55ed'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weather',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('timezone', sa.String(length=255), nullable=True),
    sa.Column('max_temp', sa.Float(), nullable=True),
    sa.Column('min_temp', sa.Float(), nullable=True),
    sa.Column('pressure', sa.Float(), nullable=True),
    sa.Column('conditions', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather')
    # ### end Alembic commands ###