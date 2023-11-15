"""added uniqueness on user_id

Revision ID: acdb241e344d
Revises: 8342fa5337b9
Create Date: 2023-11-14 19:11:12.220104

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'acdb241e344d'
down_revision: Union[str, None] = '8342fa5337b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'organizations', ['user_id'])
    op.create_unique_constraint(None, 'workers', ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'workers', type_='unique')
    op.drop_constraint(None, 'organizations', type_='unique')
    # ### end Alembic commands ###